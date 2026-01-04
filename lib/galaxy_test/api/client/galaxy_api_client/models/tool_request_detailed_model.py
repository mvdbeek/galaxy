from dataclasses import dataclass, field

from .request import Request
from .state_message import StateMessage
from .tool_request_implicit_collection_reference import ToolRequestImplicitCollectionReference
from .tool_request_job_reference import ToolRequestJobReference
from .tool_request_state import ToolRequestState

__all__ = ["ToolRequestDetailedModel"]


@dataclass
class ToolRequestDetailedModel:
    """
    ToolRequestDetailedModel dataclass.

    Args:
        id_ (str)                : Encoded ID of the role
        request (Request)        :
        state (ToolRequestState) :
        state_message (Optional[StateMessage])
                                 :
        implicit_collections (Optional[List[ToolRequestImplicitCollectionReference]])
                                 :
        jobs (Optional[List[ToolRequestJobReference]])
                                 :
    """

    id_: str  # Encoded ID of the role
    request: Request
    state: ToolRequestState
    state_message: StateMessage | None
    implicit_collections: list[ToolRequestImplicitCollectionReference] | None = field(default_factory=list)
    jobs: list[ToolRequestJobReference] | None = field(default_factory=list)
