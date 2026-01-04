from enum import Enum


class DatasetValidatedState(str, Enum):
    INVALID = "invalid"
    OK = "ok"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
