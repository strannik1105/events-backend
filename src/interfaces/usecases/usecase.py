from abc import ABCMeta, abstractmethod

from .auth import IAuthUseCase
from .events import IEventUseCase
from .metrics import IMetricUseCase
from .security import ISecurityUseCase
from .users import IUserUseCase


class IUseCase(metaclass=ABCMeta):
    @property
    @abstractmethod
    def auth(self) -> IAuthUseCase:
        raise NotImplementedError

    @property
    @abstractmethod
    def event(self) -> IEventUseCase:
        raise NotImplementedError

    @property
    @abstractmethod
    def metric(self) -> IMetricUseCase:
        raise NotImplementedError

    @property
    @abstractmethod
    def security(self) -> ISecurityUseCase:
        raise NotImplementedError

    @property
    @abstractmethod
    def user(self) -> IUserUseCase:
        raise NotImplementedError
