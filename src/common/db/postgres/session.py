from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from config import settings


session = async_sessionmaker(
    autocommit=settings.postgres.AUTOCOMMIT,
    autoflush=settings.postgres.AUTOFLUSH,
    bind=create_async_engine(
        echo=settings.postgres.ECHO,
        url=settings.postgres.DSN.unicode_string(),
        pool_pre_ping=settings.postgres.POOL_PRE_PING,
        pool_size=settings.postgres.POOL_SIZE,
        max_overflow=settings.postgres.MAX_OVERFLOW,
    ),
)


async def get_db() -> AsyncSession:
    async with session() as db:
        yield db
