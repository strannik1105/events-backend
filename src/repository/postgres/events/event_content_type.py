from sqlalchemy.ext.asyncio import AsyncSession

from models.events import EventContentType
from repository.interfaces.events import IEventContentTypeRepository
from repository.postgres.core import CoreRepository


class EventContentTypeRepository(
    IEventContentTypeRepository[EventContentType],
    CoreRepository[EventContentType],
):
    def __init__(
        self, db: AsyncSession, model: type[EventContentType]
    ) -> None:
        super().__init__(db, model)
