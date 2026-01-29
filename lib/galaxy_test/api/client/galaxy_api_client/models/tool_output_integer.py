from dataclasses import dataclass

from .tool_output_integer_hidden import ToolOutputIntegerHidden
from .tool_output_integer_label import ToolOutputIntegerLabel
from .tool_output_integer_name import ToolOutputIntegerName
from .user_tool_source_output_outputs_item_type_enum import UserToolSourceOutputOutputsItemTypeEnum

__all__ = ["ToolOutputInteger"]


@dataclass
class ToolOutputInteger:
    """
    ToolOutputInteger dataclass

    Args:
        hidden (ToolOutputIntegerHidden)
                                 : If true, the output will not be shown in the history.
        name (ToolOutputIntegerName)
                                 : Parameter name. Used when referencing parameter in
                                   workflows.
        type_ (UserToolSourceOutputOutputsItemTypeEnum)
                                 : Maps from 'type'
        label (ToolOutputIntegerLabel | None)
                                 : Output label. Will be used as dataset name in history.
    """

    hidden: ToolOutputIntegerHidden  # If true, the output will not be shown in the history.
    name: ToolOutputIntegerName  # Parameter name. Used when referencing parameter in workflows.
    type_: UserToolSourceOutputOutputsItemTypeEnum  # Maps from 'type'
    label: ToolOutputIntegerLabel | None = None  # Output label. Will be used as dataset name in history.

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
