from enum import Enum, unique

__all__ = ["DatasetSourceTransformActionType"]


@unique
class DatasetSourceTransformActionType(str, Enum):
    """
    DatasetSourceTransformActionType Enum

    Args:
        to_posix_lines (str)     : Value for TO_POSIX_LINES
        spaces_to_tabs (str)     : Value for SPACES_TO_TABS
        datatype_groom (str)     : Value for DATATYPE_GROOM
    """

    TO_POSIX_LINES = "to_posix_lines"
    SPACES_TO_TABS = "spaces_to_tabs"
    DATATYPE_GROOM = "datatype_groom"
