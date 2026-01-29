from dataclasses import dataclass

from .refactor_request_actions_item_action_type_enum import RefactorRequestActionsItemActionTypeEnum
from .update_step_label_action_step import UpdateStepLabelActionStep

__all__ = ["UpdateStepLabelAction"]


@dataclass
class UpdateStepLabelAction:
    """
    UpdateStepLabelAction dataclass

    Args:
        action_type (RefactorRequestActionsItemActionTypeEnum)
                                 :
        label (str)              : The unique label of the step being referenced.
        step (UpdateStepLabelActionStep)
                                 : The target step for this action.
    """

    action_type: RefactorRequestActionsItemActionTypeEnum
    label: str  # The unique label of the step being referenced.
    step: UpdateStepLabelActionStep  # The target step for this action.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "action_type": "action_type",
            "label": "label",
            "step": "step",
        }
        key_transform_with_dump = {
            "action_type": "action_type",
            "label": "label",
            "step": "step",
        }
