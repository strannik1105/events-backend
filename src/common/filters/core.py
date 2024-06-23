import re
import sys
from copy import deepcopy
from typing import Any, Iterable, Type, Union, get_args, get_origin

from fastapi import Depends
from fastapi.exceptions import RequestValidationError
from pydantic import (
    BaseModel,
    ConfigDict,
    Extra,
    ValidationError,
    create_model,
    field_validator,
)
from pydantic.alias_generators import to_camel
from pydantic.fields import FieldInfo
from pydantic_core.core_schema import ValidationInfo


UNION_TYPES: list = [Union]

if sys.version_info >= (3, 10):
    from types import UnionType

    UNION_TYPES.append(UnionType)


class CoreCustomFilter(BaseModel):
    pass


class CoreFilter(BaseModel, extra=Extra.forbid):  # type: ignore
    class FilterConfig:
        models: list[Type] = []
        model_field_reserve: dict[str, list[Type]] = {}
        model_field_alias: dict[Type, dict[str, str]] = {}
        model_field_exclude: dict[Type, list[str]] = {}
        ordering_field_name: str = "order_by"
        ordering_nulls_last: bool = True
        prefix: str

    model_config = ConfigDict(
        from_attributes=True, populate_by_name=True, alias_generator=to_camel
    )

    def filter(self, query: Any) -> Any:
        return query

    def sort(self, query: Any) -> Any:
        return query

    @property
    def filtering_fields(self) -> Any:
        fields = self.model_dump(exclude_none=True, exclude_unset=True)
        fields.pop(self.FilterConfig.ordering_field_name, None)
        return fields.items()

    @property
    def ordering_values(self) -> str | None:
        if hasattr(self, self.FilterConfig.ordering_field_name):
            return getattr(self, self.FilterConfig.ordering_field_name)
        return None

    @staticmethod
    def camel_to_snake(name: str) -> str:
        name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
        return re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).lower()

    @classmethod
    def reserve_validate(cls, model: Type, field_name: str) -> bool:
        reserved_models = cls.FilterConfig.model_field_reserve.get(
            field_name, []
        )
        return model not in reserved_models if reserved_models else True

    @classmethod
    def alias_validate(cls, model: Type, field_name: str) -> bool:
        return field_name in cls.FilterConfig.model_field_alias.get(model, {})

    @classmethod
    def get_alias(cls, model: Type, field_name: str) -> str:
        return cls.FilterConfig.model_field_alias[model][field_name]

    @classmethod
    def exclude_validate(cls, model: Type, field_name: str) -> bool:
        return field_name not in cls.FilterConfig.model_field_exclude.get(
            model, []
        )

    @field_validator("*", mode="before", check_fields=False)
    def strip_order_by_values(cls, value: Any, field: ValidationInfo) -> Any:
        if field.field_name != cls.FilterConfig.ordering_field_name:
            return value
        if not value:
            return None
        return [
            field_name.strip() for field_name in value if field_name.strip()
        ]

    @field_validator("*", mode="before", check_fields=False)
    def validate_order_by(cls, value: Any, field: ValidationInfo) -> Any:
        if field.field_name != cls.FilterConfig.ordering_field_name:
            return value
        if not value:
            return None
        if cls.FilterConfig.models is None:
            raise ValueError(
                "The filter scheme needs to set the target model(s)."
            )

        field_names_set = set()
        for field_name_w_direction in value:
            field_name = field_name_w_direction.lstrip("-+")
            field_name = cls.camel_to_snake(field_name)
            if field_name in field_names_set:
                raise ValueError(
                    f"The sorting field {field_name} is duplicated"
                )
            field_names_set.add(field_name)

            is_valid_field = False
            for model in cls.FilterConfig.models:
                if not cls.reserve_validate(
                    model=model, field_name=field_name
                ):
                    continue
                if cls.alias_validate(model=model, field_name=field_name):
                    field_name = cls.get_alias(
                        model=model, field_name=field_name
                    )
                if not cls.exclude_validate(
                    model=model, field_name=field_name
                ):
                    continue
                if hasattr(model, field_name):
                    is_valid_field = True

            if not is_valid_field:
                raise ValueError(
                    f"{field_name} is not a valid ordering field."
                )

        return value


def _list_to_str_fields(
    Filter: Type[CoreFilter],
) -> dict[str, tuple[object | Type, FieldInfo | None]]:
    ret: dict[str, tuple[object | Type, FieldInfo | None]] = {}
    for name, f in Filter.model_fields.items():
        field_info = deepcopy(f)
        annotation = f.annotation
        if get_origin(annotation) in UNION_TYPES:
            annotation_args: list = list(get_args(f.annotation))
            if type(None) in annotation_args:
                annotation_args.remove(type(None))
            if len(annotation_args) == 1:
                annotation = annotation_args[0]
        if annotation is list or get_origin(annotation) is list:
            if isinstance(field_info.default, Iterable):
                field_info.default = ",".join(field_info.default)
            ret[name] = (str if f.is_required() else str | None, field_info)
        else:
            ret[name] = (f.annotation, field_info)
    return ret


def FilterDepends(Filter: Type[CoreFilter], by_alias: bool = True) -> Any:
    fields = _list_to_str_fields(Filter)
    GeneratedFilter: Type[CoreFilter] = create_model(  # type: ignore
        Filter.__class__.__name__, **fields
    )

    class FilterWrapper(GeneratedFilter):  # type: ignore
        def __new__(cls, *args: Any, **kwargs: Any) -> Any:
            try:
                instance = GeneratedFilter(*args, **kwargs)
                data = instance.model_dump(
                    exclude_unset=True,
                    exclude_defaults=True,
                    by_alias=by_alias,
                )
                if original_filter := getattr(
                    Filter.FilterConfig, "original_filter", None
                ):
                    prefix = f"{Filter.FilterConfig.prefix}__"
                    stripped = {}
                    for k, v in data.items():
                        if k.startswith(prefix):
                            k = k.replace(prefix, "", 1)
                        stripped[k] = v
                    return original_filter(**stripped)
                return Filter(**data)
            except ValidationError as e:
                raise RequestValidationError(e.errors()) from e

    return Depends(FilterWrapper)
