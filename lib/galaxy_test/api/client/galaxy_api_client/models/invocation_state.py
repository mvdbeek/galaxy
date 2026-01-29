from enum import Enum, unique

__all__ = ["InvocationState"]


@unique
class InvocationState(str, Enum):
    """
    InvocationState Enum

    Args:
        new (str)                : Value for NEW
        requires_materialization (str)
                                 : Value for REQUIRES_MATERIALIZATION
        ready (str)              : Value for READY
        scheduled (str)          : Value for SCHEDULED
        cancelled (str)          : Value for CANCELLED
        cancelling (str)         : Value for CANCELLING
        failed (str)             : Value for FAILED
    """

    NEW = "new"
    REQUIRES_MATERIALIZATION = "requires_materialization"
    READY = "ready"
    SCHEDULED = "scheduled"
    CANCELLED = "cancelled"
    CANCELLING = "cancelling"
    FAILED = "failed"
