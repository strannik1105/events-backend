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
    async def set_resources(cls) -> None:
        db = PostgresSession.get_async()
        service = Service(db)
        try:
            cls._logger.info("Start resources init")
            resources_in = SecurityTemplate.get_resources()
            for resource_in in resources_in:
                resource = await service.security.get_resource_by_label(
                    label=resource_in.label, validate=False
                )
                if not resource:
                    await service.security.create_resource(
                        resource_in=resource_in
                    )
            cls._logger.info("Finish resources init")
        except Exception as exc:
            cls._logger.error(f"Resources init error: {exc}")
        finally:
            await db.close()

    @classmethod
    async def set_role_x_resources(cls) -> None:
        db = PostgresSession.get_async()
        service = Service(db)
        try:
            cls._logger.info("Start resources of role init")
            role_x_resources_in = SecurityTemplate.get_role_x_resources()
            for role_x_resource_in in role_x_resources_in:
                await service.security.get_role_by_label(
                    label=role_x_resource_in.role_label
                )
                await service.security.get_resource_by_label(
                    label=role_x_resource_in.resource_label
                )
                role_x_resource = (
                    await service.security.get_role_x_resource_by_labels(
                        role_label=role_x_resource_in.role_label,
                        resource_label=role_x_resource_in.resource_label,
                        validate=False,
                    )
                )
                if not role_x_resource:
                    await service.security.create_role_x_resource(
                        role_x_resource_in=role_x_resource_in
                    )
            cls._logger.info("Finish resources of role init")
        except Exception as exc:
            cls._logger.error(f"Resources of role init error: {exc}")
        finally:
            await db.close()
