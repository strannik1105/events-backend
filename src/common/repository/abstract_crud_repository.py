from typing import Generic, Protocol, TypeVar
from uuid import UUID

T = TypeVar("T")


class AbstractCrudRepository(Generic[T], Protocol):
    # returns all obj instanses
    async def get_all(self, limit: int = 100, offset: int = 0) -> list[T]:
        pass

    # return only one obj instance with provided sid or None
    async def get(self, sid: UUID) -> T | None:
        pass

    # return created obj or None
    async def create(self, obj: T) -> T | None:
        pass

    # update obj instance
    async def update(self, changes, sid):
        pass

    # delete obj
    async def delete(self, obj: T):
        pass
