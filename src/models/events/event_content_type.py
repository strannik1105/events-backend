from sqlalchemy.orm import Mapped, mapped_column

from common.db import PostgresBaseModel, PostgresDBSchemas
from models.mixins import DateTimeMixin


EVENTS_SCHEMA = PostgresDBSchemas.EVENTS


class EventContentType(PostgresBaseModel, DateTimeMixin):
    __tablename__ = "event_content_type"
    __table_args__ = {
        "schema": EVENTS_SCHEMA,
        "comment": "Table with all event content types",
    }

    name: Mapped[str] = mapped_column(comment="Event content type name")
    description: Mapped[str] = mapped_column(
        comment="Event content type description"
    )
