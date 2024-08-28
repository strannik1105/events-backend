import uvicorn

from app.app import ApiRegistrator, AppMaker
from events.api.event import EventApi


def main() -> None:
    app = AppMaker().get_instance()()

    ApiRegistrator.register(app, EventApi.get_instance(), "event")

    uvicorn.run(app)


if __name__ == "__main__":
    main()
