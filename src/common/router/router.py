from typing import Any, Callable, Coroutine
from fastapi import APIRouter

from common.enums.http_method import HttpMethod


class AsyncRouteCallback:
    def __init__(
        self, callback: Callable[..., Coroutine[Any, Any, Any]]
    ) -> None:
        self._callback = callback

    @property
    def callback(self) -> Coroutine[Any, Any, Any]:
        return self._callback


class Router:
    def __init__(self) -> None:
        self._router = APIRouter()

    def register_async_handler(
        self,
        path: str,
        callback: AsyncRouteCallback,
        method: HttpMethod = HttpMethod.GET,
        response_model: Any = None,
    ) -> None:
        self._router.add_api_route(
            path,
            callback.callback,
            methods=[method.value],
            response_model=response_model,
        )

    @property
    def fast_api_router(self) -> APIRouter:
        return self._router
