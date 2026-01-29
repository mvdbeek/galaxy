from enum import Enum, unique

__all__ = ["DatasetContentType"]


@unique
class DatasetContentType(str, Enum):
    """
    For retrieving content from a structured dataset (e.g. HDF5)

    Args:
        meta (str)               : Value for META
        attr (str)               : Value for ATTR
        stats (str)              : Value for STATS
        data (str)               : Value for DATA
    """

    META = "meta"
    ATTR = "attr"
    STATS = "stats"
    DATA = "data"
