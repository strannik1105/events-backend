from pydantic import Field, field_validator

from common.schemas import CoreModel, DateTimeMixin, Label


class EventContentTypeBase(CoreModel, Label):
    name: str = Field(..., description="Event content type name")
    description: str = Field(..., description="Event content type description")

    @field_validator("name", mode="after")
    def validate_name(cls, v: str) -> str:
        return v.strip()

    @field_validator("description", mode="after")
    def validate_description(cls, v: str) -> str:
        return v.strip()


class EventContentTypeDTOCreate(EventContentTypeBase):
    pass


class EventContentType(EventContentTypeBase, DateTimeMixin):
    pass
