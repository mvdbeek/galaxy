from typing import TypeAlias

__all__ = ["Handler"]

Handler: TypeAlias = str | None
"""Alias for The job handler process assigned to handle this job. Only administrator can see this value."""
