from dataclasses import dataclass

from .group_update_payload_name import GroupUpdatePayloadName
from .group_update_payload_role_ids import GroupUpdatePayloadRoleIds
from .group_update_payload_user_ids import GroupUpdatePayloadUserIds

__all__ = ["GroupUpdatePayload"]


@dataclass
class GroupUpdatePayload:
    """
    Payload schema for updating a group.

    Args:
        name (GroupUpdatePayloadName | None)
                                 :
        role_ids (GroupUpdatePayloadRoleIds | None)
                                 :
        user_ids (GroupUpdatePayloadUserIds | None)
                                 :
    """

    name: GroupUpdatePayloadName | None = None
    role_ids: GroupUpdatePayloadRoleIds | None = None
    user_ids: GroupUpdatePayloadUserIds | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "name": "name",
            "role_ids": "role_ids",
            "user_ids": "user_ids",
        }
        key_transform_with_dump = {
            "name": "name",
            "role_ids": "role_ids",
            "user_ids": "user_ids",
        }
