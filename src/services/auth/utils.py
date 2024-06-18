from sqlalchemy.ext.asyncio import AsyncSession

from models import security as security_models
from services.core import CoreServiceUtils


class AuthServiceUtils(CoreServiceUtils):
    def __init__(self, pg_db: AsyncSession) -> None:
        super().__init__(pg_db)

    @staticmethod
    def get_role_permissions(role: security_models.Role) -> dict[int, str]:
        role_permissions = {}
        for permission in role.permissions:
            role_permissions[
                permission.permission_label
            ] = permission.access_actions
        return role_permissions
