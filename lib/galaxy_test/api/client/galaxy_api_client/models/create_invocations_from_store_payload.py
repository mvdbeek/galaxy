from dataclasses import dataclass

from .create_invocations_from_store_payload_model_store_format import CreateInvocationsFromStorePayloadModelStoreFormat
from .create_invocations_from_store_payload_store_content_uri import CreateInvocationsFromStorePayloadStoreContentUri
from .create_invocations_from_store_payload_store_dict import CreateInvocationsFromStorePayloadStoreDict
from .create_invocations_from_store_payload_view import CreateInvocationsFromStorePayloadView

__all__ = ["CreateInvocationsFromStorePayload"]


@dataclass
class CreateInvocationsFromStorePayload:
    """
    CreateInvocationsFromStorePayload dataclass

    Args:
        history_id (str)         : The ID of the history associated with the invocations.
        legacy_job_state (bool | None)
                                 : Populate the invocation step state with the job state
                                   instead of the invocation step state.         This will
                                   also produce one step per job in mapping jobs to mimic
                                   the older behavior with respect to collections.
                                   Partially scheduled steps may provide incomplete
                                   information and the listed steps outputs         are not
                                   the mapped over step outputs but the individual job
                                   outputs.
        model_store_format (CreateInvocationsFromStorePayloadModelStoreFormat | None)
                                 :
        step_details (bool | None): Include details for individual invocation steps and
                                    populate a steps attribute in the resulting dictionary
        store_content_uri (CreateInvocationsFromStorePayloadStoreContentUri | None)
                                 :
        store_dict (CreateInvocationsFromStorePayloadStoreDict | None)
                                 :
        view (CreateInvocationsFromStorePayloadView | None)
                                 : The name of the view used to serialize this item. This
                                   will return a predefined set of attributes of the item.
    """

    history_id: str  # The ID of the history associated with the invocations.
    legacy_job_state: bool | None = (
        False  # Populate the invocation step state with the job state instead of the invocation step state.         This will also produce one step per job in mapping jobs to mimic the older behavior with respect to collections.         Partially scheduled steps may provide incomplete information and the listed steps outputs         are not the mapped over step outputs but the individual job outputs.
    )
    model_store_format: CreateInvocationsFromStorePayloadModelStoreFormat | None = None
    step_details: bool | None = (
        False  # Include details for individual invocation steps and populate a steps attribute in the resulting dictionary
    )
    store_content_uri: CreateInvocationsFromStorePayloadStoreContentUri | None = None
    store_dict: CreateInvocationsFromStorePayloadStoreDict | None = None
    view: CreateInvocationsFromStorePayloadView | None = (
        None  # The name of the view used to serialize this item. This will return a predefined set of attributes of the item.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "history_id": "history_id",
            "legacy_job_state": "legacy_job_state",
            "model_store_format": "model_store_format",
            "step_details": "step_details",
            "store_content_uri": "store_content_uri",
            "store_dict": "store_dict",
            "view": "view",
        }
        key_transform_with_dump = {
            "history_id": "history_id",
            "legacy_job_state": "legacy_job_state",
            "model_store_format": "model_store_format",
            "step_details": "step_details",
            "store_content_uri": "store_content_uri",
            "store_dict": "store_dict",
            "view": "view",
        }
