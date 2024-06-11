from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from common.db import PostgresBaseModel, PostgresDBSchemas
from models.mixins import DateTimeMixin


SECURITY_SCHEMA = PostgresDBSchemas.SECURITY


class RoleXPermission(PostgresBaseModel, DateTimeMixin):
    __tablename__ = "role_x_permission"
    __table_args__ = {
        "schema": SECURITY_SCHEMA,
        "comment": "Table with all role permissions",
    }

    role_sid: Mapped[UUID] = mapped_column(
        ForeignKey(f"{SECURITY_SCHEMA}.role.sid", ondelete="CASCADE"),
        index=True,
        comment="Role SID",
    )
    permission_sid: Mapped[UUID] = mapped_column(
        ForeignKey(f"{SECURITY_SCHEMA}.permission.sid", ondelete="CASCADE"),
        index=True,
        comment="Permission SID",
    )
    access_actions: Mapped[str] = mapped_column(
        comment="Access actions of role permission"
    )
