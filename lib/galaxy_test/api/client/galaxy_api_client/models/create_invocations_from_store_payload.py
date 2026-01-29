from dataclasses import dataclass

from .model_store_format import ModelStoreFormat
from .store_content_uri import StoreContentUri
from .store_dict import StoreDict
from .view import View

__all__ = ["CreateInvocationsFromStorePayload"]


@dataclass
class CreateInvocationsFromStorePayload:
    """
    CreateInvocationsFromStorePayload dataclass.

    Args:
        history_id (str)         : The ID of the history associated with the invocations.
        legacy_job_state (Optional[bool])
                                 : Populate the invocation step state with the job state
                                   instead of the invocation step state.         This will
                                   also produce one step per job in mapping jobs to mimic
                                   the older behavior with respect to collections.
                                   Partially scheduled steps may provide incomplete
                                   information and the listed steps outputs         are not
                                   the mapped over step outputs but the individual job
                                   outputs.
        model_store_format (Optional[ModelStoreFormat])
                                 :
        step_details (Optional[bool])
                                 : Include details for individual invocation steps and
                                   populate a steps attribute in the resulting dictionary
        store_content_uri (Optional[StoreContentUri])
                                 :
        store_dict (Optional[StoreDict])
                                 :
        view (Optional[View])    : The name of the view used to serialize this item. This
                                   will return a predefined set of attributes of the item.
    """

    history_id: str  # The ID of the history associated with the invocations.
    legacy_job_state: bool | None = (
        False  # Populate the invocation step state with the job state instead of the invocation step state.         This will also produce one step per job in mapping jobs to mimic the older behavior with respect to collections.         Partially scheduled steps may provide incomplete information and the listed steps outputs         are not the mapped over step outputs but the individual job outputs.
    )
    model_store_format: ModelStoreFormat | None = None
    step_details: bool | None = (
        False  # Include details for individual invocation steps and populate a steps attribute in the resulting dictionary
    )
    store_content_uri: StoreContentUri | None = None
    store_dict: StoreDict | None = None
    view: View | None = (
        None  # The name of the view used to serialize this item. This will return a predefined set of attributes of the item.
    )
