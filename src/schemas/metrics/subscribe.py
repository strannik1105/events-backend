from uuid import UUID

from pydantic import Field

from common.schemas import CoreModel, DateTimeMixin, Sid


class SubscribeBase(CoreModel):
    user_sid: UUID = Field(..., description="User SID")
    subscriber_sid: UUID = Field(..., description="Subscriber SID")
    is_notify: bool = Field(True, description="Notify status")


class SubscribeDTOCreate(SubscribeBase):
    pass


class Subscribe(SubscribeBase, Sid, DateTimeMixin):
    pass
