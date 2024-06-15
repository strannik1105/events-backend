from typing import Annotated, AsyncIterator

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from common.db.postgres import PostgresSession
import usecases


async def get_pg_session() -> AsyncIterator[AsyncSession]:
    db = PostgresSession.get_async()
    try:
        yield db
    finally:
        await db.rollback()
        await db.close()


def get_use_case(pg_db: AsyncSession = Depends(get_pg_session)) -> usecases.UseCase:
    return usecases.UseCase(pg_db)


PgSession = Annotated[AsyncSession, Depends(get_pg_session)]
UseCase = Annotated[usecases.UseCase, Depends(get_use_case)]
