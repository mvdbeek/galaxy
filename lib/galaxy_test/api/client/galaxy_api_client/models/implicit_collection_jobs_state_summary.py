from dataclasses import dataclass

from .dataset_collection_populated_state import DatasetCollectionPopulatedState
from .implicit_collection_jobs_state_summary_states import ImplicitCollectionJobsStateSummaryStates

__all__ = ["ImplicitCollectionJobsStateSummary"]


@dataclass
class ImplicitCollectionJobsStateSummary:
    """
    ImplicitCollectionJobsStateSummary dataclass.

    Args:
        id_ (str)                :
        model_ (str)             : The name of the database model class.
        populated_state (DatasetCollectionPopulatedState)
                                 :
        states (Optional[ImplicitCollectionJobsStateSummaryStates])
                                 : A dictionary of job states and the number of jobs in that
                                   state.
    """

    id_: str
    model_: str  # The name of the database model class.
    populated_state: DatasetCollectionPopulatedState
    states: ImplicitCollectionJobsStateSummaryStates | None = (
        None  # A dictionary of job states and the number of jobs in that state.
    )
