from enum import Enum


class ParseWorkbookPrefixColumnsType(str, Enum):
    MODELOBJECTS = "ModelObjects"
    URI = "URI"

    def __str__(self) -> str:
        return str(self.value)
