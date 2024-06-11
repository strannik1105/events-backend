from uuid import UUID

from pydantic import Field

from common.schemas import CoreModel, DateTimeMixin


class EventPullBase(CoreModel):
    user_sid: UUID = Field(..., description="User SID")
    event_sid: UUID = Field(..., description="Event SID")
    event_content_sid: UUID = Field(..., description="Event content SID")
    event_role_sid: UUID = Field(..., description="Event role SID")


class EventPull(EventPullBase, DateTimeMixin):
    sid: UUID = Field(..., description="Event pull SID")
