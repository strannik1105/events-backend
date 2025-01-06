from uuid import UUID
import base64

from common.api.abstract_api import AbstractApi
from common.router.router import AsyncRouteCallback
from common.singleton import Singleton
from events.schemas import ImageDescr, ImageCreate
from events.services.storage import S3ImageStorage

from fastapi import UploadFile, Depends


class EventImageApi(AbstractApi, Singleton):
    def __init__(self) -> None:
        super().__init__(
            S3ImageStorage.get_instance(),
            get_schema=ImageDescr,
            create_schema=ImageCreate,
        )

    def _get_create_callback(self) -> AsyncRouteCallback:
        async def callback(
            image: UploadFile,
            storage: S3ImageStorage = Depends(S3ImageStorage),
        ):
            await storage.upload(
                filename=image.filename, file=image.file, size=image.size
            )
            a = await self._service.create({"name": image.filename})
            img_sid = a.__dict__["sid"]
            return {"name": image.filename, "size": image.size, "sid": img_sid}

        return AsyncRouteCallback(callback)

    def _get_get_one_callback(self):
        async def callback(
            sid: UUID, storage: S3ImageStorage = Depends(S3ImageStorage)
        ):
            res = await self._service.get_one(sid)
            obj = res.__dict__
            del obj["_sa_instance_state"]
            name = obj["name"]
            a = await storage.get(name)
            encoded_data = base64.b64encode(a.data)
            obj["image"] = encoded_data
            return obj

        return AsyncRouteCallback(callback)
