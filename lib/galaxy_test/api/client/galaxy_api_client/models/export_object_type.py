from enum import Enum


class ExportObjectType(str, Enum):
    HISTORY = "history"
    INVOCATION = "invocation"

    def __str__(self) -> str:
        return str(self.value)
