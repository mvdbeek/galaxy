from dataclasses import dataclass

from .ready import Ready
from .state import State

__all__ = ["CreateLinkStep"]


@dataclass
class CreateLinkStep:
    """
    CreateLinkStep dataclass.

    Args:
        name (str)               :
        ready (Optional[Ready])  :
        state (Optional[State])  : Current state of the job.
    """

    name: str
    ready: Ready | None = False
    state: State | None = None  # Current state of the job.
