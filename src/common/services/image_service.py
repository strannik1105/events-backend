import os
import re
from dataclasses import dataclass
from datetime import datetime


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
