from uuid import UUID

from pydantic import Field

from common.schemas import CoreModel, DateTimeMixin


class RoleXPermissionBase(CoreModel):
    role_sid: UUID = Field(..., description="Role SID")
    permission_sid: UUID = Field(..., description="Permission SID")
    access_actions: str = Field(
        ..., description="Access actions of role permission"
    )


class RoleXPermission(RoleXPermissionBase, DateTimeMixin):
    sid: UUID = Field(..., description="Role permission SID")
