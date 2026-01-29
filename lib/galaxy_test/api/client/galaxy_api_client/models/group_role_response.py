from dataclasses import dataclass

__all__ = ["GroupRoleResponse"]


@dataclass
class GroupRoleResponse:
    """
    GroupRoleResponse dataclass

    Args:
        id_ (str)                : Encoded ID of the role (maps from 'id')
        name (str)               : Name of the role
        url (str)                : The relative URL to access this item.
    """

    id_: str  # Encoded ID of the role (maps from 'id')
    name: str  # Name of the role
    url: str  # The relative URL to access this item.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "id": "id_",
            "name": "name",
            "url": "url",
        }
        key_transform_with_dump = {
            "id_": "id",
            "name": "name",
            "url": "url",
        }
