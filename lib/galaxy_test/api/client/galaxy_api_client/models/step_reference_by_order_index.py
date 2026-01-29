from dataclasses import dataclass

__all__ = ["StepReferenceByOrderIndex"]


@dataclass
class StepReferenceByOrderIndex:
    """
    StepReferenceByOrderIndex dataclass.

    Args:
        order_index (int)        : The order_index of the step being referenced. The order
                                   indices of a workflow start at 0.
    """

    order_index: int  # The order_index of the step being referenced. The order indices of a workflow start at 0.
