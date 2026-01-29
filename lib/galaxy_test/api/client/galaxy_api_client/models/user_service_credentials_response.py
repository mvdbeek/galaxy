from dataclasses import dataclass

from .service_credential_group_response import ServiceCredentialGroupResponse
from .user_service_credentials_response_current_group_id import UserServiceCredentialsResponseCurrentGroupId

__all__ = ["UserServiceCredentialsResponse"]


@dataclass
class UserServiceCredentialsResponse:
    """
    UserServiceCredentialsResponse dataclass

    Args:
        groups (List[ServiceCredentialGroupResponse])
                                 :
        id_ (str)                : The encoded ID of the user credentials. (maps from 'id')
        name (str)               : The name of the service requiring credentials.
        source_id (str)          : The ID of the source (e.g., tool ID).
        source_type (str)        : The type of source (e.g., 'tool').
        source_version (str)     : The version of the source.
        user_id (str)            : The ID of the user who owns these credentials.
        version (str)            : The version of the service.
        current_group_id (UserServiceCredentialsResponseCurrentGroupId | None)
                                 : The ID of the currently active credential group.
    """

    groups: list[ServiceCredentialGroupResponse]
    id_: str  # The encoded ID of the user credentials. (maps from 'id')
    name: str  # The name of the service requiring credentials.
    source_id: str  # The ID of the source (e.g., tool ID).
    source_type: str  # The type of source (e.g., 'tool').
    source_version: str  # The version of the source.
    user_id: str  # The ID of the user who owns these credentials.
    version: str  # The version of the service.
    current_group_id: UserServiceCredentialsResponseCurrentGroupId | None = (
        None  # The ID of the currently active credential group.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "current_group_id": "current_group_id",
            "groups": "groups",
            "id": "id_",
            "name": "name",
            "source_id": "source_id",
            "source_type": "source_type",
            "source_version": "source_version",
            "user_id": "user_id",
            "version": "version",
        }
        key_transform_with_dump = {
            "current_group_id": "current_group_id",
            "groups": "groups",
            "id_": "id",
            "name": "name",
            "source_id": "source_id",
            "source_type": "source_type",
            "source_version": "source_version",
            "user_id": "user_id",
            "version": "version",
        }
