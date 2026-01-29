from typing import TypeAlias

__all__ = ["OutputReferenceByLabelOutputName"]

OutputReferenceByLabelOutputName: TypeAlias = str | None
"""Alias for The output name as defined by the workflow module corresponding to the step being referenced. The default is 'output', corresponding to the output defined by input step types."""
