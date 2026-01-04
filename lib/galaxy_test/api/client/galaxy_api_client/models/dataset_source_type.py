from enum import Enum, unique

__all__ = ["DatasetSourceType"]


@unique
class DatasetSourceType(str, Enum):
    """
    DatasetSourceType Enum

    Args:
        hda (str)                : Value for HDA
        ldda (str)               : Value for LDDA
    """

    HDA = "hda"
    LDDA = "ldda"
