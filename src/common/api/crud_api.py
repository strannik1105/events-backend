from uuid import UUID

from fastapi import Body, Path

from common.api.abstract_api import AbstractApi
from common.enums.http_method import HttpMethod
from common.router.router import AsyncRouteCallback, Router
from common.schemas.schemas import BaseSchema
from common.services.abstract_crud_service import AbstractCrudService
from events.models.event import EventModel


class CrudApi(AbstractApi):
    def __init__(
        self,
        service: AbstractCrudService,
        *,
        get_schema: BaseSchema = None,
        create_schema: BaseSchema = None,
    ) -> None:
        self._router = Router()
        self._servive = service

        self._get_schema = get_schema
        self._create_schema = create_schema

        self.register_handlers()

    @property
    def router(self) -> Router:
        return self._router

    def register_handlers(self) -> None:
        self._router.register_async_handler(
            "/get_all",
            self._get_get_all_callback(),
            HttpMethod.GET,
            list[self._get_schema] if self._get_schema is not None else None,
        )
        self._router.register_async_handler(
            "/get_one",
            self._get_get_one_callback(),
            HttpMethod.GET,
            self._get_schema,
        )
        self._router.register_async_handler(
            "/create",
            self._get_create_callback(),
            HttpMethod.POST,
            self._get_schema,
        )
        self._router.register_async_handler(
            "/update",
            self._get_update_callback(),
            HttpMethod.PUT,
            self._get_schema,
        )
        self._router.register_async_handler(
            "/delete",
            self._get_delete_callback(),
            HttpMethod.DELETE,
            self._get_schema,
        )

    def _get_get_all_callback(self) -> AsyncRouteCallback:
        async def callback(limit: int = 100, offset: int = 0):
            return await self._servive.get_all(limit, offset)

        return AsyncRouteCallback(callback)

    def _get_get_one_callback(self, sid: UUID = Path(...)):
        async def callback():
            pass

        return AsyncRouteCallback(callback)

    def _get_create_callback(self) -> AsyncRouteCallback:
        async def callback(obj: self._create_schema = Body(...)):
            return await self._servive.create(EventModel(**dict(obj)))

        return AsyncRouteCallback(callback)

    def _get_update_callback(
        self, sid: UUID = Path(...)
    ) -> AsyncRouteCallback:
        async def callback(obj: self._create_schema = Body(...)):
            return await self._servive(sid)

        return AsyncRouteCallback(callback)

    def _get_delete_callback(
        self, sid: UUID = Path(...)
    ) -> AsyncRouteCallback:
        async def callback(obj: self._create_schema = Body(...)):
            return await self._servive.delete(sid)

        return AsyncRouteCallback(callback)
