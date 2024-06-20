from sqlalchemy.orm import Mapped, mapped_column

from common.db.postgres import PostgresBaseModel, PostgresDBSchemas
from models.mixins import DateTimeMixin, Label


SECURITY_SCHEMA = PostgresDBSchemas.SECURITY


class Resource(PostgresBaseModel, Label, DateTimeMixin):
    __tablename__ = "resource"
    __table_args__ = {
        "schema": SECURITY_SCHEMA,
        "comment": "Table with all resources",
    }

    name: Mapped[str] = mapped_column(comment="Resource name")
    description: Mapped[str] = mapped_column(comment="Resource description")
