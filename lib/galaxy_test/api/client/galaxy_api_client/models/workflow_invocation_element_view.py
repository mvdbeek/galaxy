from dataclasses import dataclass
from datetime import datetime

from .inputs import Inputs
from .invocation_message_response_union import InvocationMessageResponseUnion
from .invocation_state import InvocationState
from .invocation_step import InvocationStep
from .landing_uuid import LandingUuid
from .outputs import Outputs
from .uuid_ import Uuid_
from .workflow_invocation_element_view_input_step_parameters import WorkflowInvocationElementViewInputStepParameters
from .workflow_invocation_element_view_output_collections import WorkflowInvocationElementViewOutputCollections
from .workflow_invocation_element_view_output_values import WorkflowInvocationElementViewOutputValues

__all__ = ["WorkflowInvocationElementView"]


@dataclass
class WorkflowInvocationElementView:
    """
    WorkflowInvocationElementView dataclass.

    Args:
        create_time (datetime)   : The time and date this item was created.
        history_id (str)         : The encoded ID of the history associated with the
                                   invocation.
        id_ (str)                : The encoded ID of the workflow invocation.
        input_step_parameters (WorkflowInvocationElementViewInputStepParameters)
                                 : Input step parameters of the workflow invocation.
        inputs (Inputs)          : Input datasets/dataset collections of the workflow
                                   invocation.
        messages (List[InvocationMessageResponseUnion])
                                 : A list of messages about why the invocation did not
                                   succeed.
        model_class (str)        : The name of the database model class.
        output_collections (WorkflowInvocationElementViewOutputCollections)
                                 : Output dataset collections of the workflow invocation.
        output_values (WorkflowInvocationElementViewOutputValues)
                                 : Output values of the workflow invocation.
        outputs (Outputs)        : Output datasets of the workflow invocation.
        state (InvocationState)  :
        steps (List[InvocationStep])
                                 : Steps of the workflow invocation.
        update_time (datetime)   : The last time and date this item was updated.
        workflow_id (str)        : The encoded Workflow ID associated with the invocation.
        landing_uuid (Optional[LandingUuid])
                                 : The UUID of the workflow landing request associated with
                                   this invocation.
        uuid_ (Optional[Uuid_])  : Universal unique identifier of the workflow invocation.
    """

    create_time: datetime  # The time and date this item was created.
    history_id: str  # The encoded ID of the history associated with the invocation.
    id_: str  # The encoded ID of the workflow invocation.
    input_step_parameters: (
        WorkflowInvocationElementViewInputStepParameters  # Input step parameters of the workflow invocation.
    )
    inputs: Inputs  # Input datasets/dataset collections of the workflow invocation.
    messages: list[InvocationMessageResponseUnion]  # A list of messages about why the invocation did not succeed.
    model_class: str  # The name of the database model class.
    output_collections: (
        WorkflowInvocationElementViewOutputCollections  # Output dataset collections of the workflow invocation.
    )
    output_values: WorkflowInvocationElementViewOutputValues  # Output values of the workflow invocation.
    outputs: Outputs  # Output datasets of the workflow invocation.
    state: InvocationState
    steps: list[InvocationStep]  # Steps of the workflow invocation.
    update_time: datetime  # The last time and date this item was updated.
    workflow_id: str  # The encoded Workflow ID associated with the invocation.
    landing_uuid: LandingUuid | None = None  # The UUID of the workflow landing request associated with this invocation.
    uuid_: Uuid_ | None = None  # Universal unique identifier of the workflow invocation.
