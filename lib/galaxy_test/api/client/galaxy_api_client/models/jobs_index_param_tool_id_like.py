from typing import TypeAlias

__all__ = ["JobsIndexParamToolIdLike"]

JobsIndexParamToolIdLike: TypeAlias = list[str] | None
"""Alias for Limit listing of jobs to those that match one of the included tool ID sql-like patterns. If none, all are returned"""
