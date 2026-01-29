from dataclasses import dataclass

from .created_entry_response_external_link import CreatedEntryResponseExternalLink

__all__ = ["CreatedEntryResponse"]


@dataclass
class CreatedEntryResponse:
    """
    CreatedEntryResponse dataclass

    Args:
        name (str)               : The name of the created entry.
        uri (str)                : The URI of the created entry.
        external_link (CreatedEntryResponseExternalLink | None)
                                 : An optional external link to the created entry if
                                   available.
    """

    name: str  # The name of the created entry.
    uri: str  # The URI of the created entry.
    external_link: CreatedEntryResponseExternalLink | None = (
        None  # An optional external link to the created entry if available.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "external_link": "external_link",
            "name": "name",
            "uri": "uri",
        }
        key_transform_with_dump = {
            "external_link": "external_link",
            "name": "name",
            "uri": "uri",
        }
