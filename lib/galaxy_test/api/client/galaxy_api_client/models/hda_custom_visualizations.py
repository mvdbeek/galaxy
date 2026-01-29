from typing import TypeAlias

from .visualization import Visualization

__all__ = ["HdaCustomVisualizations"]

HdaCustomVisualizations: TypeAlias = list[Visualization] | None
"""Alias for The collection of visualizations that can be applied to this dataset."""
