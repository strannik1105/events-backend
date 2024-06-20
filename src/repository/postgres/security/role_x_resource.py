from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.base import ExecutableOption

from models.security import RoleXResource
from repository.postgres.core import CoreRepository


class RoleXResourceRepository(CoreRepository[RoleXResource]):
    def __init__(self, db: AsyncSession, model: type[RoleXResource]) -> None:
        super().__init__(db, model)

    async def get_by_labels(
        self,
        role_label: int,
        resource_label: int,
        custom_options: list[ExecutableOption] | None = None,
    ) -> RoleXResource | None:
        return await self.get_by(
            filter_expression=(
                (self._model.role_label == role_label)
                & (self._model.resource_label == resource_label)
            ),
            custom_options=custom_options,
        )
