from dataclasses import dataclass

from .role_ids import RoleIds
from .user_ids import UserIds

__all__ = ["GroupCreatePayload"]


@dataclass
class GroupCreatePayload:
    """
    Payload schema for creating a group.

    Args:
        name (str)               :
        role_ids (Optional[RoleIds])
                                 :
        user_ids (Optional[UserIds])
                                 :
    """

    name: str
    role_ids: RoleIds | None = None
    user_ids: UserIds | None = None
