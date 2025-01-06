from typing import BinaryIO
from minio import Minio
from miniopy_async import S3Error

from common.config.config import S3StorageSettings
from common.services.abstract_service import AbstractService
from common.services.image_service import ImageUtils
from common.singleton import Singleton
from events.repository.event_image import EventImageRepository


class S3ImageStorage(AbstractService, Singleton):
    base_image_url = "/media/"
    settings = S3StorageSettings()

    def __init__(self):
        super().__init__(EventImageRepository.get_instance())
        self.client = Minio(
            endpoint=self.settings.endpoint,
            access_key=self.settings.access_key,
            secret_key=self.settings.secret_key,
            secure=False,
        )
        self.bucket_name = self.settings.bucket_name

    async def get(self, image_id: str) -> ImageUtils.ImageDescr:
        try:
            return self.client.get_object(self.bucket_name, image_id)
        except S3Error as e:
            if e.code == "NoSuchKey":
                raise f"Image {image_id} not found in storage" from e
            raise

    async def upload(
        self, filename: str, file: BinaryIO, size: int | None = None
    ) -> str:
        identity = await ImageUtils.create_new_id(filename)
        if not size:
            size = ImageUtils._get_file_size(file)
        img_info = ImageUtils._get_image_info(file)
        self.client.put_object(
            bucket_name=self.bucket_name,
            object_name=identity,
            data=file,
            length=size,
            content_type=img_info.content_type,
            metadata={"height": img_info.height, "width": img_info.width},
        )
        return identity
