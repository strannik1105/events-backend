from abc import ABCMeta
from typing import Generic, TypeVar

from interfaces.repository.core import ICoreRepository


T = TypeVar("T")


class IRoleRepository(Generic[T], ICoreRepository[T], metaclass=ABCMeta):
    pass
