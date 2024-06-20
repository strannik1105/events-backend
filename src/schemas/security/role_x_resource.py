from pydantic import Field

from common.schemas import CoreModel, DateTimeMixin, Sid


class RoleXResourceBase(CoreModel):
    role_label: int = Field(..., ge=0, le=32767, description="Role label")
    resource_label: int = Field(
        ..., ge=0, le=32767, description="Resource label"
    )
    permissions: str = Field(
        ..., max_length=5, description="Permissions of role resource"
    )


class RoleXResourceCreate(RoleXResourceBase):
    pass


class RoleXResource(RoleXResourceBase, Sid, DateTimeMixin):
    pass
