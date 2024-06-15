from sqlalchemy.ext.asyncio import AsyncSession

from models.metrics import EventLike
from repository.postgres.core import CoreRepository


class EventLikeRepository(CoreRepository[EventLike]):
    def __init__(self, db: AsyncSession, model: EventLike):
        super().__init__(db, model)
