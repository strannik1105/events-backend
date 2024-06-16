from sqlalchemy.ext.asyncio import AsyncSession

from .auth import AuthUseCase
from .events import EventUseCase
from .metrics import MetricUseCase
from .security import SecurityUseCase
from .users import UserUseCase


class UseCase:
    def __init__(self, pg_db: AsyncSession) -> None:
        self._auth = AuthUseCase(pg_db)
        self._event = EventUseCase(pg_db)
        self._metric = MetricUseCase(pg_db)
        self._security = SecurityUseCase(pg_db)
        self._user = UserUseCase(pg_db)

    @property
    def auth(self) -> AuthUseCase:
        return self._auth

    @property
    def event(self) -> EventUseCase:
        return self._event

    @property
    def metric(self) -> MetricUseCase:
        return self._metric

    @property
    def security(self) -> SecurityUseCase:
        return self._security

    @property
    def user(self) -> UserUseCase:
        return self._user
