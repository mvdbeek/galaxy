from dataclasses import dataclass

from .input_parameter_step_annotation import InputParameterStepAnnotation
from .input_parameter_step_input_steps import InputParameterStepInputSteps
from .input_parameter_step_tool_id import InputParameterStepToolId
from .input_parameter_step_tool_inputs import InputParameterStepToolInputs
from .input_parameter_step_tool_uuid import InputParameterStepToolUuid
from .input_parameter_step_tool_version import InputParameterStepToolVersion
from .input_parameter_step_when import InputParameterStepWhen

__all__ = ["InputParameterStep"]


@dataclass
class InputParameterStep:
    """
    InputParameterStep dataclass

    Args:
        annotation (InputParameterStepAnnotation)
                                 : An annotation to provide details or to help understand
                                   the purpose and usage of this item.
        id_ (int)                : The identifier of the step. It matches the index order of
                                   the step inside the workflow. (maps from 'id')
        input_steps (InputParameterStepInputSteps)
                                 : A dictionary containing information about the inputs
                                   connected to this workflow step.
        type_ (str)              : Maps from 'type'
        when (InputParameterStepWhen)
                                 :
        tool_id (InputParameterStepToolId | None)
                                 : The unique name of the tool associated with this step.
        tool_inputs (InputParameterStepToolInputs | None)
                                 : TODO
        tool_uuid (InputParameterStepToolUuid | None)
                                 : The universal unique identifier of the tool associated
                                   with this step. Takes precedence over tool_id if set.
        tool_version (InputParameterStepToolVersion | None)
                                 : The version of the tool associated with this step.
    """

    annotation: InputParameterStepAnnotation  # An annotation to provide details or to help understand the purpose and usage of this item.
    id_: int  # The identifier of the step. It matches the index order of the step inside the workflow. (maps from 'id')
    input_steps: InputParameterStepInputSteps  # A dictionary containing information about the inputs connected to this workflow step.
    type_: str  # Maps from 'type'
    when: InputParameterStepWhen
    tool_id: InputParameterStepToolId | None = None  # The unique name of the tool associated with this step.
    tool_inputs: InputParameterStepToolInputs | None = None  # TODO
    tool_uuid: InputParameterStepToolUuid | None = (
        None  # The universal unique identifier of the tool associated with this step. Takes precedence over tool_id if set.
    )
    tool_version: InputParameterStepToolVersion | None = None  # The version of the tool associated with this step.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "annotation": "annotation",
            "id": "id_",
            "input_steps": "input_steps",
            "tool_id": "tool_id",
            "tool_inputs": "tool_inputs",
            "tool_uuid": "tool_uuid",
            "tool_version": "tool_version",
            "type": "type_",
            "when": "when",
        }
        key_transform_with_dump = {
            "annotation": "annotation",
            "id_": "id",
            "input_steps": "input_steps",
            "tool_id": "tool_id",
            "tool_inputs": "tool_inputs",
            "tool_uuid": "tool_uuid",
            "tool_version": "tool_version",
            "type_": "type",
            "when": "when",
        }
