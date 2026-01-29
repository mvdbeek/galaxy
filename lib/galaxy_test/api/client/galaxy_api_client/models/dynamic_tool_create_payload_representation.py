from dataclasses import dataclass, field
from typing import Annotated, TypeAlias, Union

from .admin_tool_source import AdminToolSource
from .user_tool_source_input import UserToolSourceInput

from .admin_tool_source import AdminToolSource
from .user_tool_source_input import UserToolSourceInput

__all__ = ["DynamicToolCreatePayloadRepresentation", "DynamicToolCreatePayloadRepresentationDiscriminator"]


@dataclass(frozen=True)
class DynamicToolCreatePayloadRepresentationDiscriminator:
    """Discriminator metadata for DynamicToolCreatePayloadRepresentation union."""

    property_name: str = "class"
    """The discriminator property name"""

    # Mapping stored as tuple for frozen dataclass compatibility
    _mapping_data: tuple[tuple[str, str], ...] = (
        ("GalaxyTool", "AdminToolSource"),
        ("GalaxyUserTool", "UserToolSourceInput"),
    )

    def get_mapping(self) -> dict[str, type]:
        """Get discriminator mapping with actual type references."""
        from .admin_tool_source import AdminToolSource
        from .user_tool_source_input import UserToolSourceInput

        return {
            "GalaxyTool": AdminToolSource,
            "GalaxyUserTool": UserToolSourceInput,
        }


DynamicToolCreatePayloadRepresentation: TypeAlias = Annotated[
    Union[UserToolSourceInput, AdminToolSource], DynamicToolCreatePayloadRepresentationDiscriminator()
]
