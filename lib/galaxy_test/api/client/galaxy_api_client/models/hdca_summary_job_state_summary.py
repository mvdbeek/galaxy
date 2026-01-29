from typing import TypeAlias

from .hdc_job_state_summary_2 import HdcJobStateSummary2

__all__ = ["HdcaSummaryJobStateSummary"]

HdcaSummaryJobStateSummary: TypeAlias = HdcJobStateSummary2 | None
"""Alias for Overview of the job states working inside the dataset collection."""
