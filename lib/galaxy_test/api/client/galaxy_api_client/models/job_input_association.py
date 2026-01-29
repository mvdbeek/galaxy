from dataclasses import dataclass

from .encoded_data_item_source_id import EncodedDataItemSourceId

__all__ = ["JobInputAssociation"]


@dataclass
class JobInputAssociation:
    """
    JobInputAssociation dataclass

    Args:
        dataset (EncodedDataItemSourceId)
                                 :
        name (str)               : Name of the job input parameter.
    """

    dataset: EncodedDataItemSourceId
    name: str  # Name of the job input parameter.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "dataset": "dataset",
            "name": "name",
        }
        key_transform_with_dump = {
            "dataset": "dataset",
            "name": "name",
        }
