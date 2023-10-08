import os
from dotenv import load_dotenv


load_dotenv(os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.pardir)), ".env"))


HOST = os.getenv("HOST", "0.0.0.0")
PORT: int = int(os.getenv("PORT", 8000))

POSTGRES_DB: str = os.getenv("POSTGRES_DB")
POSTGRES_USER: str = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST: str = os.getenv("POSTGRES_HOST")
POSTGRES_PORT: int = int(os.getenv("POSTGRES_PORT"))
