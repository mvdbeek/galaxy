from enum import Enum


class ObjectStoreTemplateSummaryType(str, Enum):
    AWS_S3 = "aws_s3"
    AZURE_BLOB = "azure_blob"
    BOTO3 = "boto3"
    DISK = "disk"
    GENERIC_S3 = "generic_s3"
    IRODS = "irods"
    ONEDATA = "onedata"
    RUCIO = "rucio"

    def __str__(self) -> str:
        return str(self.value)
