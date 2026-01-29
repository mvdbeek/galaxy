from dataclasses import dataclass

from .detailed_user_model_preferences import DetailedUserModelPreferences
from .detailed_user_model_preferred_object_store_id import DetailedUserModelPreferredObjectStoreId
from .detailed_user_model_quota_bytes import DetailedUserModelQuotaBytes
from .detailed_user_model_quota_percent import DetailedUserModelQuotaPercent

__all__ = ["DetailedUserModel"]


@dataclass
class DetailedUserModel:
    """
    DetailedUserModel dataclass

    Args:
        deleted (bool)           :  User is deleted
        email_ (str)             : Email of the user (maps from 'email')
        id_ (str)                : Encoded ID of the user (maps from 'id')
        is_admin (bool)          : User is admin
        nice_total_disk_usage (str)
                                 : Size of all non-purged, unique datasets of the user in a
                                   nice format.
        preferences (DetailedUserModelPreferences)
                                 : Preferences of the user
        purged (bool)            : User is purged
        quota (str)              : Quota applicable to the user
        total_disk_usage (float) : Size of all non-purged, unique datasets of the user in
                                   bytes.
        username (str)           : The name of the user.
        preferred_object_store_id (DetailedUserModelPreferredObjectStoreId | None)
                                 : The ID of the object store that should be used to store
                                   new datasets in this history.
        quota_bytes (DetailedUserModelQuotaBytes | None)
                                 : Quota applicable to the user in bytes.
        quota_percent (DetailedUserModelQuotaPercent | None)
                                 : Percentage of the storage quota applicable to the user.
    """

    deleted: bool  #  User is deleted
    email_: str  # Email of the user (maps from 'email')
    id_: str  # Encoded ID of the user (maps from 'id')
    is_admin: bool  # User is admin
    nice_total_disk_usage: str  # Size of all non-purged, unique datasets of the user in a nice format.
    preferences: DetailedUserModelPreferences  # Preferences of the user
    purged: bool  # User is purged
    quota: str  # Quota applicable to the user
    total_disk_usage: float  # Size of all non-purged, unique datasets of the user in bytes.
    username: str  # The name of the user.
    preferred_object_store_id: DetailedUserModelPreferredObjectStoreId | None = (
        None  # The ID of the object store that should be used to store new datasets in this history.
    )
    quota_bytes: DetailedUserModelQuotaBytes | None = None  # Quota applicable to the user in bytes.
    quota_percent: DetailedUserModelQuotaPercent | None = (
        None  # Percentage of the storage quota applicable to the user.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "deleted": "deleted",
            "email": "email_",
            "id": "id_",
            "is_admin": "is_admin",
            "nice_total_disk_usage": "nice_total_disk_usage",
            "preferences": "preferences",
            "preferred_object_store_id": "preferred_object_store_id",
            "purged": "purged",
            "quota": "quota",
            "quota_bytes": "quota_bytes",
            "quota_percent": "quota_percent",
            "total_disk_usage": "total_disk_usage",
            "username": "username",
        }
        key_transform_with_dump = {
            "deleted": "deleted",
            "email_": "email",
            "id_": "id",
            "is_admin": "is_admin",
            "nice_total_disk_usage": "nice_total_disk_usage",
            "preferences": "preferences",
            "preferred_object_store_id": "preferred_object_store_id",
            "purged": "purged",
            "quota": "quota",
            "quota_bytes": "quota_bytes",
            "quota_percent": "quota_percent",
            "total_disk_usage": "total_disk_usage",
            "username": "username",
        }
