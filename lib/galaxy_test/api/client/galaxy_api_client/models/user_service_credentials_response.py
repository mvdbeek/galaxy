from dataclasses import dataclass

from .current_group_id import CurrentGroupId
from .service_credential_group_response import ServiceCredentialGroupResponse

__all__ = ["UserServiceCredentialsResponse"]


@dataclass
class UserServiceCredentialsResponse:
    """
    UserServiceCredentialsResponse dataclass.

    Args:
        groups (List[ServiceCredentialGroupResponse])
                                 :
        id_ (str)                : The encoded ID of the user credentials.
        name (str)               : The name of the service requiring credentials.
        source_id (str)          : The ID of the source (e.g., tool ID).
        source_type (str)        : The type of source (e.g., 'tool').
        source_version (str)     : The version of the source.
        user_id (str)            : The ID of the user who owns these credentials.
        version (str)            : The version of the service.
        current_group_id (Optional[CurrentGroupId])
                                 : The ID of the currently active credential group.
    """

    groups: list[ServiceCredentialGroupResponse]
    id_: str  # The encoded ID of the user credentials.
    name: str  # The name of the service requiring credentials.
    source_id: str  # The ID of the source (e.g., tool ID).
    source_type: str  # The type of source (e.g., 'tool').
    source_version: str  # The version of the source.
    user_id: str  # The ID of the user who owns these credentials.
    version: str  # The version of the service.
    current_group_id: CurrentGroupId | None = None  # The ID of the currently active credential group.
