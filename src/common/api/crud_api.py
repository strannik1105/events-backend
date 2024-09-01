from uuid import UUID

from fastapi import APIRouter, Path

from common.api.abstract_api import AbstractApi
from common.services.abstract_crud_service import AbstractCrudService


class CrudApi(AbstractApi):
    def __init__(self, service: AbstractCrudService) -> None:
        self._router = APIRouter()
        self._servive = service
        self.register_handlers()

    @property
    def router(self) -> APIRouter:
        return self._router

    def register_handlers(self) -> None:
        self._router.add_api_route("/get_all", self._get_all)
        self._router.add_api_route("/get/{sid}", self._get_one)
        self._router.add_api_route("/create", self._create, methods=["POST"])
        self._router.add_api_route("/update/{sid}", self._update)
        self._router.add_api_route("/delete/{sid}", self._delete)

    async def _get_all(self, limit: int = 100, offset: int = 0):
        return await self._servive.get_all(limit, offset)

    def _get_one(self, sid: UUID = Path(...)):
        pass

    async def _create(self):
        pass

    def _update(self, sid: UUID = Path(...)):
        pass

    def _delete(self, sid: UUID = Path(...)):
        pass
