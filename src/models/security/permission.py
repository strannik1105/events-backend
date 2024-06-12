from sqlalchemy.orm import Mapped, mapped_column

from common.db.postgres import PostgresBaseModel, PostgresDBSchemas
from models.mixins import DateTimeMixin, Label


SECURITY_SCHEMA = PostgresDBSchemas.SECURITY


class Permission(PostgresBaseModel, Label, DateTimeMixin):
    __tablename__ = "permission"
    __table_args__ = {
        "schema": SECURITY_SCHEMA,
        "comment": "Table with all permissions",
    }

    name: Mapped[str] = mapped_column(comment="Permission name")
    description: Mapped[str] = mapped_column(comment="Permission description")
