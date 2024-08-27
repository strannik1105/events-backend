from fastapi import FastAPI

from common.singleton import Singleton


class AppMaker(Singleton):
    def __init__(self):
        self._app = FastAPI()

    def __call__(self) -> FastAPI:
        return self._app
