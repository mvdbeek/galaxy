from enum import Enum


class HistoryContentType(str, Enum):
    DATASET = "dataset"
    DATASET_COLLECTION = "dataset_collection"

    def __str__(self) -> str:
        return str(self.value)
