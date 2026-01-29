from dataclasses import dataclass

from .tool_step_annotation import ToolStepAnnotation
from .tool_step_input_steps import ToolStepInputSteps
from .tool_step_tool_id import ToolStepToolId
from .tool_step_tool_inputs import ToolStepToolInputs
from .tool_step_tool_uuid import ToolStepToolUuid
from .tool_step_tool_version import ToolStepToolVersion
from .tool_step_when import ToolStepWhen

__all__ = ["ToolStep"]


@dataclass
class ToolStep:
    """
    ToolStep dataclass

    Args:
        annotation (ToolStepAnnotation)
                                 : An annotation to provide details or to help understand
                                   the purpose and usage of this item.
        id_ (int)                : The identifier of the step. It matches the index order of
                                   the step inside the workflow. (maps from 'id')
        input_steps (ToolStepInputSteps)
                                 : A dictionary containing information about the inputs
                                   connected to this workflow step.
        type_ (str)              : Maps from 'type'
        when (ToolStepWhen)      :
        tool_id (ToolStepToolId | None)
                                 : The unique name of the tool associated with this step.
        tool_inputs (ToolStepToolInputs | None)
                                 : TODO
        tool_uuid (ToolStepToolUuid | None)
                                 : The universal unique identifier of the tool associated
                                   with this step. Takes precedence over tool_id if set.
        tool_version (ToolStepToolVersion | None)
                                 : The version of the tool associated with this step.
    """

    annotation: (
        ToolStepAnnotation  # An annotation to provide details or to help understand the purpose and usage of this item.
    )
    id_: int  # The identifier of the step. It matches the index order of the step inside the workflow. (maps from 'id')
    input_steps: (
        ToolStepInputSteps  # A dictionary containing information about the inputs connected to this workflow step.
    )
    type_: str  # Maps from 'type'
    when: ToolStepWhen
    tool_id: ToolStepToolId | None = None  # The unique name of the tool associated with this step.
    tool_inputs: ToolStepToolInputs | None = None  # TODO
    tool_uuid: ToolStepToolUuid | None = (
        None  # The universal unique identifier of the tool associated with this step. Takes precedence over tool_id if set.
    )
    tool_version: ToolStepToolVersion | None = None  # The version of the tool associated with this step.

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
