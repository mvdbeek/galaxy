from dataclasses import dataclass

from .current_group_id import CurrentGroupId
from .service_credential_group_response import ServiceCredentialGroupResponse
from .service_credentials_definition import ServiceCredentialsDefinition

__all__ = ["UserServiceCredentialsWithDefinitionResponse"]


@dataclass
class UserServiceCredentialsWithDefinitionResponse:
    """
    UserServiceCredentialsWithDefinitionResponse dataclass.

    Args:
        definition (ServiceCredentialsDefinition)
                                 :
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

    definition: ServiceCredentialsDefinition
    groups: list[ServiceCredentialGroupResponse]
    id_: str  # The encoded ID of the user credentials.
    name: str  # The name of the service requiring credentials.
    source_id: str  # The ID of the source (e.g., tool ID).
    source_type: str  # The type of source (e.g., 'tool').
    source_version: str  # The version of the source.
    user_id: str  # The ID of the user who owns these credentials.
    version: str  # The version of the service.
    current_group_id: CurrentGroupId | None = None  # The ID of the currently active credential group.
