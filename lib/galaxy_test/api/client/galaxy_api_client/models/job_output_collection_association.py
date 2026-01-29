from dataclasses import dataclass

from .encoded_data_item_source_id import EncodedDataItemSourceId

__all__ = ["JobOutputCollectionAssociation"]


@dataclass
class JobOutputCollectionAssociation:
    """
    JobOutputCollectionAssociation dataclass.

    Args:
        dataset_collection_instance (EncodedDataItemSourceId)
                                 :
        name (str)               : Name of the job parameter.
    """

    dataset_collection_instance: EncodedDataItemSourceId
    name: str  # Name of the job parameter.
