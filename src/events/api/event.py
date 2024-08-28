from fastapi import APIRouter

from common.abstract_api import AbstractApi
from common.singleton import Singleton


class EventApi(AbstractApi, Singleton):
    def __init__(self) -> None:
        self._router = APIRouter()
        self.register_handlers()

    @property
    def router(self) -> APIRouter:
        return self._router

    def register_handlers(self) -> None:
        self._router.add_api_route("/", self.get_all)

    def get_all(self, limit: int = 100, offset: int = 50) -> None:
        pass
