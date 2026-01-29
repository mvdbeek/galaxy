from typing import TypeAlias

from .job_state import JobState

__all__ = ["JobConsoleOutputState"]

JobConsoleOutputState: TypeAlias = JobState | None
"""Alias for The current job's state"""
