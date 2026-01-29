from dataclasses import dataclass, field

from .invocation_step_action import InvocationStepAction
from .invocation_step_implicit_collection_jobs_id import InvocationStepImplicitCollectionJobsId
from .invocation_step_job_id import InvocationStepJobId
from .invocation_step_output_collections import InvocationStepOutputCollections
from .invocation_step_outputs import InvocationStepOutputs
from .invocation_step_state import InvocationStepState
from .invocation_step_subworkflow_invocation_id import InvocationStepSubworkflowInvocationId
from .invocation_step_update_time import InvocationStepUpdateTime
from .invocation_step_workflow_step_label import InvocationStepWorkflowStepLabel
from .invocation_step_workflow_step_uuid import InvocationStepWorkflowStepUuid
from .job_base_model import JobBaseModel

__all__ = ["InvocationStep"]


@dataclass
class InvocationStep:
    """
    Information about workflow invocation step

    Args:
        action (InvocationStepAction)
                                 : Whether to take action on the invocation step.
        id_ (str)                : Maps from 'id'
        model_class (str)        : The name of the database model class.
        order_index (int)        : The index of the workflow step in the workflow.
        update_time (InvocationStepUpdateTime)
                                 : The last time and date this item was updated.
        workflow_step_id (str)   : The encoded ID of the workflow step associated with this
                                   workflow invocation step.
        implicit_collection_jobs_id (InvocationStepImplicitCollectionJobsId | None)
                                 : The implicit collection job ID associated with the
                                   workflow invocation step.
        job_id (InvocationStepJobId | None)
                                 : The encoded ID of the job associated with this workflow
                                   invocation step.
        jobs (List[JobBaseModel] | None)
                                 : Jobs associated with the workflow invocation step.
        output_collections (InvocationStepOutputCollections | None)
                                 : The dataset collection outputs of the workflow invocation
                                   step.
        outputs (InvocationStepOutputs | None)
                                 : The outputs of the workflow invocation step.
        state (InvocationStepState | None)
                                 : Describes where in the scheduling process the workflow
                                   invocation step is.
        subworkflow_invocation_id (InvocationStepSubworkflowInvocationId | None)
                                 : The encoded ID of the subworkflow invocation.
        workflow_step_label (InvocationStepWorkflowStepLabel | None)
                                 : The label of the workflow step
        workflow_step_uuid (InvocationStepWorkflowStepUuid | None)
                                 : Universal unique identifier of the workflow step.
    """

    action: InvocationStepAction  # Whether to take action on the invocation step.
    id_: str  # Maps from 'id'
    model_class: str  # The name of the database model class.
    order_index: int  # The index of the workflow step in the workflow.
    update_time: InvocationStepUpdateTime  # The last time and date this item was updated.
    workflow_step_id: str  # The encoded ID of the workflow step associated with this workflow invocation step.
    implicit_collection_jobs_id: InvocationStepImplicitCollectionJobsId | None = (
        None  # The implicit collection job ID associated with the workflow invocation step.
    )
    job_id: InvocationStepJobId | None = (
        None  # The encoded ID of the job associated with this workflow invocation step.
    )
    jobs: list[JobBaseModel] | None = field(default_factory=list)  # Jobs associated with the workflow invocation step.
    output_collections: InvocationStepOutputCollections | None = (
        None  # The dataset collection outputs of the workflow invocation step.
    )
    outputs: InvocationStepOutputs | None = None  # The outputs of the workflow invocation step.
    state: InvocationStepState | None = (
        None  # Describes where in the scheduling process the workflow invocation step is.
    )
    subworkflow_invocation_id: InvocationStepSubworkflowInvocationId | None = (
        None  # The encoded ID of the subworkflow invocation.
    )
    workflow_step_label: InvocationStepWorkflowStepLabel | None = None  # The label of the workflow step
    workflow_step_uuid: InvocationStepWorkflowStepUuid | None = (
        None  # Universal unique identifier of the workflow step.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "action": "action",
            "id": "id_",
            "implicit_collection_jobs_id": "implicit_collection_jobs_id",
            "job_id": "job_id",
            "jobs": "jobs",
            "model_class": "model_class",
            "order_index": "order_index",
            "output_collections": "output_collections",
            "outputs": "outputs",
            "state": "state",
            "subworkflow_invocation_id": "subworkflow_invocation_id",
            "update_time": "update_time",
            "workflow_step_id": "workflow_step_id",
            "workflow_step_label": "workflow_step_label",
            "workflow_step_uuid": "workflow_step_uuid",
        }
        key_transform_with_dump = {
            "action": "action",
            "id_": "id",
            "implicit_collection_jobs_id": "implicit_collection_jobs_id",
            "job_id": "job_id",
            "jobs": "jobs",
            "model_class": "model_class",
            "order_index": "order_index",
            "output_collections": "output_collections",
            "outputs": "outputs",
            "state": "state",
            "subworkflow_invocation_id": "subworkflow_invocation_id",
            "update_time": "update_time",
            "workflow_step_id": "workflow_step_id",
            "workflow_step_label": "workflow_step_label",
            "workflow_step_uuid": "workflow_step_uuid",
        }
