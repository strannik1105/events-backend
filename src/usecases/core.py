from sqlalchemy.ext.asyncio import AsyncSession

from interfaces.services import IService
from interfaces.usecases import ICoreUseCase, ICoreUseCaseUtils
from services import Service


class CoreUseCase(ICoreUseCase):
    def __init__(self, pg_db: AsyncSession) -> None:
        self._pg_db = pg_db
        self._service: IService = Service(pg_db)


class CoreUseCaseUtils(ICoreUseCaseUtils):
    def __init__(self, pg_db: AsyncSession) -> None:
        self._pg_db = pg_db
