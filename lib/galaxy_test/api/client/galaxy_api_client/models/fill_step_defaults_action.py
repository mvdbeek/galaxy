from dataclasses import dataclass

from .fill_step_defaults_action_step import FillStepDefaultsActionStep
from .refactor_request_actions_item_action_type_enum import RefactorRequestActionsItemActionTypeEnum

__all__ = ["FillStepDefaultsAction"]


@dataclass
class FillStepDefaultsAction:
    """
    FillStepDefaultsAction dataclass

    Args:
        action_type (RefactorRequestActionsItemActionTypeEnum)
                                 :
        step (FillStepDefaultsActionStep)
                                 :
    """

    action_type: RefactorRequestActionsItemActionTypeEnum
    step: FillStepDefaultsActionStep

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "action_type": "action_type",
            "step": "step",
        }
        key_transform_with_dump = {
            "action_type": "action_type",
            "step": "step",
        }
