from common.services.crud_service import CrudService
from common.singleton import Singleton
from events.repository.event_content_type_repository import EventContentTypeRepository


class EventContentTypeService(CrudService, Singleton):
    def __init__(self):
        super().__init__(EventContentTypeRepository.get_instance())
        