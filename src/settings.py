import os
from dotenv import load_dotenv


load_dotenv(os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.pardir)), ".env"))


class Settings:
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", 1234))
