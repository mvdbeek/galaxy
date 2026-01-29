from dataclasses import dataclass

from .tool_output_text_hidden import ToolOutputTextHidden
from .tool_output_text_label import ToolOutputTextLabel
from .tool_output_text_name import ToolOutputTextName
from .user_tool_source_output_outputs_item_type_enum import UserToolSourceOutputOutputsItemTypeEnum

__all__ = ["ToolOutputText"]


@dataclass
class ToolOutputText:
    """
    ToolOutputText dataclass

    Args:
        hidden (ToolOutputTextHidden)
                                 : If true, the output will not be shown in the history.
        name (ToolOutputTextName): Parameter name. Used when referencing parameter in
                                   workflows.
        type_ (UserToolSourceOutputOutputsItemTypeEnum)
                                 : Maps from 'type'
        label (ToolOutputTextLabel | None)
                                 : Output label. Will be used as dataset name in history.
    """

    hidden: ToolOutputTextHidden  # If true, the output will not be shown in the history.
    name: ToolOutputTextName  # Parameter name. Used when referencing parameter in workflows.
    type_: UserToolSourceOutputOutputsItemTypeEnum  # Maps from 'type'
    label: ToolOutputTextLabel | None = None  # Output label. Will be used as dataset name in history.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "hidden": "hidden",
            "label": "label",
            "name": "name",
            "type": "type_",
        }
        key_transform_with_dump = {
            "hidden": "hidden",
            "label": "label",
            "name": "name",
            "type_": "type",
        }
