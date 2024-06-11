from uuid import UUID

from pydantic import Field

from common.schemas import CoreModel, CreatedAtMixin


class EventViewBase(CoreModel):
    user_sid: UUID = Field(..., description="User SID")
    event_sid: UUID = Field(..., description="Event SID")


class EventView(EventViewBase, CreatedAtMixin):
    sid: UUID = Field(..., description="Event view SID")
