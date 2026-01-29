from dataclasses import dataclass

from .incoming_tool_output_collection_output_hidden import IncomingToolOutputCollectionOutputHidden
from .incoming_tool_output_collection_output_label import IncomingToolOutputCollectionOutputLabel
from .incoming_tool_output_collection_output_name import IncomingToolOutputCollectionOutputName
from .tool_output_collection_structure import ToolOutputCollectionStructure
from .user_tool_source_output_outputs_item_type_enum import UserToolSourceOutputOutputsItemTypeEnum

__all__ = ["IncomingToolOutputCollectionOutput"]


@dataclass
class IncomingToolOutputCollectionOutput:
    """
    IncomingToolOutputCollectionOutput dataclass

    Args:
        structure (ToolOutputCollectionStructure)
                                 :
        type_ (UserToolSourceOutputOutputsItemTypeEnum)
                                 : Maps from 'type'
        hidden (IncomingToolOutputCollectionOutputHidden | None)
                                 : If true, the output will not be shown in the history.
        label (IncomingToolOutputCollectionOutputLabel | None)
                                 : Output label. Will be used as dataset name in history.
        name (IncomingToolOutputCollectionOutputName | None)
                                 : Parameter name. Used when referencing parameter in
                                   workflows.
    """

    structure: ToolOutputCollectionStructure
    type_: UserToolSourceOutputOutputsItemTypeEnum  # Maps from 'type'
    hidden: IncomingToolOutputCollectionOutputHidden | None = (
        None  # If true, the output will not be shown in the history.
    )
    label: IncomingToolOutputCollectionOutputLabel | None = (
        None  # Output label. Will be used as dataset name in history.
    )
    name: IncomingToolOutputCollectionOutputName | None = (
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
