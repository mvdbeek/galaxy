from dataclasses import dataclass

from .add_step_action_label import AddStepActionLabel
from .add_step_action_position import AddStepActionPosition
from .add_step_action_tool_state import AddStepActionToolState
from .refactor_request_actions_item_action_type_enum import RefactorRequestActionsItemActionTypeEnum

__all__ = ["AddStepAction"]


@dataclass
class AddStepAction:
    """
    Add a new action to the workflow.  After the workflow is updated, an order_index will be
    assigned and this step may cause other steps to have their output_index adjusted.

    Args:
        action_type (RefactorRequestActionsItemActionTypeEnum)
                                 :
        type_ (str)              : Module type of the step to add, see
                                   galaxy.workflow.modules for available types. (maps from
                                   'type')
        label (AddStepActionLabel | None)
                                 : A unique label for the step being added, must be distinct
                                   from the labels already present in the workflow.
        position (AddStepActionPosition | None)
                                 : The location of the step in the Galaxy workflow editor.
        tool_state (AddStepActionToolState | None)
                                 :
    """

    action_type: RefactorRequestActionsItemActionTypeEnum
    type_: str  # Module type of the step to add, see galaxy.workflow.modules for available types. (maps from 'type')
    label: AddStepActionLabel | None = (
        None  # A unique label for the step being added, must be distinct from the labels already present in the workflow.
    )
    position: AddStepActionPosition | None = None  # The location of the step in the Galaxy workflow editor.
    tool_state: AddStepActionToolState | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "action_type": "action_type",
            "label": "label",
            "position": "position",
            "tool_state": "tool_state",
            "type": "type_",
        }
        key_transform_with_dump = {
            "action_type": "action_type",
            "label": "label",
            "position": "position",
            "tool_state": "tool_state",
            "type_": "type",
        }
