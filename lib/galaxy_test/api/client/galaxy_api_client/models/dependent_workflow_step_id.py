from typing import TypeAlias

__all__ = ["DependentWorkflowStepId"]

DependentWorkflowStepId: TypeAlias = int | None
"""Alias for Workflow step id of step that caused failure."""
