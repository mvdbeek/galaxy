from dataclasses import dataclass
from typing import Annotated, TypeAlias

from .remote_directory import RemoteDirectory
from .remote_file import RemoteFile

__all__ = ["ListUriResponseItem", "ListUriResponseItemDiscriminator"]


@dataclass(frozen=True)
class ListUriResponseItemDiscriminator:
    """Discriminator metadata for ListUriResponseItem union."""

    property_name: str = "class"
    """The discriminator property name"""

    # Mapping stored as tuple for frozen dataclass compatibility
    _mapping_data: tuple[tuple[str, str], ...] = (
        ("Directory", "RemoteDirectory"),
        ("File", "RemoteFile"),
    )

    def get_mapping(self) -> dict[str, type]:
        """Get discriminator mapping with actual type references."""
        from .remote_directory import RemoteDirectory
        from .remote_file import RemoteFile

        return {
            "Directory": RemoteDirectory,
            "File": RemoteFile,
        }


ListUriResponseItem: TypeAlias = Annotated[RemoteFile | RemoteDirectory, ListUriResponseItemDiscriminator()]
