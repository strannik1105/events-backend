from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from common.db.postgres import PostgresBaseModel, PostgresDBSchemas
from models.mixins import DateTimeMixin, Sid


EVENTS_SCHEMA = PostgresDBSchemas.EVENTS


class EventAddress(PostgresBaseModel, Sid, DateTimeMixin):
    __tablename__ = "event_address"
    __table_args__ = {
        "schema": EVENTS_SCHEMA,
        "comment": "Table with all event addresses",
    }

    address: Mapped[str] = mapped_column(comment="Event address")
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
    start_at: Mapped[datetime] = mapped_column(
        DateTime(), comment="Event start at"
    )
    end_at: Mapped[datetime] = mapped_column(
        DateTime(), comment="Event finish at"
    )
