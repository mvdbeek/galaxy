from dataclasses import dataclass

__all__ = ["CopyDatasetsPayloadSourceEntry"]


@dataclass
class CopyDatasetsPayloadSourceEntry:
    """
    CopyDatasetsPayloadSourceEntry dataclass

    Args:
        id_ (str)                : Maps from 'id'
        type_ (str)              : Maps from 'type'
    """

    id_: str  # Maps from 'id'
    type_: str  # Maps from 'type'

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "id": "id_",
            "type": "type_",
        }
        key_transform_with_dump = {
            "id_": "id",
            "type_": "type",
        }
