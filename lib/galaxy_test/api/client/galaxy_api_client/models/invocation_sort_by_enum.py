from enum import Enum


class InvocationSortByEnum(str, Enum):
    CREATE_TIME = "create_time"
    NONE = "None"
    UPDATE_TIME = "update_time"

    def __str__(self) -> str:
        return str(self.value)
