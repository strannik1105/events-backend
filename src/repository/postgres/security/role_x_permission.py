from sqlalchemy.ext.asyncio import AsyncSession

from models.security import RoleXPermission
from repository.postgres.core import CoreRepository


class RoleXPermissionRepository(CoreRepository[RoleXPermission]):
    def __init__(self, db: AsyncSession, model: type[RoleXPermission]) -> None:
        super().__init__(db, model)
