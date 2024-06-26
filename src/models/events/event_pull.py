from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import SMALLINT, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from common.db.postgres import PostgresBaseModel, PostgresDBSchemas
from models.mixins import DateTimeMixin, Sid


if TYPE_CHECKING:
    from models.security import Role  # noqa: F401


EVENTS_SCHEMA = PostgresDBSchemas.EVENTS
USERS_SCHEMA = PostgresDBSchemas.USERS
SECURITY_SCHEMA = PostgresDBSchemas.SECURITY


class EventPull(PostgresBaseModel, Sid, DateTimeMixin):
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
    event_content_sid: Mapped[UUID | None] = mapped_column(
        ForeignKey(f"{EVENTS_SCHEMA}.event_content.sid", ondelete="CASCADE"),
        index=True,
        comment="Event content SID",
    )
    event_role_label: Mapped[int] = mapped_column(
        SMALLINT,
        ForeignKey(f"{SECURITY_SCHEMA}.role.label", ondelete="CASCADE"),
        index=True,
        comment="Event role label",
    )

    role: Mapped["Role"] = relationship(back_populates="event_pulls")
