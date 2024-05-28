from uuid import UUID

from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from common.exceptions.exceptions import HTTPNotFoundError


class CRUDService[T]:
    @staticmethod
    async def get_all(db_session: AsyncSession, repository) -> list[T]:
        return await repository.get_all(db_session)

    @staticmethod
    async def get_by_sid(db_session: AsyncSession, repository, sid: UUID) -> T:
        user = await repository.get(db_session, sid)
        if user is None:
            raise HTTPNotFoundError
        return user

    @staticmethod
    async def create(db_session: AsyncSession, repository, t_type, create_schema: BaseModel) -> T:
        return await repository.create(db_session, t_type(**create_schema.model_dump()))

    @staticmethod
    async def update(db_session: AsyncSession, repository, sid, changes):
        db_obj = await repository.get(db_session, sid)
        if db_obj is None:
            raise HTTPNotFoundError
        db_obj = await repository.update(db_session, db_obj, changes.__dict__)
        return db_obj

    @staticmethod
    async def delete(db_session: AsyncSession, repository, sid):
        db_obj = await repository.get(db_session, sid)
        if db_obj is None:
            raise HTTPNotFoundError
        await repository.remove(db_session, db_obj)