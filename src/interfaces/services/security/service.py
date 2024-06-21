from abc import ABCMeta, abstractmethod

from sqlalchemy.sql.base import ExecutableOption

from filters import security as security_filters
from interfaces.services.core import ICoreService
from models import security as security_models
from schemas import security as security_schemas


class ISecurityService(ICoreService, metaclass=ABCMeta):
    @abstractmethod
    async def get_role_by_label(
        self,
        label: int,
        validate: bool = True,
        is_exists: bool = True,
        is_rollback: bool = False,
        custom_options: list[ExecutableOption] | None = None,
    ) -> security_models.Role | None:
        raise NotImplementedError

    @abstractmethod
    async def get_resource_by_label(
        self,
        label: int,
        validate: bool = True,
        is_exists: bool = True,
        is_rollback: bool = False,
        custom_options: list[ExecutableOption] | None = None,
    ) -> security_models.Resource | None:
        raise NotImplementedError

    @abstractmethod
    async def get_role_x_resource_by_labels(
        self,
        role_label: int,
        resource_label: int,
        validate: bool = True,
        is_exists: bool = True,
        is_rollback: bool = False,
        custom_options: list[ExecutableOption] | None = None,
    ) -> security_models.RoleXResource | None:
        raise NotImplementedError

    @abstractmethod
    async def get_roles(
        self, filter_params: security_filters.RoleFilter
    ) -> list[security_models.Role]:
        raise NotImplementedError

    @abstractmethod
    async def create_role(
        self, role_in: security_schemas.RoleDTOCreate, with_commit: bool = True
    ) -> security_models.Role:
        raise NotImplementedError

    @abstractmethod
    async def create_resource(
        self,
        resource_in: security_schemas.ResourceDTOCreate,
        with_commit: bool = True,
    ) -> security_models.Resource:
        raise NotImplementedError

    @abstractmethod
    async def create_role_x_resource(
        self,
        role_x_resource_in: security_schemas.RoleXResourceDTOCreate,
        with_commit: bool = True,
    ) -> security_models.RoleXResource:
        raise NotImplementedError
