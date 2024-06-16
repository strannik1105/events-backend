from common.db.postgres import PostgresSession
from common.managers import LoggerManager
from config.templates import EventTemplate
from services import Service


class EventInit:
    _logger = LoggerManager.get_base_logger()

    @classmethod
    async def set_event_file_types(cls) -> None:
        db = PostgresSession.get_async()
        service = Service(db)
        try:
            cls._logger.info("Start event file types init")
            event_file_types_in = EventTemplate.get_event_file_types()
            for event_file_type_in in event_file_types_in:
                event_file_type = (
                    await service.event.get_event_file_type_by_label(
                        label=event_file_type_in.label, validate=False
                    )
                )
                if not event_file_type:
                    await service.event.create_event_file_type(
                        event_file_type_in=event_file_type_in
                    )
            cls._logger.info("Finish event file types init")
        except Exception as exc:
            cls._logger.error(f"Event file types init error: {exc}")
        finally:
            await db.close()
