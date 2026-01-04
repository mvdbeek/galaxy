from enum import Enum, unique

__all__ = ["DatasetCollectionPopulatedState"]


@unique
class DatasetCollectionPopulatedState(str, Enum):
    """
    DatasetCollectionPopulatedState Enum

    Args:
        new (str)                : Value for NEW
        ok (str)                 : Value for OK
        failed (str)             : Value for FAILED
    """

    NEW = "new"
    OK = "ok"
    FAILED = "failed"
