from dataclasses import dataclass
from typing import Annotated, TypeAlias

from .data_request_collection_uri import DataRequestCollectionUri
from .file_request_uri import FileRequestUri

__all__ = ["CreateFileLandingPayloadRequestStateItem", "CreateFileLandingPayloadRequestStateItemDiscriminator"]


@dataclass(frozen=True)
class CreateFileLandingPayloadRequestStateItemDiscriminator:
    """Discriminator metadata for CreateFileLandingPayloadRequestStateItem union."""

    property_name: str = "class"
    """The discriminator property name"""

    # Mapping stored as tuple for frozen dataclass compatibility
    _mapping_data: tuple[tuple[str, str], ...] = (
        ("Collection", "DataRequestCollectionUri"),
        ("File", "FileRequestUri"),
    )

    def get_mapping(self) -> dict[str, type]:
        """Get discriminator mapping with actual type references."""
        from .data_request_collection_uri import DataRequestCollectionUri
        from .file_request_uri import FileRequestUri

        return {
            "Collection": DataRequestCollectionUri,
            "File": FileRequestUri,
        }


CreateFileLandingPayloadRequestStateItem: TypeAlias = Annotated[
    FileRequestUri | DataRequestCollectionUri, CreateFileLandingPayloadRequestStateItemDiscriminator()
]
