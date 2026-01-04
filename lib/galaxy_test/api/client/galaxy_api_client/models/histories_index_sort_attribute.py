from enum import Enum


class HistoriesIndexSortAttribute(str, Enum):
    CREATE_TIME = "create_time"
    NAME = "name"
    UPDATE_TIME = "update_time"
    USERNAME = "username"

    def __str__(self) -> str:
        return str(self.value)
