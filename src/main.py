import uvicorn

from app.app import AppMaker


def main() -> None:
    app = AppMaker().get_instance()()
    uvicorn.run(app)


if __name__ == "__main__":
    main()
