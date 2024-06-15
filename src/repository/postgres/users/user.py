from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.base import ExecutableOption

from models.users import User
from repository.postgres.core import CoreRepository


class UserRepository(CoreRepository[User]):
    def __init__(self, db: AsyncSession, model: User):
        super().__init__(db, model)

    async def get_by_email(
        self, email: str, custom_options: list[ExecutableOption] | None = None
    ) -> User:
        return await self.get_by(
            filter_expression=User.email == email,
            custom_options=custom_options,
        )
