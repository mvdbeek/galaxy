from enum import Enum


class DataItemSourceType(str, Enum):
    DC = "dc"
    DCE = "dce"
    HDA = "hda"
    HDCA = "hdca"
    LDDA = "ldda"

    def __str__(self) -> str:
        return str(self.value)
