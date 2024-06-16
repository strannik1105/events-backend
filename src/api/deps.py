from typing import Annotated, AsyncIterator

from fastapi import Depends
from redis import asyncio as aioredis
from sqlalchemy.ext.asyncio import AsyncSession

import usecases
from common.db import postgres, redis


async def get_pg_session() -> AsyncIterator[AsyncSession]:
    db = postgres.PostgresSession.get_async()
    try:
        yield db
    finally:
        await db.rollback()
        await db.close()


async def get_redis_token_client() -> aioredis.Redis:
    return redis.RedisTokenClient.get_async()


def get_use_case(
    pg_db: AsyncSession = Depends(get_pg_session),
) -> usecases.UseCase:
    return usecases.UseCase(pg_db)


PgSession = Annotated[AsyncSession, Depends(get_pg_session)]
RedisTokenClient = Annotated[AsyncSession, Depends(get_redis_token_client)]
UseCase = Annotated[usecases.UseCase, Depends(get_use_case)]
