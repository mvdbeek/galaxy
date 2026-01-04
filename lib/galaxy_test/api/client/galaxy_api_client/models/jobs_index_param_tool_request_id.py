from typing import TypeAlias

__all__ = ["JobsIndexParamToolRequestId"]

JobsIndexParamToolRequestId: TypeAlias = str | None
"""Alias for Limit listing of jobs to those that were created from the supplied tool request ID. If none, jobs from any tool request (or from no workflows) may be returned."""
