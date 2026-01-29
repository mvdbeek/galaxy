from typing import TypeAlias

__all__ = ["ServiceContactUrl"]

ServiceContactUrl: TypeAlias = str | None
"""Alias for URL of the contact for the provider of this service, e.g. a link to a contact form (RFC 3986 format), or an email (RFC 2368 format)."""
