from sqlalchemy.ext.asyncio import AsyncSession

from models.events import EventFileType
from repository.postgres.core import CoreRepository


class EventFileTypeRepository(CoreRepository[EventFileType]):
    def __init__(self, db: AsyncSession, model: type[EventFileType]) -> None:
        super().__init__(db, model)
