from dataclasses import dataclass

from .roles_url import RolesUrl
from .users_url import UsersUrl

__all__ = ["GroupResponse"]


@dataclass
class GroupResponse:
    """
    Response schema for a group.

    Args:
        id_ (str)                :
        model_class (str)        : The name of the database model class.
        name (str)               :
        url (str)                :
        roles_url (Optional[RolesUrl])
                                 :
        users_url (Optional[UsersUrl])
                                 :
    """

    id_: str
    model_class: str  # The name of the database model class.
    name: str
    url: str
    roles_url: RolesUrl | None = None
    users_url: UsersUrl | None = None
