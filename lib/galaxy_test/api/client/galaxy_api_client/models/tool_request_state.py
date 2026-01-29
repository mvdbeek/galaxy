from enum import Enum, unique

__all__ = ["ToolRequestState"]


@unique
class ToolRequestState(str, Enum):
    """
    ToolRequestState Enum

    Args:
        new (str)                : Value for NEW
        submitted (str)          : Value for SUBMITTED
        failed (str)             : Value for FAILED
    """

    NEW = "new"
    SUBMITTED = "submitted"
    FAILED = "failed"
