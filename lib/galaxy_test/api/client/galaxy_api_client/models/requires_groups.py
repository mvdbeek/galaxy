from typing import TypeAlias

__all__ = ["RequiresGroups"]

RequiresGroups: TypeAlias = str | None
"""Alias for Only users belonging to the groups specified here can access this files source."""
