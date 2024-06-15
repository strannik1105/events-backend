from sqlalchemy.ext.asyncio import AsyncSession

from models.metrics import EventView
from repository.postgres.core import CoreRepository


class EventViewRepository(CoreRepository[EventView]):
    def __init__(self, db: AsyncSession, model: EventView):
        super().__init__(db, model)
