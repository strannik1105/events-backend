from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from common.db.session import get_pg_session
from models.events import Event
from models.users import User
from repository.auth.auth_repository import AuthRepository
from repository.events import event as event_repository
from repository.users import user as user_repository
from services import events
from services.auth.auth_service import AuthService
from services.crud_service.crud_service import CRUDService


PGSession = Annotated[AsyncSession, Depends(get_pg_session)]


def get_event_service():
    return events.EventService()


EventService = Annotated[events.EventService, Depends(get_event_service)]


def get_event_repository():
    return event_repository.EventRepository[Event](Event)


def get_user_repository():
    return user_repository.UserRepository[User](User)


auth_repository = AuthRepository()


def get_auth_repository() -> AuthRepository:
    return auth_repository


auth_service = AuthService(auth_repository)


def get_auth_service() -> AuthService:
    return auth_service


EventRepository = Annotated[
    event_repository.EventRepository, Depends(get_event_repository)
]

crud_service = CRUDService()


def get_crud_service():
    return crud_service


UserRepository = Annotated[
    user_repository.UserRepository, Depends(get_user_repository)
]
