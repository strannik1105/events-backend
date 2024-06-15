from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.base import ExecutableOption

from models.users import User
from repository.postgres.core import CoreRepository


class UserRepository(CoreRepository[User]):
    def __init__(self, db: AsyncSession, model: type[User]) -> None:
        super().__init__(db, model)

    async def get_by_email(
        self, email: str, custom_options: list[ExecutableOption] | None = None
    ) -> User | None:
        return await self.get_by(
            filter_expression=User.email == email,
            custom_options=custom_options,
        )

    async def update_user_password(
        self, user: User, hashed_password: str, with_commit: bool = True
    ) -> User:
        user.hashed_password = hashed_password
        if with_commit:
            await self.db.commit()
            await self.db.refresh(user)
        else:
            await self.db.flush()
        return user