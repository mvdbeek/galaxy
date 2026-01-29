from dataclasses import dataclass

from .input_data_step_annotation import InputDataStepAnnotation
from .input_data_step_input_steps import InputDataStepInputSteps
from .input_data_step_tool_id import InputDataStepToolId
from .input_data_step_tool_inputs import InputDataStepToolInputs
from .input_data_step_tool_uuid import InputDataStepToolUuid
from .input_data_step_tool_version import InputDataStepToolVersion
from .input_data_step_when import InputDataStepWhen

__all__ = ["InputDataStep"]


@dataclass
class InputDataStep:
    """
    InputDataStep dataclass

    Args:
        annotation (InputDataStepAnnotation)
                                 : An annotation to provide details or to help understand
                                   the purpose and usage of this item.
        id_ (int)                : The identifier of the step. It matches the index order of
                                   the step inside the workflow. (maps from 'id')
        input_steps (InputDataStepInputSteps)
                                 : A dictionary containing information about the inputs
                                   connected to this workflow step.
        type_ (str)              : Maps from 'type'
        when (InputDataStepWhen) :
        tool_id (InputDataStepToolId | None)
                                 : The unique name of the tool associated with this step.
        tool_inputs (InputDataStepToolInputs | None)
                                 : TODO
        tool_uuid (InputDataStepToolUuid | None)
                                 : The universal unique identifier of the tool associated
                                   with this step. Takes precedence over tool_id if set.
        tool_version (InputDataStepToolVersion | None)
                                 : The version of the tool associated with this step.
    """

    annotation: InputDataStepAnnotation  # An annotation to provide details or to help understand the purpose and usage of this item.
    id_: int  # The identifier of the step. It matches the index order of the step inside the workflow. (maps from 'id')
    input_steps: (
        InputDataStepInputSteps  # A dictionary containing information about the inputs connected to this workflow step.
    )
    type_: str  # Maps from 'type'
    when: InputDataStepWhen
    tool_id: InputDataStepToolId | None = None  # The unique name of the tool associated with this step.
    tool_inputs: InputDataStepToolInputs | None = None  # TODO
    tool_uuid: InputDataStepToolUuid | None = (
        None  # The universal unique identifier of the tool associated with this step. Takes precedence over tool_id if set.
    )
    tool_version: InputDataStepToolVersion | None = None  # The version of the tool associated with this step.

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
