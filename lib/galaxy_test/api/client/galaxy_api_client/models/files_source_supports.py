from dataclasses import dataclass

__all__ = ["FilesSourceSupports"]


@dataclass
class FilesSourceSupports:
    """
    FilesSourceSupports dataclass.

    Args:
        pagination (Optional[bool])
                                 : Whether this file source supports server-side pagination.
        search (Optional[bool])  : Whether this file source supports server-side search.
        sorting (Optional[bool]) : Whether this file source supports server-side sorting.
    """

    pagination: bool | None = False  # Whether this file source supports server-side pagination.
    search: bool | None = False  # Whether this file source supports server-side search.
    sorting: bool | None = False  # Whether this file source supports server-side sorting.
