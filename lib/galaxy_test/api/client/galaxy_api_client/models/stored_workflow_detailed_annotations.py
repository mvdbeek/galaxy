from typing import TypeAlias

__all__ = ["StoredWorkflowDetailedAnnotations"]

StoredWorkflowDetailedAnnotations: TypeAlias = list[str] | None
"""Alias for An list of annotations to provide details or to help understand the purpose and usage of this workflow."""
