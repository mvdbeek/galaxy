from typing import TypeAlias

__all__ = ["JobSummaryExternalId"]

JobSummaryExternalId: TypeAlias = str | None
"""Alias for The job id used by the external job runner (Condor, Pulsar, etc.). Only administrator can see this value."""
