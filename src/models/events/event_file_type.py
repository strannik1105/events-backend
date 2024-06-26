from sqlalchemy.orm import Mapped, mapped_column

from common.db.postgres import PostgresBaseModel, PostgresDBSchemas
from models.mixins import DateTimeMixin, Label


EVENTS_SCHEMA = PostgresDBSchemas.EVENTS


class EventFileType(PostgresBaseModel, Label, DateTimeMixin):
    __tablename__ = "event_file_type"
    __table_args__ = {
        "schema": EVENTS_SCHEMA,
        "comment": "Table with all event file types",
    }

    name: Mapped[str] = mapped_column(comment="Event file type name")
    description: Mapped[str] = mapped_column(
        comment="Event file type description"
    )
