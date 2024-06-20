from uuid import UUID

from fastapi_pagination import LimitOffsetPage
from sqlalchemy.ext.asyncio import AsyncSession

from common import enums as common_enums
from common import schemas as common_schemas
from common.security import SecurityRole
from models import users as user_models
from schemas import users as user_schemas
from usecases.core import CoreUseCase


class UserUseCase(CoreUseCase):
    def __init__(self, pg_db: AsyncSession) -> None:
        super().__init__(pg_db)

    async def get_user_by_sid(self, user_sid: UUID) -> user_models.User:
        return await self._service.user.get_user_by_sid(
            sid=user_sid,
        )

    async def get_users(self) -> LimitOffsetPage[user_models.User]:
        return await self._service.user.get_users()

    async def update_me(
        self,
        current_user: user_schemas.CurrentUser,
        user_in: user_schemas.UserUpdate,
    ) -> user_models.User:
        user = await self._service.user.get_user_by_email(
            email=current_user.email
        )
        return await self._service.user.update_user(
            user=user,
            user_in=user_in,
        )

    async def update_user_active(
        self,
        current_user: user_schemas.CurrentUser,
        user_sid: UUID,
        is_active: bool,
    ) -> user_models.User:
        user = await self._service.user.get_user_by_sid(sid=user_sid)
        SecurityRole.validate_role_branch(
            current_role_label=current_user.role_label,
            target_role_label=user.role_label,
        )
        return await self._service.user.update_user_active(
            user=user,
            is_active=is_active,
        )

    async def update_user_verify(
        self,
        current_user: user_schemas.CurrentUser,
        user_sid: UUID,
        is_verify: bool,
    ) -> user_models.User:
        user = await self._service.user.get_user_by_sid(sid=user_sid)
        SecurityRole.validate_role_branch(
            current_role_label=current_user.role_label,
            target_role_label=user.role_label,
        )
        return await self._service.user.update_user_verify(
            user=user,
            is_verify=is_verify,
        )

    async def update_user(
        self,
        current_user: user_schemas.CurrentUser,
        user_sid: UUID,
        user_in: user_schemas.UserUpdate,
    ) -> user_models.User:
        user = await self._service.user.get_user_by_sid(sid=user_sid)
        SecurityRole.validate_role_branch(
            current_role_label=current_user.role_label,
            target_role_label=user.role_label,
        )
        return await self._service.user.update_user(
            user=user,
            user_in=user_in,
        )

    async def create_user(
        self, user_in: user_schemas.UserCreate
    ) -> user_models.User:
        await self._service.user.get_user_by_email(
            email=user_in.email, is_exists=False
        )
        await self._service.security.get_role_by_label(
            label=user_in.role_label
        )
        return await self._service.user.create_user(user_in=user_in)

    async def remove_user(
        self,
        current_user: user_schemas.CurrentUser,
        user_sid: UUID,
    ) -> common_schemas.Msg:
        user = await self._service.user.get_user_by_sid(sid=user_sid)
        SecurityRole.validate_role_branch(
            current_role_label=current_user.role_label,
            target_role_label=user.role_label,
        )
        await self._service.user.remove_user(user=user)
        return common_schemas.Msg(msg=common_enums.ResponseMessages.SUCCESS)
