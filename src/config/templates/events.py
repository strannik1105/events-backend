from enums import events as event_enums
from schemas import events as event_schemas


class EventTemplate:
    @staticmethod
    def get_event_file_types() -> list[event_schemas.EventFileTypeCreate]:
        return [
            event_schemas.EventFileTypeCreate(
                label=event_enums.EventFileTypeLabel.TXT,
                name=".txt",
                description="Файл формата TXT",
            ),
            event_schemas.EventFileTypeCreate(
                label=event_enums.EventFileTypeLabel.DOC,
                name=".doc",
                description="Файл формата DOC",
            ),
            event_schemas.EventFileTypeCreate(
                label=event_enums.EventFileTypeLabel.DOCX,
                name=".docx",
                description="Файл формата DOCX",
            ),
            event_schemas.EventFileTypeCreate(
                label=event_enums.EventFileTypeLabel.ODT,
                name=".ods",
                description="Файл формата ODT",
            ),
            event_schemas.EventFileTypeCreate(
                label=event_enums.EventFileTypeLabel.GIF,
                name=".gif",
                description="Файл формата GIF",
            ),
            event_schemas.EventFileTypeCreate(
                label=event_enums.EventFileTypeLabel.JPG,
                name=".jpg",
                description="Файл формата JPG",
            ),
            event_schemas.EventFileTypeCreate(
                label=event_enums.EventFileTypeLabel.PNG,
                name=".png",
                description="Файл формата PNG",
            ),
            event_schemas.EventFileTypeCreate(
                label=event_enums.EventFileTypeLabel.PPT,
                name=".ppt",
                description="Файл формата PPT",
            ),
            event_schemas.EventFileTypeCreate(
                label=event_enums.EventFileTypeLabel.PPTX,
                name=".pptx",
                description="Файл формата PPTX",
            ),
            event_schemas.EventFileTypeCreate(
                label=event_enums.EventFileTypeLabel.ZIP,
                name=".zip",
                description="Файл формата ZIP",
            ),
            event_schemas.EventFileTypeCreate(
                label=event_enums.EventFileTypeLabel.RAR,
                name=".rar",
                description="Файл формата RAR",
            ),
            event_schemas.EventFileTypeCreate(
                label=event_enums.EventFileTypeLabel.XCL,
                name=".xcl",
                description="Файл формата XCL",
            ),
            event_schemas.EventFileTypeCreate(
                label=event_enums.EventFileTypeLabel.ODS,
                name=".ods",
                description="Файл формата ODS",
            ),
            event_schemas.EventFileTypeCreate(
                label=event_enums.EventFileTypeLabel.XLS,
                name=".xls",
                description="Файл формата XLS",
            ),
            event_schemas.EventFileTypeCreate(
                label=event_enums.EventFileTypeLabel.PPS,
                name=".pps",
                description="Файл формата PPS",
            ),
            event_schemas.EventFileTypeCreate(
                label=event_enums.EventFileTypeLabel.ODP,
                name=".odp",
                description="Файл формата ODP",
            ),
            event_schemas.EventFileTypeCreate(
                label=event_enums.EventFileTypeLabel.PDF,
                name=".pdf",
                description="Файл формата PDF",
            ),
            event_schemas.EventFileTypeCreate(
                label=event_enums.EventFileTypeLabel.HTML,
                name=".html",
                description="Файл формата HTML",
            ),
            event_schemas.EventFileTypeCreate(
                label=event_enums.EventFileTypeLabel.XLSX,
                name=".xlsx",
                description="Файл формата XLSX",
            ),
            event_schemas.EventFileTypeCreate(
                label=event_enums.EventFileTypeLabel.CSV,
                name=".csv",
                description="Файл формата CSV",
            ),
            event_schemas.EventFileTypeCreate(
                label=event_enums.EventFileTypeLabel.JSON,
                name=".json",
                description="Файл формата JSON",
            ),
        ]
