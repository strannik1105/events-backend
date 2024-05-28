from common.base.singleton import Singleton
from common.repository.repository import AbstractRepository


class UserRepository[T](AbstractRepository[T], metaclass=Singleton):
    pass
