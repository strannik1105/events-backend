from typing import Protocol

from common.db.base import SQLAlchemyBaseModel


class AbstractCrudService(Protocol):
    async def get_all(self, limit, offset) -> list[SQLAlchemyBaseModel]:
        pass

    async def get_one(self, id) -> SQLAlchemyBaseModel:
        pass

    async def create(self, obj):
        pass

    async def update(self, changes, sid):
        pass

    async def delete(self, sid):
        pass
