from typing import Protocol

from common.db.base import SQLAlchemyBaseModel


class AbstractCrudService(Protocol):
    def get_all(self, limit, offset) -> list[SQLAlchemyBaseModel]:
        pass

    async def create(self, obj):
        pass
