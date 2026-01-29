from dataclasses import dataclass

from .label import Label
from .position import Position
from .tool_state import ToolState

__all__ = ["AddStepAction"]


@dataclass
class AddStepAction:
    """
    Add a new action to the workflow.  After the workflow is updated, an order_index will be
    assigned and this step may cause other steps to have their output_index adjusted.

    Args:
        action_type (str)        :
        type_ (str)              : Module type of the step to add, see
                                   galaxy.workflow.modules for available types.
        label (Optional[Label])  : Label of the input.
        position (Optional[Position])
                                 : The location of the step in the Galaxy workflow editor.
        tool_state (Optional[ToolState])
                                 :
    """

    action_type: str
    type_: str  # Module type of the step to add, see galaxy.workflow.modules for available types.
    label: Label | None = None  # Label of the input.
    position: Position | None = None  # The location of the step in the Galaxy workflow editor.
    tool_state: ToolState | None = None
