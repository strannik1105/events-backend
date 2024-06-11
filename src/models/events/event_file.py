from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from common.db import PostgresBaseModel, PostgresDBSchemas
from models.mixins import DateTimeMixin


EVENTS_SCHEMA = PostgresDBSchemas.EVENTS


class EventFile(PostgresBaseModel, DateTimeMixin):
    __tablename__ = "event_file"
    __table_args__ = {
        "schema": EVENTS_SCHEMA,
        "comment": "Table with all event files",
    }

    file_name: Mapped[str] = mapped_column(comment="Event file name")
    file_bytes: Mapped[int] = mapped_column(comment="Event file bytes")
    event_sid: Mapped[UUID] = mapped_column(
        ForeignKey(f"{EVENTS_SCHEMA}.event.sid", ondelete="CASCADE"),
        index=True,
        comment="Event SID",
    )
    event_content_sid: Mapped[UUID] = mapped_column(
        ForeignKey(f"{EVENTS_SCHEMA}.event_content.sid", ondelete="CASCADE"),
        index=True,
        comment="Event content SID",
    )
    type_sid: Mapped[UUID] = mapped_column(
        ForeignKey(f"{EVENTS_SCHEMA}.event_file_type.sid", ondelete="CASCADE"),
        index=True,
        comment="Event file type SID",
    )
