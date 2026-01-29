from dataclasses import dataclass

from .anonymous_array_item_111_model_enum import AnonymousArrayItem111ModelEnum
from .dataset_collection_populated_state import DatasetCollectionPopulatedState
from .job_state_summary_states import JobStateSummaryStates

__all__ = ["JobStateSummary"]


@dataclass
class JobStateSummary:
    """
    JobStateSummary dataclass

    Args:
        id_ (str)                : Maps from 'id'
        model_ (AnonymousArrayItem111ModelEnum)
                                 : The name of the database model class. (maps from 'model')
        populated_state (DatasetCollectionPopulatedState)
                                 :
        states (JobStateSummaryStates | None)
                                 : A dictionary of job states and the number of jobs in that
                                   state.
    """

    id_: str  # Maps from 'id'
    model_: AnonymousArrayItem111ModelEnum  # The name of the database model class. (maps from 'model')
    populated_state: DatasetCollectionPopulatedState
    states: JobStateSummaryStates | None = None  # A dictionary of job states and the number of jobs in that state.

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
