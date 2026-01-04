from dataclasses import dataclass

from .label import Label
from .service_parameter_definition import ServiceParameterDefinition

__all__ = ["ServiceCredentialsDefinition"]


@dataclass
class ServiceCredentialsDefinition:
    """
    ServiceCredentialsDefinition dataclass.

    Args:
        description (str)        : A description of the service.
        name (str)               : The name of the service.
        optional (bool)          : If true, tools can run without credentials; if false,
                                   credentials must be provided before execution.
        secrets (List[ServiceParameterDefinition])
                                 :
        variables (List[ServiceParameterDefinition])
                                 :
        version (str)            : The version of the service.
        label (Optional[Label])  : Label of the input.
    """

    description: str  # A description of the service.
    name: str  # The name of the service.
    optional: (
        bool  # If true, tools can run without credentials; if false, credentials must be provided before execution.
    )
    secrets: list[ServiceParameterDefinition]
    variables: list[ServiceParameterDefinition]
    version: str  # The version of the service.
    label: Label | None = None  # Label of the input.
