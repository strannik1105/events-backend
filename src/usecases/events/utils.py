from fastapi import UploadFile

from config.exceptions import APIException
from config.settings import settings
from interfaces.usecases.events import IEventUseCaseUtils
from usecases.core import CoreUseCaseUtils


class EventUseCaseUtils(IEventUseCaseUtils, CoreUseCaseUtils):
    @staticmethod
    def validate_file_size(
        file: UploadFile, is_raise: bool = True
    ) -> bool | None:
        if (
            file.size
            > settings.unit.MB * settings.s3.MAX_EVENTS_BUCKET_FILE_MB_SIZE
        ):
            if is_raise:
                raise APIException.invalid_event_file_size
            return False
        return True

    @staticmethod
    def get_file_extension(file: UploadFile, with_dot: bool = True) -> str:
        file_extension = ""
        if file.filename:
            file_extension = file.filename.split(".")[-1]
        if with_dot:
            return "." + file_extension
        return file_extension
