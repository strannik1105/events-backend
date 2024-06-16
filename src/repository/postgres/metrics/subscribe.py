from sqlalchemy.ext.asyncio import AsyncSession

from models.metrics import Subscribe
from repository.postgres.core import CoreRepository


class SubscribeRepository(CoreRepository[Subscribe]):
    def __init__(self, db: AsyncSession, model: type[Subscribe]) -> None:
        super().__init__(db, model)
