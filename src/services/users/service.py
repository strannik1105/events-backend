from sqlalchemy.ext.asyncio import AsyncSession

from services.core import CoreService


class UserService(CoreService):
    def __init__(self, pg_db: AsyncSession) -> None:
        super().__init__(pg_db)
