from common.filters import PostgresFilter
from models import security as security_models


class RoleFilter(PostgresFilter):
    is_event: bool | None = None
    order_by: list[str] | None = None

    class FilterConfig:
        models = [security_models.Role]
        model_field_reserve = {}
        model_field_alias = {}
        model_field_exclude = {}
        ordering_field_name: str = "order_by"
        ordering_nulls_last: bool = True
        is_camel_case: bool = True
