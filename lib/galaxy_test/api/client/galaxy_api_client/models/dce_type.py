from enum import Enum, unique

__all__ = ["DceType"]


@unique
class DceType(str, Enum):
    """
    Available types of dataset collection elements.

    Args:
        hda (str)                : Value for HDA
        dataset_collection (str) : Value for DATASET_COLLECTION
    """

    HDA = "hda"
    DATASET_COLLECTION = "dataset_collection"
