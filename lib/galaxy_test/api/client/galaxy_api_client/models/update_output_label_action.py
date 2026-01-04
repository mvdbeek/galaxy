from dataclasses import dataclass

from .output import Output

__all__ = ["UpdateOutputLabelAction"]


@dataclass
class UpdateOutputLabelAction:
    """
    UpdateOutputLabelAction dataclass.

    Args:
        action_type (str)        :
        output (Output)          :
        output_label (str)       :
    """

    action_type: str
    output: Output
    output_label: str
