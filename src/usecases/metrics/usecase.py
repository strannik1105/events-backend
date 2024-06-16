from sqlalchemy.ext.asyncio import AsyncSession

from usecases.core import CoreUseCase


class MetricUseCase(CoreUseCase):
    def __init__(self, pg_db: AsyncSession) -> None:
        super().__init__(pg_db)
