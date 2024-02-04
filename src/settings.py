import os
from dotenv import load_dotenv
from sys import platform

load_dotenv(
    os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.pardir)), ".env.local")
)


def get_local_host():
    match platform:
        case "linux" | "darwin":
            return "0.0.0.0"
        case "win32":
            return "localhost"
        case _:
            raise OSError("Unsupported platform")


HOST = os.getenv("HOST", get_local_host())
PORT: int = int(os.getenv("PORT", 8000))

POSTGRES_DB: str = os.getenv("POSTGRES_DB", "events")
POSTGRES_USER: str = os.getenv("POSTGRES_USER", "user")
POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "password")
POSTGRES_HOST: str = os.getenv("POSTGRES_HOST", get_local_host())
POSTGRES_PORT: int = int(os.getenv("POSTGRES_PORT", "5432"))
