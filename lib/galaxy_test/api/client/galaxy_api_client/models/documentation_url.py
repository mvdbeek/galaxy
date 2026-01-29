from typing import TypeAlias

__all__ = ["DocumentationUrl"]

DocumentationUrl: TypeAlias = str | None
"""Alias for URL of the documentation of this service (RFC 3986 format). This should help someone learn how to use your service, including any specifics required to access data, e.g. authentication."""
