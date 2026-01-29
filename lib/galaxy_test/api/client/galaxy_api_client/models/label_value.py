from dataclasses import dataclass

__all__ = ["LabelValue"]


@dataclass
class LabelValue:
    """
    LabelValue dataclass.

    Args:
        label (str)              :
        selected (bool)          :
        value (str)              :
    """

    label: str
    selected: bool
    value: str
