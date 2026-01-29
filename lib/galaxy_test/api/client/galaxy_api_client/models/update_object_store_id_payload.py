from dataclasses import dataclass

__all__ = ["UpdateObjectStoreIdPayload"]


@dataclass
class UpdateObjectStoreIdPayload:
    """
    UpdateObjectStoreIdPayload dataclass

    Args:
        object_store_id (str)    : Object store ID to update to, it must be an object store
                                   with the same device ID as the target dataset currently.
    """

    object_store_id: str  # Object store ID to update to, it must be an object store with the same device ID as the target dataset currently.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "object_store_id": "object_store_id",
        }
        key_transform_with_dump = {
            "object_store_id": "object_store_id",
        }
