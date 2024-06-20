from typing import TYPE_CHECKING

from sqlalchemy import SMALLINT, VARCHAR, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from common.db.postgres import PostgresBaseModel, PostgresDBSchemas
from models.mixins import DateTimeMixin, Sid


if TYPE_CHECKING:
    from models.security import Role  # noqa: F401


SECURITY_SCHEMA = PostgresDBSchemas.SECURITY


class RoleXResource(PostgresBaseModel, Sid, DateTimeMixin):
    __tablename__ = "role_x_resource"
    __table_args__ = {
        "schema": SECURITY_SCHEMA,
        "comment": "Table with all role resource permissions",
    }

    role_label: Mapped[int] = mapped_column(
        SMALLINT,
        ForeignKey(f"{SECURITY_SCHEMA}.role.label", ondelete="CASCADE"),
        index=True,
        comment="Role label",
    )
    resource_label: Mapped[int] = mapped_column(
        SMALLINT,
        ForeignKey(f"{SECURITY_SCHEMA}.resource.label", ondelete="CASCADE"),
        index=True,
        comment="Resource label",
    )
    permissions: Mapped[str] = mapped_column(
        VARCHAR(5), comment="Permissions of role resource"
    )

    role: Mapped[list["Role"]] = relationship(back_populates="permissions")
