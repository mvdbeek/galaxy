from typing import TypeAlias

__all__ = ["JobsIndexParamState"]

JobsIndexParamState: TypeAlias = list[str] | None
"""Alias for A list or comma-separated list of states to filter job query on. If unspecified, jobs of any state may be returned."""
