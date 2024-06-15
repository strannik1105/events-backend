from sqlalchemy.ext.asyncio import AsyncSession

from models.events import EventPull
from repository.postgres.core import CoreRepository


class EventPullRepository(CoreRepository[EventPull]):
    def __init__(self, db: AsyncSession, model: EventPull):
        super().__init__(db, model)
