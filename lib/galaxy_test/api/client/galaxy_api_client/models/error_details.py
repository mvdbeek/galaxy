from typing import Any, TypeAlias

__all__ = ["ErrorDetails"]

ErrorDetails: TypeAlias = dict[str, Any] | None
"""Alias for Additional error details"""
