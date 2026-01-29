from typing import TypeAlias

from .display_app import DisplayApp

__all__ = ["HdaCustomDisplayApps"]

HdaCustomDisplayApps: TypeAlias = list[DisplayApp] | None
"""Alias for Contains new-style display app urls."""
