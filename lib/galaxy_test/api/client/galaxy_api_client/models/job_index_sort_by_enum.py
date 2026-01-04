from enum import Enum


class JobIndexSortByEnum(str, Enum):
    CREATE_TIME = "create_time"
    UPDATE_TIME = "update_time"

    def __str__(self) -> str:
        return str(self.value)
