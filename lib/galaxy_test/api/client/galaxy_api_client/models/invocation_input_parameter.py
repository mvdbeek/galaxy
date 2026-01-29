from dataclasses import dataclass

from .parameter_value import ParameterValue

__all__ = ["InvocationInputParameter"]


@dataclass
class InvocationInputParameter:
    """
    InvocationInputParameter dataclass.

    Args:
        label (str)              : Label of the workflow step associated with the input
                                   parameter.
        parameter_value (ParameterValue)
                                 : Value of the input parameter.
        workflow_step_id (str)   : The encoded ID of the workflow step associated with the
                                   input parameter.
    """

    label: str  # Label of the workflow step associated with the input parameter.
    parameter_value: ParameterValue  # Value of the input parameter.
    workflow_step_id: str  # The encoded ID of the workflow step associated with the input parameter.
