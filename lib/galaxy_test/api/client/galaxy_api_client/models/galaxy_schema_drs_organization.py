from dataclasses import dataclass

__all__ = ["GalaxySchemaDrsOrganization"]


@dataclass
class GalaxySchemaDrsOrganization:
    """
    GalaxySchemaDrsOrganization dataclass.

    Args:
        name (str)               : Name of the organization responsible for the service
        url (str)                : URL of the website of the organization (RFC 3986 format)
    """

    name: str  # Name of the organization responsible for the service
    url: str  # URL of the website of the organization (RFC 3986 format)
