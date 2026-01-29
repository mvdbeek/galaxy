from dataclasses import dataclass

from .tool_output_float_hidden import ToolOutputFloatHidden
from .tool_output_float_label import ToolOutputFloatLabel
from .tool_output_float_name import ToolOutputFloatName
from .user_tool_source_output_outputs_item_type_enum import UserToolSourceOutputOutputsItemTypeEnum

__all__ = ["ToolOutputFloat"]


@dataclass
class ToolOutputFloat:
    """
    ToolOutputFloat dataclass

    Args:
        hidden (ToolOutputFloatHidden)
                                 : If true, the output will not be shown in the history.
        name (ToolOutputFloatName): Parameter name. Used when referencing parameter in
                                    workflows.
        type_ (UserToolSourceOutputOutputsItemTypeEnum)
                                 : Maps from 'type'
        label (ToolOutputFloatLabel | None)
                                 : Output label. Will be used as dataset name in history.
    """

    hidden: ToolOutputFloatHidden  # If true, the output will not be shown in the history.
    name: ToolOutputFloatName  # Parameter name. Used when referencing parameter in workflows.
    type_: UserToolSourceOutputOutputsItemTypeEnum  # Maps from 'type'
    label: ToolOutputFloatLabel | None = None  # Output label. Will be used as dataset name in history.

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
