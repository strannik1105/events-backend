from sqlalchemy import SMALLINT, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from common.db.postgres import PostgresBaseModel, PostgresDBSchemas
from models.mixins import DateTimeMixin, Sid


EVENTS_SCHEMA = PostgresDBSchemas.EVENTS


class EventContent(PostgresBaseModel, Sid, DateTimeMixin):
    __tablename__ = "event_content"
    __table_args__ = {
        "schema": EVENTS_SCHEMA,
        "comment": "Table with all events content",
    }

    name: Mapped[str] = mapped_column(comment="Event name")
    description: Mapped[str] = mapped_column(comment="Event description")
    type_label: Mapped[int] = mapped_column(
        SMALLINT,
        ForeignKey(
            f"{EVENTS_SCHEMA}.event_content_type.label", ondelete="CASCADE"
        ),
        index=True,
        comment="Event content type label",
    )
