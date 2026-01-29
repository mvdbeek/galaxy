from dataclasses import dataclass, field
from typing import Annotated, TypeAlias, Union

from .incoming_tool_output_collection_input import IncomingToolOutputCollectionInput
from .incoming_tool_output_dataset import IncomingToolOutputDataset
from .tool_output_boolean import ToolOutputBoolean
from .tool_output_float import ToolOutputFloat
from .tool_output_integer import ToolOutputInteger
from .tool_output_text import ToolOutputText

from .incoming_tool_output_collection_input import IncomingToolOutputCollectionInput
from .incoming_tool_output_dataset import IncomingToolOutputDataset
from .tool_output_boolean import ToolOutputBoolean
from .tool_output_float import ToolOutputFloat
from .tool_output_integer import ToolOutputInteger
from .tool_output_text import ToolOutputText

__all__ = ["AdminToolSourceOutputsItem", "AdminToolSourceOutputsItemDiscriminator"]


@dataclass(frozen=True)
class AdminToolSourceOutputsItemDiscriminator:
    """Discriminator metadata for AdminToolSourceOutputsItem union."""

    property_name: str = "type"
    """The discriminator property name"""

    # Mapping stored as tuple for frozen dataclass compatibility
    _mapping_data: tuple[tuple[str, str], ...] = (
        ("boolean", "ToolOutputBoolean"),
        ("collection", "IncomingToolOutputCollectionInput"),
        ("data", "IncomingToolOutputDataset"),
        ("float", "ToolOutputFloat"),
        ("integer", "ToolOutputInteger"),
        ("text", "ToolOutputText"),
    )

    def get_mapping(self) -> dict[str, type]:
        """Get discriminator mapping with actual type references."""
        from .tool_output_boolean import ToolOutputBoolean
        from .incoming_tool_output_collection_input import IncomingToolOutputCollectionInput
        from .incoming_tool_output_dataset import IncomingToolOutputDataset
        from .tool_output_float import ToolOutputFloat
        from .tool_output_integer import ToolOutputInteger
        from .tool_output_text import ToolOutputText

        return {
            "boolean": ToolOutputBoolean,
            "collection": IncomingToolOutputCollectionInput,
            "data": IncomingToolOutputDataset,
            "float": ToolOutputFloat,
            "integer": ToolOutputInteger,
            "text": ToolOutputText,
        }


AdminToolSourceOutputsItem: TypeAlias = Annotated[
    Union[
        IncomingToolOutputDataset,
        IncomingToolOutputCollectionInput,
        ToolOutputText,
        ToolOutputInteger,
        ToolOutputFloat,
        ToolOutputBoolean,
    ],
    AdminToolSourceOutputsItemDiscriminator(),
]
