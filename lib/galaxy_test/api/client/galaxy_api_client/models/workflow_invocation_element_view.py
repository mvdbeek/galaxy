from dataclasses import dataclass
from datetime import datetime

from .invocation_message_response_union import InvocationMessageResponseUnion
from .invocation_state import InvocationState
from .invocation_step import InvocationStep
from .uuid__10 import Uuid10
from .workflow_invocation_element_view_input_step_parameters import WorkflowInvocationElementViewInputStepParameters
from .workflow_invocation_element_view_inputs import WorkflowInvocationElementViewInputs
from .workflow_invocation_element_view_landing_uuid import WorkflowInvocationElementViewLandingUuid
from .workflow_invocation_element_view_output_collections import WorkflowInvocationElementViewOutputCollections
from .workflow_invocation_element_view_output_values import WorkflowInvocationElementViewOutputValues
from .workflow_invocation_element_view_outputs import WorkflowInvocationElementViewOutputs

__all__ = ["WorkflowInvocationElementView"]


@dataclass
class WorkflowInvocationElementView:
    """
    WorkflowInvocationElementView dataclass

    Args:
        create_time (datetime)   : The time and date this item was created.
        history_id (str)         : The encoded ID of the history associated with the
                                   invocation.
        id_ (str)                : The encoded ID of the workflow invocation. (maps from
                                   'id')
        input_step_parameters (WorkflowInvocationElementViewInputStepParameters)
                                 : Input step parameters of the workflow invocation.
        inputs (WorkflowInvocationElementViewInputs)
                                 : Input datasets/dataset collections of the workflow
                                   invocation.
        messages (List[InvocationMessageResponseUnion])
                                 : A list of messages about why the invocation did not
                                   succeed.
        model_class (str)        : The name of the database model class.
        output_collections (WorkflowInvocationElementViewOutputCollections)
                                 : Output dataset collections of the workflow invocation.
        output_values (WorkflowInvocationElementViewOutputValues)
                                 : Output values of the workflow invocation.
        outputs (WorkflowInvocationElementViewOutputs)
                                 : Output datasets of the workflow invocation.
        state (InvocationState)  :
        steps (List[InvocationStep])
                                 : Steps of the workflow invocation.
        update_time (datetime)   : The last time and date this item was updated.
        workflow_id (str)        : The encoded Workflow ID associated with the invocation.
        landing_uuid (WorkflowInvocationElementViewLandingUuid | None)
                                 : The UUID of the workflow landing request associated with
                                   this invocation.
        uuid_ (Uuid10 | None)    : Universal unique identifier of the workflow invocation.
                                   (maps from 'uuid')
    """

    create_time: datetime  # The time and date this item was created.
    history_id: str  # The encoded ID of the history associated with the invocation.
    id_: str  # The encoded ID of the workflow invocation. (maps from 'id')
    input_step_parameters: (
        WorkflowInvocationElementViewInputStepParameters  # Input step parameters of the workflow invocation.
    )
    inputs: WorkflowInvocationElementViewInputs  # Input datasets/dataset collections of the workflow invocation.
    messages: list[InvocationMessageResponseUnion]  # A list of messages about why the invocation did not succeed.
    model_class: str  # The name of the database model class.
    output_collections: (
        WorkflowInvocationElementViewOutputCollections  # Output dataset collections of the workflow invocation.
    )
    output_values: WorkflowInvocationElementViewOutputValues  # Output values of the workflow invocation.
    outputs: WorkflowInvocationElementViewOutputs  # Output datasets of the workflow invocation.
    state: InvocationState
    steps: list[InvocationStep]  # Steps of the workflow invocation.
    update_time: datetime  # The last time and date this item was updated.
    workflow_id: str  # The encoded Workflow ID associated with the invocation.
    landing_uuid: WorkflowInvocationElementViewLandingUuid | None = (
        None  # The UUID of the workflow landing request associated with this invocation.
    )
    uuid_: Uuid10 | None = None  # Universal unique identifier of the workflow invocation. (maps from 'uuid')

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "create_time": "create_time",
            "history_id": "history_id",
            "id": "id_",
            "input_step_parameters": "input_step_parameters",
            "inputs": "inputs",
            "landing_uuid": "landing_uuid",
            "messages": "messages",
            "model_class": "model_class",
            "output_collections": "output_collections",
            "output_values": "output_values",
            "outputs": "outputs",
            "state": "state",
            "steps": "steps",
            "update_time": "update_time",
            "uuid": "uuid_",
            "workflow_id": "workflow_id",
        }
        key_transform_with_dump = {
            "create_time": "create_time",
            "history_id": "history_id",
            "id_": "id",
            "input_step_parameters": "input_step_parameters",
            "inputs": "inputs",
            "landing_uuid": "landing_uuid",
            "messages": "messages",
            "model_class": "model_class",
            "output_collections": "output_collections",
            "output_values": "output_values",
            "outputs": "outputs",
            "state": "state",
            "steps": "steps",
            "update_time": "update_time",
            "uuid_": "uuid",
            "workflow_id": "workflow_id",
        }
