from sqlalchemy.ext.asyncio import AsyncSession

from models.metrics import EventLike
from repository.postgres.core import CoreRepository


class EventLikeRepository(CoreRepository[EventLike]):
    def __init__(self, db: AsyncSession, model: type[EventLike]) -> None:
        super().__init__(db, model)
