from dataclasses import dataclass

__all__ = ["UpdateObjectStoreIdPayload"]


@dataclass
class UpdateObjectStoreIdPayload:
    """
    UpdateObjectStoreIdPayload dataclass.

    Args:
        object_store_id (str)    : Object store ID to update to, it must be an object store
                                   with the same device ID as the target dataset currently.
    """

    object_store_id: str  # Object store ID to update to, it must be an object store with the same device ID as the target dataset currently.
