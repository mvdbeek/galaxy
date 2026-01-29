from dataclasses import dataclass

__all__ = ["GroupModel"]


@dataclass
class GroupModel:
    """
    User group model

    Args:
        id_ (str)                : Encoded group ID (maps from 'id')
        model_class (str)        : The name of the database model class.
        name (str)               : The name of the group.
    """

    id_: str  # Encoded group ID (maps from 'id')
    model_class: str  # The name of the database model class.
    name: str  # The name of the group.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "id": "id_",
            "model_class": "model_class",
            "name": "name",
        }
        key_transform_with_dump = {
            "id_": "id",
            "model_class": "model_class",
            "name": "name",
        }
