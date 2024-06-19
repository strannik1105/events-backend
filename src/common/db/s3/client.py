from typing import Any

from boto3 import client
from botocore.client import BaseClient, Config

from config.settings import settings


class S3Client:
    _instance: Any = None
    _client: BaseClient | None = None

    def __new__(cls) -> Any:
        if cls._instance is None:
            cls._instance = super(S3Client, cls).__new__(cls)
            s3_client = client(
                aws_access_key_id=settings.minio.USER,
                aws_secret_access_key=settings.minio.PASS,
                endpoint_url=settings.minio.ADDR,
                service_name=settings.s3.SERVICE_NAME,
                config=Config(signature_version=settings.s3.SIGNATURE_VERSION),
                verify=settings.s3.VERIFY,
            )
            cls._client = s3_client
        return cls._instance

    @classmethod
    def get(cls) -> BaseClient:
        if cls._instance is None:
            cls()
        assert cls._client is not None, "S3 client has not been initialized"
        return cls._client
