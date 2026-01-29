from enum import Enum, unique

__all__ = ["FilePatternDatasetCollectionDescriptionSortKey"]


@unique
class FilePatternDatasetCollectionDescriptionSortKey(str, Enum):
    """
    FilePatternDatasetCollectionDescriptionSortKey Enum

    Args:
        filename (str)           : Value for FILENAME
        name (str)               : Value for NAME
        designation (str)        : Value for DESIGNATION
        dbkey (str)              : Value for DBKEY
    """

    FILENAME = "filename"
    NAME = "name"
    DESIGNATION = "designation"
    DBKEY = "dbkey"
