from dataclasses import dataclass

from .landing_request_state import LandingRequestState
from .workflow_landing_request_origin import WorkflowLandingRequestOrigin
from .workflow_landing_request_request_state import WorkflowLandingRequestRequestState
from .workflow_landing_request_workflow_target_type import WorkflowLandingRequestWorkflowTargetType

__all__ = ["WorkflowLandingRequest"]


@dataclass
class WorkflowLandingRequest:
    """
    WorkflowLandingRequest dataclass

    Args:
        request_state (WorkflowLandingRequestRequestState)
                                 :
        state (LandingRequestState)
                                 :
        uuid_ (str)              : Universal unique identifier for this dataset. (maps from
                                   'uuid')
        workflow_id (str)        :
        workflow_target_type (WorkflowLandingRequestWorkflowTargetType)
                                 :
        origin (WorkflowLandingRequestOrigin | None)
                                 :
    """

    request_state: WorkflowLandingRequestRequestState
    state: LandingRequestState
    uuid_: str  # Universal unique identifier for this dataset. (maps from 'uuid')
    workflow_id: str
    workflow_target_type: WorkflowLandingRequestWorkflowTargetType
    origin: WorkflowLandingRequestOrigin | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "origin": "origin",
            "request_state": "request_state",
            "state": "state",
            "uuid": "uuid_",
            "workflow_id": "workflow_id",
            "workflow_target_type": "workflow_target_type",
        }
        key_transform_with_dump = {
            "origin": "origin",
            "request_state": "request_state",
            "state": "state",
            "uuid_": "uuid",
            "workflow_id": "workflow_id",
            "workflow_target_type": "workflow_target_type",
        }
