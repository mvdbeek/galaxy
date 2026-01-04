from dataclasses import dataclass

from .input_ import Input_
from .label import Label
from .position import Position

__all__ = ["ExtractInputAction"]


@dataclass
class ExtractInputAction:
    """
    ExtractInputAction dataclass.

    Args:
        action_type (str)        :
        input_ (Input_)          :
        label (Optional[Label])  : Label of the input.
        position (Optional[Position])
                                 : The location of the step in the Galaxy workflow editor.
    """

    action_type: str
    input_: Input_
    label: Label | None = None  # Label of the input.
    position: Position | None = None  # The location of the step in the Galaxy workflow editor.
