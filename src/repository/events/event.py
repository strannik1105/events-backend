from common.base.singleton import Singleton
from common.repository.repository import AbstractRepository


class EventRepository[T](AbstractRepository[T], metaclass=Singleton):
    pass
