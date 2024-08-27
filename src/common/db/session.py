from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from common.config.config import Config
from common.singleton import Singleton


config = Config.get_instance()


class PostgresSession(Singleton):
    def __init__(self):
        self._async_session: AsyncSession = async_sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=create_async_engine(
                echo=True,
                url=f"postgresql+asyncpg://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@{config.POSTGRES_HOST}:{config.POSTGRES_PORT}/{config.POSTGRES_DB}",
            ),
        )()
        
    def get_async(self) -> AsyncSession:
        return self._session
