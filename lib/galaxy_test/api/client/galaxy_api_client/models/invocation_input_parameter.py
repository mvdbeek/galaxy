from dataclasses import dataclass

from .invocation_input_parameter_parameter_value import InvocationInputParameterParameterValue

__all__ = ["InvocationInputParameter"]


@dataclass
class InvocationInputParameter:
    """
    InvocationInputParameter dataclass

    Args:
        label (str)              : Label of the workflow step associated with the input
                                   parameter.
        parameter_value (InvocationInputParameterParameterValue)
                                 : Value of the input parameter.
        workflow_step_id (str)   : The encoded ID of the workflow step associated with the
                                   input parameter.
    """

    label: str  # Label of the workflow step associated with the input parameter.
    parameter_value: InvocationInputParameterParameterValue  # Value of the input parameter.
    workflow_step_id: str  # The encoded ID of the workflow step associated with the input parameter.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "label": "label",
            "parameter_value": "parameter_value",
            "workflow_step_id": "workflow_step_id",
        }
        key_transform_with_dump = {
            "label": "label",
            "parameter_value": "parameter_value",
            "workflow_step_id": "workflow_step_id",
        }
