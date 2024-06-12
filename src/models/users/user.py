from datetime import datetime

from sqlalchemy import BIGINT, SMALLINT, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from common.db.postgres import PostgresBaseModel, PostgresDBSchemas
from models.mixins import DateTimeMixin, Sid


USERS_SCHEMA = PostgresDBSchemas.USERS
SECURITY_SCHEMA = PostgresDBSchemas.SECURITY


class User(PostgresBaseModel, Sid, DateTimeMixin):
    __tablename__ = "user"
    __table_args__ = {
        "schema": USERS_SCHEMA,
        "comment": "Table with all users",
    }

    first_name: Mapped[str] = mapped_column(comment="User first name")
    middle_name: Mapped[str | None] = mapped_column(comment="User middle name")
    last_name: Mapped[str] = mapped_column(comment="User last name")
    email: Mapped[str] = mapped_column(unique=True, comment="User email")
    hashed_password: Mapped[str] = mapped_column(
        comment="User hashed password"
    )
    telegram_id: Mapped[int | None] = mapped_column(
        BIGINT, unique=True, comment="User telegram id"
    )
    is_active: Mapped[bool] = mapped_column(
        default=True, server_default="true", comment="User active status"
    )
    is_verified: Mapped[bool] = mapped_column(
        default=False, server_default="false", comment="User verified status"
    )
    last_login_at: Mapped[datetime | None] = mapped_column(
        DateTime(), comment="User last login at"
    )
    role_label: Mapped[int] = mapped_column(
        SMALLINT,
        ForeignKey(f"{SECURITY_SCHEMA}.role.label", ondelete="CASCADE"),
        index=True,
        comment="Role label",
    )
