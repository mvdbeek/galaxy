from enum import Enum, unique

__all__ = ["JobState"]


@unique
class JobState(str, Enum):
    """
    JobState Enum

    Args:
        new (str)                : Value for NEW
        resubmitted (str)        : Value for RESUBMITTED
        upload (str)             : Value for UPLOAD
        waiting (str)            : Value for WAITING
        queued (str)             : Value for QUEUED
        running (str)            : Value for RUNNING
        ok (str)                 : Value for OK
        error (str)              : Value for ERROR
        failed (str)             : Value for FAILED
        paused (str)             : Value for PAUSED
        deleting (str)           : Value for DELETING
        deleted (str)            : Value for DELETED
        stop (str)               : Value for STOP
        stopped (str)            : Value for STOPPED
        skipped (str)            : Value for SKIPPED
    """

    NEW = "new"
    RESUBMITTED = "resubmitted"
    UPLOAD = "upload"
    WAITING = "waiting"
    QUEUED = "queued"
    RUNNING = "running"
    OK = "ok"
    ERROR = "error"
    FAILED = "failed"
    PAUSED = "paused"
    DELETING = "deleting"
    DELETED = "deleted"
    STOP = "stop"
    STOPPED = "stopped"
    SKIPPED = "skipped"
