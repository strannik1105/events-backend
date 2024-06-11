from passlib.context import CryptContext


class SecurityManager:
    _pwd_context = CryptContext(schemes=["bcrypt"])

    @classmethod
    def get_password_hash(cls, password: str) -> str:
        return cls._pwd_context.hash(password)

    @classmethod
    def verify_password(cls, password: str, hashed_password: str) -> bool:
        return cls._pwd_context.verify(password, hashed_password)
