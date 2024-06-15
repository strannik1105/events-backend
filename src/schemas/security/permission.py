from pydantic import Field, field_validator

from common.schemas import CoreModel, DateTimeMixin, Label


class PermissionBase(CoreModel, Label):
    name: str = Field(..., description="Permission name")
    description: str = Field(..., description="Permission description")

    @field_validator("name", mode="after")
    def validate_name(cls, v: str) -> str:
        return v.strip()

    @field_validator("description", mode="after")
    def validate_description(cls, v: str) -> str:
        return v.strip()


class PermissionCreate(PermissionBase):
    pass


class Permission(PermissionBase, DateTimeMixin):
    pass