from dataclasses import dataclass

from .dataset_source_id import DatasetSourceId
from .delete_dataset_batch_payload_purge import DeleteDatasetBatchPayloadPurge

__all__ = ["DeleteDatasetBatchPayload"]


@dataclass
class DeleteDatasetBatchPayload:
    """
    DeleteDatasetBatchPayload dataclass

    Args:
        datasets (List[DatasetSourceId])
                                 : The list of datasets IDs with their sources to be
                                   deleted/purged.
        purge (DeleteDatasetBatchPayloadPurge | None)
                                 : Whether to permanently delete from disk the specified
                                   datasets. *Warning*: this is a destructive operation.
    """

    datasets: list[DatasetSourceId]  # The list of datasets IDs with their sources to be deleted/purged.
    purge: DeleteDatasetBatchPayloadPurge | None = (
        False  # Whether to permanently delete from disk the specified datasets. *Warning*: this is a destructive operation.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "datasets": "datasets",
            "purge": "purge",
        }
        key_transform_with_dump = {
            "datasets": "datasets",
            "purge": "purge",
        }
