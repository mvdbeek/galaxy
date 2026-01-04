from enum import Enum


class ToolRequestState(str, Enum):
    FAILED = "failed"
    NEW = "new"
    SUBMITTED = "submitted"

    def __str__(self) -> str:
        return str(self.value)
