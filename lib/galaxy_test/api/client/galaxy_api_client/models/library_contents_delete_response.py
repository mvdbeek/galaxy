from dataclasses import dataclass

__all__ = ["LibraryContentsDeleteResponse"]


@dataclass
class LibraryContentsDeleteResponse:
    """
    LibraryContentsDeleteResponse dataclass

    Args:
        deleted (bool)           :
        id_ (str)                : Maps from 'id'
    """

    deleted: bool
    id_: str  # Maps from 'id'

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "deleted": "deleted",
            "id": "id_",
        }
        key_transform_with_dump = {
            "deleted": "deleted",
            "id_": "id",
        }
