import json

from botocore.exceptions import ClientError

from common.db.s3 import S3Client
from common.managers import LoggerManager
from config.settings import settings


class S3Init:
    _logger = LoggerManager.get_base_logger()

    @classmethod
    async def events_bucket(cls) -> None:
        cls._logger.info("Start events bucket init")
        s3_client = S3Client.get()
        bucket_name = settings.s3.EVENTS_BUCKET
        bucket_policy = settings.s3.EVENTS_BUCKET_POLICY
        try:
            s3_client.head_bucket(Bucket=bucket_name)
        except ClientError:
            s3_client.create_bucket(Bucket=bucket_name)
            s3_client.put_bucket_policy(
                Bucket=bucket_name,
                Policy=json.dumps(bucket_policy),
            )
        cls._logger.info("Finish events bucket init")
