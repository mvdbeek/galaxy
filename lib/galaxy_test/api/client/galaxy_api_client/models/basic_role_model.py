from dataclasses import dataclass

__all__ = ["BasicRoleModel"]


@dataclass
class BasicRoleModel:
    """
    BasicRoleModel dataclass

    Args:
        id_ (str)                : Encoded ID of the role (maps from 'id')
        name (str)               : Name of the role
        type_ (str)              : Type or category of the role (maps from 'type')
    """

    id_: str  # Encoded ID of the role (maps from 'id')
    name: str  # Name of the role
    type_: str  # Type or category of the role (maps from 'type')

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "id": "id_",
            "name": "name",
            "type": "type_",
        }
        key_transform_with_dump = {
            "id_": "id",
            "name": "name",
            "type_": "type",
        }
