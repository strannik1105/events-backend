from uuid import UUID

from pydantic import Field

from common.schemas import CoreModel, CreatedAtMixin, Sid


class EventViewBase(CoreModel):
    user_sid: UUID = Field(..., description="User SID")
    event_sid: UUID = Field(..., description="Event SID")


class EventView(EventViewBase, Sid, CreatedAtMixin):
    pass
