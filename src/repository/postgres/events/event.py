from sqlalchemy.ext.asyncio import AsyncSession

from interfaces.repository.events import IEventRepository
from models.events import Event
from repository.postgres.core import CoreRepository


class EventRepository(IEventRepository[Event], CoreRepository[Event]):
    def __init__(self, db: AsyncSession, model: type[Event]) -> None:
        super().__init__(db, model)
