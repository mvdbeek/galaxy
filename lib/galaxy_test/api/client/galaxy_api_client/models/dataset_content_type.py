from enum import Enum


class DatasetContentType(str, Enum):
    ATTR = "attr"
    DATA = "data"
    META = "meta"
    STATS = "stats"

    def __str__(self) -> str:
        return str(self.value)
