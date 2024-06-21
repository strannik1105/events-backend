from pydantic import Field, field_validator

from common.schemas import CoreModel, DateTimeMixin, Label


class ResourceBase(CoreModel, Label):
    name: str = Field(..., description="Resource name")
    description: str = Field(..., description="Resource description")

    @field_validator("name", mode="after")
    def validate_name(cls, v: str) -> str:
        return v.strip()

    @field_validator("description", mode="after")
    def validate_description(cls, v: str) -> str:
        return v.strip()


class ResourceDTOCreate(ResourceBase):
    pass


class Resource(ResourceBase, DateTimeMixin):
    pass
