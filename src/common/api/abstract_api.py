from typing import Protocol

from common.router.router import Router


class AbstractApi(Protocol):
    def register_handlers(self) -> None:
        pass

    @property
    def router(self) -> Router:
        pass
