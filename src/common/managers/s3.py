from typing import BinaryIO

from botocore.client import BaseClient
from botocore.response import StreamingBody


class S3Manager:
    @staticmethod
    def _build_path(obj: str, folder: str | None) -> str:
        if not folder:
            return obj
        return folder + "/" + obj

    @classmethod
    def fget(
        cls,
        s3_client: BaseClient,
        bucket: str,
        obj: str,
        folder: str | None,
        file_name: str,
    ) -> None:
        path = cls._build_path(obj=obj, folder=folder)
        s3_client.download_file(
            Bucket=bucket,
            Key=path,
            Filename=file_name,
        )

    @classmethod
    def get(
        cls, s3_client: BaseClient, bucket: str, obj: str, folder: str | None
    ) -> StreamingBody:
        path = cls._build_path(obj=obj, folder=folder)
        response = s3_client.get_object(
            Bucket=bucket,
            Key=path,
        )
        return response["Body"]

    @classmethod
    def fput(
        cls,
        s3_client: BaseClient,
        bucket: str,
        file: str,
        obj: str,
        folder: str | None,
    ) -> None:
        path = cls._build_path(obj=obj, folder=folder)
        s3_client.upload_file(
            Filename=file,
            Bucket=bucket,
            Key=path,
        )

    @classmethod
    def put_obj(
        cls,
        s3_client: BaseClient,
        bucket: str,
        fileobj: BinaryIO,
        obj: str,
        folder: str | None,
        content_type: str | None = None,
    ) -> None:
        path = cls._build_path(obj=obj, folder=folder)
        s3_client.upload_fileobj(
            Fileobj=fileobj,
            Bucket=bucket,
            Key=path,
            ExtraArgs={
                "ContentType": content_type,
            },
        )

    @classmethod
    def remove(
        cls, s3_client: BaseClient, bucket: str, obj: str, folder: str | None
    ) -> None:
        path = cls._build_path(obj=obj, folder=folder)
        s3_client.delete_object(
            Bucket=bucket,
            Key=path,
        )

    @classmethod
    def generate_url(
        cls,
        s3_client: BaseClient,
        bucket: str,
        obj: str,
        folder: str | None,
        expire: int = 1800,
    ) -> str:
        path = cls._build_path(obj=obj, folder=folder)
        link = s3_client.generate_presigned_url(
            ClientMethod="get_object",
            Params={
                "Bucket": bucket,
                "Key": path,
            },
            ExpiresIn=expire,
        )
        return link

    @classmethod
    def copy_object(
        cls,
        s3_client: BaseClient,
        bucket: str,
        d_obj: str,
        d_folder: str | None,
        s_obj: str,
        s_folder: str | None,
    ) -> None:
        path = cls._build_path(obj=d_obj, folder=d_folder)
        s_path = cls._build_path(obj=s_obj, folder=s_folder)
        s3_client.copy_object(
            Bucket=bucket,
            CopySource=f"{bucket}/{s_path}",
            Key=path,
        )
