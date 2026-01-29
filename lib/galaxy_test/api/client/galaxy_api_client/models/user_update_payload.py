from dataclasses import dataclass

from .active import Active
from .preferred_object_store_id import PreferredObjectStoreId
from .username import Username

__all__ = ["UserUpdatePayload"]


@dataclass
class UserUpdatePayload:
    """
    UserUpdatePayload dataclass.

    Args:
        active (Optional[Active]): User is active
        preferred_object_store_id (Optional[PreferredObjectStoreId])
                                 : The ID of the object store that should be used to store
                                   all datasets (can instead specify object store IDs for
                                   intermediate and outputs datasts separately) -  -
                                   Galaxy's job configuration may override this in some
                                   cases but this workflow preference will override tool and
                                   user preferences
        username (Optional[Username])
                                 : The name of the user.
    """

    active: Active | None = True  # User is active
    preferred_object_store_id: PreferredObjectStoreId | None = (
        None  # The ID of the object store that should be used to store all datasets (can instead specify object store IDs for intermediate and outputs datasts separately) -  - Galaxy's job configuration may override this in some cases but this workflow preference will override tool and user preferences
    )
    username: Username | None = None  # The name of the user.
