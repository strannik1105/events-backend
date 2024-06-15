from sqlalchemy import text
from tenacity import retry, stop_after_attempt, wait_fixed

from common.db.postgres import PostgresSession
from common.managers import LoggerManager
from config.settings import settings


class PostgresConnection:
    _logger = LoggerManager.get_base_logger()

    @classmethod
    @retry(
        stop=stop_after_attempt(settings.postgres.CONN_DEADLINE_SECONDS),
        wait=wait_fixed(settings.postgres.CONN_WAIT_SECONDS),
    )
    async def ping(cls) -> None:
        db = PostgresSession.get_async()
        try:
            cls._logger.info("Ping to postgres")
            response = await db.execute(text("SELECT 1"))
            cls._logger.info(f"Pong: response value - {response.first()}")
        except Exception as e:
            cls._logger.error(e)
            raise e
        finally:
            await db.close()
