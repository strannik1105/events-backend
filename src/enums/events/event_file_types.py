from enum import IntEnum, unique


@unique
class EventFileTypeLabel(IntEnum):
    TXT = 0
    DOC = 1
    DOCX = 2
    ODT = 3
    GIF = 4
    JPG = 5
    PNG = 6
    PPT = 7
    PPTX = 8
    ZIP = 9
    RAR = 10
    XCL = 11
    ODS = 12
    XLS = 13
    PPS = 14
    ODP = 15
    PDF = 16
    HTML = 17
    XLSX = 20
    CSV = 21
    JSON = 22
