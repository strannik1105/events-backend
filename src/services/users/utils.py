from sqlalchemy.ext.asyncio import AsyncSession

from interfaces.services.users import IUserServiceUtils
from services.core import CoreServiceUtils


class UserServiceUtils(IUserServiceUtils, CoreServiceUtils):
    def __init__(self, pg_db: AsyncSession) -> None:
        super().__init__(pg_db)
