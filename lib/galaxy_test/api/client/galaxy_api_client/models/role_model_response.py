from dataclasses import dataclass

from .description import Description

__all__ = ["RoleModelResponse"]


@dataclass
class RoleModelResponse:
    """
    RoleModelResponse dataclass.

    Args:
        description (Optional[Description])
                                 : Detailed text description for this Quota.
        id_ (str)                : Encoded ID of the role
        model_class (str)        : The name of the database model class.
        name (str)               : Name of the role
        type_ (str)              : Type or category of the role
        url (str)                : The relative URL to access this item.
    """

    description: Description | None  # Detailed text description for this Quota.
    id_: str  # Encoded ID of the role
    model_class: str  # The name of the database model class.
    name: str  # Name of the role
    type_: str  # Type or category of the role
    url: str  # The relative URL to access this item.
