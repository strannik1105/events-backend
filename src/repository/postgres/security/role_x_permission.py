from sqlalchemy.ext.asyncio import AsyncSession

from models.security import RoleXPermission
from repository.postgres.core import CoreRepository


class RoleXPermissionRepository(CoreRepository[RoleXPermission]):
    def __init__(self, db: AsyncSession, model: RoleXPermission):
        super().__init__(db, model)
