from enum import Enum, unique

__all__ = ["ModelStoreFormat"]


@unique
class ModelStoreFormat(str, Enum):
    """
    Available types of model stores for export.

    Args:
        tgz (str)                : Value for TGZ
        tar (str)                : Value for TAR
        tar.gz (str)             : Value for TARGZ
        bag.zip (str)            : Value for BAGZIP
        bag.tar (str)            : Value for BAGTAR
        bag.tgz (str)            : Value for BAGTGZ
        rocrate.zip (str)        : Value for ROCRATEZIP
        bco.json (str)           : Value for BCOJSON
    """

    TGZ = "tgz"
    TAR = "tar"
    TARGZ = "tar.gz"
    BAGZIP = "bag.zip"
    BAGTAR = "bag.tar"
    BAGTGZ = "bag.tgz"
    ROCRATEZIP = "rocrate.zip"
    BCOJSON = "bco.json"
