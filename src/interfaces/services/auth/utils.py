from abc import ABCMeta, abstractmethod

from interfaces.services.core import ICoreServiceUtils
from models import security as security_models


class IAuthServiceUtils(ICoreServiceUtils, metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def get_resource_permissions(role: security_models.Role) -> dict[int, str]:
        raise NotImplementedError
