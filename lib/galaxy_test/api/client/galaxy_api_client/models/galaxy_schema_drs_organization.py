from dataclasses import dataclass

__all__ = ["GalaxySchemaDrsOrganization"]


@dataclass
class GalaxySchemaDrsOrganization:
    """
    GalaxySchemaDrsOrganization dataclass

    Args:
        name (str)               : Name of the organization responsible for the service
        url (str)                : URL of the website of the organization (RFC 3986 format)
    """

    name: str  # Name of the organization responsible for the service
    url: str  # URL of the website of the organization (RFC 3986 format)

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "name": "name",
            "url": "url",
        }
        key_transform_with_dump = {
            "name": "name",
            "url": "url",
        }
