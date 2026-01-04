from enum import Enum


class HistoriesExportsIndexExportsAccept(str, Enum):
    APPLICATIONJSON = "application/json"
    APPLICATIONVND_GALAXY_TASK_EXPORTJSON = "application/vnd.galaxy.task.export+json"

    def __str__(self) -> str:
        return str(self.value)
