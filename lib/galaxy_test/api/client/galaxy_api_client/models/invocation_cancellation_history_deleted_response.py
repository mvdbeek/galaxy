from dataclasses import dataclass

__all__ = ["InvocationCancellationHistoryDeletedResponse"]


@dataclass
class InvocationCancellationHistoryDeletedResponse:
    """
    InvocationCancellationHistoryDeletedResponse dataclass.

    Args:
        history_id (str)         : History ID of history that was deleted.
        reason (str)             :
    """

    history_id: str  # History ID of history that was deleted.
    reason: str
