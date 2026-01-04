from dataclasses import dataclass

from .targets import Targets

__all__ = ["DataLandingRequestState"]


@dataclass
class DataLandingRequestState:
    """
    DataLandingRequestState dataclass.

    Args:
        targets (Targets)        :
    """

    targets: Targets
