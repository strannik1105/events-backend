from sqlalchemy.ext.asyncio import AsyncSession

from models.events import EventType
from repository.postgres.core import CoreRepository


class EventTypeRepository(CoreRepository[EventType]):
    def __init__(self, db: AsyncSession, model: type[EventType]) -> None:
        super().__init__(db, model)