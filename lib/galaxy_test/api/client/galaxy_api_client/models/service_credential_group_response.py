from dataclasses import dataclass
from datetime import datetime

from .secret_response import SecretResponse
from .variable_response import VariableResponse

__all__ = ["ServiceCredentialGroupResponse"]


@dataclass
class ServiceCredentialGroupResponse:
    """
    ServiceCredentialGroupResponse dataclass

    Args:
        id_ (str)                : Encoded ID of the credential group. (maps from 'id')
        name (str)               : The name of the credential group.
        secrets (List[SecretResponse])
                                 :
        update_time (datetime)   : The last time the credential group was updated.
        variables (List[VariableResponse])
                                 :
    """

    id_: str  # Encoded ID of the credential group. (maps from 'id')
    name: str  # The name of the credential group.
    secrets: list[SecretResponse]
    update_time: datetime  # The last time the credential group was updated.
    variables: list[VariableResponse]

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "id": "id_",
            "name": "name",
            "secrets": "secrets",
            "update_time": "update_time",
            "variables": "variables",
        }
        key_transform_with_dump = {
            "id_": "id",
            "name": "name",
            "secrets": "secrets",
            "update_time": "update_time",
            "variables": "variables",
        }
