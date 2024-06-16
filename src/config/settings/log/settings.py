from pydantic import Field

from ..core import EnvCoreSettings


class LogSettings(EnvCoreSettings):
    BASE_NAME: str = "EVENTS"
    BASE_LEVEL: str = Field(..., alias="BASE_LOG_LEVEL")
    BASE_FORMAT: str = "%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
