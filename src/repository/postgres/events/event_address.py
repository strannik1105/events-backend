from sqlalchemy.ext.asyncio import AsyncSession

from interfaces.repository.events import IEventAddressRepository
from models.events import EventAddress
from repository.postgres.core import CoreRepository


class EventAddressRepository(
    IEventAddressRepository[EventAddress], CoreRepository[EventAddress]
):
    def __init__(self, db: AsyncSession, model: type[EventAddress]) -> None:
        super().__init__(db, model)
