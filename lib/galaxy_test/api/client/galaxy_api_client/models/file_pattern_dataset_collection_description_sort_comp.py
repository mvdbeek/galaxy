from enum import Enum, unique

__all__ = ["FilePatternDatasetCollectionDescriptionSortComp"]


@unique
class FilePatternDatasetCollectionDescriptionSortComp(str, Enum):
    """
    FilePatternDatasetCollectionDescriptionSortComp Enum

    Args:
        lexical (str)            : Value for LEXICAL
        numeric (str)            : Value for NUMERIC
    """

    LEXICAL = "lexical"
    NUMERIC = "numeric"
