from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.base import ExecutableOption

from config.exceptions import APIException
from filters import security as security_filters
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
        role = await self.repository.role.get_by_label(
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

    async def get_resource_by_label(
        self,
        label: int,
        validate: bool = True,
        is_exists: bool = True,
        is_rollback: bool = False,
        custom_options: list[ExecutableOption] | None = None,
    ) -> security_models.Resource | None:
        permission = await self.repository.resource.get_by_label(
            label=label, custom_options=custom_options
        )
        if validate:
            await self._utils.exists_validate(
                obj=permission,
                is_exists=is_exists,
                is_rollback=is_rollback,
                exists_exception=APIException.resource_already_exists,
                not_found_exception=APIException.resource_not_found,
            )
        return permission

    async def get_role_x_resource_by_labels(
        self,
        role_label: int,
        resource_label: int,
        validate: bool = True,
        is_exists: bool = True,
        is_rollback: bool = False,
        custom_options: list[ExecutableOption] | None = None,
    ) -> security_models.RoleXResource | None:
        role_x_permission = (
            await self.repository.role_x_resource.get_by_labels(
                role_label=role_label,
                resource_label=resource_label,
                custom_options=custom_options,
            )
        )
        if validate:
            await self._utils.exists_validate(
                obj=role_x_permission,
                is_exists=is_exists,
                is_rollback=is_rollback,
                exists_exception=APIException.role_x_resource_already_exists,
                not_found_exception=APIException.role_x_resource_not_found,
            )
        return role_x_permission

    async def get_roles(
        self, filter_params: security_filters.RoleFilter
    ) -> list[security_models.Role]:
        return await self.repository.role.get_all_by_filter(
            filter_params=filter_params
        )

    async def create_role(
        self, role_in: security_schemas.RoleCreate, with_commit: bool = True
    ) -> security_models.Role:
        return await self.repository.role.create(
            obj_in=role_in,
            with_commit=with_commit,
        )

    async def create_resource(
        self,
        resource_in: security_schemas.ResourceCreate,
        with_commit: bool = True,
    ) -> security_models.Resource:
        return await self.repository.resource.create(
            obj_in=resource_in,
            with_commit=with_commit,
        )

    async def create_role_x_resource(
        self,
        role_x_resource_in: security_schemas.RoleXResourceCreate,
        with_commit: bool = True,
    ) -> security_models.RoleXResource:
        return await self.repository.role_x_resource.create(
            obj_in=role_x_resource_in,
            with_commit=with_commit,
        )
