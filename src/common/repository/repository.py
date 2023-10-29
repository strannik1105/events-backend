from typing import List
from uuid import UUID

from common.db.session import get_session
from interfaces.common.repository.repository import IRepository
from models import User


class AbstractRepository[T](IRepository):
    def __init__(self, t_model: type(T)):
        self.__t_model = t_model

    def get(self, *, sid: UUID) -> T:
        session = get_session()
        obj = (
            session.query(self.__t_model).filter(self.__t_model.sid == str(sid)).first()
        )
        return obj

    def get_all(self, *, limit: int = 50, offset: int = 0) -> List[T]:
        session = get_session()
        obj = session.query(self.__t_model).offset(offset).limit(limit).all()
        return obj

    def create(self, obj: T, *, with_commit: bool = True) -> T:
        session = get_session()
        session.add(obj)
        if with_commit:
            session.commit()
        else:
            session.flush()
        return obj

    def update(self, db_obj: T, changes: dict) -> T:
        session = get_session()
        for k, v in changes:
            setattr(db_obj, k, v)
        session.commit()
        return db_obj
