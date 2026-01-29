from dataclasses import dataclass

from .incoming_tool_output_collection_input_hidden import IncomingToolOutputCollectionInputHidden
from .incoming_tool_output_collection_input_label import IncomingToolOutputCollectionInputLabel
from .incoming_tool_output_collection_input_name import IncomingToolOutputCollectionInputName
from .tool_output_collection_structure import ToolOutputCollectionStructure

__all__ = ["IncomingToolOutputCollectionInput2"]


@dataclass
class IncomingToolOutputCollectionInput2:
    """
    IncomingToolOutputCollectionInput2 dataclass

    Args:
        structure (ToolOutputCollectionStructure)
                                 :
        type_ (str)              : Maps from 'type'
        hidden (IncomingToolOutputCollectionInputHidden | None)
                                 : If true, the output will not be shown in the history.
        label (IncomingToolOutputCollectionInputLabel | None)
                                 : Output label. Will be used as dataset name in history.
        name (IncomingToolOutputCollectionInputName | None)
                                 : Parameter name. Used when referencing parameter in
                                   workflows.
    """

    structure: ToolOutputCollectionStructure
    type_: str  # Maps from 'type'
    hidden: IncomingToolOutputCollectionInputHidden | None = (
        None  # If true, the output will not be shown in the history.
    )
    label: IncomingToolOutputCollectionInputLabel | None = (
        None  # Output label. Will be used as dataset name in history.
    )
    name: IncomingToolOutputCollectionInputName | None = (
        None  # Parameter name. Used when referencing parameter in workflows.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "hidden": "hidden",
            "label": "label",
            "name": "name",
            "structure": "structure",
            "type": "type_",
        }
        key_transform_with_dump = {
            "hidden": "hidden",
            "label": "label",
            "name": "name",
            "structure": "structure",
            "type_": "type",
        }
