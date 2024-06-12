from sqlalchemy import SMALLINT, VARCHAR, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from common.db.postgres import PostgresBaseModel, PostgresDBSchemas
from models.mixins import DateTimeMixin, Sid


SECURITY_SCHEMA = PostgresDBSchemas.SECURITY


class RoleXPermission(PostgresBaseModel, Sid, DateTimeMixin):
    __tablename__ = "role_x_permission"
    __table_args__ = {
        "schema": SECURITY_SCHEMA,
        "comment": "Table with all role permissions",
    }

    role_label: Mapped[int] = mapped_column(
        SMALLINT,
        ForeignKey(f"{SECURITY_SCHEMA}.role.label", ondelete="CASCADE"),
        index=True,
        comment="Role label",
    )
    permission_label: Mapped[int] = mapped_column(
        SMALLINT,
        ForeignKey(f"{SECURITY_SCHEMA}.permission.label", ondelete="CASCADE"),
        index=True,
        comment="Permission label",
    )
    access_actions: Mapped[str] = mapped_column(
        VARCHAR(5), comment="Access actions of role permission"
    )
