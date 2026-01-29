from typing import TypeAlias

from .position import Position

__all__ = ["AddStepActionPosition"]

AddStepActionPosition: TypeAlias = Position | None
"""Alias for The location of the step in the Galaxy workflow editor."""
