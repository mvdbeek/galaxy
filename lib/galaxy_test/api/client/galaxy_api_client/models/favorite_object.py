from dataclasses import dataclass

__all__ = ["FavoriteObject"]


@dataclass
class FavoriteObject:
    """
    FavoriteObject dataclass

    Args:
        object_id (str)          : The id of an object the user wants to favorite.
    """

    object_id: str  # The id of an object the user wants to favorite.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "object_id": "object_id",
        }
        key_transform_with_dump = {
            "object_id": "object_id",
        }
