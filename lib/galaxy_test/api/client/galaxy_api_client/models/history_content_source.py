from enum import Enum, unique

__all__ = ["HistoryContentSource"]


@unique
class HistoryContentSource(str, Enum):
    """
    HistoryContentSource Enum

    Args:
        hda (str)                : Value for HDA
        hdca (str)               : Value for HDCA
        library (str)            : Value for LIBRARY
        library_folder (str)     : Value for LIBRARY_FOLDER
        new_collection (str)     : Value for NEW_COLLECTION
    """

    HDA = "hda"
    HDCA = "hdca"
    LIBRARY = "library"
    LIBRARY_FOLDER = "library_folder"
    NEW_COLLECTION = "new_collection"
