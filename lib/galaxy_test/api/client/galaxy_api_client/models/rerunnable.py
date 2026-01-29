from typing import TypeAlias

__all__ = ["Rerunnable"]

Rerunnable: TypeAlias = bool | None
"""Alias for Whether the job creating this dataset can be run again."""
