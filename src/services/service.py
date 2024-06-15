from sqlalchemy.ext.asyncio import AsyncSession

from .events import EventService
from .metrics import MetricService
from .security import SecurityService
from .users import UserService


class Service:
    def __init__(self, pg_db: AsyncSession) -> None:
        self._event = EventService(pg_db)
        self._metric = MetricService(pg_db)
        self._security = SecurityService(pg_db)
        self._user = UserService(pg_db)

    @property
    def event(self) -> EventService:
        return self._event

    @property
    def metric(self) -> MetricService:
        return self._metric

    @property
    def security(self) -> SecurityService:
        return self._security

    @property
    def user(self) -> UserService:
        return self._user
