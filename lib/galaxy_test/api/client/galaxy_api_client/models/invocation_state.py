from enum import Enum


class InvocationState(str, Enum):
    CANCELLED = "cancelled"
    CANCELLING = "cancelling"
    FAILED = "failed"
    NEW = "new"
    READY = "ready"
    REQUIRES_MATERIALIZATION = "requires_materialization"
    SCHEDULED = "scheduled"

    def __str__(self) -> str:
        return str(self.value)
