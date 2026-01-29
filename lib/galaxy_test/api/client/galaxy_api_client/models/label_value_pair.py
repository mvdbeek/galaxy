from dataclasses import dataclass

__all__ = ["LabelValuePair"]


@dataclass
class LabelValuePair:
    """
    Generic Label/Value pair model.

    Args:
        label (str)              : The label of the item.
        value (str)              : The value of the item.
    """

    label: str  # The label of the item.
    value: str  # The value of the item.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "label": "label",
            "value": "value",
        }
        key_transform_with_dump = {
            "label": "label",
            "value": "value",
        }
