from enum import Enum


class ParsedWorkbookElementElementType(str, Enum):
    CHILD_COLLECTION = "child_collection"
    HDA = "hda"

    def __str__(self) -> str:
        return str(self.value)
