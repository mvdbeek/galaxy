from dataclasses import dataclass

from .detailed_user_model_preferences import DetailedUserModelPreferences
from .preferred_object_store_id import PreferredObjectStoreId
from .quota_bytes import QuotaBytes
from .quota_percent import QuotaPercent

__all__ = ["DetailedUserModel"]


@dataclass
class DetailedUserModel:
    """
    DetailedUserModel dataclass.

    Args:
        deleted (bool)           :  User is deleted
        email_ (str)             : Email of the user
        id_ (str)                : Encoded ID of the user
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
        preferred_object_store_id (Optional[PreferredObjectStoreId])
                                 : The ID of the object store that should be used to store
                                   all datasets (can instead specify object store IDs for
                                   intermediate and outputs datasts separately) -  -
                                   Galaxy's job configuration may override this in some
                                   cases but this workflow preference will override tool and
                                   user preferences
        quota_bytes (Optional[QuotaBytes])
                                 : Quota applicable to the user in bytes.
        quota_percent (Optional[QuotaPercent])
                                 : Percentage of the storage quota applicable to the user.
    """

    deleted: bool  #  User is deleted
    email_: str  # Email of the user
    id_: str  # Encoded ID of the user
    is_admin: bool  # User is admin
    nice_total_disk_usage: str  # Size of all non-purged, unique datasets of the user in a nice format.
    preferences: DetailedUserModelPreferences  # Preferences of the user
    purged: bool  # User is purged
    quota: str  # Quota applicable to the user
    total_disk_usage: float  # Size of all non-purged, unique datasets of the user in bytes.
    username: str  # The name of the user.
    preferred_object_store_id: PreferredObjectStoreId | None = (
        None  # The ID of the object store that should be used to store all datasets (can instead specify object store IDs for intermediate and outputs datasts separately) -  - Galaxy's job configuration may override this in some cases but this workflow preference will override tool and user preferences
    )
    quota_bytes: QuotaBytes | None = None  # Quota applicable to the user in bytes.
    quota_percent: QuotaPercent | None = None  # Percentage of the storage quota applicable to the user.
