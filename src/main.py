import uvicorn

from app.app import AppMaker
from events.api.event import EventApi


def main() -> None:
    app = AppMaker().get_instance()()
    app.include_router(EventApi.get_instance().router)
    uvicorn.run(app)


if __name__ == "__main__":
    main()
