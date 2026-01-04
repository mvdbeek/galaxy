from enum import Enum


class AccessMethodType(str, Enum):
    FILE = "file"
    FTP = "ftp"
    GLOBUS = "globus"
    GS = "gs"
    GSIFTP = "gsiftp"
    HTSGET = "htsget"
    HTTPS = "https"
    S3 = "s3"

    def __str__(self) -> str:
        return str(self.value)
