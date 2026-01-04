from enum import Enum


class DatasetSourceTransformActionType(str, Enum):
    DATATYPE_GROOM = "datatype_groom"
    SPACES_TO_TABS = "spaces_to_tabs"
    TO_POSIX_LINES = "to_posix_lines"

    def __str__(self) -> str:
        return str(self.value)
