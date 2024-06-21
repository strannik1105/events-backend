from sqlalchemy.ext.asyncio import AsyncSession

from filters import security as security_filters
from interfaces.usecases.security import ISecurityUseCase
from models import security as security_models
from usecases.core import CoreUseCase


class SecurityUseCase(ISecurityUseCase, CoreUseCase):
    def __init__(self, pg_db: AsyncSession) -> None:
        super().__init__(pg_db)

    async def get_role_by_label(self, role_label: int) -> security_models.Role:
        return await self.service.security.get_role_by_label(label=role_label)

    async def get_roles(
        self, filter_params: security_filters.RoleFilter
    ) -> list[security_models.Role]:
        return await self.service.security.get_roles(
            filter_params=filter_params
        )
