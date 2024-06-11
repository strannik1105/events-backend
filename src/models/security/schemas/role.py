from uuid import UUID

from pydantic import Field, field_validator

from common.schemas import CoreModel, DateTimeMixin


class RoleBase(CoreModel):
    name: str = Field(..., description="Role name")
    description: str = Field(..., description="Role description")

    @field_validator("name", mode="after")
    def validate_name(cls, v: str) -> str:
        return v.strip()

    @field_validator("description", mode="after")
    def validate_description(cls, v: str) -> str:
        return v.strip()


class Role(RoleBase, DateTimeMixin):
    sid: UUID = Field(..., description="Role SID")
