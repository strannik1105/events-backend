from common.base.singleton import Singleton


class UserService(metaclass=Singleton):
    def __init__(self):
        pass

    @staticmethod
    async def get_all_users(repository, session):
        return await repository.get_all(session)

    @staticmethod
    async def get_user_by_name(repository, name, session):
        pass
