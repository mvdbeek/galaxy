from dataclasses import dataclass

from .pause_step_annotation import PauseStepAnnotation
from .pause_step_input_steps import PauseStepInputSteps
from .pause_step_tool_id import PauseStepToolId
from .pause_step_tool_inputs import PauseStepToolInputs
from .pause_step_tool_uuid import PauseStepToolUuid
from .pause_step_tool_version import PauseStepToolVersion
from .pause_step_when import PauseStepWhen

__all__ = ["PauseStep"]


@dataclass
class PauseStep:
    """
    PauseStep dataclass

    Args:
        annotation (PauseStepAnnotation)
                                 : An annotation to provide details or to help understand
                                   the purpose and usage of this item.
        id_ (int)                : The identifier of the step. It matches the index order of
                                   the step inside the workflow. (maps from 'id')
        input_steps (PauseStepInputSteps)
                                 : A dictionary containing information about the inputs
                                   connected to this workflow step.
        type_ (str)              : Maps from 'type'
        when (PauseStepWhen)     :
        tool_id (PauseStepToolId | None)
                                 : The unique name of the tool associated with this step.
        tool_inputs (PauseStepToolInputs | None)
                                 : TODO
        tool_uuid (PauseStepToolUuid | None)
                                 : The universal unique identifier of the tool associated
                                   with this step. Takes precedence over tool_id if set.
        tool_version (PauseStepToolVersion | None)
                                 : The version of the tool associated with this step.
    """

    annotation: PauseStepAnnotation  # An annotation to provide details or to help understand the purpose and usage of this item.
    id_: int  # The identifier of the step. It matches the index order of the step inside the workflow. (maps from 'id')
    input_steps: (
        PauseStepInputSteps  # A dictionary containing information about the inputs connected to this workflow step.
    )
    type_: str  # Maps from 'type'
    when: PauseStepWhen
    tool_id: PauseStepToolId | None = None  # The unique name of the tool associated with this step.
    tool_inputs: PauseStepToolInputs | None = None  # TODO
    tool_uuid: PauseStepToolUuid | None = (
        None  # The universal unique identifier of the tool associated with this step. Takes precedence over tool_id if set.
    )
    tool_version: PauseStepToolVersion | None = None  # The version of the tool associated with this step.

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
