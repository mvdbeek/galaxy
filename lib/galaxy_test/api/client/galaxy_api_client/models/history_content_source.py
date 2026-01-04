from enum import Enum


class HistoryContentSource(str, Enum):
    HDA = "hda"
    HDCA = "hdca"
    LIBRARY = "library"
    LIBRARY_FOLDER = "library_folder"
    NEW_COLLECTION = "new_collection"

    def __str__(self) -> str:
        return str(self.value)
