from enum import Enum


class MandatoryNotificationCategory(str, Enum):
    BROADCAST = "broadcast"

    def __str__(self) -> str:
        return str(self.value)
