from typing import TypeAlias

from .display_app import DisplayApp

__all__ = ["DisplayApps"]

DisplayApps: TypeAlias = list[DisplayApp] | None
"""Alias for Contains new-style display app urls."""
