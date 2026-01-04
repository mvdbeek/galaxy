from dataclasses import dataclass

from .output_name import OutputName

__all__ = ["OutputReferenceByOrderIndex"]


@dataclass
class OutputReferenceByOrderIndex:
    """
    OutputReferenceByOrderIndex dataclass.

    Args:
        order_index (int)        : The order_index of the step being referenced. The order
                                   indices of a workflow start at 0.
        output_name (Optional[OutputName])
                                 : If this message is about an output to a step, this field
                                   describes the target output name. The output name as
                                   defined by the workflow module corresponding to the step
                                   being referenced.
    """

    order_index: int  # The order_index of the step being referenced. The order indices of a workflow start at 0.
    output_name: OutputName | None = (
        "output"  # If this message is about an output to a step, this field describes the target output name. The output name as defined by the workflow module corresponding to the step being referenced.
    )
