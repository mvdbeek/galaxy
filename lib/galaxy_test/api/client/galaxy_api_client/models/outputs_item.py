from typing import TypeAlias

from .incoming_tool_output_collection_input import IncomingToolOutputCollectionInput
from .incoming_tool_output_dataset import IncomingToolOutputDataset
from .tool_output_boolean import ToolOutputBoolean
from .tool_output_float import ToolOutputFloat
from .tool_output_integer import ToolOutputInteger
from .tool_output_text import ToolOutputText

__all__ = ["OutputsItem"]

OutputsItem: TypeAlias = (
    IncomingToolOutputCollectionInput
    | IncomingToolOutputDataset
    | ToolOutputBoolean
    | ToolOutputFloat
    | ToolOutputInteger
    | ToolOutputText
)
