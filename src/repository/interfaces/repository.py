from abc import ABCMeta, abstractmethod

from .events import (
    IEventAddressRepository,
    IEventContentRepository,
    IEventContentTypeRepository,
    IEventFileRepository,
    IEventFileTypeRepository,
    IEventPullRepository,
    IEventRepository,
    IEventTypeRepository,
)
from .metrics import (
    IEventLikeRepository,
    IEventViewRepository,
    ISubscribeRepository,
)
from .security import (
    IResourceRepository,
    IRoleRepository,
    IRoleXResourceRepository,
)
from .users import IUserRepository


class IRepository(metaclass=ABCMeta):
    @property
    @abstractmethod
    def event(self) -> IEventRepository:
        raise NotImplementedError

    @property
    @abstractmethod
    def event_address(self) -> IEventAddressRepository:
        raise NotImplementedError

    @property
    @abstractmethod
    def event_content(self) -> IEventContentRepository:
        raise NotImplementedError

    @property
    @abstractmethod
    def event_content_type(self) -> IEventContentTypeRepository:
        raise NotImplementedError

    @property
    @abstractmethod
    def event_file(self) -> IEventFileRepository:
        raise NotImplementedError

    @property
    @abstractmethod
    def event_file_type(self) -> IEventFileTypeRepository:
        raise NotImplementedError

    @property
    @abstractmethod
    def event_pull(self) -> IEventPullRepository:
        raise NotImplementedError

    @property
    @abstractmethod
    def event_type(self) -> IEventTypeRepository:
        raise NotImplementedError

    @property
    @abstractmethod
    def event_like(self) -> IEventLikeRepository:
        raise NotImplementedError

    @property
    @abstractmethod
    def event_view(self) -> IEventViewRepository:
        raise NotImplementedError

    @property
    @abstractmethod
    def subscribe(self) -> ISubscribeRepository:
        raise NotImplementedError

    @property
    @abstractmethod
    def role(self) -> IRoleRepository:
        raise NotImplementedError

    @property
    @abstractmethod
    def resource(self) -> IResourceRepository:
        raise NotImplementedError

    @property
    @abstractmethod
    def role_x_resource(self) -> IRoleXResourceRepository:
        raise NotImplementedError

    @property
    @abstractmethod
    def user(self) -> IUserRepository:
        raise NotImplementedError
