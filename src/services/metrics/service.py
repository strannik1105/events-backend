from sqlalchemy.ext.asyncio import AsyncSession

from interfaces.services.metrics import IMetricService
from services.core import CoreService


class MetricService(IMetricService, CoreService):
    def __init__(self, pg_db: AsyncSession) -> None:
        super().__init__(pg_db)
