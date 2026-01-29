from dataclasses import dataclass

from .refactor_request_actions_item_action_type_enum import RefactorRequestActionsItemActionTypeEnum
from .upgrade_subworkflow_action_content_id import UpgradeSubworkflowActionContentId
from .upgrade_subworkflow_action_step import UpgradeSubworkflowActionStep

__all__ = ["UpgradeSubworkflowAction"]


@dataclass
class UpgradeSubworkflowAction:
    """
    UpgradeSubworkflowAction dataclass

    Args:
        action_type (RefactorRequestActionsItemActionTypeEnum)
                                 :
        step (UpgradeSubworkflowActionStep)
                                 : The target step for this action.
        content_id (UpgradeSubworkflowActionContentId | None)
                                 :
    """

    action_type: RefactorRequestActionsItemActionTypeEnum
    step: UpgradeSubworkflowActionStep  # The target step for this action.
    content_id: UpgradeSubworkflowActionContentId | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "action_type": "action_type",
            "content_id": "content_id",
            "step": "step",
        }
        key_transform_with_dump = {
            "action_type": "action_type",
            "content_id": "content_id",
            "step": "step",
        }
