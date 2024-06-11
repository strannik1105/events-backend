from uuid import UUID

from pydantic import Field, field_validator

from common.schemas import CoreModel, DateTimeMixin


class EventBase(CoreModel):
    name: str = Field(..., description="Event name")
    description: str = Field(..., description="Event description")
    type_sid: UUID = Field(..., description="Event type SID")

    @field_validator("name", mode="after")
    def validate_name(cls, v: str) -> str:
        return v.strip()

    @field_validator("description", mode="after")
    def validate_description(cls, v: str) -> str:
        return v.strip()


class Event(EventBase, DateTimeMixin):
    sid: UUID = Field(..., description="Event SID")
