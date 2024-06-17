from config.exceptions import APIExceptionBook


class APIDoc:
    @staticmethod
    def _get_exceptions() -> str:
        return "\n".join(
            [
                f"| {exc.detail.code} | {exc.status_code} | {exc.detail.description}"
                for exc in APIExceptionBook
            ]
        )

    @staticmethod
    def get_tags() -> list[dict[str, str]]:
        return [
            {
                "name": "Auth",
                "description": "Auth methods",
            },
            {
                "name": "Security",
                "description": "Security methods",
            },
            {
                "name": "Event file",
                "description": "Event file methods",
            },
        ]

    @classmethod
    def get_description(cls) -> str:
        return f"""
<details>
<summary>Possible service error codes</summary>
<br>

| Service Error Code | HTTP Error Code | Description |
|--------------------|-----------------|-------------|
{cls._get_exceptions()}
</details>
"""
