from dataclasses import dataclass

__all__ = ["ServiceParameterDefinition"]


@dataclass
class ServiceParameterDefinition:
    """
    ServiceParameterDefinition dataclass.

    Args:
        description (str)        : A description of what this credential is used for.
        label (str)              : The human-readable label for the credential.
        name (str)               : The name of the credential definition.
        optional (bool)          : Whether this credential is optional or required.
    """

    description: str  # A description of what this credential is used for.
    label: str  # The human-readable label for the credential.
    name: str  # The name of the credential definition.
    optional: bool  # Whether this credential is optional or required.
