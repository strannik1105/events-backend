from typing import Annotated
from fastapi import Body, File

from common.api.abstract_api import AbstractApi
from common.enums.http_method import HttpMethod
from common.router.router import AsyncRouteCallback, Router
from common.singleton import Singleton
from common.telegram.client import TelegramClient


class TgApi(AbstractApi, Singleton):
    def __init__(self) -> None:
        self._router = Router()

        self.register_handlers()

    def register_handlers(self) -> None:
        self._router.register_async_handler("publish", self._get_publish_message_callback(), HttpMethod.POST)
    
    @property
    def router(self) -> Router:
        return self._router

    def _get_publish_message_callback(self) -> AsyncRouteCallback:
        async def callback(image: Annotated[bytes, File()], title: str = Body(...), description: str = Body(...)) -> None:
            client = TelegramClient()
            await client.publish_message(image, title, description)
            return {}
        
        return AsyncRouteCallback(callback)
