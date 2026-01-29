from dataclasses import dataclass

__all__ = ["DatasetInheritanceChainEntry"]


@dataclass
class DatasetInheritanceChainEntry:
    """
    DatasetInheritanceChainEntry dataclass

    Args:
        dep (str)                : Name of the source of the referenced dataset at this
                                   point of the inheritance chain.
        id_ (str)                : ID of the referenced dataset (maps from 'id')
        name (str)               : Name of the referenced dataset
        user_id (str)            : ID of the user who owns the referenced dataset.
    """

    dep: str  # Name of the source of the referenced dataset at this point of the inheritance chain.
    id_: str  # ID of the referenced dataset (maps from 'id')
    name: str  # Name of the referenced dataset
    user_id: str  # ID of the user who owns the referenced dataset.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "dep": "dep",
            "id": "id_",
            "name": "name",
            "user_id": "user_id",
        }
        key_transform_with_dump = {
            "dep": "dep",
            "id_": "id",
            "name": "name",
            "user_id": "user_id",
        }
