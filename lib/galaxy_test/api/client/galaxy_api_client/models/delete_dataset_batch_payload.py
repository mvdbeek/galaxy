from dataclasses import dataclass

from .dataset_source_id import DatasetSourceId
from .purge import Purge

__all__ = ["DeleteDatasetBatchPayload"]


@dataclass
class DeleteDatasetBatchPayload:
    """
    DeleteDatasetBatchPayload dataclass.

    Args:
        datasets (List[DatasetSourceId])
                                 : The list of datasets IDs with their sources to be
                                   deleted/purged.
        purge (Optional[Purge])  : Whether to permanently delete from disk the specified
                                   datasets. *Warning*: this is a destructive operation.
    """

    datasets: list[DatasetSourceId]  # The list of datasets IDs with their sources to be deleted/purged.
    purge: Purge | None = (
        False  # Whether to permanently delete from disk the specified datasets. *Warning*: this is a destructive operation.
    )
