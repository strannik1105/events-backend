from enum import StrEnum
from typing import Any, override

from pydantic import FieldValidationInfo, field_validator
from sqlalchemy import and_, nullslast, or_
from sqlalchemy.orm import Query
from sqlalchemy.sql.selectable import Select

from ..core import CoreFilter


def _backward_compatible_value_for_like_and_ilike(value: str):
    return value if "%" in value else f"%{value}%"


_orm_operator_transformer = {
    "neq": lambda value: ("__ne__", value),
    "gt": lambda value: ("__gt__", value),
    "ge": lambda value: ("__ge__", value),
    "in": lambda value: ("in_", value),
    "contains": lambda value: ("contains", value),
    "isnull": lambda value: (
        ("is_", None) if value is True else ("is_not", None)
    ),
    "isempty": lambda value: (
        ("__eq__|is_", ("", None))
        if value is True
        else ("__ne__|is_not", ("", None))
    ),
    "lt": lambda value: ("__lt__", value),
    "le": lambda value: ("__le__", value),
    "like": lambda value: (
        "like",
        _backward_compatible_value_for_like_and_ilike(value),
    ),
    "ilike": lambda value: (
        "ilike",
        _backward_compatible_value_for_like_and_ilike(value),
    ),
    "not": lambda value: ("is_not", value),
    "not_in": lambda value: ("not_in", value),
}


class OrderDirection(StrEnum):
    ASC = "asc"
    DESC = "desc"


class PostgresFilter(CoreFilter):
    @field_validator("*", mode="before")
    def split_str(cls, value: Any, field: FieldValidationInfo) -> Any:
        if (
            field.field_name == cls.FilterConfig.ordering_field_name
            or field.field_name.endswith("__in")
            or field.field_name.endswith("__not_in")
            or field.field_name.endswith("__contains")
        ) and isinstance(value, str):
            if not value:
                return []
            return list(value.split(","))
        return value

    @override
    def filter(self, query: Query | Select) -> Query | Select:
        for field_name, value in self.filtering_fields:
            field_value = getattr(self, field_name)
            if isinstance(field_value, PostgresFilter):
                query = field_value.filter(query)
            else:
                if "__" in field_name:
                    field_name, operator = field_name.split("__")
                    operator, value = _orm_operator_transformer[operator](
                        value
                    )
                else:
                    operator = "__eq__"

                if self.FilterConfig.is_camel_case:
                    field_name = self.camel_to_snake(field_name)

                for model in self.FilterConfig.models:
                    if not self.reserve_validate(
                        model=model, field_name=field_name
                    ):
                        continue
                    if self.alias_validate(model=model, field_name=field_name):
                        field_name = self.get_alias(
                            model=model, field_name=field_name
                        )
                    if not self.exclude_validate(
                        model=model, field_name=field_name
                    ):
                        continue

                    if hasattr(model, field_name):
                        model_field = getattr(model, field_name)

                        operator_split = operator.split("|")
                        len_operator_split = len(operator_split)

                        if len_operator_split > 1:
                            filter_conditions = []
                            logical_operator = (
                                or_ if "__eq__" in operator_split else and_
                            )
                            for i in range(len_operator_split):
                                filter_conditions.append(
                                    getattr(model_field, operator_split[i])(
                                        value[i]
                                    )
                                )
                            query = query.filter(
                                logical_operator(*filter_conditions)
                            )
                        else:
                            query = query.filter(
                                getattr(model_field, operator)(value)
                            )
        return query

    @override
    def sort(self, query: Query | Select) -> Query | Select:
        if not self.ordering_values:
            return query

        for field_name_w_direction in self.ordering_values:
            direction = OrderDirection.ASC
            if field_name_w_direction.startswith("-"):
                direction = OrderDirection.DESC

            field_name = field_name_w_direction.lstrip("-+")

            if self.FilterConfig.is_camel_case:
                field_name = self.camel_to_snake(field_name)

            for model in self.FilterConfig.models:
                if not self.reserve_validate(
                    model=model, field_name=field_name
                ):
                    continue
                if self.alias_validate(model=model, field_name=field_name):
                    field_name = self.get_alias(
                        model=model, field_name=field_name
                    )
                if not self.exclude_validate(
                    model=model, field_name=field_name
                ):
                    continue
                if hasattr(model, field_name):
                    if self.FilterConfig.ordering_nulls_last:
                        query = query.order_by(
                            nullslast(
                                getattr(
                                    getattr(model, field_name), direction
                                )()
                            )
                        )
                    else:
                        query = query.order_by(
                            getattr(getattr(model, field_name), direction)()
                        )

        return query
