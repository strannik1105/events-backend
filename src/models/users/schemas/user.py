from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    email: str
    role: str


class User(UserBase):
    pass


class UserCreate(UserBase):
    password: str


class UserUpdate:
    old_password: str
    new_password: str
