from typing import TypeAlias

__all__ = ["JobsIndexParamHistoryId"]

JobsIndexParamHistoryId: TypeAlias = str | None
"""Alias for Limit listing of jobs to those that match the history_id. If none, jobs from any history may be returned."""
