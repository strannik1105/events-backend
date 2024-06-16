from sqlalchemy.ext.asyncio import AsyncSession

from models.metrics import EventView
from repository.postgres.core import CoreRepository


class EventViewRepository(CoreRepository[EventView]):
    def __init__(self, db: AsyncSession, model: type[EventView]) -> None:
        super().__init__(db, model)
