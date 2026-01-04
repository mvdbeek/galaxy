from enum import Enum, unique

__all__ = ["DatasetState"]


@unique
class DatasetState(str, Enum):
    """
    DatasetState Enum

    Args:
        new (str)                : Value for NEW
        upload (str)             : Value for UPLOAD
        queued (str)             : Value for QUEUED
        running (str)            : Value for RUNNING
        ok (str)                 : Value for OK
        empty (str)              : Value for EMPTY
        error (str)              : Value for ERROR
        paused (str)             : Value for PAUSED
        setting_metadata (str)   : Value for SETTING_METADATA
        failed_metadata (str)    : Value for FAILED_METADATA
        deferred (str)           : Value for DEFERRED
        discarded (str)          : Value for DISCARDED
    """

    NEW = "new"
    UPLOAD = "upload"
    QUEUED = "queued"
    RUNNING = "running"
    OK = "ok"
    EMPTY = "empty"
    ERROR = "error"
    PAUSED = "paused"
    SETTING_METADATA = "setting_metadata"
    FAILED_METADATA = "failed_metadata"
    DEFERRED = "deferred"
    DISCARDED = "discarded"
