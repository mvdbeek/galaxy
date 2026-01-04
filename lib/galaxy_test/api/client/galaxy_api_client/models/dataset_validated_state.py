from enum import Enum, unique

__all__ = ["DatasetValidatedState"]


@unique
class DatasetValidatedState(str, Enum):
    """
    DatasetValidatedState Enum

    Args:
        unknown (str)            : Value for UNKNOWN
        invalid (str)            : Value for INVALID
        ok (str)                 : Value for OK
    """

    UNKNOWN = "unknown"
    INVALID = "invalid"
    OK = "ok"
