from uuid import UUID

from fastapi import Body, Path, HTTPException

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
        self._service = service

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
            self._create_schema,
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
            return await self._service.get_all(limit, offset)

        return AsyncRouteCallback(callback)

    def _get_get_one_callback(self, sid: UUID = Path(...)):
        async def callback():
            pass

        return AsyncRouteCallback(callback)

    def _get_create_callback(self) -> AsyncRouteCallback:
        async def callback(obj: self._create_schema = Body(...)):
            await self._service.create(dict(obj))
            return self._create_schema(**dict(obj))

        return AsyncRouteCallback(callback)

    def _get_update_callback(self) -> AsyncRouteCallback:
        async def callback(sid: UUID, obj_changes: self._create_schema = Body(...)):
            obj = await self._service.get_one(sid)
            if obj is None:
                raise HTTPException(404, detail="Not Found")
            await self._service.update(dict(obj_changes), sid)
            res = dict(obj_changes)
            res["sid"] = sid
            return self._get_schema(**res)

        return AsyncRouteCallback(callback)

    def _get_delete_callback(self) -> AsyncRouteCallback:
        async def callback(sid: UUID):
            obj = await self._service.get_one(sid)
            if obj is None:
                raise HTTPException(404, detail="Not Found")
            await self._service.delete(obj)
            return self._get_schema(**obj.__dict__)

        return AsyncRouteCallback(callback)
