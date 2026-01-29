from dataclasses import dataclass

from .data_elements_from_target_destination_type_enum import DataElementsFromTargetDestinationTypeEnum

__all__ = ["HdaDestination"]


@dataclass
class HdaDestination:
    """
    HdaDestination dataclass

    Args:
        type_ (DataElementsFromTargetDestinationTypeEnum)
                                 : Maps from 'type'
    """

    type_: DataElementsFromTargetDestinationTypeEnum  # Maps from 'type'

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "type": "type_",
        }
        key_transform_with_dump = {
            "type_": "type",
        }
