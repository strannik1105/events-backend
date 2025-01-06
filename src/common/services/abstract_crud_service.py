from abc import ABC, abstractmethod
from typing import Any
from uuid import UUID

from common.db.base import SQLAlchemyBaseModel
from common.services.abstract_service import AbstractService


class AbstractCrudService(AbstractService, ABC):
    @abstractmethod
    async def get_all(self, limit, offset) -> list[SQLAlchemyBaseModel]:
        pass

    @abstractmethod
    async def get_one(self, sid: UUID) -> SQLAlchemyBaseModel:
        pass

    @abstractmethod
    async def create(self, obj: dict[str, Any]) -> SQLAlchemyBaseModel:
        pass

    @abstractmethod
    async def update(
        self, obj: dict[str, Any], changes: dict[str, Any], sid: UUID
    ):
        pass

    @abstractmethod
    async def delete(self, obj: dict[str, Any]) -> None:
        pass
