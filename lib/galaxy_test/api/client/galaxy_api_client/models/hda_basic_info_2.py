from dataclasses import dataclass

__all__ = ["HdaBasicInfo2"]


@dataclass
class HdaBasicInfo2:
    """
    HdaBasicInfo2 dataclass

    Args:
        id_ (str)                : Maps from 'id'
        name (str)               :
    """

    id_: str  # Maps from 'id'
    name: str

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "id": "id_",
            "name": "name",
        }
        key_transform_with_dump = {
            "id_": "id",
            "name": "name",
        }
