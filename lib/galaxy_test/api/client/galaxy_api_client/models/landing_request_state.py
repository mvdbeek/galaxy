from enum import Enum


class LandingRequestState(str, Enum):
    CLAIMED = "claimed"
    UNCLAIMED = "unclaimed"

    def __str__(self) -> str:
        return str(self.value)
