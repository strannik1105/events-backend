from common.api.crud_api import CrudApi
from common.singleton import Singleton
from events.schemas.event import EventSchema, EventCreateSchema
from events.services.event_service import EventService


class EventApi(CrudApi, Singleton):
    def __init__(self) -> None:
        super().__init__(
            EventService.get_instance(),
            get_schema=EventSchema,
            create_schema=EventCreateSchema,
        )
