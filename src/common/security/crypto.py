from passlib.context import CryptContext

from config.exceptions import APIException


class SecurityCrypto:
    _pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @classmethod
    def get_password_hash(cls, password: str) -> str:
        return cls._pwd_context.hash(password)

    @classmethod
    def verify_password(
        cls, password: str, hashed_password: str | None, is_raise: bool = True
    ) -> bool | None:
        if not cls._pwd_context.verify(secret=password, hash=hashed_password):
            if is_raise:
                raise APIException.invalid_password
            return False
        return True
