from typing import TypeAlias

from .step_reference_by_label import StepReferenceByLabel
from .step_reference_by_order_index import StepReferenceByOrderIndex

__all__ = ["Step"]

Step: TypeAlias = StepReferenceByLabel | StepReferenceByOrderIndex
"""Alias for The target step for this action."""
