from typing import TypeAlias

from .display_app import DisplayApp

__all__ = ["DisplayTypes"]

DisplayTypes: TypeAlias = list[DisplayApp] | None
"""Alias for Contains old-style display app urls."""
