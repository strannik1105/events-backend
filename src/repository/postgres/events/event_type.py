from sqlalchemy.ext.asyncio import AsyncSession

from models.events import EventType
from interfaces.repository.events import IEventTypeRepository
from repository.postgres.core import CoreRepository


class EventTypeRepository(
    IEventTypeRepository[EventType], CoreRepository[EventType]
):
    def __init__(self, db: AsyncSession, model: type[EventType]) -> None:
        super().__init__(db, model)
