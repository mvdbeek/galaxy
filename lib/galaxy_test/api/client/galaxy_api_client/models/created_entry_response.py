from dataclasses import dataclass

from .external_link import ExternalLink

__all__ = ["CreatedEntryResponse"]


@dataclass
class CreatedEntryResponse:
    """
    CreatedEntryResponse dataclass.

    Args:
        name (str)               : The name of the created entry.
        uri (str)                : The URI of the created entry.
        external_link (Optional[ExternalLink])
                                 : An optional external link to the created entry if
                                   available.
    """

    name: str  # The name of the created entry.
    uri: str  # The URI of the created entry.
    external_link: ExternalLink | None = None  # An optional external link to the created entry if available.
