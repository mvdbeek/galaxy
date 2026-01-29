from dataclasses import dataclass

from .composite_items_elements import CompositeItemsElements

__all__ = ["CompositeItems"]


@dataclass
class CompositeItems:
    """
    CompositeItems dataclass

    Args:
        elements (CompositeItemsElements)
                                 :
    """

    elements: CompositeItemsElements

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "elements": "elements",
        }
        key_transform_with_dump = {
            "elements": "elements",
        }
