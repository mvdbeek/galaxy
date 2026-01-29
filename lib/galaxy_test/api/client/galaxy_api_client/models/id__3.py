from typing import TypeAlias

__all__ = ["Id3"]

Id3: TypeAlias = str | None
"""Alias for A DRS identifier of a `DrsObject` (either a single blob or a nested bundle). If this ContentsObject is an object within a nested bundle, then the id is optional. Otherwise, the id is required."""
