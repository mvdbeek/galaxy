from enum import Enum, unique

__all__ = ["Type13"]


@unique
class Type13(str, Enum):
    """
    Type13 Enum

    Args:
        ftp (str)                : Value for FTP
        posix (str)              : Value for POSIX
        s3fs (str)               : Value for S3FS
        azure (str)              : Value for AZURE
        azureflat (str)          : Value for AZUREFLAT
        onedata (str)            : Value for ONEDATA
        webdav (str)             : Value for WEBDAV
        dropbox (str)            : Value for DROPBOX
        googledrive (str)        : Value for GOOGLEDRIVE
        elabftw (str)            : Value for ELABFTW
        inveniordm (str)         : Value for INVENIORDM
        zenodo (str)             : Value for ZENODO
        rspace (str)             : Value for RSPACE
        dataverse (str)          : Value for DATAVERSE
        huggingface (str)        : Value for HUGGINGFACE
        omero (str)              : Value for OMERO
    """

    FTP = "ftp"
    POSIX = "posix"
    S3FS = "s3fs"
    AZURE = "azure"
    AZUREFLAT = "azureflat"
    ONEDATA = "onedata"
    WEBDAV = "webdav"
    DROPBOX = "dropbox"
    GOOGLEDRIVE = "googledrive"
    ELABFTW = "elabftw"
    INVENIORDM = "inveniordm"
    ZENODO = "zenodo"
    RSPACE = "rspace"
    DATAVERSE = "dataverse"
    HUGGINGFACE = "huggingface"
    OMERO = "omero"
