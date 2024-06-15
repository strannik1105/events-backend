from models.events import enums, schemas


class EventTemplate:
    @staticmethod
    def get_event_file_types() -> list[schemas.EventFileTypeCreate]:
        return [
            schemas.EventFileTypeCreate(
                label=enums.EventFileTypeLabel.TXT,
                name=".txt",
                description="Файл формата TXT",
            ),
            schemas.EventFileTypeCreate(
                label=enums.EventFileTypeLabel.DOC,
                name=".doc",
                description="Файл формата DOC",
            ),
            schemas.EventFileTypeCreate(
                label=enums.EventFileTypeLabel.DOCX,
                name=".docx",
                description="Файл формата DOC",
            ),
            schemas.EventFileTypeCreate(
                label=enums.EventFileTypeLabel.ODT,
                name=".ods",
                description="Файл формата ODT",
            ),
            schemas.EventFileTypeCreate(
                label=enums.EventFileTypeLabel.GIF,
                name=".gif",
                description="Файл формата GIF",
            ),
            schemas.EventFileTypeCreate(
                label=enums.EventFileTypeLabel.JPG,
                name=".jpg",
                description="Файл формата JPG",
            ),
            schemas.EventFileTypeCreate(
                label=enums.EventFileTypeLabel.PNG,
                name=".png",
                description="Файл формата PNG",
            ),
            schemas.EventFileTypeCreate(
                label=enums.EventFileTypeLabel.PPT,
                name=".ppt",
                description="Файл формата PPT",
            ),
            schemas.EventFileTypeCreate(
                label=enums.EventFileTypeLabel.PPTX,
                name=".pptx",
                description="Файл формата PPTX",
            ),
            schemas.EventFileTypeCreate(
                label=enums.EventFileTypeLabel.ZIP,
                name=".zip",
                description="Файл формата ZIP",
            ),
            schemas.EventFileTypeCreate(
                label=enums.EventFileTypeLabel.RAR,
                name=".rar",
                description="Файл формата RAR",
            ),
            schemas.EventFileTypeCreate(
                label=enums.EventFileTypeLabel.XCL,
                name=".xcl",
                description="Файл формата XCL",
            ),
            schemas.EventFileTypeCreate(
                label=enums.EventFileTypeLabel.ODS,
                name=".ods",
                description="Файл формата ODS",
            ),
            schemas.EventFileTypeCreate(
                label=enums.EventFileTypeLabel.XLS,
                name=".xls",
                description="Файл формата XLS",
            ),
            schemas.EventFileTypeCreate(
                label=enums.EventFileTypeLabel.PPS,
                name=".pps",
                description="Файл формата PPS",
            ),
            schemas.EventFileTypeCreate(
                label=enums.EventFileTypeLabel.ODP,
                name=".odp",
                description="Файл формата ODP",
            ),
            schemas.EventFileTypeCreate(
                label=enums.EventFileTypeLabel.PDF,
                name=".pdf",
                description="Файл формата PDF",
            ),
            schemas.EventFileTypeCreate(
                label=enums.EventFileTypeLabel.HTML,
                name=".html",
                description="Файл формата HTML",
            ),
        ]
