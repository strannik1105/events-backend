import os.path
from typing import AsyncGenerator, BinaryIO

import imgspy
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

    async def list(
        self, prefix: str | None = None, start_after: str | None = None
    ) -> AsyncGenerator[ImageUtils.ImageDescr, None]:
        for obj in await self.client.list_objects(
            self.bucket_name,
            prefix=prefix,
            start_after=start_after,
            include_user_meta=True,
        ):
            yield self._create_image_descr(obj)

    async def get(self, image_id: str) -> ImageUtils.ImageDescr:
        try:
            return self.client.get_object(self.bucket_name, image_id)
        except S3Error as e:
            if e.code == "NoSuchKey":
                raise f"Image {image_id} not found in storage" from e
            raise

    def _create_image_descr(self, obj) -> ImageUtils.ImageDescr:
        return ImageUtils.ImageDescr(
            name=obj.object_name,
            content_type=obj.metadata["content-type"],
            width=int(obj.metadata["X-Amz-Meta-Width"]),
            height=int(obj.metadata["X-Amz-Meta-Height"]),
            url=f"{self.base_image_url}{self.bucket_name}/{obj.object_name}",
            size=obj.size,
            created_at=obj.last_modified,
        )

    async def upload(
        self, filename: str, file: BinaryIO, size: int | None = None
    ) -> str:
        identity = await self.create_new_id(filename)
        if not size:
            size = self._get_file_size(file)
        img_info = self._get_image_info(file)
        self.client.put_object(
            bucket_name=self.bucket_name,
            object_name=identity,
            data=file,
            length=size,
            content_type=img_info.content_type,
            metadata={"height": img_info.height, "width": img_info.width},
        )
        return identity

    @staticmethod
    def _get_file_size(file: BinaryIO) -> int:
        file.seek(0, os.SEEK_END)
        size = file.tell()
        file.seek(0, os.SEEK_SET)
        return size

    @staticmethod
    def _get_image_info(file: BinaryIO) -> ImageUtils.ImageInfo:
        info = imgspy.info(file)
        file.seek(0, os.SEEK_SET)
        type = {"jpg": "jpeg"}.get(info["type"], info["type"])
        return ImageUtils.ImageInfo(
            content_type=f"image/{type}",
            width=info["width"],
            height=info["height"],
        )

    async def create_new_id(self, filename: str) -> str:
        identity = ImageUtils.secure_filename(filename)
        return identity
