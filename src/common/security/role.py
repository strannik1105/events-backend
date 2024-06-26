from common import schemas as common_schemas
from common.sql.options import events as event_options
from config.exceptions import APIException
from enums import security as security_enums
from interfaces.services import IService
from schemas import users as user_schemas


class SecurityRole:
    _superuser_label = security_enums.RoleLabel.SUPERUSER
    _admin_label = security_enums.RoleLabel.ADMIN
    _user_label = security_enums.RoleLabel.USER
    _event_creator_label = security_enums.EventRoleLabel.CREATOR
    _event_speaker_label = security_enums.EventRoleLabel.SPEAKER
    _event_member_label = security_enums.EventRoleLabel.MEMBER

    _c_label = security_enums.PermissionLabel.CREATE
    _u_label = security_enums.PermissionLabel.UPDATE
    _d_label = security_enums.PermissionLabel.DELETE

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

    @classmethod
    async def validate_event_role_permission(
        cls,
        service: IService,
        resource_label: security_enums.ResourceLabel,
        permission_label: security_enums.PermissionLabel,
        current_user: user_schemas.CurrentUser,
        event_sids: common_schemas.EventSids,
    ) -> None:
        if permission_label in current_user.resource_permissions.get(
            resource_label, ""
        ):
            return

        event_pull = await service.event.get_event_pull_by_event_user_sids(
            event_user_sids=common_schemas.EventUserSids(
                event_sid=event_sids.event_sid,
                user_sid=current_user.sid,
            ),
            validate=False,
            custom_options=event_options.SQLEventPullOptions.permissions(),
        )
        if not event_pull:
            raise APIException.not_allowed

        for permission in event_pull.role.permissions:
            if (
                permission.resource_label == resource_label
                and permission_label in permission.permissions
            ):
                if (
                    event_pull.event_role_label
                    == security_enums.EventRoleLabel.SPEAKER
                    and event_sids.event_content_sid is not None
                    and permission_label
                    in (cls._c_label, cls._u_label, cls._d_label)
                ):
                    event_pull = await service.event.get_event_pull_by_sids(
                        event_pull_sids=common_schemas.EventPullSids(
                            **event_sids.model_dump(),
                            user_sid=current_user.sid,
                        ),
                        validate=False,
                        custom_options=event_options.SQLEventPullOptions.permissions(),
                    )
                    if not event_pull:
                        raise APIException.not_allowed
                return

        raise APIException.not_allowed

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
