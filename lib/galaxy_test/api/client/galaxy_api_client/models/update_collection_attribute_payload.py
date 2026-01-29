from dataclasses import dataclass

__all__ = ["UpdateCollectionAttributePayload"]


@dataclass
class UpdateCollectionAttributePayload:
    """
    Contains attributes that can be updated for all elements in a dataset collection.

    Args:
        dbkey (str)              : TODO
    """

    dbkey: str  # TODO
