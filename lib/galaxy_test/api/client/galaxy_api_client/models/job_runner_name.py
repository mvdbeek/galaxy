from typing import TypeAlias

__all__ = ["JobRunnerName"]

JobRunnerName: TypeAlias = str | None
"""Alias for Name of the job runner plugin that handles this job. Only administrator can see this value."""
