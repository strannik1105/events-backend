from sqlalchemy.orm import Mapped, mapped_column

from common.db import PostgresBaseModel, PostgresDBSchemas
from models.mixins import DateTimeMixin


SECURITY_SCHEMA = PostgresDBSchemas.SECURITY


class Role(PostgresBaseModel, DateTimeMixin):
    __tablename__ = "role"
    __table_args__ = {
        "schema": SECURITY_SCHEMA,
        "comment": "Table with all roles",
    }

    name: Mapped[str] = mapped_column(comment="Role name")
    description: Mapped[str] = mapped_column(comment="Role description")
