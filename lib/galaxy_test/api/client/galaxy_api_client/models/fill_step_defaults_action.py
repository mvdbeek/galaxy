from dataclasses import dataclass

from .step import Step

__all__ = ["FillStepDefaultsAction"]


@dataclass
class FillStepDefaultsAction:
    """
    FillStepDefaultsAction dataclass.

    Args:
        action_type (str)        :
        step (Step)              : The target step for this action.
    """

    action_type: str
    step: Step  # The target step for this action.
