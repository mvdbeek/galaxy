from dataclasses import dataclass

__all__ = ["LibraryContentsDeletePayload"]


@dataclass
class LibraryContentsDeletePayload:
    """
    LibraryContentsDeletePayload dataclass

    Args:
        purge (bool | None)      : if True, purge the library dataset
    """

    purge: bool | None = False  # if True, purge the library dataset

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "purge": "purge",
        }
        key_transform_with_dump = {
            "purge": "purge",
        }
