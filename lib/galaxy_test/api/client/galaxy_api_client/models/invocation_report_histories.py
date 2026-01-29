from typing import Any, TypeAlias

__all__ = ["InvocationReportHistories"]

InvocationReportHistories: TypeAlias = dict[str, Any] | None
"""Alias for Histories associated with the invocation."""
