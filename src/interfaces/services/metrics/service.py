from abc import ABCMeta

from interfaces.services.core import ICoreService


class IMetricService(ICoreService, metaclass=ABCMeta):
    pass
