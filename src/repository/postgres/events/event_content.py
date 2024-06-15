from sqlalchemy.ext.asyncio import AsyncSession

from models.events import EventContent
from repository.postgres.core import CoreRepository


class EventContentRepository(CoreRepository[EventContent]):
    def __init__(self, db: AsyncSession, model: type[EventContent]) -> None:
        super().__init__(db, model)