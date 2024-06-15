from sqlalchemy.ext.asyncio import AsyncSession

from models.events import Event
from repository.postgres.core import CoreRepository


class EventRepository(CoreRepository[Event]):
    def __init__(self, db: AsyncSession, model: Event):
        super().__init__(db, model)
