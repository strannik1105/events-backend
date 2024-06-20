from abc import ABCMeta
from typing import Generic, TypeVar

from repository.interfaces.core import ICoreRepository


T = TypeVar("T")


class IResourceRepository(Generic[T], ICoreRepository[T], metaclass=ABCMeta):
    pass
