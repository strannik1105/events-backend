from common.db.postgres import PostgresSession
from common.managers import LoggerManager
from config.templates import UserTemplate
from services import Service


class UserInit:
    _logger = LoggerManager.get_base_logger()

    @classmethod
    async def superuser(cls) -> None:
        db = PostgresSession.get_async()
        service = Service(db)
        try:
            cls._logger.info("Start superuser init")
            superuser_in = UserTemplate.get_superuser()
            superuser = await service.user.get_user_by_email(
                email=superuser_in.email, validate=False
            )
            if not superuser:
                await service.user.create_verify_user(user_in=superuser_in)
            cls._logger.info("Finish superuser init")
        except Exception as exc:
            cls._logger.error(f"Event superuser error: {exc}")
        finally:
            await db.close()
