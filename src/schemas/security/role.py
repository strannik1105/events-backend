from pydantic import Field, field_validator

from common.schemas import CoreModel, DateTimeMixin, Label


class RoleBase(CoreModel, Label):
    name: str = Field(..., description="Role name")
    description: str = Field(..., description="Role description")
    is_event: bool = Field(..., description="Role event status")

    @field_validator("name", mode="after")
    def validate_name(cls, v: str) -> str:
        return v.strip()

    @field_validator("description", mode="after")
    def validate_description(cls, v: str) -> str:
        return v.strip()


class RoleDTOCreate(RoleBase):
    pass


class Role(RoleBase, DateTimeMixin):
    pass
