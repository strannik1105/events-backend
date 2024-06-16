from sqlalchemy.orm import Mapped, mapped_column

from common.db.postgres import PostgresBaseModel, PostgresDBSchemas
from models.mixins import DateTimeMixin, Label


SECURITY_SCHEMA = PostgresDBSchemas.SECURITY


class Role(PostgresBaseModel, Label, DateTimeMixin):
    __tablename__ = "role"
    __table_args__ = {
        "schema": SECURITY_SCHEMA,
        "comment": "Table with all roles",
    }

    name: Mapped[str] = mapped_column(comment="Role name")
    description: Mapped[str] = mapped_column(comment="Role description")
