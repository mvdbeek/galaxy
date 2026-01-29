from dataclasses import dataclass

from .name import Name
from .role_ids import RoleIds
from .user_ids import UserIds

__all__ = ["GroupUpdatePayload"]


@dataclass
class GroupUpdatePayload:
    """
    Payload schema for updating a group.

    Args:
        name (Optional[Name])    : The name of the creator.
        role_ids (Optional[RoleIds])
                                 :
        user_ids (Optional[UserIds])
                                 :
    """

    name: Name | None = None  # The name of the creator.
    role_ids: RoleIds | None = None
    user_ids: UserIds | None = None
