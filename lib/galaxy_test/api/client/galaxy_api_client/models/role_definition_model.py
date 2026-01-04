from dataclasses import dataclass

from .group_ids import GroupIds
from .role_type import RoleType
from .user_ids import UserIds

__all__ = ["RoleDefinitionModel"]


@dataclass
class RoleDefinitionModel:
    """
    RoleDefinitionModel dataclass.

    Args:
        description (str)        : Description of the role
        name (str)               : Name of the role
        group_ids (Optional[GroupIds])
                                 : The list of encoded group IDs of the groups that should
                                   receive the notification.
        role_type (Optional[RoleType])
                                 :
        user_ids (Optional[UserIds])
                                 :
    """

    description: str  # Description of the role
    name: str  # Name of the role
    group_ids: GroupIds | None = (
        None  # The list of encoded group IDs of the groups that should receive the notification.
    )
    role_type: RoleType | None = "admin"
    user_ids: UserIds | None = None
