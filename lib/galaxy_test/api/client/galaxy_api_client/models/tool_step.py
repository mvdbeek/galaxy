from dataclasses import dataclass

from .annotation import Annotation
from .tool_id import ToolId
from .tool_inputs import ToolInputs
from .tool_step_input_steps import ToolStepInputSteps
from .tool_uuid import ToolUuid
from .tool_version import ToolVersion
from .when import When

__all__ = ["ToolStep"]


@dataclass
class ToolStep:
    """
    ToolStep dataclass.

    Args:
        annotation (Optional[Annotation])
                                 : The annotation of this Visualization.
        id_ (int)                : The identifier of the step. It matches the index order of
                                   the step inside the workflow.
        input_steps (ToolStepInputSteps)
                                 : A dictionary containing information about the inputs
                                   connected to this workflow step.
        type_ (str)              :
        when (Optional[When])    :
        tool_id (Optional[ToolId]): The unique name of the tool associated with this step.
        tool_inputs (Optional[ToolInputs])
                                 : TODO
        tool_uuid (Optional[ToolUuid])
                                 : The universal unique identifier of the tool associated
                                   with this step. Takes precedence over tool_id if set.
        tool_version (Optional[ToolVersion])
                                 : The version of the tool associated with this step.
    """

    annotation: Annotation | None  # The annotation of this Visualization.
    id_: int  # The identifier of the step. It matches the index order of the step inside the workflow.
    input_steps: (
        ToolStepInputSteps  # A dictionary containing information about the inputs connected to this workflow step.
    )
    type_: str
    when: When | None
    tool_id: ToolId | None = None  # The unique name of the tool associated with this step.
    tool_inputs: ToolInputs | None = None  # TODO
    tool_uuid: ToolUuid | None = (
        None  # The universal unique identifier of the tool associated with this step. Takes precedence over tool_id if set.
    )
    tool_version: ToolVersion | None = None  # The version of the tool associated with this step.
