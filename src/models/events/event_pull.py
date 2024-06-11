from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from common.db import PostgresBaseModel, PostgresDBSchemas
from models.mixins import DateTimeMixin


EVENTS_SCHEMA = PostgresDBSchemas.EVENTS
USERS_SCHEMA = PostgresDBSchemas.USERS
SECURITY_SCHEMA = PostgresDBSchemas.SECURITY


class EventPull(PostgresBaseModel, DateTimeMixin):
    __tablename__ = "event_pull"
    __table_args__ = {
        "schema": EVENTS_SCHEMA,
        "comment": "Table with all event pulls",
    }

    user_sid: Mapped[UUID] = mapped_column(
        ForeignKey(f"{USERS_SCHEMA}.user.sid", ondelete="CASCADE"),
        index=True,
        comment="User SID",
    )
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
    event_role_sid: Mapped[UUID] = mapped_column(
        ForeignKey(f"{SECURITY_SCHEMA}.role.sid", ondelete="CASCADE"),
        index=True,
        comment="Event role SID",
    )
