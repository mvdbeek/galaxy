from enum import Enum


class NotificationVariant(str, Enum):
    INFO = "info"
    URGENT = "urgent"
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
