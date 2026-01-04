from enum import Enum


class VisualizationsIndexSortAttribute(str, Enum):
    CREATE_TIME = "create_time"
    TITLE = "title"
    UPDATE_TIME = "update_time"
    USERNAME = "username"

    def __str__(self) -> str:
        return str(self.value)
