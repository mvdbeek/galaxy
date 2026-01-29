from dataclasses import dataclass

__all__ = ["DeleteLibraryPayload"]


@dataclass
class DeleteLibraryPayload:
    """
    DeleteLibraryPayload dataclass

    Args:
        undelete (bool)          : Whether to restore this previously deleted library.
    """

    undelete: bool  # Whether to restore this previously deleted library.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "undelete": "undelete",
        }
        key_transform_with_dump = {
            "undelete": "undelete",
        }
