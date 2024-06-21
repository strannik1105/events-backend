from enums import security as security_enums
from schemas import security as security_schemas


R = security_enums.PermissionLabel.READ
C = security_enums.PermissionLabel.CREATE
U = security_enums.PermissionLabel.UPDATE
D = security_enums.PermissionLabel.DELETE
E = security_enums.PermissionLabel.EXPORT

CRUD = C + R + U + D
CRUDE = CRUD + E


class SecurityTemplate:
    @staticmethod
    def get_roles() -> list[security_schemas.RoleDTOCreate]:
        return [
            security_schemas.RoleDTOCreate(
                label=security_enums.RoleLabel.SUPERUSER,
                name="Суперпользователь",
                description="Роль с правами суперпользователя",
                is_event=False,
            ),
            security_schemas.RoleDTOCreate(
                label=security_enums.RoleLabel.ADMIN,
                name="Администратор",
                description="Роль с правами администратора",
                is_event=False,
            ),
            security_schemas.RoleDTOCreate(
                label=security_enums.RoleLabel.USER,
                name="Обычный пользователь",
                description="Роль с правами обычного пользователя",
                is_event=False,
            ),
            security_schemas.RoleDTOCreate(
                label=security_enums.EventRoleLabel.CREATOR,
                name="Создатель мероприятия",
                description="Роль мероприятия с правами создателя",
                is_event=True,
            ),
            security_schemas.RoleDTOCreate(
                label=security_enums.EventRoleLabel.SPEAKER,
                name="Спикер мероприятия",
                description="Роль мероприятия с правами спикера",
                is_event=True,
            ),
            security_schemas.RoleDTOCreate(
                label=security_enums.EventRoleLabel.MEMBER,
                name="Участник мероприятия",
                description="Роль мероприятия с правами участника",
                is_event=True,
            ),
        ]

    @staticmethod
    def get_resources() -> list[security_schemas.ResourceDTOCreate]:
        return [
            security_schemas.ResourceDTOCreate(
                label=security_enums.ResourceLabel.USER,
                name="Пользователь",
                description="Взаимодействие с пользователем",
            ),
            security_schemas.ResourceDTOCreate(
                label=security_enums.ResourceLabel.EVENT,
                name="Мероприятие",
                description="Взаимодействие с мероприятием",
            ),
            security_schemas.ResourceDTOCreate(
                label=security_enums.ResourceLabel.EVENT_CONTENT,
                name="Контент мероприятия",
                description="Взаимодействие с контентом мероприятия",
            ),
            security_schemas.ResourceDTOCreate(
                label=security_enums.ResourceLabel.EVENT_FILE,
                name="Файлы мероприятия",
                description="Взаимодействие с файлами мероприятия",
            ),
            security_schemas.ResourceDTOCreate(
                label=security_enums.ResourceLabel.EVENT_SPEAKER_FILE,
                name="Файлы спикера мероприятия",
                description="Взаимодействие с файлами спикеров мероприятия",
            ),
        ]

    @staticmethod
    def get_role_x_resources() -> (
        list[security_schemas.RoleXResourceDTOCreate]
    ):
        return [
            security_schemas.RoleXResourceDTOCreate(
                role_label=security_enums.RoleLabel.SUPERUSER,
                resource_label=security_enums.ResourceLabel.USER,
                permissions=CRUD,
            ),
            security_schemas.RoleXResourceDTOCreate(
                role_label=security_enums.RoleLabel.SUPERUSER,
                resource_label=security_enums.ResourceLabel.EVENT,
                permissions=CRUD,
            ),
            security_schemas.RoleXResourceDTOCreate(
                role_label=security_enums.RoleLabel.SUPERUSER,
                resource_label=security_enums.ResourceLabel.EVENT_CONTENT,
                permissions=CRUD,
            ),
            security_schemas.RoleXResourceDTOCreate(
                role_label=security_enums.RoleLabel.SUPERUSER,
                resource_label=security_enums.ResourceLabel.EVENT_FILE,
                permissions=CRUDE,
            ),
            security_schemas.RoleXResourceDTOCreate(
                role_label=security_enums.RoleLabel.SUPERUSER,
                resource_label=security_enums.ResourceLabel.EVENT_SPEAKER_FILE,
                permissions=CRUDE,
            ),
            security_schemas.RoleXResourceDTOCreate(
                role_label=security_enums.RoleLabel.ADMIN,
                resource_label=security_enums.ResourceLabel.USER,
                permissions=CRUD,
            ),
            security_schemas.RoleXResourceDTOCreate(
                role_label=security_enums.RoleLabel.ADMIN,
                resource_label=security_enums.ResourceLabel.EVENT,
                permissions=CRUD,
            ),
            security_schemas.RoleXResourceDTOCreate(
                role_label=security_enums.RoleLabel.ADMIN,
                resource_label=security_enums.ResourceLabel.EVENT_CONTENT,
                permissions=CRUD,
            ),
            security_schemas.RoleXResourceDTOCreate(
                role_label=security_enums.RoleLabel.ADMIN,
                resource_label=security_enums.ResourceLabel.EVENT_FILE,
                permissions=CRUDE,
            ),
            security_schemas.RoleXResourceDTOCreate(
                role_label=security_enums.RoleLabel.ADMIN,
                resource_label=security_enums.ResourceLabel.EVENT_SPEAKER_FILE,
                permissions=CRUDE,
            ),
            security_schemas.RoleXResourceDTOCreate(
                role_label=security_enums.RoleLabel.USER,
                resource_label=security_enums.ResourceLabel.USER,
                permissions=R,
            ),
            security_schemas.RoleXResourceDTOCreate(
                role_label=security_enums.RoleLabel.USER,
                resource_label=security_enums.ResourceLabel.EVENT,
                permissions=R,
            ),
            security_schemas.RoleXResourceDTOCreate(
                role_label=security_enums.RoleLabel.USER,
                resource_label=security_enums.ResourceLabel.EVENT_CONTENT,
                permissions=R,
            ),
            security_schemas.RoleXResourceDTOCreate(
                role_label=security_enums.RoleLabel.USER,
                resource_label=security_enums.ResourceLabel.EVENT_FILE,
                permissions=R + E,
            ),
            security_schemas.RoleXResourceDTOCreate(
                role_label=security_enums.RoleLabel.USER,
                resource_label=security_enums.ResourceLabel.EVENT_SPEAKER_FILE,
                permissions=R,
            ),
            security_schemas.RoleXResourceDTOCreate(
                role_label=security_enums.EventRoleLabel.CREATOR,
                resource_label=security_enums.ResourceLabel.EVENT,
                permissions=R + U + D,
            ),
            security_schemas.RoleXResourceDTOCreate(
                role_label=security_enums.EventRoleLabel.CREATOR,
                resource_label=security_enums.ResourceLabel.EVENT_CONTENT,
                permissions=CRUD,
            ),
            security_schemas.RoleXResourceDTOCreate(
                role_label=security_enums.EventRoleLabel.CREATOR,
                resource_label=security_enums.ResourceLabel.EVENT_FILE,
                permissions=CRUDE,
            ),
            security_schemas.RoleXResourceDTOCreate(
                role_label=security_enums.EventRoleLabel.CREATOR,
                resource_label=security_enums.ResourceLabel.EVENT_SPEAKER_FILE,
                permissions=CRUDE,
            ),
            security_schemas.RoleXResourceDTOCreate(
                role_label=security_enums.EventRoleLabel.SPEAKER,
                resource_label=security_enums.ResourceLabel.EVENT,
                permissions=R,
            ),
            security_schemas.RoleXResourceDTOCreate(
                role_label=security_enums.EventRoleLabel.SPEAKER,
                resource_label=security_enums.ResourceLabel.EVENT_CONTENT,
                permissions=R + U,
            ),
            security_schemas.RoleXResourceDTOCreate(
                role_label=security_enums.EventRoleLabel.SPEAKER,
                resource_label=security_enums.ResourceLabel.EVENT_FILE,
                permissions=R + E,
            ),
            security_schemas.RoleXResourceDTOCreate(
                role_label=security_enums.EventRoleLabel.SPEAKER,
                resource_label=security_enums.ResourceLabel.EVENT_SPEAKER_FILE,
                permissions=CRUDE,
            ),
            security_schemas.RoleXResourceDTOCreate(
                role_label=security_enums.EventRoleLabel.MEMBER,
                resource_label=security_enums.ResourceLabel.EVENT,
                permissions=R,
            ),
            security_schemas.RoleXResourceDTOCreate(
                role_label=security_enums.EventRoleLabel.MEMBER,
                resource_label=security_enums.ResourceLabel.EVENT_CONTENT,
                permissions=R,
            ),
            security_schemas.RoleXResourceDTOCreate(
                role_label=security_enums.EventRoleLabel.MEMBER,
                resource_label=security_enums.ResourceLabel.EVENT_FILE,
                permissions=R + E,
            ),
            security_schemas.RoleXResourceDTOCreate(
                role_label=security_enums.EventRoleLabel.MEMBER,
                resource_label=security_enums.ResourceLabel.EVENT_SPEAKER_FILE,
                permissions=R + E,
            ),
        ]
