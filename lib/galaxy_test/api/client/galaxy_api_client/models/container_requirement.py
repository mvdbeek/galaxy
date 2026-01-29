from dataclasses import dataclass

from .container import Container

__all__ = ["ContainerRequirement"]


@dataclass
class ContainerRequirement:
    """
    ContainerRequirement dataclass

    Args:
        container (Container)    :
        type_ (str)              : Maps from 'type'
    """

    container: Container
    type_: str  # Maps from 'type'

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "container": "container",
            "type": "type_",
        }
        key_transform_with_dump = {
            "container": "container",
            "type_": "type",
        }
