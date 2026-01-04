from enum import Enum


class InvocationStepState(str, Enum):
    NEW = "new"
    READY = "ready"
    SCHEDULED = "scheduled"

    def __str__(self) -> str:
        return str(self.value)
