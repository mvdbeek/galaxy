from typing import TypeAlias

from .job_state import JobState

__all__ = ["SearchJobsPayloadState"]

SearchJobsPayloadState: TypeAlias = JobState | None
"""Alias for Current state of the job."""
