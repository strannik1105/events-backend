from common.services.crud_service import CrudService
from common.singleton import Singleton
from events.repository.event_type_repository import EventTypeRepository


class EventTypeService(CrudService, Singleton):
    def __init__(self):
        super().__init__(EventTypeRepository.get_instance())
