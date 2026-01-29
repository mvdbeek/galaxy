from dataclasses import dataclass

__all__ = ["Citation"]


@dataclass
class Citation:
    """
    Citation dataclass

    Args:
        content (str)            :
        type_ (str)              : Maps from 'type'
    """

    content: str
    type_: str  # Maps from 'type'

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "content": "content",
            "type": "type_",
        }
        key_transform_with_dump = {
            "content": "content",
            "type_": "type",
        }
