from typing import Any, TypeAlias

__all__ = ["InvocationReportWorkflows"]

InvocationReportWorkflows: TypeAlias = dict[str, Any] | None
"""Alias for Workflows associated with the invocation."""
