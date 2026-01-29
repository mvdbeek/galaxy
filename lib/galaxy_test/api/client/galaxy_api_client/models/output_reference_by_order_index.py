from dataclasses import dataclass

from .output_reference_by_order_index_output_name import OutputReferenceByOrderIndexOutputName

__all__ = ["OutputReferenceByOrderIndex"]


@dataclass
class OutputReferenceByOrderIndex:
    """
    OutputReferenceByOrderIndex dataclass

    Args:
        order_index (int)        : The order_index of the step being referenced. The order
                                   indices of a workflow start at 0.
        output_name (OutputReferenceByOrderIndexOutputName | None)
                                 : The output name as defined by the workflow module
                                   corresponding to the step being referenced. The default
                                   is 'output', corresponding to the output defined by input
                                   step types.
    """

    order_index: int  # The order_index of the step being referenced. The order indices of a workflow start at 0.
    output_name: OutputReferenceByOrderIndexOutputName | None = (
        "output"  # The output name as defined by the workflow module corresponding to the step being referenced. The default is 'output', corresponding to the output defined by input step types.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "order_index": "order_index",
            "output_name": "output_name",
        }
        key_transform_with_dump = {
            "order_index": "order_index",
            "output_name": "output_name",
        }
