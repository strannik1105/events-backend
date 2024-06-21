from sqlalchemy.ext.asyncio import AsyncSession

from interfaces.usecases.metrics import IMetricUseCase
from usecases.core import CoreUseCase


class MetricUseCase(IMetricUseCase, CoreUseCase):
    def __init__(self, pg_db: AsyncSession) -> None:
        super().__init__(pg_db)
