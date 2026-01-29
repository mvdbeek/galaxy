from typing import TypeAlias

__all__ = ["LibraryPermissionsPayloadAccessIds"]

LibraryPermissionsPayloadAccessIds: TypeAlias = list[str] | str | None
"""Alias for A list of role encoded IDs defining roles that should have access permission on the library."""
