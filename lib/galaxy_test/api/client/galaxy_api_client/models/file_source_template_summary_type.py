from enum import Enum


class FileSourceTemplateSummaryType(str, Enum):
    AZURE = "azure"
    AZUREFLAT = "azureflat"
    DATAVERSE = "dataverse"
    DROPBOX = "dropbox"
    ELABFTW = "elabftw"
    FTP = "ftp"
    GOOGLEDRIVE = "googledrive"
    HUGGINGFACE = "huggingface"
    INVENIORDM = "inveniordm"
    OMERO = "omero"
    ONEDATA = "onedata"
    POSIX = "posix"
    RSPACE = "rspace"
    S3FS = "s3fs"
    WEBDAV = "webdav"
    ZENODO = "zenodo"

    def __str__(self) -> str:
        return str(self.value)
