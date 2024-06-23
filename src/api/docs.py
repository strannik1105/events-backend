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
    def _get_filters_bool() -> list[dict[str, str]]:
        return [
            {
                "type": "Eq (equal)",
                "example_field": "kpiScore: 10",
                "description": "The target value is equal to the value in the filter",
            },
            {
                "type": "Neq (noq equal)",
                "example_field": "kpiScoreNeq: 10",
                "description": "The target value is not equal to the value in the filter",
            },
            {
                "type": "Is Null",
                "example_field": "kpiScoreIsNull: True",
                "description": "Checking whether the target value is null or not: True is, False is not",
            },
            {
                "type": "Is Empty",
                "example_field": "statusIsEmpty: True",
                "description": "Checking the target value for emptiness",
            },
            {
                "type": "Contains",
                "example_field": "statusContains: ACTIVE,INACTIVE",
                "description": "Checking the target value for the values it contains",
            },
            {
                "type": "Lt (less than)",
                "example_field": "kpiScoreLt: 10",
                "description": "The target value is less than the value in the filter",
            },
            {
                "type": "Le (less than or equal to)",
                "example_field": "kpiScoreLe: 10",
                "description": "The target value is less or equal than the value in the filter",
            },
            {
                "type": "Gt (more than)",
                "example_field": "kpiScoreGt: 10",
                "description": "The target value is more than the value in the filter",
            },
            {
                "type": "Ge (more than or equal to)",
                "example_field": "kpiScoreGe: 10",
                "description": "The target value is more or equal than the value in the filter",
            },
            {
                "type": "Like (sql like function)",
                "example_field": "NameLike: Ivan",
                "description": "The input field is a template for  <a href=https://www.postgresql.org/docs/current/functions-matching.html>more documentation</a>",
            },
            {
                "type": "ILike (sql ilike function)",
                "example_field": "NameILike: IVAN",
                "description": "The input field is a template for <a href=https://www.postgresql.org/docs/current/functions-matching.html>more documentation</a>",
            },
            {
                "type": "In",
                "example_field": "StatusIn: ACTIVE,INACTIVE",
                "description": "Checking the occurrence of the target value in the transmitted list",
            },
            {
                "type": "Not In",
                "example_field": "StatusNotIn: ACTIVE,INACTIVE",
                "description": "Checking if the target value does not appear in the transmitted list",
            },
            {
                "type": "Not",
                "example_field": "StatusNot: ACTIVE",
                "description": "Checking the negation of the target value from the transmitted value",
            },
            {
                "type": "Order By (sorting)",
                "example_field": "orderBy: +name,-age",
                "description": "'+' - sort in ascending order, '-' - sort in descending order",
            },
        ]

    @classmethod
    def _get_filters(cls) -> str:
        return "\n".join(
            [
                f"| {doc.get('type')} | {doc.get('example_field')} | {doc.get('description')}"
                for doc in cls._get_filters_bool()
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
                "name": "User",
                "description": "User methods",
            },
            {
                "name": "Security",
                "description": "Security methods",
            },
            {
                "name": "Event",
                "description": "Event methods",
            },
            {
                "name": "Event content",
                "description": "Event content methods",
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

<details>
<summary>Service filters</summary>
<br>

| Filter Type | Example Field | Description |
|--------------------|-----------------|-------------|
{cls._get_filters()}
</details>
"""
