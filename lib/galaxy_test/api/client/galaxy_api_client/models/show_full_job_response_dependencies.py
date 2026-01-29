from typing import Any, TypeAlias

__all__ = ["ShowFullJobResponseDependencies"]

ShowFullJobResponseDependencies: TypeAlias = list[dict[str, Any]] | None
"""Alias for The dependencies of the job."""
