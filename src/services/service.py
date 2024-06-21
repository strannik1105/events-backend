from sqlalchemy.ext.asyncio import AsyncSession

from interfaces.services import IService
from interfaces.services.auth import IAuthService
from interfaces.services.events import IEventService
from interfaces.services.metrics import IMetricService
from interfaces.services.security import ISecurityService
from interfaces.services.users import IUserService

from .auth import AuthService
from .events import EventService
from .metrics import MetricService
from .security import SecurityService
from .users import UserService


class Service(IService):
    def __init__(self, pg_db: AsyncSession) -> None:
        self._auth = AuthService(pg_db)
        self._event = EventService(pg_db)
        self._metric = MetricService(pg_db)
        self._security = SecurityService(pg_db)
        self._user = UserService(pg_db)

    @property
    def auth(self) -> IAuthService:
        return self._auth

    @property
    def event(self) -> IEventService:
        return self._event

    @property
    def metric(self) -> IMetricService:
        return self._metric

    @property
    def security(self) -> ISecurityService:
        return self._security

    @property
    def user(self) -> IUserService:
        return self._user
