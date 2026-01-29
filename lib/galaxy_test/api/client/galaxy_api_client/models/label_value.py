from dataclasses import dataclass

__all__ = ["LabelValue"]


@dataclass
class LabelValue:
    """
    LabelValue dataclass

    Args:
        label (str)              :
        selected (bool)          :
        value (str)              :
    """

    label: str
    selected: bool
    value: str

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "label": "label",
            "selected": "selected",
            "value": "value",
        }
        key_transform_with_dump = {
            "label": "label",
            "selected": "selected",
            "value": "value",
        }
