from abc import ABC
from typing import TypeVar, Generic, List
from uuid import UUID

T = TypeVar("T")


class IRepository(ABC, Generic[T]):
    def get(self, *, sid: UUID) -> T:
        raise NotImplementedError

    def get_all(self, *, limit: int, offset: int) -> List[T]:
        raise NotImplementedError

    def create(self, obj: T) -> T:
        raise NotImplementedError

    def update(self, db_obj: T, new_obj):
        raise NotImplementedError
