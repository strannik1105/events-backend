from typing import Protocol

from fastapi import APIRouter


class AbstractApi(Protocol):
    def register_handlers(self) -> None:
        pass

    @property
    def router(self) -> APIRouter:
        pass
