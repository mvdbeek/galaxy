from dataclasses import dataclass

from .type__8 import Type8

__all__ = ["TagOperationParams"]


@dataclass
class TagOperationParams:
    """
    TagOperationParams dataclass

    Args:
        tags (List[str])         :
        type_ (Type8)            : Maps from 'type'
    """

    tags: list[str]
    type_: Type8  # Maps from 'type'

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "tags": "tags",
            "type": "type_",
        }
        key_transform_with_dump = {
            "tags": "tags",
            "type_": "type",
        }
