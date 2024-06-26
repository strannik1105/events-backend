from sqlalchemy.ext.asyncio import AsyncSession

from interfaces.repository.metrics import ISubscribeRepository
from models.metrics import Subscribe
from repository.postgres.core import CoreRepository


class SubscribeRepository(
    ISubscribeRepository[Subscribe], CoreRepository[Subscribe]
):
    def __init__(self, db: AsyncSession, model: type[Subscribe]) -> None:
        super().__init__(db, model)
