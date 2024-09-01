from typing import Any, Callable, Coroutine
from uuid import UUID

from fastapi import APIRouter, Body, Path

from common.api.abstract_api import AbstractApi
from common.schemas.schemas import BaseSchema
from common.services.abstract_crud_service import AbstractCrudService
from events.models.event import EventModel


class CrudApi(AbstractApi):
    def __init__(self, service: AbstractCrudService, *, get_schema: BaseSchema = None, create_schema: BaseSchema = None) -> None:
        self._router = APIRouter()
        self._servive = service

        self._get_schema = get_schema
        self._create_schema = create_schema

        self.register_handlers()

    @property
    def router(self) -> APIRouter:
        return self._router

    def register_handlers(self) -> None:
        self._get_all()
        self._get_one()
        self._create()

    def _get_all(self):
        async def callback(limit: int = 100, offset: int = 0):
            return await self._servive.get_all(limit, offset)
        
        self._router.add_api_route("/get_all", callback, methods=["GET"], response_model=list[self._get_schema] if self._get_schema is not None else None)

    def _get_one(self, sid: UUID = Path(...)):
        async def callback():
            pass
            
        self._router.add_api_route("/get/{sid}", callback)

    def _create(self) -> Callable[..., Coroutine[Any, Any, None]]:
        async def callback(obj: self._create_schema = Body(...)):
            return await self._servive.create(EventModel(**dict(obj)))

        self._router.add_api_route("/create", callback, methods=["POST"], response_model=self._get_schema)
    
    def _update(self, sid: UUID = Path(...)):
        pass

    def _delete(self, sid: UUID = Path(...)):
        pass
