from enums import security as security_enums
from schemas import security as security_schemas


R = security_enums.PermissionAccessAction.READ
C = security_enums.PermissionAccessAction.CREATE
U = security_enums.PermissionAccessAction.UPDATE
D = security_enums.PermissionAccessAction.DELETE
E = security_enums.PermissionAccessAction.EXPORT

CRUD = C + R + U + D
CRUDE = CRUD + E


class SecurityTemplate:
    @staticmethod
    def get_roles() -> list[security_schemas.RoleCreate]:
        return [
            security_schemas.RoleCreate(
                label=security_enums.RoleLabel.SUPERUSER,
                name="Суперпользователь",
                description="Роль с правами суперпользователя",
                is_event=False,
            ),
            security_schemas.RoleCreate(
                label=security_enums.RoleLabel.ADMIN,
                name="Администратор",
                description="Роль с правами администратора",
                is_event=False,
            ),
            security_schemas.RoleCreate(
                label=security_enums.RoleLabel.USER,
                name="Обычный пользователь",
                description="Роль с правами обычного пользователя",
                is_event=False,
            ),
            security_schemas.RoleCreate(
                label=security_enums.EventRoleLabel.CREATOR,
                name="Создатель мероприятия",
                description="Роль мероприятия с правами создателя",
                is_event=True,
            ),
            security_schemas.RoleCreate(
                label=security_enums.EventRoleLabel.SPEAKER,
                name="Спикер мероприятия",
                description="Роль мероприятия с правами спикера",
                is_event=True,
            ),
            security_schemas.RoleCreate(
                label=security_enums.EventRoleLabel.MEMBER,
                name="Участник мероприятия",
                description="Роль мероприятия с правами участника",
                is_event=True,
            ),
        ]

    @staticmethod
    def get_permissions() -> list[security_schemas.PermissionCreate]:
        return [
            security_schemas.PermissionCreate(
                label=security_enums.PermissionLabel.USER,
                name="Пользователь",
                description="Взаимодействие с пользователем",
            ),
            security_schemas.PermissionCreate(
                label=security_enums.PermissionLabel.EVENT,
                name="Мероприятие",
                description="Взаимодействие с мероприятием",
            ),
            security_schemas.PermissionCreate(
                label=security_enums.PermissionLabel.EVENT_CONTENT,
                name="Контент мероприятия",
                description="Взаимодействие с контентом мероприятия",
            ),
            security_schemas.PermissionCreate(
                label=security_enums.PermissionLabel.EVENT_FILE,
                name="Файлы мероприятия",
                description="Взаимодействие с файлами мероприятия",
            ),
            security_schemas.PermissionCreate(
                label=security_enums.PermissionLabel.EVENT_SPEAKER_FILE,
                name="Файлы спикера мероприятия",
                description="Взаимодействие с файлами спикеров мероприятия",
            ),
        ]

    @staticmethod
    def get_roles_x_permissions() -> (
        list[security_schemas.RoleXPermissionCreate]
    ):
        return [
            security_schemas.RoleXPermissionCreate(
                role_label=security_enums.RoleLabel.SUPERUSER,
                permission_label=security_enums.PermissionLabel.USER,
                access_actions=CRUD,
            ),
            security_schemas.RoleXPermissionCreate(
                role_label=security_enums.RoleLabel.SUPERUSER,
                permission_label=security_enums.PermissionLabel.EVENT,
                access_actions=CRUD,
            ),
            security_schemas.RoleXPermissionCreate(
                role_label=security_enums.RoleLabel.SUPERUSER,
                permission_label=security_enums.PermissionLabel.EVENT_CONTENT,
                access_actions=CRUD,
            ),
            security_schemas.RoleXPermissionCreate(
                role_label=security_enums.RoleLabel.SUPERUSER,
                permission_label=security_enums.PermissionLabel.EVENT_FILE,
                access_actions=CRUDE,
            ),
            security_schemas.RoleXPermissionCreate(
                role_label=security_enums.RoleLabel.SUPERUSER,
                permission_label=security_enums.PermissionLabel.EVENT_SPEAKER_FILE,
                access_actions=CRUDE,
            ),
            security_schemas.RoleXPermissionCreate(
                role_label=security_enums.RoleLabel.ADMIN,
                permission_label=security_enums.PermissionLabel.USER,
                access_actions=CRUD,
            ),
            security_schemas.RoleXPermissionCreate(
                role_label=security_enums.RoleLabel.ADMIN,
                permission_label=security_enums.PermissionLabel.EVENT,
                access_actions=CRUD,
            ),
            security_schemas.RoleXPermissionCreate(
                role_label=security_enums.RoleLabel.ADMIN,
                permission_label=security_enums.PermissionLabel.EVENT_CONTENT,
                access_actions=CRUD,
            ),
            security_schemas.RoleXPermissionCreate(
                role_label=security_enums.RoleLabel.ADMIN,
                permission_label=security_enums.PermissionLabel.EVENT_FILE,
                access_actions=CRUDE,
            ),
            security_schemas.RoleXPermissionCreate(
                role_label=security_enums.RoleLabel.ADMIN,
                permission_label=security_enums.PermissionLabel.EVENT_SPEAKER_FILE,
                access_actions=CRUDE,
            ),
            security_schemas.RoleXPermissionCreate(
                role_label=security_enums.RoleLabel.USER,
                permission_label=security_enums.PermissionLabel.USER,
                access_actions=R,
            ),
            security_schemas.RoleXPermissionCreate(
                role_label=security_enums.RoleLabel.USER,
                permission_label=security_enums.PermissionLabel.EVENT,
                access_actions=R,
            ),
            security_schemas.RoleXPermissionCreate(
                role_label=security_enums.RoleLabel.USER,
                permission_label=security_enums.PermissionLabel.EVENT_CONTENT,
                access_actions=R,
            ),
            security_schemas.RoleXPermissionCreate(
                role_label=security_enums.RoleLabel.USER,
                permission_label=security_enums.PermissionLabel.EVENT_FILE,
                access_actions=R + E,
            ),
            security_schemas.RoleXPermissionCreate(
                role_label=security_enums.RoleLabel.USER,
                permission_label=security_enums.PermissionLabel.EVENT_SPEAKER_FILE,
                access_actions=R,
            ),
            security_schemas.RoleXPermissionCreate(
                role_label=security_enums.EventRoleLabel.CREATOR,
                permission_label=security_enums.PermissionLabel.EVENT,
                access_actions=CRUD,
            ),
            security_schemas.RoleXPermissionCreate(
                role_label=security_enums.EventRoleLabel.CREATOR,
                permission_label=security_enums.PermissionLabel.EVENT_CONTENT,
                access_actions=CRUD,
            ),
            security_schemas.RoleXPermissionCreate(
                role_label=security_enums.EventRoleLabel.CREATOR,
                permission_label=security_enums.PermissionLabel.EVENT_FILE,
                access_actions=CRUDE,
            ),
            security_schemas.RoleXPermissionCreate(
                role_label=security_enums.EventRoleLabel.CREATOR,
                permission_label=security_enums.PermissionLabel.EVENT_SPEAKER_FILE,
                access_actions=CRUDE,
            ),
            security_schemas.RoleXPermissionCreate(
                role_label=security_enums.EventRoleLabel.SPEAKER,
                permission_label=security_enums.PermissionLabel.EVENT,
                access_actions=R,
            ),
            security_schemas.RoleXPermissionCreate(
                role_label=security_enums.EventRoleLabel.SPEAKER,
                permission_label=security_enums.PermissionLabel.EVENT_CONTENT,
                access_actions=R + U,
            ),
            security_schemas.RoleXPermissionCreate(
                role_label=security_enums.EventRoleLabel.SPEAKER,
                permission_label=security_enums.PermissionLabel.EVENT_FILE,
                access_actions=R + E,
            ),
            security_schemas.RoleXPermissionCreate(
                role_label=security_enums.EventRoleLabel.SPEAKER,
                permission_label=security_enums.PermissionLabel.EVENT_SPEAKER_FILE,
                access_actions=CRUDE,
            ),
            security_schemas.RoleXPermissionCreate(
                role_label=security_enums.EventRoleLabel.MEMBER,
                permission_label=security_enums.PermissionLabel.EVENT,
                access_actions=R,
            ),
            security_schemas.RoleXPermissionCreate(
                role_label=security_enums.EventRoleLabel.MEMBER,
                permission_label=security_enums.PermissionLabel.EVENT_CONTENT,
                access_actions=R,
            ),
            security_schemas.RoleXPermissionCreate(
                role_label=security_enums.EventRoleLabel.MEMBER,
                permission_label=security_enums.PermissionLabel.EVENT_FILE,
                access_actions=R + E,
            ),
            security_schemas.RoleXPermissionCreate(
                role_label=security_enums.EventRoleLabel.MEMBER,
                permission_label=security_enums.PermissionLabel.EVENT_SPEAKER_FILE,
                access_actions=R + E,
            ),
        ]
