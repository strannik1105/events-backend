from abc import ABCMeta, abstractmethod

from fastapi import UploadFile

from interfaces.usecases.core import ICoreUseCaseUtils


class IEventUseCaseUtils(ICoreUseCaseUtils, metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def validate_file_size(
        file: UploadFile, is_raise: bool = True
    ) -> bool | None:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def get_file_extension(file: UploadFile, with_dot: bool = True) -> str:
        raise NotImplementedError
