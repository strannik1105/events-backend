from common.api.crud_api import CrudApi
from common.singleton import Singleton
from events.schemas.event_content_type import EventContentTypeBaseSchema, EventContentTypeCreateSchema
from events.services.event_content_type_service import EventContentTypeService


class EventContentTypeApi(CrudApi, Singleton):
    def __init__(self):
        super().__init__(
            EventContentTypeService.get_instance(),
            get_schema=EventContentTypeBaseSchema,
            create_schema=EventContentTypeCreateSchema
        )