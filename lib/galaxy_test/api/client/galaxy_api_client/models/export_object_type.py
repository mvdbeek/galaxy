from enum import Enum, unique

__all__ = ["ExportObjectType"]


@unique
class ExportObjectType(str, Enum):
    """
    Types of objects that can be exported.

    Args:
        history (str)            : Value for HISTORY
        invocation (str)         : Value for INVOCATION
    """

    HISTORY = "history"
    INVOCATION = "invocation"
