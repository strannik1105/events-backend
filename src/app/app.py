from fastapi import FastAPI
import uvicorn

from common.api.abstract_api import AbstractApi
from common.config.config import Config
from common.singleton import Singleton
from starlette.middleware.cors import CORSMiddleware


class App(Singleton):
    def __init__(self) -> None:
        config = Config().get_instance()

        self._app = FastAPI()
        self._host = config.HOST
        self._port = config.PORT

    def run(self):
        self._app.add_middleware(
            CORSMiddleware,
            allow_origins=['*'],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        uvicorn.run(self._app, host=self._host, port=self._port)

    def register_route(self, api: AbstractApi, url):
        self._app.include_router(
            api.router.fast_api_router, prefix=f"/{url}", tags=[url]
        )


class ApiRegistrator:
    @staticmethod
    def register(app: App, api: AbstractApi, url: str) -> None:
        app.register_route(api, url)
