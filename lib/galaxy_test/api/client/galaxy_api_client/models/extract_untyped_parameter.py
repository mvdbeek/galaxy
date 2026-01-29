from dataclasses import dataclass

from .label import Label
from .position import Position

__all__ = ["ExtractUntypedParameter"]


@dataclass
class ExtractUntypedParameter:
    """
    ExtractUntypedParameter dataclass.

    Args:
        action_type (str)        :
        name (str)               :
        label (Optional[Label])  : Label of the input.
        position (Optional[Position])
                                 : The location of the step in the Galaxy workflow editor.
    """

    action_type: str
    name: str
    label: Label | None = None  # Label of the input.
    position: Position | None = None  # The location of the step in the Galaxy workflow editor.
