from sqlalchemy.ext.asyncio import AsyncSession

from interfaces.repository import IRepository
from interfaces.repository.events import (
    IEventAddressRepository,
    IEventContentRepository,
    IEventContentTypeRepository,
    IEventFileRepository,
    IEventFileTypeRepository,
    IEventPullRepository,
    IEventRepository,
    IEventTypeRepository,
)
from interfaces.repository.metrics import (
    IEventLikeRepository,
    IEventViewRepository,
    ISubscribeRepository,
)
from interfaces.repository.security import (
    IResourceRepository,
    IRoleRepository,
    IRoleXResourceRepository,
)
from interfaces.repository.users import IUserRepository
from models.events import (
    Event,
    EventAddress,
    EventContent,
    EventContentType,
    EventFile,
    EventFileType,
    EventPull,
    EventType,
)
from models.metrics import EventLike, EventView, Subscribe
from models.security import Resource, Role, RoleXResource
from models.users import User

from .events import (
    EventAddressRepository,
    EventContentRepository,
    EventContentTypeRepository,
    EventFileRepository,
    EventFileTypeRepository,
    EventPullRepository,
    EventRepository,
    EventTypeRepository,
)
from .metrics import (
    EventLikeRepository,
    EventViewRepository,
    SubscribeRepository,
)
from .security import (
    ResourceRepository,
    RoleRepository,
    RoleXResourceRepository,
)
from .users import UserRepository


class PostgresRepository(IRepository):
    def __init__(self, db: AsyncSession) -> None:
        self._event = EventRepository(db=db, model=Event)
        self._event_address = EventAddressRepository(db=db, model=EventAddress)
        self._event_content = EventContentRepository(db=db, model=EventContent)
        self._event_content_type = EventContentTypeRepository(
            db=db, model=EventContentType
        )
        self._event_file = EventFileRepository(db=db, model=EventFile)
        self._event_file_type = EventFileTypeRepository(
            db=db, model=EventFileType
        )
        self._event_pull = EventPullRepository(db=db, model=EventPull)
        self._event_type = EventTypeRepository(db=db, model=EventType)

        self._event_like = EventLikeRepository(db=db, model=EventLike)
        self._event_view = EventViewRepository(db=db, model=EventView)
        self._subscribe = SubscribeRepository(db=db, model=Subscribe)

        self._role = RoleRepository(db=db, model=Role)
        self._resource = ResourceRepository(db=db, model=Resource)
        self._role_x_resource = RoleXResourceRepository(
            db=db, model=RoleXResource
        )

        self._user = UserRepository(db=db, model=User)

    @property
    def event(self) -> IEventRepository:
        return self._event

    @property
    def event_address(self) -> IEventAddressRepository:
        return self._event_address

    @property
    def event_content(self) -> IEventContentRepository:
        return self._event_content

    @property
    def event_content_type(self) -> IEventContentTypeRepository:
        return self._event_content_type

    @property
    def event_file(self) -> IEventFileRepository:
        return self._event_file

    @property
    def event_file_type(self) -> IEventFileTypeRepository:
        return self._event_file_type

    @property
    def event_pull(self) -> IEventPullRepository:
        return self._event_pull

    @property
    def event_type(self) -> IEventTypeRepository:
        return self._event_type

    @property
    def event_like(self) -> IEventLikeRepository:
        return self._event_like

    @property
    def event_view(self) -> IEventViewRepository:
        return self._event_view

    @property
    def subscribe(self) -> ISubscribeRepository:
        return self._subscribe

    @property
    def role(self) -> IRoleRepository:
        return self._role

    @property
    def resource(self) -> IResourceRepository:
        return self._resource

    @property
    def role_x_resource(self) -> IRoleXResourceRepository:
        return self._role_x_resource

    @property
    def user(self) -> IUserRepository:
        return self._user
