from typing import TypeAlias

__all__ = ["JobsIndexParamWorkflowId"]

JobsIndexParamWorkflowId: TypeAlias = str | None
"""Alias for Limit listing of jobs to those that match the specified workflow ID. If none, jobs from any workflow (or from no workflows) may be returned."""
