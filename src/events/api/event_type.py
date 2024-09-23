from common.api.crud_api import CrudApi
from common.singleton import Singleton
from events.schemas.event_type import EventTypeBaseSchema, EventTypeCreateSchema
from events.services.event_type_service import EventTypeService


class EventTypeApi(CrudApi, Singleton):
    def __init__(self):
        super().__init__(
            EventTypeService.get_instance(),
            get_schema=EventTypeBaseSchema,
            create_schema=EventTypeCreateSchema
        )