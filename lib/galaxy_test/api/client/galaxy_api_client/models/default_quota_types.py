from enum import Enum


class DefaultQuotaTypes(str, Enum):
    REGISTERED = "registered"
    UNREGISTERED = "unregistered"

    def __str__(self) -> str:
        return str(self.value)
