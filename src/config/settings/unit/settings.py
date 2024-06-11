from ..core import CoreSettings


class UnitSettings(CoreSettings):
    BYTE: int = 1
    KB: int = BYTE * 1024
    MB: int = KB * 1024
    GB: int = MB * 1024
