from uuid import UUID

from passlib.context import CryptContext

from config.exceptions import APIException
from enums import security as security_enums


class SecurityManager:
    _superuser_label = security_enums.RoleLabel.SUPERUSER
    _admin_label = security_enums.RoleLabel.ADMIN
    _user_label = security_enums.RoleLabel.USER
    _event_creator_label = security_enums.EventRoleLabel.CREATOR
    _event_speaker_label = security_enums.EventRoleLabel.SPEAKER
    _event_member_label = security_enums.EventRoleLabel.MEMBER

    _invalid_role_transitions = {
        (_admin_label, _superuser_label),
        (_admin_label, _admin_label),
        (_superuser_label, _superuser_label),
        (_user_label, _admin_label),
        (_user_label, _superuser_label),
    }

    _invalid_event_role_transitions = {
        (_event_speaker_label, _event_creator_label),
        (_event_speaker_label, _event_speaker_label),
        (_event_creator_label, _event_creator_label),
        (_event_member_label, _event_speaker_label),
        (_event_member_label, _event_creator_label),
    }

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

    @staticmethod
    async def validate_user_permission(
        permission: security_enums.PermissionLabel,
        action: security_enums.PermissionAccessAction,
        user_sid: UUID,
        event_sid: UUID | None = None,
        is_raise: bool = True,
    ) -> bool | None:
        if is_raise:
            raise APIException.not_allowed
        return True

    @classmethod
    def get_role_label_by_int(
        cls, role_label: int
    ) -> security_enums.RoleLabel:
        if role_label == cls._superuser_label:
            return cls._superuser_label
        if role_label == cls._admin_label:
            return cls._admin_label
        if role_label == cls._user_label:
            return cls._user_label
        raise APIException.role_not_found

    @classmethod
    def get_event_role_label_by_int(
        cls, event_role_label: int
    ) -> security_enums.EventRoleLabel:
        if event_role_label == cls._event_creator_label:
            return cls._event_creator_label
        if event_role_label == cls._event_speaker_label:
            return cls._event_speaker_label
        if event_role_label == cls._event_member_label:
            return cls._event_member_label
        raise APIException.role_not_found

    @classmethod
    def validate_role_branch(
        cls,
        current_role_label: security_enums.RoleLabel,
        target_role_label: security_enums.RoleLabel,
        is_raise: bool = True,
    ) -> bool | None:
        if (
            current_role_label,
            target_role_label,
        ) in cls._invalid_role_transitions:
            if is_raise:
                raise APIException.violation_role_branch
            return False
        return True

    @classmethod
    def validate_event_role_branch(
        cls,
        current_event_role_label: security_enums.EventRoleLabel,
        target_event_role_label: security_enums.EventRoleLabel,
        is_raise: bool = True,
    ) -> bool | None:
        if (
            current_event_role_label,
            target_event_role_label,
        ) in cls._invalid_event_role_transitions:
            if is_raise:
                raise APIException.violation_event_role_branch
            return False
        return True
