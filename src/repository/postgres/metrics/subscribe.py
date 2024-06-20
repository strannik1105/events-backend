from sqlalchemy.ext.asyncio import AsyncSession

from models.metrics import Subscribe
from repository.interfaces.metrics import ISubscribeRepository
from repository.postgres.core import CoreRepository


class SubscribeRepository(
    ISubscribeRepository[Subscribe], CoreRepository[Subscribe]
):
    def __init__(self, db: AsyncSession, model: type[Subscribe]) -> None:
        super().__init__(db, model)
