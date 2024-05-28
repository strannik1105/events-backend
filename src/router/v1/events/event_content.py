from typing import Optional, Annotated
from uuid import UUID

from common.repository.repository import AbstractRepository
from models.events import EventContent
from fastapi import APIRouter, Path, Depends

from router import deps
from router.deps import get_crud_service
from router.v1.events.schemas import EventContentSchema, EventContentCreateSchema, EventContentUpdateSchema
from services.crud_service.crud_service import CRUDService

router = APIRouter()

MODEL = EventContent
GET_SCHEMA = EventContentSchema
CREATE_SCHEMA = EventContentCreateSchema
UPDATE_SCHEMA = EventContentUpdateSchema


@router.get("/", response_model=Optional[list[GET_SCHEMA]])
async def get_all(
        db_session: deps.PGSession,
        service: Annotated[CRUDService, Depends(get_crud_service)],
):
    repository = AbstractRepository[MODEL](MODEL)
    items = await service.get_all(db_session, repository)
    return items


@router.get("/{sid}", response_model=Optional[GET_SCHEMA])
async def get_by_sid(
        db_session: deps.PGSession,
        service: Annotated[CRUDService, Depends(get_crud_service)],
        sid: UUID = Path(...)
):
    repository = AbstractRepository[MODEL](MODEL)
    items = await service.get_by_sid(db_session, repository, sid)
    return items


@router.post("/", response_model=GET_SCHEMA)
async def create(
        db_session: deps.PGSession,
        service: Annotated[CRUDService, Depends(get_crud_service)],
        create_schema: CREATE_SCHEMA
):
    repository = AbstractRepository[MODEL](MODEL)
    item = await service.create(db_session, repository, MODEL, create_schema)
    return item


@router.put("/{sid}", response_model=GET_SCHEMA)
async def update(
        db_session: deps.PGSession,
        service: Annotated[CRUDService, Depends(get_crud_service)],
        update_schema: UPDATE_SCHEMA,
        sid: UUID = Path(...)
):
    repository = AbstractRepository[MODEL](MODEL)
    item = await service.update(db_session, repository, sid, update_schema)
    return item


@router.delete("/{sid}")
async def delete(
        db_session: deps.PGSession,
        service: Annotated[CRUDService, Depends(get_crud_service)],
        sid: UUID = Path(...)
):
    repository = AbstractRepository[MODEL](MODEL)
    item = await service.delete(db_session, repository, sid)
    return item
