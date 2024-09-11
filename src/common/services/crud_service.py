from typing import Any
from uuid import UUID

from common.db.base import SQLAlchemyBaseModel
from common.repository.abstract_crud_repository import AbstractCrudRepository
from common.services.abstract_crud_service import AbstractCrudService


class CrudService(AbstractCrudService):
    def __init__(self, repository: AbstractCrudRepository):
        self._repository = repository

    async def get_all(self, limit, offset) -> list[SQLAlchemyBaseModel]:
        return await self._repository.get_all(limit, offset)

    async def get_one(self, sid: UUID):
        return await self._repository.get(sid)

    async def create(self, obj):
        await self._repository.create(obj)

    async def update(self, obj, changes: dict[str, Any], sid: UUID):
        return await self._repository.update(obj, changes, sid)

    async def delete(self, obj):
        await self._repository.delete(obj)
