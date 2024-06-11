from uuid import UUID

from pydantic import Field

from common.schemas import CoreModel, DateTimeMixin


class SubscribeBase(CoreModel):
    user_sid: UUID = Field(..., description="User SID")
    subscriber_sid: UUID = Field(..., description="Subscriber SID")
    is_notify: bool = Field(True, description="Notify status")


class Subscribe(SubscribeBase, DateTimeMixin):
    sid: UUID = Field(..., description="Subscribe SID")
