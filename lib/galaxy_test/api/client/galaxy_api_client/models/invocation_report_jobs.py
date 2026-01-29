from typing import Any, TypeAlias

__all__ = ["InvocationReportJobs"]

InvocationReportJobs: TypeAlias = dict[str, Any] | None
"""Alias for Jobs associated with the invocation."""
