from enum import Enum, unique

__all__ = ["SortComp"]


@unique
class SortComp(str, Enum):
    """
    SortComp Enum

    Args:
        lexical (str)            : Value for LEXICAL
        numeric (str)            : Value for NUMERIC
    """

    LEXICAL = "lexical"
    NUMERIC = "numeric"
