from dataclasses import dataclass

from .type_ import Type_

__all__ = ["Container"]


@dataclass
class Container:
    """
    Container dataclass

    Args:
        container_id (str)       :
        type_ (Type_)            : Maps from 'type'
    """

    container_id: str
    type_: Type_  # Maps from 'type'

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "container_id": "container_id",
            "type": "type_",
        }
        key_transform_with_dump = {
            "container_id": "container_id",
            "type_": "type",
        }
