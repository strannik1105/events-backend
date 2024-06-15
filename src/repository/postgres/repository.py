from events import (
    EventAddressRepository,
    EventContentRepository,
    EventContentTypeRepository,
    EventFileRepository,
    EventFileTypeRepository,
    EventPullRepository,
    EventRepository,
    EventTypeRepository,
)
from sqlalchemy.ext.asyncio import AsyncSession

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
from models.security import Permission, Role, RoleXPermission
from models.users import User

from .metrics import (
    EventLikeRepository,
    EventViewRepository,
    SubscribeRepository,
)
from .security import (
    PermissionRepository,
    RoleRepository,
    RoleXPermissionRepository,
)
from .users import UserRepository


class PostgresRepository:
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
        self._permission = PermissionRepository(db=db, model=Permission)
        self._role_x_permission = RoleXPermissionRepository(
            db=db, model=RoleXPermission
        )

        self._user = UserRepository(db=db, model=User)

    @property
    def event(self) -> EventRepository:
        return self._event

    @property
    def event_address(self) -> EventAddressRepository:
        return self._event_address

    @property
    def event_content(self) -> EventContentRepository:
        return self._event_content

    @property
    def event_content_type(self) -> EventContentTypeRepository:
        return self._event_content_type

    @property
    def event_file(self) -> EventFileRepository:
        return self._event_file

    @property
    def event_file_type(self) -> EventFileTypeRepository:
        return self._event_file_type

    @property
    def event_pull(self) -> EventPullRepository:
        return self._event_pull

    @property
    def event_type(self) -> EventTypeRepository:
        return self._event_type

    @property
    def event_like(self) -> EventLikeRepository:
        return self._event_like

    @property
    def event_view(self) -> EventViewRepository:
        return self._event_view

    @property
    def subscribe(self) -> SubscribeRepository:
        return self._subscribe

    @property
    def role(self) -> RoleRepository:
        return self._role

    @property
    def permission(self) -> PermissionRepository:
        return self._permission

    @property
    def role_x_permission(self) -> RoleXPermissionRepository:
        return self._role_x_permission

    @property
    def user(self) -> UserRepository:
        return self._user
