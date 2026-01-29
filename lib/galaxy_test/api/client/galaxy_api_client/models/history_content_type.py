from enum import Enum, unique

__all__ = ["HistoryContentType"]


@unique
class HistoryContentType(str, Enum):
    """
    Available types of History contents.

    Args:
        dataset (str)            : Value for DATASET
        dataset_collection (str) : Value for DATASET_COLLECTION
    """

    DATASET = "dataset"
    DATASET_COLLECTION = "dataset_collection"
