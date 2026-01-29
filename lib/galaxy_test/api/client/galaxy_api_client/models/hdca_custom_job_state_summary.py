from typing import TypeAlias

from .hdc_job_state_summary import HdcJobStateSummary

__all__ = ["HdcaCustomJobStateSummary"]

HdcaCustomJobStateSummary: TypeAlias = HdcJobStateSummary | None
"""Alias for Overview of the job states working inside the dataset collection."""
