from common.api.crud_api import CrudApi
from common.singleton import Singleton
from events.models.event import EventModel
from events.services.event_service import EventService


class EventApi(CrudApi, Singleton):
    def __init__(self) -> None:
        super().__init__(EventService.get_instance())

    async def _create(self):
        obj = EventModel()
        obj.name = "123"
        await self._servive.create(obj)
