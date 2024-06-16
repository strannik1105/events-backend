from common.db.postgres import PostgresSession
from common.managers import LoggerManager
from config.templates import SecurityTemplate
from services import Service


class SecurityInit:
    _logger = LoggerManager.get_base_logger()

    @classmethod
    async def set_roles(cls) -> None:
        db = PostgresSession.get_async()
        service = Service(db)
        try:
            cls._logger.info("Start roles init")
            roles_in = SecurityTemplate.get_roles()
            for role_in in roles_in:
                role = await service.security.get_role_by_label(
                    label=role_in.label, validate=False
                )
                if not role:
                    await service.security.create_role(role_in=role_in)
            cls._logger.info("Finish roles init")
        except Exception as exc:
            cls._logger.error(f"Roles init error: {exc}")
        finally:
            await db.close()

    @classmethod
    async def set_permissions(cls) -> None:
        db = PostgresSession.get_async()
        service = Service(db)
        try:
            cls._logger.info("Start permissions init")
            permissions_in = SecurityTemplate.get_permissions()
            for permission_in in permissions_in:
                permission = await service.security.get_permission_by_label(
                    label=permission_in.label, validate=False
                )
                if not permission:
                    await service.security.create_permission(
                        permission_in=permission_in
                    )
            cls._logger.info("Finish permissions init")
        except Exception as exc:
            cls._logger.error(f"Permissions init error: {exc}")
        finally:
            await db.close()

    @classmethod
    async def set_role_x_permissions(cls) -> None:
        db = PostgresSession.get_async()
        service = Service(db)
        try:
            cls._logger.info("Start permissions of role init")
            role_x_permissions_in = SecurityTemplate.get_roles_x_permissions()
            for role_x_permission_in in role_x_permissions_in:
                await service.security.get_role_by_label(
                    label=role_x_permission_in.role_label
                )
                await service.security.get_permission_by_label(
                    label=role_x_permission_in.permission_label
                )
                role_x_permission = (
                    await service.security.get_role_x_permission_by_labels(
                        role_label=role_x_permission_in.role_label,
                        permission_label=role_x_permission_in.permission_label,
                        validate=False,
                    )
                )
                if not role_x_permission:
                    await service.security.create_role_x_permission(
                        role_x_permission_in=role_x_permission_in
                    )
            cls._logger.info("Finish permissions of role init")
        except Exception as exc:
            cls._logger.error(f"Permissions of role init error: {exc}")
        finally:
            await db.close()
