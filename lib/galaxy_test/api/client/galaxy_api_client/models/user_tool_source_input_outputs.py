from typing import TypeAlias

from .user_tool_source_input_outputs_item import UserToolSourceInputOutputsItem

__all__ = ["UserToolSourceInputOutputs"]

UserToolSourceInputOutputs: TypeAlias = list[UserToolSourceInputOutputsItem]
