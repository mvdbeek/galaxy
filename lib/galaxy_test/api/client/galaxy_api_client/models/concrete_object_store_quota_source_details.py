from dataclasses import dataclass

from .source import Source

__all__ = ["ConcreteObjectStoreQuotaSourceDetails"]


@dataclass
class ConcreteObjectStoreQuotaSourceDetails:
    """
    ConcreteObjectStoreQuotaSourceDetails dataclass.

    Args:
        enabled (bool)           : Whether the object store tracks quota on the data
                                   (independent of Galaxy's configuration)
        source (Source)          : The source of the notification. Represents the agent that
                                   created the notification.
    """

    enabled: bool  # Whether the object store tracks quota on the data (independent of Galaxy's configuration)
    source: Source  # The source of the notification. Represents the agent that created the notification.
