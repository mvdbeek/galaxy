from dataclasses import dataclass

from .create_link_feedback_messages import CreateLinkFeedbackMessages
from .create_link_feedback_preparable_steps import CreateLinkFeedbackPreparableSteps
from .create_link_feedback_refresh import CreateLinkFeedbackRefresh
from .create_link_feedback_resource import CreateLinkFeedbackResource

__all__ = ["CreateLinkFeedback"]


@dataclass
class CreateLinkFeedback:
    """
    CreateLinkFeedback dataclass

    Args:
        messages (CreateLinkFeedbackMessages | None)
                                 :
        preparable_steps (CreateLinkFeedbackPreparableSteps | None)
                                 :
        refresh (CreateLinkFeedbackRefresh | None)
                                 :
        resource (CreateLinkFeedbackResource | None)
                                 :
    """

    messages: CreateLinkFeedbackMessages | None = None
    preparable_steps: CreateLinkFeedbackPreparableSteps | None = None
    refresh: CreateLinkFeedbackRefresh | None = False
    resource: CreateLinkFeedbackResource | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "messages": "messages",
            "preparable_steps": "preparable_steps",
            "refresh": "refresh",
            "resource": "resource",
        }
        key_transform_with_dump = {
            "messages": "messages",
            "preparable_steps": "preparable_steps",
            "refresh": "refresh",
            "resource": "resource",
        }
