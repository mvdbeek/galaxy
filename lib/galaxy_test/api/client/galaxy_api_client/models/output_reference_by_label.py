from dataclasses import dataclass

from .output_name import OutputName

__all__ = ["OutputReferenceByLabel"]


@dataclass
class OutputReferenceByLabel:
    """
    OutputReferenceByLabel dataclass.

    Args:
        label (str)              : The unique label of the step being referenced.
        output_name (Optional[OutputName])
                                 : If this message is about an output to a step, this field
                                   describes the target output name. The output name as
                                   defined by the workflow module corresponding to the step
                                   being referenced.
    """

    label: str  # The unique label of the step being referenced.
    output_name: OutputName | None = (
        "output"  # If this message is about an output to a step, this field describes the target output name. The output name as defined by the workflow module corresponding to the step being referenced.
    )
