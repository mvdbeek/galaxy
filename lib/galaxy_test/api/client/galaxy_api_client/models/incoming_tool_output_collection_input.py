from dataclasses import dataclass

from .hidden import Hidden
from .label import Label
from .name import Name
from .tool_output_collection_structure import ToolOutputCollectionStructure

__all__ = ["IncomingToolOutputCollectionInput"]


@dataclass
class IncomingToolOutputCollectionInput:
    """
    IncomingToolOutputCollectionInput dataclass.

    Args:
        structure (ToolOutputCollectionStructure)
                                 :
        type_ (str)              :
        hidden (Optional[Hidden]): If true, the output will not be shown in the history.
        label (Optional[Label])  : Label of the input.
        name (Optional[Name])    : The name of the creator.
    """

    structure: ToolOutputCollectionStructure
    type_: str
    hidden: Hidden | None = False  # If true, the output will not be shown in the history.
    label: Label | None = None  # Label of the input.
    name: Name | None = None  # The name of the creator.
