from sqlalchemy.ext.asyncio import AsyncSession

from models import security as security_models
from services.core import CoreServiceUtils


class AuthServiceUtils(CoreServiceUtils):
    def __init__(self, pg_db: AsyncSession) -> None:
        super().__init__(pg_db)

    @staticmethod
    def get_resource_permissions(role: security_models.Role) -> dict[int, str]:
        resource_permissions = {}
        for permission in role.permissions:
            resource_permissions[
                permission.resource_label
            ] = permission.permissions
        return resource_permissions
