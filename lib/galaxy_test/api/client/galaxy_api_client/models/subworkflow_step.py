from dataclasses import dataclass

from .subworkflow_step_annotation import SubworkflowStepAnnotation
from .subworkflow_step_input_steps import SubworkflowStepInputSteps
from .subworkflow_step_tool_id import SubworkflowStepToolId
from .subworkflow_step_tool_inputs import SubworkflowStepToolInputs
from .subworkflow_step_tool_uuid import SubworkflowStepToolUuid
from .subworkflow_step_tool_version import SubworkflowStepToolVersion
from .subworkflow_step_when import SubworkflowStepWhen

__all__ = ["SubworkflowStep"]


@dataclass
class SubworkflowStep:
    """
    SubworkflowStep dataclass

    Args:
        annotation (SubworkflowStepAnnotation)
                                 : An annotation to provide details or to help understand
                                   the purpose and usage of this item.
        id_ (int)                : The identifier of the step. It matches the index order of
                                   the step inside the workflow. (maps from 'id')
        input_steps (SubworkflowStepInputSteps)
                                 : A dictionary containing information about the inputs
                                   connected to this workflow step.
        type_ (str)              : Maps from 'type'
        when (SubworkflowStepWhen):
        workflow_id (str)        : The encoded ID of the workflow that will be run on this
                                   step.
        tool_id (SubworkflowStepToolId | None)
                                 : The unique name of the tool associated with this step.
        tool_inputs (SubworkflowStepToolInputs | None)
                                 : TODO
        tool_uuid (SubworkflowStepToolUuid | None)
                                 : The universal unique identifier of the tool associated
                                   with this step. Takes precedence over tool_id if set.
        tool_version (SubworkflowStepToolVersion | None)
                                 : The version of the tool associated with this step.
    """

    annotation: SubworkflowStepAnnotation  # An annotation to provide details or to help understand the purpose and usage of this item.
    id_: int  # The identifier of the step. It matches the index order of the step inside the workflow. (maps from 'id')
    input_steps: SubworkflowStepInputSteps  # A dictionary containing information about the inputs connected to this workflow step.
    type_: str  # Maps from 'type'
    when: SubworkflowStepWhen
    workflow_id: str  # The encoded ID of the workflow that will be run on this step.
    tool_id: SubworkflowStepToolId | None = None  # The unique name of the tool associated with this step.
    tool_inputs: SubworkflowStepToolInputs | None = None  # TODO
    tool_uuid: SubworkflowStepToolUuid | None = (
        None  # The universal unique identifier of the tool associated with this step. Takes precedence over tool_id if set.
    )
    tool_version: SubworkflowStepToolVersion | None = None  # The version of the tool associated with this step.

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
            "workflow_id": "workflow_id",
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
            "workflow_id": "workflow_id",
        }
