from uuid import UUID

from pydantic import Field, field_validator

from common.schemas import CoreModel, DateTimeMixin


class PermissionBase(CoreModel):
    name: str = Field(..., description="Permission name")
    description: str = Field(..., description="Permission description")

    @field_validator("name", mode="after")
    def validate_name(cls, v: str) -> str:
        return v.strip()

    @field_validator("description", mode="after")
    def validate_description(cls, v: str) -> str:
        return v.strip()


class Permission(PermissionBase, DateTimeMixin):
    sid: UUID = Field(..., description="Permission SID")
