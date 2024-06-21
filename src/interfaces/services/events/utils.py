from abc import ABCMeta

from sqlalchemy.ext.asyncio import AsyncSession

from interfaces.services.core import ICoreServiceUtils


class IEventServiceUtils(ICoreServiceUtils, metaclass=ABCMeta):
    def __init__(self, pg_db: AsyncSession) -> None:
        super().__init__(pg_db)
