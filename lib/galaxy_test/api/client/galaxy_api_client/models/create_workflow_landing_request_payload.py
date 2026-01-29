from dataclasses import dataclass

from .create_workflow_landing_request_payload_client_secret import CreateWorkflowLandingRequestPayloadClientSecret
from .create_workflow_landing_request_payload_origin import CreateWorkflowLandingRequestPayloadOrigin
from .create_workflow_landing_request_payload_request_state import CreateWorkflowLandingRequestPayloadRequestState
from .create_workflow_landing_request_payload_workflow_target_type import (
    CreateWorkflowLandingRequestPayloadWorkflowTargetType,
)

__all__ = ["CreateWorkflowLandingRequestPayload"]


@dataclass
class CreateWorkflowLandingRequestPayload:
    """
    CreateWorkflowLandingRequestPayload dataclass

    Args:
        workflow_id (str)        :
        workflow_target_type (CreateWorkflowLandingRequestPayloadWorkflowTargetType)
                                 :
        client_secret (CreateWorkflowLandingRequestPayloadClientSecret | None)
                                 :
        origin (CreateWorkflowLandingRequestPayloadOrigin | None)
                                 : The origin of the landing request.
        public (bool | None)     : If workflow landing request is public anyone with the
                                   uuid can use the landing request. If not public the
                                   request must be claimed before use and additional
                                   verification might occur.
        request_state (CreateWorkflowLandingRequestPayloadRequestState | None)
                                 :
    """

    workflow_id: str
    workflow_target_type: CreateWorkflowLandingRequestPayloadWorkflowTargetType
    client_secret: CreateWorkflowLandingRequestPayloadClientSecret | None = None
    origin: CreateWorkflowLandingRequestPayloadOrigin | None = None  # The origin of the landing request.
    public: bool | None = (
        False  # If workflow landing request is public anyone with the uuid can use the landing request. If not public the request must be claimed before use and additional verification might occur.
    )
    request_state: CreateWorkflowLandingRequestPayloadRequestState | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "client_secret": "client_secret",
            "origin": "origin",
            "public": "public",
            "request_state": "request_state",
            "workflow_id": "workflow_id",
            "workflow_target_type": "workflow_target_type",
        }
        key_transform_with_dump = {
            "client_secret": "client_secret",
            "origin": "origin",
            "public": "public",
            "request_state": "request_state",
            "workflow_id": "workflow_id",
            "workflow_target_type": "workflow_target_type",
        }
