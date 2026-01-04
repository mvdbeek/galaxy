from enum import Enum, unique

__all__ = ["WorkbookType"]


@unique
class WorkbookType(str, Enum):
    """
    WorkbookType Enum

    Args:
        datasets (str)           : Value for DATASETS
        collection (str)         : Value for COLLECTION
        collections (str)        : Value for COLLECTIONS
    """

    DATASETS = "datasets"
    COLLECTION = "collection"
    COLLECTIONS = "collections"
