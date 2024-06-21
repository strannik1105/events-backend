from sqlalchemy.ext.asyncio import AsyncSession

from interfaces.repository.metrics import IEventLikeRepository
from models.metrics import EventLike
from repository.postgres.core import CoreRepository


class EventLikeRepository(
    IEventLikeRepository[EventLike], CoreRepository[EventLike]
):
    def __init__(self, db: AsyncSession, model: type[EventLike]) -> None:
        super().__init__(db, model)
