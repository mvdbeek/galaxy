from enum import Enum, unique

__all__ = ["TaskState"]


@unique
class TaskState(str, Enum):
    """
    Enum representing the possible states of a task.

    Args:
        PENDING (str)            : Value for PENDING
        STARTED (str)            : Value for STARTED
        RETRY (str)              : Value for RETRY
        FAILURE (str)            : Value for FAILURE
        SUCCESS (str)            : Value for SUCCESS
    """

    PENDING = "PENDING"
    STARTED = "STARTED"
    RETRY = "RETRY"
    FAILURE = "FAILURE"
    SUCCESS = "SUCCESS"
