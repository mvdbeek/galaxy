from dataclasses import dataclass

from .dataset_collection_populated_state import DatasetCollectionPopulatedState
from .workflow_invocation_state_summary_states import WorkflowInvocationStateSummaryStates

__all__ = ["WorkflowInvocationStateSummary"]


@dataclass
class WorkflowInvocationStateSummary:
    """
    WorkflowInvocationStateSummary dataclass.

    Args:
        id_ (str)                :
        model_ (str)             : The name of the database model class.
        populated_state (DatasetCollectionPopulatedState)
                                 :
        states (Optional[WorkflowInvocationStateSummaryStates])
                                 : A dictionary of job states and the number of jobs in that
                                   state.
    """

    id_: str
    model_: str  # The name of the database model class.
    populated_state: DatasetCollectionPopulatedState
    states: WorkflowInvocationStateSummaryStates | None = (
        None  # A dictionary of job states and the number of jobs in that state.
    )
