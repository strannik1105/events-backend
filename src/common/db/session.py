from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from common.config.config import Config

config = Config.get_instance()


class PostgresSession:
    @staticmethod
    def get_async() -> AsyncSession:
        session = async_sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=create_async_engine(
                echo=True,
                url=f"postgresql+asyncpg://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@{config.POSTGRES_HOST}:{config.POSTGRES_PORT}/{config.POSTGRES_DB}",
            ),
        )
        return session()
