from dataclasses import dataclass

from .source import Source

__all__ = ["ImportToolDataBundle"]


@dataclass
class ImportToolDataBundle:
    """
    ImportToolDataBundle dataclass.

    Args:
        source (Source)          : The source of the notification. Represents the agent that
                                   created the notification.
    """

    source: Source  # The source of the notification. Represents the agent that created the notification.
