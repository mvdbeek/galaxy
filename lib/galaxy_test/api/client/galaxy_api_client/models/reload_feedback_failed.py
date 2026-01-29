from typing import TypeAlias

from .reload_feedback_failed_item import ReloadFeedbackFailedItem

__all__ = ["ReloadFeedbackFailed"]

ReloadFeedbackFailed: TypeAlias = list[ReloadFeedbackFailedItem]
