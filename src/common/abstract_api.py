from typing import Protocol


class AbstractApi(Protocol):
    def register_handlers(self) -> None:
        pass
