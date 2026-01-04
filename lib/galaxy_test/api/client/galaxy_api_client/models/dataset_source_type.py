from enum import Enum


class DatasetSourceType(str, Enum):
    HDA = "hda"
    LDDA = "ldda"

    def __str__(self) -> str:
        return str(self.value)
