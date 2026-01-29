from dataclasses import dataclass

from .refactor_request_actions_item_action_type_enum import RefactorRequestActionsItemActionTypeEnum
from .upgrade_tool_action_step import UpgradeToolActionStep
from .upgrade_tool_action_tool_version import UpgradeToolActionToolVersion

__all__ = ["UpgradeToolAction"]


@dataclass
class UpgradeToolAction:
    """
    UpgradeToolAction dataclass

    Args:
        action_type (RefactorRequestActionsItemActionTypeEnum)
                                 :
        step (UpgradeToolActionStep)
                                 : The target step for this action.
        tool_version (UpgradeToolActionToolVersion | None)
                                 :
    """

    action_type: RefactorRequestActionsItemActionTypeEnum
    step: UpgradeToolActionStep  # The target step for this action.
    tool_version: UpgradeToolActionToolVersion | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "action_type": "action_type",
            "step": "step",
            "tool_version": "tool_version",
        }
        key_transform_with_dump = {
            "action_type": "action_type",
            "step": "step",
            "tool_version": "tool_version",
        }
