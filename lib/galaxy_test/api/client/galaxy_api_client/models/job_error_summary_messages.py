from typing import TypeAlias

from .job_error_summary_messages_item import JobErrorSummaryMessagesItem

__all__ = ["JobErrorSummaryMessages"]

JobErrorSummaryMessages: TypeAlias = list[JobErrorSummaryMessagesItem]
"""Alias for The error messages for the specified job."""
