from sqlalchemy.ext.asyncio import AsyncSession

from models.events import EventFile
from repository.postgres.core import CoreRepository


class EventFileRepository(CoreRepository[EventFile]):
    def __init__(self, db: AsyncSession, model: type[EventFile]) -> None:
        super().__init__(db, model)
