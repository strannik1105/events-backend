from sqlalchemy.ext.asyncio import AsyncSession

from interfaces.services.security import ISecurityServiceUtils
from services.core import CoreServiceUtils


class SecurityServiceUtils(ISecurityServiceUtils, CoreServiceUtils):
    def __init__(self, pg_db: AsyncSession) -> None:
        super().__init__(pg_db)
