from dataclasses import dataclass

from .group_response_roles_url import GroupResponseRolesUrl
from .group_response_users_url import GroupResponseUsersUrl

__all__ = ["GroupResponse"]


@dataclass
class GroupResponse:
    """
    Response schema for a group.

    Args:
        id_ (str)                : Maps from 'id'
        model_class (str)        : The name of the database model class.
        name (str)               :
        url (str)                :
        roles_url (GroupResponseRolesUrl | None)
                                 :
        users_url (GroupResponseUsersUrl | None)
                                 :
    """

    id_: str  # Maps from 'id'
    model_class: str  # The name of the database model class.
    name: str
    url: str
    roles_url: GroupResponseRolesUrl | None = None
    users_url: GroupResponseUsersUrl | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "id": "id_",
            "model_class": "model_class",
            "name": "name",
            "roles_url": "roles_url",
            "url": "url",
            "users_url": "users_url",
        }
        key_transform_with_dump = {
            "id_": "id",
            "model_class": "model_class",
            "name": "name",
            "roles_url": "roles_url",
            "url": "url",
            "users_url": "users_url",
        }
