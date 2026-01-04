from dataclasses import dataclass

__all__ = ["FavoriteObject"]


@dataclass
class FavoriteObject:
    """
    FavoriteObject dataclass.

    Args:
        object_id (str)          : The id of an object the user wants to favorite.
    """

    object_id: str  # The id of an object the user wants to favorite.
