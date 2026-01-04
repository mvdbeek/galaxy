from enum import Enum


class DatasetCollectionsSuitableConvertersSuitableConvertersInstanceType(str, Enum):
    HISTORY = "history"
    LIBRARY = "library"

    def __str__(self) -> str:
        return str(self.value)
