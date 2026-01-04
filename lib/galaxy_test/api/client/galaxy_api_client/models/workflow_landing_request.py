from dataclasses import dataclass

from .landing_request_state import LandingRequestState
from .origin import Origin
from .request_state import RequestState
from .workflow_target_type import WorkflowTargetType

__all__ = ["WorkflowLandingRequest"]


@dataclass
class WorkflowLandingRequest:
    """
    WorkflowLandingRequest dataclass.

    Args:
        request_state (RequestState)
                                 :
        state (LandingRequestState)
                                 :
        uuid_ (str)              : Universal unique identifier for this dataset.
        workflow_id (str)        :
        workflow_target_type (WorkflowTargetType)
                                 :
        origin (Optional[Origin]): The origin of the landing request.
    """

    request_state: RequestState
    state: LandingRequestState
    uuid_: str  # Universal unique identifier for this dataset.
    workflow_id: str
    workflow_target_type: WorkflowTargetType
    origin: Origin | None = None  # The origin of the landing request.
