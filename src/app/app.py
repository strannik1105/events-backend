from fastapi import FastAPI

from common.abstract_api import AbstractApi
from common.singleton import Singleton


class AppMaker(Singleton):
    def __init__(self):
        self._app = FastAPI()

    def __call__(self) -> FastAPI:
        return self._app


class ApiRegistrator:
    @staticmethod
    def register(app: FastAPI, api: AbstractApi, url: str):
        app.include_router(api.router, prefix=f"/{url}", tags=[url])
