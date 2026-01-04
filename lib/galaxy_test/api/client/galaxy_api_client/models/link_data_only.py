from enum import Enum


class LinkDataOnly(str, Enum):
    COPY_FILES = "copy_files"
    LINK_TO_FILES = "link_to_files"

    def __str__(self) -> str:
        return str(self.value)
