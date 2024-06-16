from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.base import ExecutableOption

from models.security import RoleXPermission
from repository.postgres.core import CoreRepository


class RoleXPermissionRepository(CoreRepository[RoleXPermission]):
    def __init__(self, db: AsyncSession, model: type[RoleXPermission]) -> None:
        super().__init__(db, model)

    async def get_by_labels(
        self,
        role_label: int,
        permission_label: int,
        custom_options: list[ExecutableOption] | None = None,
    ) -> RoleXPermission | None:
        return await self.get_by(
            filter_expression=(
                (self._model.role_label == role_label)
                & (self._model.permission_label == permission_label)
            ),
            custom_options=custom_options,
        )
