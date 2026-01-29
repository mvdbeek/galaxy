from dataclasses import dataclass

__all__ = ["StepReferenceByLabel"]


@dataclass
class StepReferenceByLabel:
    """
    StepReferenceByLabel dataclass.

    Args:
        label (str)              : The unique label of the step being referenced.
    """

    label: str  # The unique label of the step being referenced.
