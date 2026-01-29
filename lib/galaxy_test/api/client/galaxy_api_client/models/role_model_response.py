from dataclasses import dataclass

from .role_model_response_description import RoleModelResponseDescription

__all__ = ["RoleModelResponse"]


@dataclass
class RoleModelResponse:
    """
    RoleModelResponse dataclass

    Args:
        description (RoleModelResponseDescription)
                                 :
        id_ (str)                : Encoded ID of the role (maps from 'id')
        model_class (str)        : The name of the database model class.
        name (str)               : Name of the role
        type_ (str)              : Type or category of the role (maps from 'type')
        url (str)                : The relative URL to access this item.
    """

    description: RoleModelResponseDescription
    id_: str  # Encoded ID of the role (maps from 'id')
    model_class: str  # The name of the database model class.
    name: str  # Name of the role
    type_: str  # Type or category of the role (maps from 'type')
    url: str  # The relative URL to access this item.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "description": "description",
            "id": "id_",
            "model_class": "model_class",
            "name": "name",
            "type": "type_",
            "url": "url",
        }
        key_transform_with_dump = {
            "description": "description",
            "id_": "id",
            "model_class": "model_class",
            "name": "name",
            "type_": "type",
            "url": "url",
        }
