from dataclasses import dataclass

from .user_update_payload_active import UserUpdatePayloadActive
from .user_update_payload_preferred_object_store_id import UserUpdatePayloadPreferredObjectStoreId
from .user_update_payload_username import UserUpdatePayloadUsername

__all__ = ["UserUpdatePayload"]


@dataclass
class UserUpdatePayload:
    """
    UserUpdatePayload dataclass

    Args:
        active (UserUpdatePayloadActive | None)
                                 : User is active
        preferred_object_store_id (UserUpdatePayloadPreferredObjectStoreId | None)
                                 : The ID of the object store that should be used to store
                                   new datasets in this history.
        username (UserUpdatePayloadUsername | None)
                                 : The name of the user.
    """

    active: UserUpdatePayloadActive | None = None  # User is active
    preferred_object_store_id: UserUpdatePayloadPreferredObjectStoreId | None = (
        None  # The ID of the object store that should be used to store new datasets in this history.
    )
    username: UserUpdatePayloadUsername | None = None  # The name of the user.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "active": "active",
            "preferred_object_store_id": "preferred_object_store_id",
            "username": "username",
        }
        key_transform_with_dump = {
            "active": "active",
            "preferred_object_store_id": "preferred_object_store_id",
            "username": "username",
        }
