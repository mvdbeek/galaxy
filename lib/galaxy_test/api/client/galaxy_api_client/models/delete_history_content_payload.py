from dataclasses import dataclass

__all__ = ["DeleteHistoryContentPayload"]


@dataclass
class DeleteHistoryContentPayload:
    """
    DeleteHistoryContentPayload dataclass

    Args:
        purge (bool | None)      : Whether to remove the dataset from storage. Datasets will
                                   only be removed from storage once all HDAs or LDDAs that
                                   refer to this datasets are deleted.
        recursive (bool | None)  : When deleting a dataset collection, whether to also
                                   delete containing datasets.
        stop_job (bool | None)   : Whether to stop the creating job if all the job's outputs
                                   are deleted.
    """

    purge: bool | None = (
        False  # Whether to remove the dataset from storage. Datasets will only be removed from storage once all HDAs or LDDAs that refer to this datasets are deleted.
    )
    recursive: bool | None = False  # When deleting a dataset collection, whether to also delete containing datasets.
    stop_job: bool | None = False  # Whether to stop the creating job if all the job's outputs are deleted.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "purge": "purge",
            "recursive": "recursive",
            "stop_job": "stop_job",
        }
        key_transform_with_dump = {
            "purge": "purge",
            "recursive": "recursive",
            "stop_job": "stop_job",
        }
