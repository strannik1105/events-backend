from abc import ABCMeta, abstractmethod

from filters import security as security_filters
from interfaces.usecases.core import ICoreUseCase
from models import security as security_models


class ISecurityUseCase(ICoreUseCase, metaclass=ABCMeta):
    @abstractmethod
    async def get_role_by_label(self, role_label: int) -> security_models.Role:
        raise NotImplementedError

    @abstractmethod
    async def get_roles(
        self, filter_params: security_filters.RoleFilter
    ) -> list[security_models.Role]:
        raise NotImplementedError
