from dataclasses import dataclass

__all__ = ["LibraryContentsIndexDatasetResponse"]


@dataclass
class LibraryContentsIndexDatasetResponse:
    """
    LibraryContentsIndexDatasetResponse dataclass

    Args:
        id_ (str)                : Maps from 'id'
        name (str)               :
        type_ (str)              : Maps from 'type'
        url (str)                :
    """

    id_: str  # Maps from 'id'
    name: str
    type_: str  # Maps from 'type'
    url: str

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "id": "id_",
            "name": "name",
            "type": "type_",
            "url": "url",
        }
        key_transform_with_dump = {
            "id_": "id",
            "name": "name",
            "type_": "type",
            "url": "url",
        }
