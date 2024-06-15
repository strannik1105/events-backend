from typing import Any

from fastapi import Body, File, Header, Path, Query, params


class APIParam:
    @staticmethod
    def query(
        default: Any, description: str | None = None, alias: str | None = None
    ) -> params.Query:
        return Query(
            default=default,
            description=description,
            alias=alias,
            validation_alias=alias,
        )

    @staticmethod
    def path(
        default: Any, description: str | None = None, alias: str | None = None
    ) -> params.Path:
        return Path(
            default=default,
            description=description,
            alias=alias,
            validation_alias=alias,
        )

    @staticmethod
    def body(
        default: Any,
        description: str | None = None,
        alias: str | None = None,
        embed: bool = False,
    ) -> params.Body:
        return Body(
            default=default,
            description=description,
            alias=alias,
            validation_alias=alias,
            embed=embed,
        )

    @staticmethod
    def file(
        default: Any, description: str | None = None, alias: str | None = None
    ) -> params.File:
        return File(
            default=default,
            description=description,
            alias=alias,
            validation_alias=alias,
        )

    @staticmethod
    def header(
        default: Any,
        description: str | None = None,
        alias: str | None = None,
        convert_underscores: bool = True,
    ) -> params.Header:
        return Header(
            default=default,
            description=description,
            alias=alias,
            validation_alias=alias,
            convert_underscores=convert_underscores,
        )
