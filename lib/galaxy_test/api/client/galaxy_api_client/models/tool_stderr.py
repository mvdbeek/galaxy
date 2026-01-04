from typing import TypeAlias

__all__ = ["ToolStderr"]

ToolStderr: TypeAlias = str | None
"""Alias for The captured standard error of the tool executed by the job."""
