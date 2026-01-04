from dataclasses import dataclass

from .source import Source

__all__ = ["QuotaModel"]


@dataclass
class QuotaModel:
    """
    QuotaModel dataclass.

    Args:
        enabled (bool)           :
        source (Optional[Source]): The source of the notification. Represents the agent that
                                   created the notification.
    """

    enabled: bool
    source: Source | None = None  # The source of the notification. Represents the agent that created the notification.
