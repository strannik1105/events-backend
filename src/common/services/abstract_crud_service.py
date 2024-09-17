from typing import Protocol, Any
from uuid import UUID

from common.db.base import SQLAlchemyBaseModel


class AbstractCrudService(Protocol):
    async def get_all(self, limit, offset) -> list[SQLAlchemyBaseModel]:
        pass

    async def get_one(self, sid: UUID) -> SQLAlchemyBaseModel:
        pass

    async def create(self, obj) -> SQLAlchemyBaseModel:
        pass

    async def update(self, changes: dict[str, Any], sid: UUID):
        pass

    async def delete(self, sid: UUID):
        pass
