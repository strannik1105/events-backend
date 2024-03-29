from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

import settings

# PostgresSQL Client
engine = create_async_engine(
    f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}",
    echo=True,
)
SessionLocal = async_sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine,
)


async def get_pg_session() -> AsyncSession:
    async with SessionLocal() as session:
        yield session
