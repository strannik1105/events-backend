from typing import Generic, Protocol, TypeVar
from uuid import UUID

T = TypeVar("T")


class AbstractCrudRepository(Generic[T], Protocol):
    # returns all obj instanses
    def get_all(self, limit: int = 100, offset: int = 0) -> list[T]:
        pass

    # return only one obj instance with provided sid or None
    def get(self, sid: UUID) -> T | None:
        pass

    # return created obj or None
    def create(self, obj: T) -> T | None:
        pass

    # update obj instance
    def update(self, obj: T, changes, sid):
        pass

    # delete obj
    def delete(self, obj: T):
        pass
