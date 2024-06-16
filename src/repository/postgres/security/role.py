from sqlalchemy.ext.asyncio import AsyncSession

from models.security import Role
from repository.postgres.core import CoreRepository


class RoleRepository(CoreRepository[Role]):
    def __init__(self, db: AsyncSession, model: type[Role]) -> None:
        super().__init__(db, model)
