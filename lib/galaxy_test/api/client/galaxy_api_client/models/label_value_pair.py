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
