from enum import Enum


class ModelStoreFormat(str, Enum):
    BAG_TAR = "bag.tar"
    BAG_TGZ = "bag.tgz"
    BAG_ZIP = "bag.zip"
    BCO_JSON = "bco.json"
    ROCRATE_ZIP = "rocrate.zip"
    TAR = "tar"
    TAR_GZ = "tar.gz"
    TGZ = "tgz"

    def __str__(self) -> str:
        return str(self.value)
