from dataclasses import dataclass

from .hidden import Hidden
from .label import Label
from .name import Name

__all__ = ["ToolOutputBoolean"]


@dataclass
class ToolOutputBoolean:
    """
    ToolOutputBoolean dataclass.

    Args:
        hidden (Optional[Hidden]): If true, the output will not be shown in the history.
        name (Optional[Name])    : The name of the creator.
        type_ (str)              :
        label (Optional[Label])  : Label of the input.
    """

    hidden: Hidden | None  # If true, the output will not be shown in the history.
    name: Name | None  # The name of the creator.
    type_: str
    label: Label | None = None  # Label of the input.
