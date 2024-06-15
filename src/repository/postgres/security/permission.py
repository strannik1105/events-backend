from sqlalchemy.ext.asyncio import AsyncSession

from models.security import Permission
from repository.postgres.core import CoreRepository


class PermissionRepository(CoreRepository[Permission]):
    def __init__(self, db: AsyncSession, model: Permission):
        super().__init__(db, model)
