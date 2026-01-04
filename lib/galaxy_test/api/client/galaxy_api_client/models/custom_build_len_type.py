from enum import Enum


class CustomBuildLenType(str, Enum):
    FASTA = "fasta"
    FILE = "file"
    TEXT = "text"

    def __str__(self) -> str:
        return str(self.value)
