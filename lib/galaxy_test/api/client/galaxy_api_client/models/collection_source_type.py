from enum import Enum


class CollectionSourceType(str, Enum):
    HDA = "hda"
    HDCA = "hdca"
    LDDA = "ldda"
    NEW_COLLECTION = "new_collection"

    def __str__(self) -> str:
        return str(self.value)
