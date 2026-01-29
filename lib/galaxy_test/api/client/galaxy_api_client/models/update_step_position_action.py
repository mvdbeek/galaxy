from dataclasses import dataclass

from .position import Position
from .refactor_request_actions_item_action_type_enum import RefactorRequestActionsItemActionTypeEnum
from .update_step_position_action_step import UpdateStepPositionActionStep

__all__ = ["UpdateStepPositionAction"]


@dataclass
class UpdateStepPositionAction:
    """
    UpdateStepPositionAction dataclass

    Args:
        action_type (RefactorRequestActionsItemActionTypeEnum)
                                 :
        position_shift (Position):
        step (UpdateStepPositionActionStep)
                                 : The target step for this action.
    """

    action_type: RefactorRequestActionsItemActionTypeEnum
    position_shift: Position
    step: UpdateStepPositionActionStep  # The target step for this action.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "action_type": "action_type",
            "position_shift": "position_shift",
            "step": "step",
        }
        key_transform_with_dump = {
            "action_type": "action_type",
            "position_shift": "position_shift",
            "step": "step",
        }
