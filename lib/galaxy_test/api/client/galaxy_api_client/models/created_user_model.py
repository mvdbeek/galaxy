from dataclasses import dataclass

from .created_user_model_last_password_change import CreatedUserModelLastPasswordChange
from .created_user_model_preferred_object_store_id import CreatedUserModelPreferredObjectStoreId

__all__ = ["CreatedUserModel"]


@dataclass
class CreatedUserModel:
    """
    CreatedUserModel dataclass

    Args:
        active (bool)            : User is active
        deleted (bool)           :  User is deleted
        email_ (str)             : Email of the user (maps from 'email')
        id_ (str)                : Encoded ID of the user (maps from 'id')
        last_password_change (CreatedUserModelLastPasswordChange)
                                 :
        model_class (str)        : The name of the database model class.
        nice_total_disk_usage (str)
                                 : Size of all non-purged, unique datasets of the user in a
                                   nice format.
        total_disk_usage (float) : Size of all non-purged, unique datasets of the user in
                                   bytes.
        username (str)           : The name of the user.
        preferred_object_store_id (CreatedUserModelPreferredObjectStoreId | None)
                                 : The ID of the object store that should be used to store
                                   new datasets in this history.
    """

    active: bool  # User is active
    deleted: bool  #  User is deleted
    email_: str  # Email of the user (maps from 'email')
    id_: str  # Encoded ID of the user (maps from 'id')
    last_password_change: CreatedUserModelLastPasswordChange
    model_class: str  # The name of the database model class.
    nice_total_disk_usage: str  # Size of all non-purged, unique datasets of the user in a nice format.
    total_disk_usage: float  # Size of all non-purged, unique datasets of the user in bytes.
    username: str  # The name of the user.
    preferred_object_store_id: CreatedUserModelPreferredObjectStoreId | None = (
        None  # The ID of the object store that should be used to store new datasets in this history.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "active": "active",
            "deleted": "deleted",
            "email": "email_",
            "id": "id_",
            "last_password_change": "last_password_change",
            "model_class": "model_class",
            "nice_total_disk_usage": "nice_total_disk_usage",
            "preferred_object_store_id": "preferred_object_store_id",
            "total_disk_usage": "total_disk_usage",
            "username": "username",
        }
        key_transform_with_dump = {
            "active": "active",
            "deleted": "deleted",
            "email_": "email",
            "id_": "id",
            "last_password_change": "last_password_change",
            "model_class": "model_class",
            "nice_total_disk_usage": "nice_total_disk_usage",
            "preferred_object_store_id": "preferred_object_store_id",
            "total_disk_usage": "total_disk_usage",
            "username": "username",
        }
