from dataclasses import dataclass

__all__ = ["DeleteHistoryContentPayload"]


@dataclass
class DeleteHistoryContentPayload:
    """
    DeleteHistoryContentPayload dataclass.

    Args:
        purge (Optional[bool])   : Whether to remove the dataset from storage. Datasets will
                                   only be removed from storage once all HDAs or LDDAs that
                                   refer to this datasets are deleted.
        recursive (Optional[bool]): When deleting a dataset collection, whether to also
                                    delete containing datasets.
        stop_job (Optional[bool]): Whether to stop the creating job if all the job's outputs
                                   are deleted.
    """

    purge: bool | None = (
        False  # Whether to remove the dataset from storage. Datasets will only be removed from storage once all HDAs or LDDAs that refer to this datasets are deleted.
    )
    recursive: bool | None = False  # When deleting a dataset collection, whether to also delete containing datasets.
    stop_job: bool | None = False  # Whether to stop the creating job if all the job's outputs are deleted.
