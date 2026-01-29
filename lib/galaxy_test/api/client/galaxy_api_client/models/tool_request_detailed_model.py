from dataclasses import dataclass, field

from .tool_request_detailed_model_request import ToolRequestDetailedModelRequest
from .tool_request_detailed_model_state_message import ToolRequestDetailedModelStateMessage
from .tool_request_implicit_collection_reference import ToolRequestImplicitCollectionReference
from .tool_request_job_reference import ToolRequestJobReference
from .tool_request_state import ToolRequestState

__all__ = ["ToolRequestDetailedModel"]


@dataclass
class ToolRequestDetailedModel:
    """
    ToolRequestDetailedModel dataclass

    Args:
        id_ (str)                : Encoded ID of the role (maps from 'id')
        request (ToolRequestDetailedModelRequest)
                                 :
        state (ToolRequestState) :
        state_message (ToolRequestDetailedModelStateMessage)
                                 :
        implicit_collections (List[ToolRequestImplicitCollectionReference] | None)
                                 :
        jobs (List[ToolRequestJobReference] | None)
                                 :
    """

    id_: str  # Encoded ID of the role (maps from 'id')
    request: ToolRequestDetailedModelRequest
    state: ToolRequestState
    state_message: ToolRequestDetailedModelStateMessage
    implicit_collections: list[ToolRequestImplicitCollectionReference] | None = field(default_factory=list)
    jobs: list[ToolRequestJobReference] | None = field(default_factory=list)

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "id": "id_",
            "implicit_collections": "implicit_collections",
            "jobs": "jobs",
            "request": "request",
            "state": "state",
            "state_message": "state_message",
        }
        key_transform_with_dump = {
            "id_": "id",
            "implicit_collections": "implicit_collections",
            "jobs": "jobs",
            "request": "request",
            "state": "state",
            "state_message": "state_message",
        }
