from dataclasses import dataclass

from .messages import Messages
from .preparable_steps import PreparableSteps
from .refresh import Refresh
from .resource import Resource

__all__ = ["CreateLinkFeedback"]


@dataclass
class CreateLinkFeedback:
    """
    CreateLinkFeedback dataclass.

    Args:
        messages (Optional[Messages])
                                 : The error messages for the specified job.
        preparable_steps (Optional[PreparableSteps])
                                 :
        refresh (Optional[Refresh])
                                 :
        resource (Optional[Resource])
                                 :
    """

    messages: Messages | None = None  # The error messages for the specified job.
    preparable_steps: PreparableSteps | None = None
    refresh: Refresh | None = False
    resource: Resource | None = None
