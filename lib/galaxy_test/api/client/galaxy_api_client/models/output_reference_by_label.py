from dataclasses import dataclass

from .output_reference_by_label_output_name import OutputReferenceByLabelOutputName

__all__ = ["OutputReferenceByLabel"]


@dataclass
class OutputReferenceByLabel:
    """
    OutputReferenceByLabel dataclass

    Args:
        label (str)              : The unique label of the step being referenced.
        output_name (OutputReferenceByLabelOutputName | None)
                                 : The output name as defined by the workflow module
                                   corresponding to the step being referenced. The default
                                   is 'output', corresponding to the output defined by input
                                   step types.
    """

    label: str  # The unique label of the step being referenced.
    output_name: OutputReferenceByLabelOutputName | None = (
        "output"  # The output name as defined by the workflow module corresponding to the step being referenced. The default is 'output', corresponding to the output defined by input step types.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "label": "label",
            "output_name": "output_name",
        }
        key_transform_with_dump = {
            "label": "label",
            "output_name": "output_name",
        }
