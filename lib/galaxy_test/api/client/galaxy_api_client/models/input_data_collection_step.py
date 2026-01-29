from dataclasses import dataclass

from .input_data_collection_step_annotation import InputDataCollectionStepAnnotation
from .input_data_collection_step_input_steps import InputDataCollectionStepInputSteps
from .input_data_collection_step_tool_id import InputDataCollectionStepToolId
from .input_data_collection_step_tool_inputs import InputDataCollectionStepToolInputs
from .input_data_collection_step_tool_uuid import InputDataCollectionStepToolUuid
from .input_data_collection_step_tool_version import InputDataCollectionStepToolVersion
from .input_data_collection_step_when import InputDataCollectionStepWhen

__all__ = ["InputDataCollectionStep"]


@dataclass
class InputDataCollectionStep:
    """
    InputDataCollectionStep dataclass

    Args:
        annotation (InputDataCollectionStepAnnotation)
                                 : An annotation to provide details or to help understand
                                   the purpose and usage of this item.
        id_ (int)                : The identifier of the step. It matches the index order of
                                   the step inside the workflow. (maps from 'id')
        input_steps (InputDataCollectionStepInputSteps)
                                 : A dictionary containing information about the inputs
                                   connected to this workflow step.
        type_ (str)              : Maps from 'type'
        when (InputDataCollectionStepWhen)
                                 :
        tool_id (InputDataCollectionStepToolId | None)
                                 : The unique name of the tool associated with this step.
        tool_inputs (InputDataCollectionStepToolInputs | None)
                                 : TODO
        tool_uuid (InputDataCollectionStepToolUuid | None)
                                 : The universal unique identifier of the tool associated
                                   with this step. Takes precedence over tool_id if set.
        tool_version (InputDataCollectionStepToolVersion | None)
                                 : The version of the tool associated with this step.
    """

    annotation: InputDataCollectionStepAnnotation  # An annotation to provide details or to help understand the purpose and usage of this item.
    id_: int  # The identifier of the step. It matches the index order of the step inside the workflow. (maps from 'id')
    input_steps: InputDataCollectionStepInputSteps  # A dictionary containing information about the inputs connected to this workflow step.
    type_: str  # Maps from 'type'
    when: InputDataCollectionStepWhen
    tool_id: InputDataCollectionStepToolId | None = None  # The unique name of the tool associated with this step.
    tool_inputs: InputDataCollectionStepToolInputs | None = None  # TODO
    tool_uuid: InputDataCollectionStepToolUuid | None = (
        None  # The universal unique identifier of the tool associated with this step. Takes precedence over tool_id if set.
    )
    tool_version: InputDataCollectionStepToolVersion | None = None  # The version of the tool associated with this step.

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
