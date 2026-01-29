from dataclasses import dataclass

__all__ = ["LibraryContentsCreateFolderResponse"]


@dataclass
class LibraryContentsCreateFolderResponse:
    """
    LibraryContentsCreateFolderResponse dataclass

    Args:
        id_ (str)                : Maps from 'id'
        name (str)               :
        url (str)                :
    """

    id_: str  # Maps from 'id'
    name: str
    url: str

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "id": "id_",
            "name": "name",
            "url": "url",
        }
        key_transform_with_dump = {
            "id_": "id",
            "name": "name",
            "url": "url",
        }
