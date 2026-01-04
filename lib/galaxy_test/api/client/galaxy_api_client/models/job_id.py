from typing import TypeAlias

__all__ = ["JobId"]

JobId: TypeAlias = str | None
"""Alias for The encoded ID of the job associated with this workflow invocation step."""
