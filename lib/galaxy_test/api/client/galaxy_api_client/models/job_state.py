from enum import Enum


class JobState(str, Enum):
    DELETED = "deleted"
    DELETING = "deleting"
    ERROR = "error"
    FAILED = "failed"
    NEW = "new"
    OK = "ok"
    PAUSED = "paused"
    QUEUED = "queued"
    RESUBMITTED = "resubmitted"
    RUNNING = "running"
    SKIPPED = "skipped"
    STOP = "stop"
    STOPPED = "stopped"
    UPLOAD = "upload"
    WAITING = "waiting"

    def __str__(self) -> str:
        return str(self.value)
