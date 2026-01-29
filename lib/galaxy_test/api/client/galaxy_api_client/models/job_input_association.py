from dataclasses import dataclass

from .encoded_data_item_source_id import EncodedDataItemSourceId

__all__ = ["JobInputAssociation"]


@dataclass
class JobInputAssociation:
    """
    JobInputAssociation dataclass.

    Args:
        dataset (EncodedDataItemSourceId)
                                 :
        name (str)               : Name of the job input parameter.
    """

    dataset: EncodedDataItemSourceId
    name: str  # Name of the job input parameter.
