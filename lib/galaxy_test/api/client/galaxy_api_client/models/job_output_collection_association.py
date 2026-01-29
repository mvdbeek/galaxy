from dataclasses import dataclass

from .encoded_data_item_source_id import EncodedDataItemSourceId

__all__ = ["JobOutputCollectionAssociation"]


@dataclass
class JobOutputCollectionAssociation:
    """
    JobOutputCollectionAssociation dataclass

    Args:
        dataset_collection_instance (EncodedDataItemSourceId)
                                 :
        name (str)               : Name of the job parameter.
    """

    dataset_collection_instance: EncodedDataItemSourceId
    name: str  # Name of the job parameter.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "dataset_collection_instance": "dataset_collection_instance",
            "name": "name",
        }
        key_transform_with_dump = {
            "dataset_collection_instance": "dataset_collection_instance",
            "name": "name",
        }
