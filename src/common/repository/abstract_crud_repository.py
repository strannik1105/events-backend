from typing import Generic, Protocol, TypeVar
from uuid import UUID

T = TypeVar("T")


class AbstractCrudRepository(Generic[T], Protocol):
    # returns all obj instanses
    def get_all(limit: int = 100, offset: int = 0) -> list[T]:
        pass

    # return only one obj instance with provided sid or None
    def get(sid: UUID) -> T | None:
        pass

    # return created obj or None
    def create(obj: T) -> T | None:
        pass

    # update obj instance
    def update(obj: T, changes):
        pass

    # delete obj
    def delete(obj: T):
        pass
