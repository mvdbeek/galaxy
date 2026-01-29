from dataclasses import dataclass

__all__ = ["FilesSourceSupports"]


@dataclass
class FilesSourceSupports:
    """
    FilesSourceSupports dataclass

    Args:
        pagination (bool | None) : Whether this file source supports server-side pagination.
        search (bool | None)     : Whether this file source supports server-side search.
        sorting (bool | None)    : Whether this file source supports server-side sorting.
    """

    pagination: bool | None = False  # Whether this file source supports server-side pagination.
    search: bool | None = False  # Whether this file source supports server-side search.
    sorting: bool | None = False  # Whether this file source supports server-side sorting.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "pagination": "pagination",
            "search": "search",
            "sorting": "sorting",
        }
        key_transform_with_dump = {
            "pagination": "pagination",
            "search": "search",
            "sorting": "sorting",
        }
