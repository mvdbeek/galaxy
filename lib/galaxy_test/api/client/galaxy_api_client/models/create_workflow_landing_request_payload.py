from dataclasses import dataclass

from .client_secret import ClientSecret
from .origin import Origin
from .request_state import RequestState
from .workflow_target_type import WorkflowTargetType

__all__ = ["CreateWorkflowLandingRequestPayload"]


@dataclass
class CreateWorkflowLandingRequestPayload:
    """
    CreateWorkflowLandingRequestPayload dataclass.

    Args:
        workflow_id (str)        :
        workflow_target_type (WorkflowTargetType)
                                 :
        client_secret (Optional[ClientSecret])
                                 :
        origin (Optional[Origin]): The origin of the landing request.
        public (Optional[bool])  : If workflow landing request is public anyone with the
                                   uuid can use the landing request. If not public the
                                   request must be claimed before use and additional
                                   verification might occur.
        request_state (Optional[RequestState])
                                 :
    """

    workflow_id: str
    workflow_target_type: WorkflowTargetType
    client_secret: ClientSecret | None = None
    origin: Origin | None = None  # The origin of the landing request.
    public: bool | None = (
        False  # If workflow landing request is public anyone with the uuid can use the landing request. If not public the request must be claimed before use and additional verification might occur.
    )
    request_state: RequestState | None = None
