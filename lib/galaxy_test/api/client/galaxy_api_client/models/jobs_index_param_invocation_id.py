from typing import TypeAlias

__all__ = ["JobsIndexParamInvocationId"]

JobsIndexParamInvocationId: TypeAlias = str | None
"""Alias for Limit listing of jobs to those that match the specified workflow invocation ID. If none, jobs from any workflow invocation (or from no workflows) may be returned."""
