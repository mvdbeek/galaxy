from enum import Enum


class DatasetState(str, Enum):
    DEFERRED = "deferred"
    DISCARDED = "discarded"
    EMPTY = "empty"
    ERROR = "error"
    FAILED_METADATA = "failed_metadata"
    NEW = "new"
    OK = "ok"
    PAUSED = "paused"
    QUEUED = "queued"
    RUNNING = "running"
    SETTING_METADATA = "setting_metadata"
    UPLOAD = "upload"

    def __str__(self) -> str:
        return str(self.value)
