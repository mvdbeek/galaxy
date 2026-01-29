from dataclasses import dataclass

from .access_url_headers import AccessUrlHeaders

__all__ = ["AccessUrl"]


@dataclass
class AccessUrl:
    """
    AccessUrl dataclass

    Args:
        url (str)                : A fully resolvable URL that can be used to fetch the
                                   actual object bytes.
        headers (AccessUrlHeaders | None)
                                 : An optional list of headers to include in the HTTP
                                   request to `url`. These headers can be used to provide
                                   auth tokens required to fetch the object bytes.
    """

    url: str  # A fully resolvable URL that can be used to fetch the actual object bytes.
    headers: AccessUrlHeaders | None = (
        None  # An optional list of headers to include in the HTTP request to `url`. These headers can be used to provide auth tokens required to fetch the object bytes.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "headers": "headers",
            "url": "url",
        }
        key_transform_with_dump = {
            "headers": "headers",
            "url": "url",
        }
