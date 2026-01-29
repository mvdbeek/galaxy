from dataclasses import dataclass

from .share_with_payload_share_option import ShareWithPayloadShareOption
from .share_with_payload_user_ids import ShareWithPayloadUserIds

__all__ = ["ShareWithPayload"]


@dataclass
class ShareWithPayload:
    """
    ShareWithPayload dataclass

    Args:
        user_ids (ShareWithPayloadUserIds)
                                 : A collection of encoded IDs (or email addresses) of users
                                   that this resource will be shared with.
        share_option (ShareWithPayloadShareOption | None)
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

    user_ids: ShareWithPayloadUserIds  # A collection of encoded IDs (or email addresses) of users that this resource will be shared with.
    share_option: ShareWithPayloadShareOption | None = (
        None  # User choice for sharing resources which its contents may be restricted:  - None: The user did not choose anything yet or no option is needed.  - make_public: The contents of the resource will be made publicly accessible.  - make_accessible_to_shared: This will automatically create a new `sharing role` allowing protected contents to be accessed only by the desired users.  - no_changes: This won't change the current permissions for the contents. The user which this resource will be shared may not be able to access all its contents.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "share_option": "share_option",
            "user_ids": "user_ids",
        }
        key_transform_with_dump = {
            "share_option": "share_option",
            "user_ids": "user_ids",
        }
