from abc import ABCMeta, abstractmethod
from uuid import UUID


class ICoreUseCase(metaclass=ABCMeta):
    pass


class ICoreUseCaseUtils(metaclass=ABCMeta):
    pass


class ICrudUseCase(metaclass=ABCMeta):
    @abstractmethod
    def get_all():
        pass

    @abstractmethod
    def get_by_sid(sid: UUID):
        pass
