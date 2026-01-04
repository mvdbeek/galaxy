from dataclasses import dataclass

from .share_option import ShareOption
from .user_ids import UserIds

__all__ = ["ShareWithPayload"]


@dataclass
class ShareWithPayload:
    """
    ShareWithPayload dataclass.

    Args:
        user_ids (UserIds)       : A collection of encoded IDs (or email addresses) of users
                                   that this resource will be shared with.
        share_option (Optional[ShareOption])
                                 : User choice for sharing resources which its contents may
                                   be restricted:  - None: The user did not choose anything
                                   yet or no option is needed.  - make_public: The contents
                                   of the resource will be made publicly accessible.  -
                                   make_accessible_to_shared: This will automatically create
                                   a new `sharing role` allowing protected contents to be
                                   accessed only by the desired users.  - no_changes: This
                                   won't change the current permissions for the contents.
                                   The user which this resource will be shared may not be
                                   able to access all its contents.
    """

    user_ids: (
        UserIds  # A collection of encoded IDs (or email addresses) of users that this resource will be shared with.
    )
    share_option: ShareOption | None = (
        None  # User choice for sharing resources which its contents may be restricted:  - None: The user did not choose anything yet or no option is needed.  - make_public: The contents of the resource will be made publicly accessible.  - make_accessible_to_shared: This will automatically create a new `sharing role` allowing protected contents to be accessed only by the desired users.  - no_changes: This won't change the current permissions for the contents. The user which this resource will be shared may not be able to access all its contents.
    )
