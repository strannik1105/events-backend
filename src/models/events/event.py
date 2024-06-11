from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from common.db import PostgresBaseModel, PostgresDBSchemas
from models.mixins import DateTimeMixin


EVENTS_SCHEMA = PostgresDBSchemas.EVENTS


class Event(PostgresBaseModel, DateTimeMixin):
    __tablename__ = "event"
    __table_args__ = {
        "schema": EVENTS_SCHEMA,
        "comment": "Table with all events",
    }

    name: Mapped[str] = mapped_column(comment="Event name")
    description: Mapped[str] = mapped_column(comment="Event description")
    type_sid: Mapped[UUID] = mapped_column(
        ForeignKey(f"{EVENTS_SCHEMA}.event_type.sid", ondelete="CASCADE"),
        index=True,
        comment="Event type SID",
    )
