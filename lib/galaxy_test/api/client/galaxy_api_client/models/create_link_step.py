from dataclasses import dataclass

from .create_link_step_ready import CreateLinkStepReady
from .create_link_step_state import CreateLinkStepState

__all__ = ["CreateLinkStep"]


@dataclass
class CreateLinkStep:
    """
    CreateLinkStep dataclass

    Args:
        name (str)               :
        ready (CreateLinkStepReady | None)
                                 :
        state (CreateLinkStepState | None)
                                 :
    """

    name: str
    ready: CreateLinkStepReady | None = False
    state: CreateLinkStepState | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "name": "name",
            "ready": "ready",
            "state": "state",
        }
        key_transform_with_dump = {
            "name": "name",
            "ready": "ready",
            "state": "state",
        }
