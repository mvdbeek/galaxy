from typing import TypeAlias

__all__ = ["JobSummaryUserEmail"]

JobSummaryUserEmail: TypeAlias = str | None
"""Alias for The email of the user that owns this job. Only the owner of the job and administrators can see this value."""
