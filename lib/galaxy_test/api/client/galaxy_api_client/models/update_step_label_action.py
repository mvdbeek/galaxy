from dataclasses import dataclass

from .step import Step

__all__ = ["UpdateStepLabelAction"]


@dataclass
class UpdateStepLabelAction:
    """
    UpdateStepLabelAction dataclass.

    Args:
        action_type (str)        :
        label (str)              : The unique label of the step being referenced.
        step (Step)              : The target step for this action.
    """

    action_type: str
    label: str  # The unique label of the step being referenced.
    step: Step  # The target step for this action.
