from pydantic import Field, field_validator

from common.schemas import CoreModel, DateTimeMixin, Sid


class EventBase(CoreModel):
    name: str = Field(..., description="Event name")
    description: str | None = Field(None, description="Event description")
    type_label: int = Field(..., description="Event type label")

    @field_validator("name", mode="after")
    def validate_name(cls, v: str) -> str:
        return v.strip()

    @field_validator("description", mode="after")
    def validate_description(cls, v: str) -> str:
        return v.strip()


class EventDTOCreate(EventBase):
    pass


class EventDTOUpdate(EventBase):
    pass


class Event(EventBase, Sid, DateTimeMixin):
    pass
