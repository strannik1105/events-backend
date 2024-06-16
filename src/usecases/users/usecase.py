from sqlalchemy.ext.asyncio import AsyncSession

from models import users as user_models
from schemas import users as user_schemas
from usecases.core import CoreUseCase


class UserUseCase(CoreUseCase):
    def __init__(self, pg_db: AsyncSession) -> None:
        super().__init__(pg_db)

    async def create_user(
        self, user_in: user_schemas.UserCreate
    ) -> user_models.User:
        await self._service.user.get_user_by_email(
            email=user_in.email, is_exists=False
        )
        await self._service.security.get_role_by_label(
            label=user_in.role_label
        )
        return await self._service.user.create_user(user_in)
