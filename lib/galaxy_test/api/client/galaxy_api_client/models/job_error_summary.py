from dataclasses import dataclass

from .messages import Messages

__all__ = ["JobErrorSummary"]


@dataclass
class JobErrorSummary:
    """
    JobErrorSummary dataclass.

    Args:
        messages (Optional[Messages])
                                 : The error messages for the specified job.
    """

    messages: Messages | None  # The error messages for the specified job.
