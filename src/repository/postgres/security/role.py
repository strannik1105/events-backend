from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.base import ExecutableOption

from filters import security as security_filters
from models.security import Role
from interfaces.repository.security import IRoleRepository
from repository.postgres.core import CoreRepository


class RoleRepository(IRoleRepository[Role], CoreRepository[Role]):
    def __init__(self, db: AsyncSession, model: type[Role]) -> None:
        super().__init__(db, model)

    async def get_all_by_filter(
        self,
        filter_params: security_filters.RoleFilter,
        custom_options: list[ExecutableOption] | None = None,
    ) -> list[Role]:
        filter_expression = None
        if filter_params.is_event is not None:
            filter_expression = self._model.is_event == filter_params.is_event
        return await self.get_all_by(
            filter_expression=filter_expression,
            custom_options=custom_options,
        )
