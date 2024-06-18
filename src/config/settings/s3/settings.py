from pydantic import Field, field_validator
from pydantic_core.core_schema import ValidationInfo

from ..core import EnvCoreSettings


class S3Settings(EnvCoreSettings):
    SERVICE_NAME: str = "s3"
    SIGNATURE_VERSION: str = "s3v4"
    VERIFY: bool = False

    EVENTS_BUCKET: str = Field(..., alias="S3_EVENTS_BUCKET")
    EVENTS_BUCKET_POLICY: dict = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Deny",
                "Principal": "*",
                "Action": ["s3:*"],
                "Resource": ["arn:aws:s3:::{}", "arn:aws:s3:::{}/*"],
            },
            {
                "Effect": "Allow",
                "Principal": "*",
                "Action": ["s3:GetObject"],
                "Resource": ["arn:aws:s3:::{}/*"],
                "Condition": {
                    "StringEquals": {"s3:authType": "REST-QUERY-STRING"}
                },
            },
        ],
    }
    MAX_EVENTS_BUCKET_FILE_MB_SIZE: int = 10

    @field_validator("EVENTS_BUCKET_POLICY", mode="before")
    def assemble_events_bucket_policy(
        cls, v: dict, values: ValidationInfo
    ) -> dict:
        events_bucket = values.data.get("EVENTS_BUCKET", "events")
        v["Statement"][0]["Resource"][0] = v["Statement"][0]["Resource"][
            0
        ].format(events_bucket)
        v["Statement"][0]["Resource"][1] = v["Statement"][0]["Resource"][
            1
        ].format(events_bucket)
        v["Statement"][1]["Resource"][0] = v["Statement"][1]["Resource"][
            0
        ].format(events_bucket)
        return v
