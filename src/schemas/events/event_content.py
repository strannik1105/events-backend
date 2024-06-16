from pydantic import Field, field_validator

from common.schemas import CoreModel, DateTimeMixin, Sid


class EventContentBase(CoreModel):
    name: str = Field(..., description="Event name")
    description: str = Field(..., description="Event description")
    type_label: int = Field(..., description="Event content type label")

    @field_validator("name", mode="after")
    def validate_name(cls, v: str) -> str:
        return v.strip()

    @field_validator("description", mode="after")
    def validate_description(cls, v: str) -> str:
        return v.strip()


class EventContent(EventContentBase, Sid, DateTimeMixin):
    pass
