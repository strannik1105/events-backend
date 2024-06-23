from typing import Type

from common.filters import PostgresFilter
from models import security as security_models


class RoleFilter(PostgresFilter):
    is_event: bool | None = None
    order_by: list[str] | None = None

    class FilterConfig:
        models: list[Type] = [security_models.Role]
        model_field_reserve: dict[str, list[Type]] = {}
        model_field_alias: dict[Type, dict[str, str]] = {}
        model_field_exclude: dict[Type, list[str]] = {}
        ordering_field_name: str = "order_by"
        ordering_nulls_last: bool = True
