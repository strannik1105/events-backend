import logging
import sys

from config.settings import settings


class LoggerManager:
    _base_log_name = settings.log.BASE_NAME
    _base_log_level = settings.log.BASE_LEVEL
    _base_log_format = settings.log.BASE_FORMAT

    @staticmethod
    def _configure_logger(
        logger: logging.Logger, level: str, format_str: str
    ) -> None:
        logger.setLevel(level)
        logger.propagate = False

        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(level)
        console_handler.setFormatter(logging.Formatter(format_str))
        logger.addHandler(console_handler)

    @classmethod
    def _get_logger(
        cls, name: str, level: str, format_str: str
    ) -> logging.Logger:
        logger = logging.getLogger(name)
        if not logger.hasHandlers():
            cls._configure_logger(
                logger=logger,
                level=level,
                format_str=format_str,
            )
        return logger

    @classmethod
    def get_base_logger(cls) -> logging.Logger:
        return cls._get_logger(
            name=cls._base_log_name,
            level=cls._base_log_level,
            format_str=cls._base_log_format,
        )
