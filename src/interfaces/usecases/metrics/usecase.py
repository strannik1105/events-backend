from abc import ABCMeta

from interfaces.usecases.core import ICoreUseCase


class IMetricUseCase(ICoreUseCase, metaclass=ABCMeta):
    pass
