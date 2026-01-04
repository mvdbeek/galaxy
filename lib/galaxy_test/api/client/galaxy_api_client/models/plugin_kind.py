from enum import Enum


class PluginKind(str, Enum):
    DRS = "drs"
    RDM = "rdm"
    RFS = "rfs"
    STOCK = "stock"

    def __str__(self) -> str:
        return str(self.value)
