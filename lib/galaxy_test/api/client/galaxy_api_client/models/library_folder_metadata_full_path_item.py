from dataclasses import dataclass, field
from typing import Any

__all__ = ["LibraryFolderMetadataFullPathItem"]


@dataclass
class LibraryFolderMetadataFullPathItem:
    """
    LibraryFolderMetadataFullPathItem dataclass

    Args:
        items (List[dict[str, Any]] | None)
                                 : A list of dict[str, Any] items.
    """

    items: list[dict[str, Any]] | None = field(default_factory=list)  # A list of dict[str, Any] items.
