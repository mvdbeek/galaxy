from enum import Enum, unique

__all__ = ["ParsedFetchWorkbookForDatasetsWorkbookType"]


@unique
class ParsedFetchWorkbookForDatasetsWorkbookType(str, Enum):
    """
    ParsedFetchWorkbookForDatasetsWorkbookType Enum

    Args:
        datasets (str)           : Value for DATASETS
        collection (str)         : Value for COLLECTION
        collections (str)        : Value for COLLECTIONS
    """

    DATASETS = "datasets"
    COLLECTION = "collection"
    COLLECTIONS = "collections"
