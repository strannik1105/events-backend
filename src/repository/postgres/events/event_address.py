from sqlalchemy.ext.asyncio import AsyncSession

from models.events import EventAddress
from repository.postgres.core import CoreRepository


class EventAddressRepository(CoreRepository[EventAddress]):
    def __init__(self, db: AsyncSession, model: type[EventAddress]) -> None:
        super().__init__(db, model)
