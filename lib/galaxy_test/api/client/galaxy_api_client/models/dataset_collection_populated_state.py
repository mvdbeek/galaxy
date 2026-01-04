from enum import Enum


class DatasetCollectionPopulatedState(str, Enum):
    FAILED = "failed"
    NEW = "new"
    OK = "ok"

    def __str__(self) -> str:
        return str(self.value)
