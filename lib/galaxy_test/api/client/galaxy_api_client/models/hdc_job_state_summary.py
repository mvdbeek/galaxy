from dataclasses import dataclass

__all__ = ["HdcJobStateSummary"]


@dataclass
class HdcJobStateSummary:
    """
    Overview of the job states working inside a dataset collection.

    Args:
        all_jobs (Optional[int]) : Total number of jobs associated with a dataset
                                   collection.
        deleted (Optional[int])  : Number of jobs in the `deleted` state.
        deleted_new (Optional[int])
                                 : Number of jobs in the `deleted_new` state.
        error (Optional[int])    : Number of jobs in the `error` state.
        failed (Optional[int])   : Number of jobs in the `failed` state.
        new (Optional[int])      : Number of jobs in the `new` state.
        ok (Optional[int])       : Number of jobs in the `ok` state.
        paused (Optional[int])   : Number of jobs in the `paused` state.
        queued (Optional[int])   : Number of jobs in the `queued` state.
        resubmitted (Optional[int])
                                 : Number of jobs in the `resubmitted` state.
        running (Optional[int])  : Number of jobs in the `running` state.
        skipped (Optional[int])  : Number of jobs that were skipped due to conditional
                                   workflow step execution.
        upload (Optional[int])   : Number of jobs in the `upload` state.
        waiting (Optional[int])  : Number of jobs in the `waiting` state.
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
