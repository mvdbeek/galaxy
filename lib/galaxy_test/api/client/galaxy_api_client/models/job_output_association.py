from dataclasses import dataclass

from .encoded_data_item_source_id import EncodedDataItemSourceId

__all__ = ["JobOutputAssociation"]


@dataclass
class JobOutputAssociation:
    """
    JobOutputAssociation dataclass.

    Args:
        dataset (EncodedDataItemSourceId)
                                 :
        name (str)               : Name of the job output parameter.
    """

    dataset: EncodedDataItemSourceId
    name: str  # Name of the job output parameter.
