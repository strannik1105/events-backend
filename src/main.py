from app.app import ApiRegistrator, App
from events.api.event import EventApi


def main() -> None:
    app = App().get_instance()

    ApiRegistrator.register(app, EventApi.get_instance(), "event")

    app.run()


if __name__ == "__main__":
    main()
