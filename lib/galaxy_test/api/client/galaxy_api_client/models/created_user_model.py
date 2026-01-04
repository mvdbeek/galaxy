from dataclasses import dataclass

from .last_password_change import LastPasswordChange
from .preferred_object_store_id import PreferredObjectStoreId

__all__ = ["CreatedUserModel"]


@dataclass
class CreatedUserModel:
    """
    CreatedUserModel dataclass.

    Args:
        active (bool)            : User is active
        deleted (bool)           :  User is deleted
        email_ (str)             : Email of the user
        id_ (str)                : Encoded ID of the user
        last_password_change (Optional[LastPasswordChange])
                                 :
        model_class (str)        : The name of the database model class.
        nice_total_disk_usage (str)
                                 : Size of all non-purged, unique datasets of the user in a
                                   nice format.
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
    """

    active: bool  # User is active
    deleted: bool  #  User is deleted
    email_: str  # Email of the user
    id_: str  # Encoded ID of the user
    last_password_change: LastPasswordChange | None
    model_class: str  # The name of the database model class.
    nice_total_disk_usage: str  # Size of all non-purged, unique datasets of the user in a nice format.
    total_disk_usage: float  # Size of all non-purged, unique datasets of the user in bytes.
    username: str  # The name of the user.
    preferred_object_store_id: PreferredObjectStoreId | None = (
        None  # The ID of the object store that should be used to store all datasets (can instead specify object store IDs for intermediate and outputs datasts separately) -  - Galaxy's job configuration may override this in some cases but this workflow preference will override tool and user preferences
    )
