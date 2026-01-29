from dataclasses import dataclass

from .service_credentials_definition_label import ServiceCredentialsDefinitionLabel
from .service_parameter_definition import ServiceParameterDefinition

__all__ = ["ServiceCredentialsDefinition"]


@dataclass
class ServiceCredentialsDefinition:
    """
    ServiceCredentialsDefinition dataclass

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
        label (ServiceCredentialsDefinitionLabel | None)
                                 : A human-readable label for the service.
    """

    description: str  # A description of the service.
    name: str  # The name of the service.
    optional: (
        bool  # If true, tools can run without credentials; if false, credentials must be provided before execution.
    )
    secrets: list[ServiceParameterDefinition]
    variables: list[ServiceParameterDefinition]
    version: str  # The version of the service.
    label: ServiceCredentialsDefinitionLabel | None = None  # A human-readable label for the service.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "description": "description",
            "label": "label",
            "name": "name",
            "optional": "optional",
            "secrets": "secrets",
            "variables": "variables",
            "version": "version",
        }
        key_transform_with_dump = {
            "description": "description",
            "label": "label",
            "name": "name",
            "optional": "optional",
            "secrets": "secrets",
            "variables": "variables",
            "version": "version",
        }
