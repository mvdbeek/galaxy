from enum import Enum, unique

__all__ = ["CustomBuildLenType"]


@unique
class CustomBuildLenType(str, Enum):
    """
    CustomBuildLenType Enum

    Args:
        file (str)               : Value for FILE
        fasta (str)              : Value for FASTA
        text (str)               : Value for TEXT
    """

    FILE = "file"
    FASTA = "fasta"
    TEXT = "text"
