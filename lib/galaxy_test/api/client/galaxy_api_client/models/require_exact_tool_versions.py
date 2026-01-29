from typing import TypeAlias

__all__ = ["RequireExactToolVersions"]

RequireExactToolVersions: TypeAlias = bool | None
"""Alias for If true, exact tool versions are required for workflow invocation."""
