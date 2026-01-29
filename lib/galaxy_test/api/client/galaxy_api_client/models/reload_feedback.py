from dataclasses import dataclass

from .reload_feedback_failed import ReloadFeedbackFailed
from .reload_feedback_reloaded import ReloadFeedbackReloaded

__all__ = ["ReloadFeedback"]


@dataclass
class ReloadFeedback:
    """
    ReloadFeedback dataclass

    Args:
        failed (ReloadFeedbackFailed)
                                 :
        message (str)            :
        reloaded (ReloadFeedbackReloaded)
                                 :
    """

    failed: ReloadFeedbackFailed
    message: str
    reloaded: ReloadFeedbackReloaded

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "failed": "failed",
            "message": "message",
            "reloaded": "reloaded",
        }
        key_transform_with_dump = {
            "failed": "failed",
            "message": "message",
            "reloaded": "reloaded",
        }
