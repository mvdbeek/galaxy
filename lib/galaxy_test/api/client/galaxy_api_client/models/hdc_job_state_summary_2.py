from dataclasses import dataclass

__all__ = ["HdcJobStateSummary2"]


@dataclass
class HdcJobStateSummary2:
    """
    Overview of the job states working inside a dataset collection.

    Args:
        all_jobs (int | None)    : Total number of jobs associated with a dataset
                                   collection.
        deleted (int | None)     : Number of jobs in the `deleted` state.
        deleted_new (int | None) : Number of jobs in the `deleted_new` state.
        error (int | None)       : Number of jobs in the `error` state.
        failed (int | None)      : Number of jobs in the `failed` state.
        new (int | None)         : Number of jobs in the `new` state.
        ok (int | None)          : Number of jobs in the `ok` state.
        paused (int | None)      : Number of jobs in the `paused` state.
        queued (int | None)      : Number of jobs in the `queued` state.
        resubmitted (int | None) : Number of jobs in the `resubmitted` state.
        running (int | None)     : Number of jobs in the `running` state.
        skipped (int | None)     : Number of jobs that were skipped due to conditional
                                   workflow step execution.
        upload (int | None)      : Number of jobs in the `upload` state.
        waiting (int | None)     : Number of jobs in the `waiting` state.
    """

    all_jobs: int | None = 0  # Total number of jobs associated with a dataset collection.
    deleted: int | None = 0  # Number of jobs in the `deleted` state.
    deleted_new: int | None = 0  # Number of jobs in the `deleted_new` state.
    error: int | None = 0  # Number of jobs in the `error` state.
    failed: int | None = 0  # Number of jobs in the `failed` state.
    new: int | None = 0  # Number of jobs in the `new` state.
    ok: int | None = 0  # Number of jobs in the `ok` state.
    paused: int | None = 0  # Number of jobs in the `paused` state.
    queued: int | None = 0  # Number of jobs in the `queued` state.
    resubmitted: int | None = 0  # Number of jobs in the `resubmitted` state.
    running: int | None = 0  # Number of jobs in the `running` state.
    skipped: int | None = 0  # Number of jobs that were skipped due to conditional workflow step execution.
    upload: int | None = 0  # Number of jobs in the `upload` state.
    waiting: int | None = 0  # Number of jobs in the `waiting` state.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "all_jobs": "all_jobs",
            "deleted": "deleted",
            "deleted_new": "deleted_new",
            "error": "error",
            "failed": "failed",
            "new": "new",
            "ok": "ok",
            "paused": "paused",
            "queued": "queued",
            "resubmitted": "resubmitted",
            "running": "running",
            "skipped": "skipped",
            "upload": "upload",
            "waiting": "waiting",
        }
        key_transform_with_dump = {
            "all_jobs": "all_jobs",
            "deleted": "deleted",
            "deleted_new": "deleted_new",
            "error": "error",
            "failed": "failed",
            "new": "new",
            "ok": "ok",
            "paused": "paused",
            "queued": "queued",
            "resubmitted": "resubmitted",
            "running": "running",
            "skipped": "skipped",
            "upload": "upload",
            "waiting": "waiting",
        }
