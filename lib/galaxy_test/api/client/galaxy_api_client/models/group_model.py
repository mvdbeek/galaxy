from dataclasses import dataclass

__all__ = ["GroupModel"]


@dataclass
class GroupModel:
    """
    User group model

    Args:
        id_ (str)                : Encoded group ID
        model_class (str)        : The name of the database model class.
        name (str)               : The name of the group.
    """

    id_: str  # Encoded group ID
    model_class: str  # The name of the database model class.
    name: str  # The name of the group.
