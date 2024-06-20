from sqlalchemy.ext.asyncio import AsyncSession

from models.security import Resource
from repository.postgres.core import CoreRepository


class ResourceRepository(CoreRepository[Resource]):
    def __init__(self, db: AsyncSession, model: type[Resource]) -> None:
        super().__init__(db, model)
