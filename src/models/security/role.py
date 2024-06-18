from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from common.db.postgres import PostgresBaseModel, PostgresDBSchemas
from models.mixins import DateTimeMixin, Label


if TYPE_CHECKING:
    from models.security import RoleXPermission  # noqa: F401
    from models.users import User  # noqa: F401


SECURITY_SCHEMA = PostgresDBSchemas.SECURITY


class Role(PostgresBaseModel, Label, DateTimeMixin):
    __tablename__ = "role"
    __table_args__ = {
        "schema": SECURITY_SCHEMA,
        "comment": "Table with all roles",
    }

    name: Mapped[str] = mapped_column(comment="Role name")
    description: Mapped[str] = mapped_column(comment="Role description")
    is_event: Mapped[bool] = mapped_column(comment="Role event status")

    users: Mapped[list["User"]] = relationship(back_populates="role")
    permissions: Mapped[list["RoleXPermission"]] = relationship(
        back_populates="role"
    )
