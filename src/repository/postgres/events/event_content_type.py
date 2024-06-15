from sqlalchemy.ext.asyncio import AsyncSession

from models.events import EventContentType
from repository.postgres.core import CoreRepository


class EventContentTypeRepository(CoreRepository[EventContentType]):
    def __init__(
        self, db: AsyncSession, model: type[EventContentType]
    ) -> None:
        super().__init__(db, model)
