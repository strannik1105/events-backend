from abc import ABCMeta

from interfaces.services.core import ICoreServiceUtils


class IUserServiceUtils(ICoreServiceUtils, metaclass=ABCMeta):
    pass
