from typing import TypeAlias

__all__ = ["JobSummaryHandler"]

JobSummaryHandler: TypeAlias = str | None
"""Alias for The job handler process assigned to handle this job. Only administrator can see this value."""
