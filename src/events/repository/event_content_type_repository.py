from common.db.session import PostgresSession
from common.repository.crud_repository import CrudRepository
from common.singleton import Singleton
from events.models.event_content_type import EventContentTypeModel


class EventTypeTypeRepository(CrudRepository, Singleton):
    def __init__(self) -> None:
        super().__init__(PostgresSession.get_instance(), EventContentTypeModel)
