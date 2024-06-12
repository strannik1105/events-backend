from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from config.settings import settings


class PostgresSession:
    @staticmethod
    def get_async() -> AsyncSession:
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
        return session()
