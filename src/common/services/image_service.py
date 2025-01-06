import os
import re
from dataclasses import dataclass
from datetime import datetime
from typing import BinaryIO

import imgspy


class ImageUtils:
    _filename_ascii_strip_re = re.compile(r"[^A-Za-z0-9_.-]")

    @dataclass(frozen=True)
    class ImageInfo:
        content_type: str
        width: int
        height: int

    @dataclass(frozen=True)
    class ImageDescr(ImageInfo):
        name: str
        url: str
        size: int
        created_at: datetime

    @classmethod
    def secure_filename(cls, filename: str) -> str:
        """
        From Werkzeug secure_filename.
        """

        for sep in os.path.sep, os.path.altsep:
            if sep:
                filename = filename.replace(sep, " ")

        normalized_filename = cls._filename_ascii_strip_re.sub(
            "", "_".join(filename.split())
        )
        filename = str(normalized_filename).strip("._")
        return filename

    async def create_new_id(self, filename: str) -> str:
        identity = ImageUtils.secure_filename(filename)
        return identity

    @staticmethod
    def _get_file_size(file: BinaryIO) -> int:
        file.seek(0, os.SEEK_END)
        size = file.tell()
        file.seek(0, os.SEEK_SET)
        return size

    @staticmethod
    def _get_image_info(file: BinaryIO) -> ImageInfo:
        info = imgspy.info(file)
        file.seek(0, os.SEEK_SET)
        type = {"jpg": "jpeg"}.get(info["type"], info["type"])
        return ImageUtils.ImageInfo(
            content_type=f"image/{type}",
            width=info["width"],
            height=info["height"],
        )
