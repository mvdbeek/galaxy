from dataclasses import dataclass

from .headers import Headers

__all__ = ["AccessUrl"]


@dataclass
class AccessUrl:
    """
    AccessUrl dataclass.

    Args:
        url (str)                : A fully resolvable URL that can be used to fetch the
                                   actual object bytes.
        headers (Optional[Headers])
                                 : An optional list of headers to include in the HTTP
                                   request to `url`. These headers can be used to provide
                                   auth tokens required to fetch the object bytes.
    """

    url: str  # A fully resolvable URL that can be used to fetch the actual object bytes.
    headers: Headers | None = (
        None  # An optional list of headers to include in the HTTP request to `url`. These headers can be used to provide auth tokens required to fetch the object bytes.
    )
