from dataclasses import dataclass

from .state import State

__all__ = ["PluginAspectStatus"]


@dataclass
class PluginAspectStatus:
    """
    PluginAspectStatus dataclass.

    Args:
        message (str)            :
        state (Optional[State])  : Current state of the job.
    """

    message: str
    state: State | None  # Current state of the job.
