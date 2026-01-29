from enum import Enum, unique

__all__ = ["AccessMethodType"]


@unique
class AccessMethodType(str, Enum):
    """
    AccessMethodType Enum

    Args:
        s3 (str)                 : Value for S3
        gs (str)                 : Value for GS
        ftp (str)                : Value for FTP
        gsiftp (str)             : Value for GSIFTP
        globus (str)             : Value for GLOBUS
        htsget (str)             : Value for HTSGET
        https (str)              : Value for HTTPS
        file (str)               : Value for FILE
    """

    S3 = "s3"
    GS = "gs"
    FTP = "ftp"
    GSIFTP = "gsiftp"
    GLOBUS = "globus"
    HTSGET = "htsget"
    HTTPS = "https"
    FILE = "file"
