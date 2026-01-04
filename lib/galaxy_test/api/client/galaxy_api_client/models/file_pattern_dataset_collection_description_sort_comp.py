from enum import Enum


class FilePatternDatasetCollectionDescriptionSortComp(str, Enum):
    LEXICAL = "lexical"
    NUMERIC = "numeric"

    def __str__(self) -> str:
        return str(self.value)
