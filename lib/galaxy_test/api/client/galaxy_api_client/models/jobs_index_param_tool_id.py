from typing import TypeAlias

__all__ = ["JobsIndexParamToolId"]

JobsIndexParamToolId: TypeAlias = list[str] | None
"""Alias for Limit listing of jobs to those that match one of the included tool_ids. If none, all are returned"""
