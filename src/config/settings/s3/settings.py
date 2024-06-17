from pydantic import Field

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
                "Effect": "Allow",
                "Principal": {"AWS": "*"},
                "Action": ["s3:GetBucketLocation", "s3:ListBucket"],
                "Resource": "arn:aws:s3:::events",
            },
            {
                "Effect": "Allow",
                "Principal": {"AWS": "*"},
                "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::events/*",
            },
        ],
    }
    MAX_EVENTS_BUCKET_FILE_MB_SIZE: int = 10
