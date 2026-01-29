from dataclasses import dataclass

__all__ = ["GroupRoleResponse"]


@dataclass
class GroupRoleResponse:
    """
    GroupRoleResponse dataclass.

    Args:
        id_ (str)                : Encoded ID of the role
        name (str)               : Name of the role
        url (str)                : The relative URL to access this item.
    """

    id_: str  # Encoded ID of the role
    name: str  # Name of the role
    url: str  # The relative URL to access this item.
