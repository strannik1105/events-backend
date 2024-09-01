from common.db.base import SQLAlchemyBaseModel
from common.repository.abstract_crud_repository import AbstractCrudRepository
from common.services.abstract_crud_service import AbstractCrudService


class CrudService(AbstractCrudService):
    def __init__(self, repository: AbstractCrudRepository):
        self._repository = repository

    async def get_all(self, limit, offset) -> list[SQLAlchemyBaseModel]:
        print(await self._repository.get_all(limit, offset))
        return await self._repository.get_all(limit, offset)

    async def create(self, obj):
        await self._repository.create(obj)