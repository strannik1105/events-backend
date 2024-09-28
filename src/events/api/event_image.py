from fastapi import UploadFile, Depends

from common.api.crud_api import CrudApi
from common.router.router import AsyncRouteCallback
from common.singleton import Singleton
from events.services.storage import S3ImageStorage

from dataclasses import dataclass



@dataclass(frozen=True)
class ImageDescr:
    name: str
    size: int

    
    
class EventImageApi(CrudApi, Singleton):
    def __init__(self) -> None:
        super().__init__(
            S3ImageStorage.get_instance(),
            get_schema=ImageDescr,
            create_schema=ImageDescr,
        )
        
    def _get_create_callback(self) -> AsyncRouteCallback:
        async def callback(image: UploadFile, storage: S3ImageStorage=Depends(S3ImageStorage)):
           await storage.upload(
               filename=image.filename,
               file=image.file,
               size=image.size
            )
           # self._service.create({'name': image.filename})
           return ImageDescr(name=image.filename, size=image.size)
        return AsyncRouteCallback(callback)
        
        
        