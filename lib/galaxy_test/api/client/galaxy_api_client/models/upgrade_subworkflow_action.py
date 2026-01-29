from dataclasses import dataclass

from .content_id import ContentId
from .step import Step

__all__ = ["UpgradeSubworkflowAction"]


@dataclass
class UpgradeSubworkflowAction:
    """
    UpgradeSubworkflowAction dataclass.

    Args:
        action_type (str)        :
        step (Step)              : The target step for this action.
        content_id (Optional[ContentId])
                                 :
    """

    action_type: str
    step: Step  # The target step for this action.
    content_id: ContentId | None = None
