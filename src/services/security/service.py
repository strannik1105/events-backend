from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.base import ExecutableOption

from config.exceptions import APIException
from models import security as security_models
from schemas import security as security_schemas
from services.core import CoreService

from .utils import SecurityServiceUtils


class SecurityService(CoreService):
    def __init__(self, pg_db: AsyncSession) -> None:
        super().__init__(pg_db)
        self._utils = SecurityServiceUtils(pg_db)

    async def get_role_by_label(
        self,
        label: int,
        validate: bool = True,
        is_exists: bool = True,
        is_rollback: bool = False,
        custom_options: list[ExecutableOption] | None = None,
    ) -> security_models.Role | None:
        role = await self._pg_repository.role.get_by_label(
            label=label, custom_options=custom_options
        )
        if validate:
            await self._utils.exists_validate(
                obj=role,
                is_exists=is_exists,
                is_rollback=is_rollback,
                exists_exception=APIException.role_already_exists,
                not_found_exception=APIException.role_not_found,
            )
        return role

    async def get_permission_by_label(
        self,
        label: int,
        validate: bool = True,
        is_exists: bool = True,
        is_rollback: bool = False,
        custom_options: list[ExecutableOption] | None = None,
    ) -> security_models.Permission | None:
        permission = await self._pg_repository.permission.get_by_label(
            label=label, custom_options=custom_options
        )
        if validate:
            await self._utils.exists_validate(
                obj=permission,
                is_exists=is_exists,
                is_rollback=is_rollback,
                exists_exception=APIException.permission_already_exists,
                not_found_exception=APIException.permission_not_found,
            )
        return permission

    async def get_role_x_permission_by_labels(
        self,
        role_label: int,
        permission_label: int,
        validate: bool = True,
        is_exists: bool = True,
        is_rollback: bool = False,
        custom_options: list[ExecutableOption] | None = None,
    ) -> security_models.RoleXPermission | None:
        role_x_permission = (
            await self._pg_repository.role_x_permission.get_by_labels(
                role_label=role_label,
                permission_label=permission_label,
                custom_options=custom_options,
            )
        )
        if validate:
            await self._utils.exists_validate(
                obj=role_x_permission,
                is_exists=is_exists,
                is_rollback=is_rollback,
                exists_exception=APIException.role_x_permission_already_exists,
                not_found_exception=APIException.role_x_permission_not_found,
            )
        return role_x_permission

    async def create_role(
        self, role_in: security_schemas.RoleCreate, with_commit: bool = True
    ) -> security_models.Role:
        return await self._pg_repository.role.create(
            obj_in=role_in,
            with_commit=with_commit,
        )

    async def create_permission(
        self,
        permission_in: security_schemas.PermissionCreate,
        with_commit: bool = True,
    ) -> security_models.Permission:
        return await self._pg_repository.permission.create(
            obj_in=permission_in,
            with_commit=with_commit,
        )

    async def create_role_x_permission(
        self,
        role_x_permission_in: security_schemas.RoleXPermissionCreate,
        with_commit: bool = True,
    ) -> security_models.RoleXPermission:
        return await self._pg_repository.role_x_permission.create(
            obj_in=role_x_permission_in,
            with_commit=with_commit,
        )
