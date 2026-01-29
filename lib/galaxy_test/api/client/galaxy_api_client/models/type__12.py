from enum import Enum, unique

__all__ = ["Type12"]


@unique
class Type12(str, Enum):
    """
    Type12 Enum

    Args:
        aws_s3 (str)             : Value for AWS_S3
        azure_blob (str)         : Value for AZURE_BLOB
        boto3 (str)              : Value for BOTO3
        disk (str)               : Value for DISK
        generic_s3 (str)         : Value for GENERIC_S3
        onedata (str)            : Value for ONEDATA
        rucio (str)              : Value for RUCIO
        irods (str)              : Value for IRODS
    """

    AWS_S3 = "aws_s3"
    AZURE_BLOB = "azure_blob"
    BOTO3 = "boto3"
    DISK = "disk"
    GENERIC_S3 = "generic_s3"
    ONEDATA = "onedata"
    RUCIO = "rucio"
    IRODS = "irods"
