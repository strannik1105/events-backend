from sqlalchemy.ext.asyncio import AsyncSession

from interfaces.usecases import IUseCase
from interfaces.usecases.auth import IAuthUseCase
from interfaces.usecases.events import IEventUseCase
from interfaces.usecases.metrics import IMetricUseCase
from interfaces.usecases.security import ISecurityUseCase
from interfaces.usecases.users import IUserUseCase

from .auth import AuthUseCase
from .events import EventUseCase
from .metrics import MetricUseCase
from .security import SecurityUseCase
from .users import UserUseCase


class UseCase(IUseCase):
    def __init__(self, pg_db: AsyncSession) -> None:
        self._auth = AuthUseCase(pg_db)
        self._event = EventUseCase(pg_db)
        self._metric = MetricUseCase(pg_db)
        self._security = SecurityUseCase(pg_db)
        self._user = UserUseCase(pg_db)

    @property
    def auth(self) -> IAuthUseCase:
        return self._auth

    @property
    def event(self) -> IEventUseCase:
        return self._event

    @property
    def metric(self) -> IMetricUseCase:
        return self._metric

    @property
    def security(self) -> ISecurityUseCase:
        return self._security

    @property
    def user(self) -> IUserUseCase:
        return self._user
