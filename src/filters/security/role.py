from pydantic import Field

from common.filters import CoreFilter


class RoleFilter(CoreFilter):
    is_event: bool | None = Field(None, alias="isEvent")
