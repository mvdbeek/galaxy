from dataclasses import dataclass

from .position import Position
from .step import Step

__all__ = ["UpdateStepPositionAction"]


@dataclass
class UpdateStepPositionAction:
    """
    UpdateStepPositionAction dataclass.

    Args:
        action_type (str)        :
        position_shift (Optional[Position])
                                 : The location of the step in the Galaxy workflow editor.
        step (Step)              : The target step for this action.
    """

    action_type: str
    position_shift: Position | None  # The location of the step in the Galaxy workflow editor.
    step: Step  # The target step for this action.
