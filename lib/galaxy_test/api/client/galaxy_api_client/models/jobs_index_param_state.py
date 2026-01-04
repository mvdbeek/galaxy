from typing import TypeAlias

from .anonymous_array_item_204 import AnonymousArrayItem204

__all__ = ["JobsIndexParamState"]

JobsIndexParamState: TypeAlias = list[AnonymousArrayItem204] | None
"""Alias for A list or comma-separated list of states to filter job query on. If unspecified, jobs of any state may be returned."""
