from sqlalchemy.ext.asyncio import AsyncSession

from interfaces.repository.security import IResourceRepository
from models.security import Resource
from repository.postgres.core import CoreRepository


class ResourceRepository(
    IResourceRepository[Resource], CoreRepository[Resource]
):
    def __init__(self, db: AsyncSession, model: type[Resource]) -> None:
        super().__init__(db, model)
