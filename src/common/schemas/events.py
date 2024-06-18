from uuid import UUID

from pydantic import Field

from common.schemas import CoreModel


class EventSids(CoreModel):
    event_sid: UUID = Field(..., description="Event SID")
    event_content_sid: UUID | None = Field(
        None, description="Event content SID"
    )


class EventPullSids(CoreModel):
    user_sid: UUID = Field(..., description="User SID")
    event_sid: UUID = Field(..., description="Event SID")
    event_content_sid: UUID | None = Field(
        None, description="Event content SID"
    )
