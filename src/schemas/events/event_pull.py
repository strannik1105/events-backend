from uuid import UUID

from pydantic import Field

from common.schemas import CoreModel, DateTimeMixin, Sid


class EventPullBase(CoreModel):
    user_sid: UUID = Field(..., description="User SID")
    event_sid: UUID = Field(..., description="Event SID")
    event_content_sid: UUID | None = Field(
        None, description="Event content SID"
    )
    event_role_label: int = Field(..., description="Event role label")


class EventPull(EventPullBase, Sid, DateTimeMixin):
    pass
