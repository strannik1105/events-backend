from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from models.events import Event
from repository.events import event as event_repository
from services import events
from common.db.session import get_pg_session
from services.crud_service.crud_service import CRUDService

PGSession = Annotated[AsyncSession, Depends(get_pg_session)]


def get_event_service():
    return events.EventService()


EventService = Annotated[events.EventService, Depends(get_event_service)]


def get_event_repository():
    return event_repository.EventRepository[Event](Event)


EventRepository = Annotated[
    event_repository.EventRepository, Depends(get_event_repository)
]

crud_service = CRUDService()


def get_crud_service():
    return crud_service
