from common.services.crud_service import CrudService
from common.singleton import Singleton
from events.repository.event_repository import EventRepository


class EventService(CrudService, Singleton):
    def __init__(self):
        super().__init__(EventRepository.get_instance())
