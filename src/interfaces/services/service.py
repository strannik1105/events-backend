from abc import ABCMeta, abstractmethod

from .auth import IAuthService
from .events import IEventService
from .metrics import IMetricService
from .security import ISecurityService
from .users import IUserService


class IService(metaclass=ABCMeta):
    @property
    @abstractmethod
    def auth(self) -> IAuthService:
        raise NotImplementedError

    @property
    @abstractmethod
    def event(self) -> IEventService:
        raise NotImplementedError

    @property
    @abstractmethod
    def metric(self) -> IMetricService:
        raise NotImplementedError

    @property
    @abstractmethod
    def security(self) -> ISecurityService:
        raise NotImplementedError

    @property
    @abstractmethod
    def user(self) -> IUserService:
        raise NotImplementedError
