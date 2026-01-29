from dataclasses import dataclass

from .job_error_summary_messages import JobErrorSummaryMessages

__all__ = ["JobErrorSummary"]


@dataclass
class JobErrorSummary:
    """
    JobErrorSummary dataclass

    Args:
        messages (JobErrorSummaryMessages)
                                 : The error messages for the specified job.
    """

    messages: JobErrorSummaryMessages  # The error messages for the specified job.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "messages": "messages",
        }
        key_transform_with_dump = {
            "messages": "messages",
        }
