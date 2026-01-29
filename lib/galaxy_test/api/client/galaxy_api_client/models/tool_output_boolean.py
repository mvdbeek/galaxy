from dataclasses import dataclass

from .tool_output_boolean_hidden import ToolOutputBooleanHidden
from .tool_output_boolean_label import ToolOutputBooleanLabel
from .tool_output_boolean_name import ToolOutputBooleanName
from .user_tool_source_output_outputs_item_type_enum import UserToolSourceOutputOutputsItemTypeEnum

__all__ = ["ToolOutputBoolean"]


@dataclass
class ToolOutputBoolean:
    """
    ToolOutputBoolean dataclass

    Args:
        hidden (ToolOutputBooleanHidden)
                                 : If true, the output will not be shown in the history.
        name (ToolOutputBooleanName)
                                 : Parameter name. Used when referencing parameter in
                                   workflows.
        type_ (UserToolSourceOutputOutputsItemTypeEnum)
                                 : Maps from 'type'
        label (ToolOutputBooleanLabel | None)
                                 : Output label. Will be used as dataset name in history.
    """

    hidden: ToolOutputBooleanHidden  # If true, the output will not be shown in the history.
    name: ToolOutputBooleanName  # Parameter name. Used when referencing parameter in workflows.
    type_: UserToolSourceOutputOutputsItemTypeEnum  # Maps from 'type'
    label: ToolOutputBooleanLabel | None = None  # Output label. Will be used as dataset name in history.

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
