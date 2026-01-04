from enum import Enum, unique

__all__ = ["CollectionSourceType"]


@unique
class CollectionSourceType(str, Enum):
    """
    CollectionSourceType Enum

    Args:
        hda (str)                : Value for HDA
        ldda (str)               : Value for LDDA
        hdca (str)               : Value for HDCA
        new_collection (str)     : Value for NEW_COLLECTION
    """

    HDA = "hda"
    LDDA = "ldda"
    HDCA = "hdca"
    NEW_COLLECTION = "new_collection"
