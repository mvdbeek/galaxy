from enum import Enum


class DCEType(str, Enum):
    DATASET_COLLECTION = "dataset_collection"
    HDA = "hda"

    def __str__(self) -> str:
        return str(self.value)
