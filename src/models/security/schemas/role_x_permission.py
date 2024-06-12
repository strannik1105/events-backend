from uuid import UUID

from pydantic import Field

from common.schemas import CoreModel, DateTimeMixin


class RoleXPermissionBase(CoreModel):
    role_sid: UUID = Field(..., description="Role SID")
    permission_sid: UUID = Field(..., description="Permission SID")
    access_actions: str = Field(
        ..., description="Access actions of role permission"
    )


class RoleXPermissionCreate(RoleXPermissionBase):
    pass


class PermissionTemplate(CoreModel):
    permission_label: int = Field(..., description="Permission label")
    access_actions: str = Field(
        ..., description="Access actions of role permission"
    )


class RoleXPermissionTemplate(CoreModel):
    role_label: int = Field(..., description="Role label")
    permissions: list[PermissionTemplate] = Field(
        ..., description="Permission templates"
    )


class RoleXPermission(RoleXPermissionBase, DateTimeMixin):
    sid: UUID = Field(..., description="Role permission SID")
