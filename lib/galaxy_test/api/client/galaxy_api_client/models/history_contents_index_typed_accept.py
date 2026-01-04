from enum import Enum


class HistoryContentsIndexTypedAccept(str, Enum):
    APPLICATIONJSON = "application/json"
    APPLICATIONVND_GALAXY_HISTORY_CONTENTS_STATSJSON = "application/vnd.galaxy.history.contents.stats+json"

    def __str__(self) -> str:
        return str(self.value)
