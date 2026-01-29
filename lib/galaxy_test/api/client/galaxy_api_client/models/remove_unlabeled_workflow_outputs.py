from dataclasses import dataclass

from .refactor_request_actions_item_action_type_enum import RefactorRequestActionsItemActionTypeEnum

__all__ = ["RemoveUnlabeledWorkflowOutputs"]


@dataclass
class RemoveUnlabeledWorkflowOutputs:
    """
    RemoveUnlabeledWorkflowOutputs dataclass

    Args:
        action_type (RefactorRequestActionsItemActionTypeEnum)
                                 :
    """

    action_type: RefactorRequestActionsItemActionTypeEnum

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "action_type": "action_type",
        }
        key_transform_with_dump = {
            "action_type": "action_type",
        }
