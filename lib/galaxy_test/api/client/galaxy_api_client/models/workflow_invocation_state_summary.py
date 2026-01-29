from dataclasses import dataclass

from .anonymous_array_item_111_model_enum import AnonymousArrayItem111ModelEnum
from .dataset_collection_populated_state import DatasetCollectionPopulatedState
from .workflow_invocation_state_summary_states import WorkflowInvocationStateSummaryStates

__all__ = ["WorkflowInvocationStateSummary"]


@dataclass
class WorkflowInvocationStateSummary:
    """
    WorkflowInvocationStateSummary dataclass

    Args:
        id_ (str)                : Maps from 'id'
        model_ (AnonymousArrayItem111ModelEnum)
                                 : The name of the database model class. (maps from 'model')
        populated_state (DatasetCollectionPopulatedState)
                                 :
        states (WorkflowInvocationStateSummaryStates | None)
                                 : A dictionary of job states and the number of jobs in that
                                   state.
    """

    id_: str  # Maps from 'id'
    model_: AnonymousArrayItem111ModelEnum  # The name of the database model class. (maps from 'model')
    populated_state: DatasetCollectionPopulatedState
    states: WorkflowInvocationStateSummaryStates | None = (
        None  # A dictionary of job states and the number of jobs in that state.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "id": "id_",
            "model": "model_",
            "populated_state": "populated_state",
            "states": "states",
        }
        key_transform_with_dump = {
            "id_": "id",
            "model_": "model",
            "populated_state": "populated_state",
            "states": "states",
        }
