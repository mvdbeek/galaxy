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

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "dbkey": "dbkey",
        }
        key_transform_with_dump = {
            "dbkey": "dbkey",
        }
