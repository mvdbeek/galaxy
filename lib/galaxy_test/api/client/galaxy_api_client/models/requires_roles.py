from typing import TypeAlias

__all__ = ["RequiresRoles"]

RequiresRoles: TypeAlias = str | None
"""Alias for Only users with the roles specified here can access this files source."""
