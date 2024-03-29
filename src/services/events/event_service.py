from common.base.singleton import Singleton


class EventService(metaclass=Singleton):
    def __init__(self):
        pass

    @staticmethod
    async def get_all_events(repository, session):
        return await repository.get_all(session)
