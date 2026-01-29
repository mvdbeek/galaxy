from dataclasses import dataclass

__all__ = ["BasicRoleModel"]


@dataclass
class BasicRoleModel:
    """
    BasicRoleModel dataclass.

    Args:
        id_ (str)                : Encoded ID of the role
        name (str)               : Name of the role
        type_ (str)              : Type or category of the role
    """

    id_: str  # Encoded ID of the role
    name: str  # Name of the role
    type_: str  # Type or category of the role
