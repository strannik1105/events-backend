from uuid import UUID
from fastapi import APIRouter, Path

from common.api.abstract_api import AbstractApi
from common.singleton import Singleton


class CrudApi(AbstractApi, Singleton):
    def __init__(self) -> None:
        self._router = APIRouter()
        self.register_handlers()

    @property
    def router(self) -> APIRouter:
        return self._router

    def register_handlers(self) -> None:
        self._router.add_api_route("/get_all", self._get_all)
        self._router.add_api_route("/get/{sid}", self._get_one)
        self._router.add_api_route("/create", self._create)
        self._router.add_api_route("/update/{sid}", self._update)
        self._router.add_api_route("/delete/{sid}", self._delete)

    def _get_all(self, limit: int = 100, offset: int = 50):
        pass

    def _get_one(self, sid: UUID = Path(...)):
        pass

    def _create(self):
        pass

    def _update(self, sid: UUID = Path(...)):
        pass

    def _delete(self, sid: UUID = Path(...)):
        pass
