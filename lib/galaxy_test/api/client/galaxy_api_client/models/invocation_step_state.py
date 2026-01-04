from enum import Enum, unique

__all__ = ["InvocationStepState"]


@unique
class InvocationStepState(str, Enum):
    """
    InvocationStepState Enum

    Args:
        new (str)                : Value for NEW
        ready (str)              : Value for READY
        scheduled (str)          : Value for SCHEDULED
    """

    NEW = "new"
    READY = "ready"
    SCHEDULED = "scheduled"
