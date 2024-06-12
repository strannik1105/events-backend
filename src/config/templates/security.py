from models.security import enums, schemas


R = enums.PermissionAccessAction.READ
C = enums.PermissionAccessAction.CREATE
U = enums.PermissionAccessAction.UPDATE
D = enums.PermissionAccessAction.DELETE
E = enums.PermissionAccessAction.EXPORT

CRUD = C + R + U + D
CRUDE = CRUD + E


class SecurityTemplate:
    @staticmethod
    def get_roles() -> list[schemas.RoleCreate]:
        return [
            schemas.RoleCreate(
                label=enums.RoleLabel.SUPERUSER,
                name="Суперпользователь",
                description="Роль с правами суперпользователя",
            ),
            schemas.RoleCreate(
                label=enums.RoleLabel.ADMIN,
                name="Администратор",
                description="Роль с правами администратора",
            ),
            schemas.RoleCreate(
                label=enums.RoleLabel.USER,
                name="Обычный пользователь",
                description="Роль с правами обычного пользователя",
            ),
            schemas.RoleCreate(
                label=enums.EventRoleLabel.CREATOR,
                name="Создатель мероприятия",
                description="Роль мероприятия с правами создателя",
            ),
            schemas.RoleCreate(
                label=enums.EventRoleLabel.SPEAKER,
                name="Спикер мероприятия",
                description="Роль мероприятия с правами спикера",
            ),
            schemas.RoleCreate(
                label=enums.EventRoleLabel.MEMBER,
                name="Участник мероприятия",
                description="Роль мероприятия с правами участника",
            ),
        ]

    @staticmethod
    def get_permissions() -> list[schemas.PermissionCreate]:
        return [
            schemas.PermissionCreate(
                label=enums.PermissionLabel.USER,
                name="Пользователь",
                description="Взаимодействие с пользователем",
            ),
            schemas.PermissionCreate(
                label=enums.PermissionLabel.EVENT,
                name="Мероприятие",
                description="Взаимодействие с мероприятием",
            ),
            schemas.PermissionCreate(
                label=enums.PermissionLabel.EVENT_CONTENT,
                name="Контент мероприятия",
                description="Взаимодействие с контентом мероприятия",
            ),
            schemas.PermissionCreate(
                label=enums.PermissionLabel.EVENT_FILE,
                name="Файлы мероприятия",
                description="Взаимодействие с файлами мероприятия",
            ),
            schemas.PermissionCreate(
                label=enums.PermissionLabel.EVENT_SPEAKER_FILE,
                name="Файлы спикера мероприятия",
                description="Взаимодействие с файлами спикеров мероприятия",
            ),
        ]

    @staticmethod
    def get_roles_x_permissions() -> list[schemas.RoleXPermissionCreate]:
        return [
            schemas.RoleXPermissionCreate(
                role_label=enums.RoleLabel.SUPERUSER,
                permission_label=enums.PermissionLabel.USER,
                access_actions=CRUD,
            ),
            schemas.RoleXPermissionCreate(
                role_label=enums.RoleLabel.SUPERUSER,
                permission_label=enums.PermissionLabel.EVENT,
                access_actions=CRUD,
            ),
            schemas.RoleXPermissionCreate(
                role_label=enums.RoleLabel.SUPERUSER,
                permission_label=enums.PermissionLabel.EVENT_CONTENT,
                access_actions=CRUD,
            ),
            schemas.RoleXPermissionCreate(
                role_label=enums.RoleLabel.SUPERUSER,
                permission_label=enums.PermissionLabel.EVENT_FILE,
                access_actions=CRUDE,
            ),
            schemas.RoleXPermissionCreate(
                role_label=enums.RoleLabel.SUPERUSER,
                permission_label=enums.PermissionLabel.EVENT_SPEAKER_FILE,
                access_actions=CRUDE,
            ),
            schemas.RoleXPermissionCreate(
                role_label=enums.RoleLabel.ADMIN,
                permission_label=enums.PermissionLabel.USER,
                access_actions=CRUD,
            ),
            schemas.RoleXPermissionCreate(
                role_label=enums.RoleLabel.ADMIN,
                permission_label=enums.PermissionLabel.EVENT,
                access_actions=CRUD,
            ),
            schemas.RoleXPermissionCreate(
                role_label=enums.RoleLabel.ADMIN,
                permission_label=enums.PermissionLabel.EVENT_CONTENT,
                access_actions=CRUD,
            ),
            schemas.RoleXPermissionCreate(
                role_label=enums.RoleLabel.ADMIN,
                permission_label=enums.PermissionLabel.EVENT_FILE,
                access_actions=CRUDE,
            ),
            schemas.RoleXPermissionCreate(
                role_label=enums.RoleLabel.ADMIN,
                permission_label=enums.PermissionLabel.EVENT_SPEAKER_FILE,
                access_actions=CRUDE,
            ),
            schemas.RoleXPermissionCreate(
                role_label=enums.RoleLabel.USER,
                permission_label=enums.PermissionLabel.USER,
                access_actions=R,
            ),
            schemas.RoleXPermissionCreate(
                role_label=enums.RoleLabel.USER,
                permission_label=enums.PermissionLabel.EVENT,
                access_actions=R,
            ),
            schemas.RoleXPermissionCreate(
                role_label=enums.RoleLabel.USER,
                permission_label=enums.PermissionLabel.EVENT_CONTENT,
                access_actions=R,
            ),
            schemas.RoleXPermissionCreate(
                role_label=enums.RoleLabel.USER,
                permission_label=enums.PermissionLabel.EVENT_FILE,
                access_actions=R + E,
            ),
            schemas.RoleXPermissionCreate(
                role_label=enums.RoleLabel.USER,
                permission_label=enums.PermissionLabel.EVENT_SPEAKER_FILE,
                access_actions=R,
            ),
            schemas.RoleXPermissionCreate(
                role_label=enums.EventRoleLabel.CREATOR,
                permission_label=enums.PermissionLabel.EVENT,
                access_actions=CRUD,
            ),
            schemas.RoleXPermissionCreate(
                role_label=enums.EventRoleLabel.CREATOR,
                permission_label=enums.PermissionLabel.EVENT_CONTENT,
                access_actions=CRUD,
            ),
            schemas.RoleXPermissionCreate(
                role_label=enums.EventRoleLabel.CREATOR,
                permission_label=enums.PermissionLabel.EVENT_FILE,
                access_actions=CRUDE,
            ),
            schemas.RoleXPermissionCreate(
                role_label=enums.EventRoleLabel.CREATOR,
                permission_label=enums.PermissionLabel.EVENT_SPEAKER_FILE,
                access_actions=CRUDE,
            ),
            schemas.RoleXPermissionCreate(
                role_label=enums.EventRoleLabel.SPEAKER,
                permission_label=enums.PermissionLabel.EVENT,
                access_actions=R,
            ),
            schemas.RoleXPermissionCreate(
                role_label=enums.EventRoleLabel.SPEAKER,
                permission_label=enums.PermissionLabel.EVENT_CONTENT,
                access_actions=R + U,
            ),
            schemas.RoleXPermissionCreate(
                role_label=enums.EventRoleLabel.SPEAKER,
                permission_label=enums.PermissionLabel.EVENT_FILE,
                access_actions=R + E,
            ),
            schemas.RoleXPermissionCreate(
                role_label=enums.EventRoleLabel.SPEAKER,
                permission_label=enums.PermissionLabel.EVENT_SPEAKER_FILE,
                access_actions=CRUDE,
            ),
            schemas.RoleXPermissionCreate(
                role_label=enums.EventRoleLabel.MEMBER,
                permission_label=enums.PermissionLabel.EVENT,
                access_actions=R,
            ),
            schemas.RoleXPermissionCreate(
                role_label=enums.EventRoleLabel.MEMBER,
                permission_label=enums.PermissionLabel.EVENT_CONTENT,
                access_actions=R,
            ),
            schemas.RoleXPermissionCreate(
                role_label=enums.EventRoleLabel.MEMBER,
                permission_label=enums.PermissionLabel.EVENT_FILE,
                access_actions=R + E,
            ),
            schemas.RoleXPermissionCreate(
                role_label=enums.EventRoleLabel.MEMBER,
                permission_label=enums.PermissionLabel.EVENT_SPEAKER_FILE,
                access_actions=R + E,
            ),
        ]
