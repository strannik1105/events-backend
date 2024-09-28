from app.app import ApiRegistrator, App
from events.api.event import EventApi
from events.api.event_type import EventTypeApi
from events.api.event_image import EventImageApi


def main() -> None:
    app = App().get_instance()

    ApiRegistrator.register(app, EventApi.get_instance(), "event")
    ApiRegistrator.register(app, EventTypeApi.get_instance(), "event_type")
    ApiRegistrator.register(app, EventImageApi.get_instance(), "event_image")

    app.run()


if __name__ == "__main__":
    main()
