from typing import TypeAlias

__all__ = ["FilesSourcePluginRequiresRoles"]

FilesSourcePluginRequiresRoles: TypeAlias = str | None
"""Alias for Only users with the roles specified here can access this files source."""
