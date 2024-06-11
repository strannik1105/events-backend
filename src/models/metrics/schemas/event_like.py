from uuid import UUID

from pydantic import Field

from common.schemas import CoreModel, CreatedAtMixin


class EventLikeBase(CoreModel):
    user_sid: UUID = Field(..., description="User SID")
    event_sid: UUID = Field(..., description="Event SID")


class EventLike(EventLikeBase, CreatedAtMixin):
    sid: UUID = Field(..., description="Event like SID")
