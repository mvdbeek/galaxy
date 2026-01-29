from dataclasses import dataclass, field

from .action import Action
from .implicit_collection_jobs_id import ImplicitCollectionJobsId
from .invocation_step_output_collections import InvocationStepOutputCollections
from .job_base_model import JobBaseModel
from .job_id import JobId
from .outputs import Outputs
from .state import State
from .subworkflow_invocation_id import SubworkflowInvocationId
from .update_time import UpdateTime
from .workflow_step_label import WorkflowStepLabel
from .workflow_step_uuid import WorkflowStepUuid

__all__ = ["InvocationStep"]


@dataclass
class InvocationStep:
    """
    Information about workflow invocation step

    Args:
        action (Optional[Action]): Indicates what action should be performed on the dataset.
        id_ (str)                :
        model_class (str)        : The name of the database model class.
        order_index (int)        : The index of the workflow step in the workflow.
        update_time (Optional[UpdateTime])
                                 : The last time and date this item was updated.
        workflow_step_id (str)   : The encoded ID of the workflow step associated with this
                                   workflow invocation step.
        implicit_collection_jobs_id (Optional[ImplicitCollectionJobsId])
                                 : The implicit collection job ID associated with the
                                   workflow invocation step.
        job_id (Optional[JobId]) : The encoded ID of the job associated with this workflow
                                   invocation step.
        jobs (Optional[List[JobBaseModel]])
                                 : Jobs associated with the workflow invocation step.
        output_collections (Optional[InvocationStepOutputCollections])
                                 : The dataset collection outputs of the workflow invocation
                                   step.
        outputs (Optional[Outputs])
                                 : The outputs of the workflow invocation step.
        state (Optional[State])  : Current state of the job.
        subworkflow_invocation_id (Optional[SubworkflowInvocationId])
                                 : The encoded ID of the subworkflow invocation.
        workflow_step_label (Optional[WorkflowStepLabel])
                                 : The label of the workflow step
        workflow_step_uuid (Optional[WorkflowStepUuid])
                                 : Universal unique identifier of the workflow step.
    """

    action: Action | None  # Indicates what action should be performed on the dataset.
    id_: str
    model_class: str  # The name of the database model class.
    order_index: int  # The index of the workflow step in the workflow.
    update_time: UpdateTime | None  # The last time and date this item was updated.
    workflow_step_id: str  # The encoded ID of the workflow step associated with this workflow invocation step.
    implicit_collection_jobs_id: ImplicitCollectionJobsId | None = (
        None  # The implicit collection job ID associated with the workflow invocation step.
    )
    job_id: JobId | None = None  # The encoded ID of the job associated with this workflow invocation step.
    jobs: list[JobBaseModel] | None = field(default_factory=list)  # Jobs associated with the workflow invocation step.
    output_collections: InvocationStepOutputCollections | None = (
        None  # The dataset collection outputs of the workflow invocation step.
    )
    outputs: Outputs | None = None  # The outputs of the workflow invocation step.
    state: State | None = None  # Current state of the job.
    subworkflow_invocation_id: SubworkflowInvocationId | None = None  # The encoded ID of the subworkflow invocation.
    workflow_step_label: WorkflowStepLabel | None = None  # The label of the workflow step
    workflow_step_uuid: WorkflowStepUuid | None = None  # Universal unique identifier of the workflow step.
