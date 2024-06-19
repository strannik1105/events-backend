from common import schemas as common_schemas
from common.sql.options import events as event_options
from config.exceptions import APIException
from enums import security as security_enums
from schemas import users as user_schemas
from services import Service


class SecurityPermissions:
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

    @staticmethod
    async def validate_user_event_permission(
        service: Service,
        permission: security_enums.PermissionLabel,
        action: security_enums.PermissionAccessAction,
        current_user: user_schemas.CurrentUser,
        event_sids: common_schemas.EventSids,
        is_raise: bool = True,
    ) -> bool | None:
        is_valid_role = False

        if action in current_user.role_permissions.get(permission, ""):
            is_valid_role = True

        if not is_valid_role:
            event_pull = await service.event.get_event_pull_by_sids(
                event_pull_sids=common_schemas.EventPullSids(
                    **event_sids.model_dump(),
                    user_sid=current_user.sid,
                ),
                validate=False,
                custom_options=event_options.SQLEventPullOptions.permissions(),
            )
            if event_pull:
                for role_permission in event_pull.role.permissions:
                    if (
                        role_permission.permission_label == permission
                        and action in role_permission.access_actions
                    ):
                        is_valid_role = True
                        break

        if is_raise:
            if not is_valid_role:
                raise APIException.not_allowed

        return is_valid_role

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
