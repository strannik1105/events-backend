from pydantic import Field

from common.schemas import CoreModel, DateTimeMixin, Sid


class RoleXPermissionBase(CoreModel):
    role_label: int = Field(..., ge=0, le=32767, description="Role label")
    permission_label: int = Field(
        ..., ge=0, le=32767, description="Permission label"
    )
    access_actions: str = Field(
        ..., max_length=5, description="Access actions of role permission"
    )


class RoleXPermissionCreate(RoleXPermissionBase):
    pass


class RoleXPermission(RoleXPermissionBase, Sid, DateTimeMixin):
    pass
