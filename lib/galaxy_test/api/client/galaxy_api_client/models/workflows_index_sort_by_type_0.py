from enum import Enum


class WorkflowsIndexSortByType0(str, Enum):
    CREATE_TIME = "create_time"
    NAME = "name"
    UPDATE_TIME = "update_time"

    def __str__(self) -> str:
        return str(self.value)
