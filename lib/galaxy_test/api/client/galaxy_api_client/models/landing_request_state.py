from enum import Enum, unique

__all__ = ["LandingRequestState"]


@unique
class LandingRequestState(str, Enum):
    """
    LandingRequestState Enum

    Args:
        unclaimed (str)          : Value for UNCLAIMED
        claimed (str)            : Value for CLAIMED
    """

    UNCLAIMED = "unclaimed"
    CLAIMED = "claimed"
