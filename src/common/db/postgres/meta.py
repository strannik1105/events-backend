from sqlalchemy.sql.schema import MetaData

from models.events import *  # noqa: F403
from models.metrics import *  # noqa: F403
from models.security import *  # noqa: F403
from models.users import *  # noqa: F403

from .base import PostgresBaseModel


class PostgresMetadata:
    @staticmethod
    def get() -> MetaData:
        return PostgresBaseModel.metadata
