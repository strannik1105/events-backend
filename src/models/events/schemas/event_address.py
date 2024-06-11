from datetime import datetime
from uuid import UUID

from pydantic import Field, field_validator

from common.schemas import CoreModel, DateTimeMixin


class EventAddressBase(CoreModel):
    address: str = Field(..., description="Event address")
    event_sid: UUID = Field(..., description="Event SID")
    event_content_sid: UUID = Field(..., description="Event content SID")
    start_at: datetime = Field(..., description="Event start at")
    end_at: datetime = Field(..., description="Event end at")

    @field_validator("address", mode="after")
    def validate_address(cls, v: str) -> str:
        return v.strip()


class EventAddress(EventAddressBase, DateTimeMixin):
    sid: UUID = Field(..., description="Event address SID")
