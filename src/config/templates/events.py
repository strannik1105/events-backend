from models.events import enums, schemas


class EventTemplate:
    @staticmethod
    def get_file_types() -> list[schemas.EventFileType]:
        return [
            schemas.EventFileType(
                label=enums.EventFileTypeLabel.TXT,
                name=".txt",
                description="Файл формата TXT",
            ),
            schemas.EventFileType(
                label=enums.EventFileTypeLabel.DOC,
                name=".doc",
                description="Файл формата DOC",
            ),
            schemas.EventFileType(
                label=enums.EventFileTypeLabel.DOCX,
                name=".docx",
                description="Файл формата DOC",
            ),
            schemas.EventFileType(
                label=enums.EventFileTypeLabel.ODT,
                name=".ods",
                description="Файл формата ODT",
            ),
            schemas.EventFileType(
                label=enums.EventFileTypeLabel.GIF,
                name=".gif",
                description="Файл формата GIF",
            ),
            schemas.EventFileType(
                label=enums.EventFileTypeLabel.JPG,
                name=".jpg",
                description="Файл формата JPG",
            ),
            schemas.EventFileType(
                label=enums.EventFileTypeLabel.PNG,
                name=".png",
                description="Файл формата PNG",
            ),
            schemas.EventFileType(
                label=enums.EventFileTypeLabel.PPT,
                name=".ppt",
                description="Файл формата PPT",
            ),
            schemas.EventFileType(
                label=enums.EventFileTypeLabel.PPTX,
                name=".pptx",
                description="Файл формата PPTX",
            ),
            schemas.EventFileType(
                label=enums.EventFileTypeLabel.ZIP,
                name=".zip",
                description="Файл формата ZIP",
            ),
            schemas.EventFileType(
                label=enums.EventFileTypeLabel.RAR,
                name=".rar",
                description="Файл формата RAR",
            ),
            schemas.EventFileType(
                label=enums.EventFileTypeLabel.XCL,
                name=".xcl",
                description="Файл формата XCL",
            ),
            schemas.EventFileType(
                label=enums.EventFileTypeLabel.ODS,
                name=".ods",
                description="Файл формата ODS",
            ),
            schemas.EventFileType(
                label=enums.EventFileTypeLabel.XLS,
                name=".xls",
                description="Файл формата XLS",
            ),
            schemas.EventFileType(
                label=enums.EventFileTypeLabel.PPS,
                name=".pps",
                description="Файл формата PPS",
            ),
            schemas.EventFileType(
                label=enums.EventFileTypeLabel.ODP,
                name=".odp",
                description="Файл формата ODP",
            ),
            schemas.EventFileType(
                label=enums.EventFileTypeLabel.PDF,
                name=".pdf",
                description="Файл формата PDF",
            ),
            schemas.EventFileType(
                label=enums.EventFileTypeLabel.HTML,
                name=".html",
                description="Файл формата HTML",
            ),
        ]
