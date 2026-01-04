from enum import Enum, unique

__all__ = ["DataItemSourceType"]


@unique
class DataItemSourceType(str, Enum):
    """
    DataItemSourceType Enum

    Args:
        hda (str)                : Value for HDA
        ldda (str)               : Value for LDDA
        hdca (str)               : Value for HDCA
        dce (str)                : Value for DCE
        dc (str)                 : Value for DC
    """

    HDA = "hda"
    LDDA = "ldda"
    HDCA = "hdca"
    DCE = "dce"
    DC = "dc"
