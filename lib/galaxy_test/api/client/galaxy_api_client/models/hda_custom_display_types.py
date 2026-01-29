from typing import TypeAlias

from .display_app import DisplayApp

__all__ = ["HdaCustomDisplayTypes"]

HdaCustomDisplayTypes: TypeAlias = list[DisplayApp] | None
"""Alias for Contains old-style display app urls."""
