from enum import Enum


class DefaultQuotaValues(str, Enum):
    NO = "no"
    REGISTERED = "registered"
    UNREGISTERED = "unregistered"

    def __str__(self) -> str:
        return str(self.value)
