from enum import Enum


class StoredItemOrderBy(str, Enum):
    NAME_ASC = "name-asc"
    NAME_DSC = "name-dsc"
    SIZE_ASC = "size-asc"
    SIZE_DSC = "size-dsc"
    UPDATE_TIME_ASC = "update_time-asc"
    UPDATE_TIME_DSC = "update_time-dsc"

    def __str__(self) -> str:
        return str(self.value)
