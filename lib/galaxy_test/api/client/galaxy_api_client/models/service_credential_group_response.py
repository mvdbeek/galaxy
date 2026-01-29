from dataclasses import dataclass
from datetime import datetime

from .secret_response import SecretResponse
from .variable_response import VariableResponse

__all__ = ["ServiceCredentialGroupResponse"]


@dataclass
class ServiceCredentialGroupResponse:
    """
    ServiceCredentialGroupResponse dataclass.

    Args:
        id_ (str)                : Encoded ID of the credential group.
        name (str)               : The name of the credential group.
        secrets (List[SecretResponse])
                                 :
        update_time (datetime)   : The last time the credential group was updated.
        variables (List[VariableResponse])
                                 :
    """

    id_: str  # Encoded ID of the credential group.
    name: str  # The name of the credential group.
    secrets: list[SecretResponse]
    update_time: datetime  # The last time the credential group was updated.
    variables: list[VariableResponse]
