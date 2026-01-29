from dataclasses import dataclass

from .role_definition_model_group_ids import RoleDefinitionModelGroupIds
from .role_definition_model_role_type import RoleDefinitionModelRoleType
from .role_definition_model_user_ids import RoleDefinitionModelUserIds

__all__ = ["RoleDefinitionModel"]


@dataclass
class RoleDefinitionModel:
    """
    RoleDefinitionModel dataclass

    Args:
        description (str)        : Description of the role
        name (str)               : Name of the role
        group_ids (RoleDefinitionModelGroupIds | None)
                                 :
        role_type (RoleDefinitionModelRoleType | None)
                                 :
        user_ids (RoleDefinitionModelUserIds | None)
                                 :
    """

    description: str  # Description of the role
    name: str  # Name of the role
    group_ids: RoleDefinitionModelGroupIds | None = None
    role_type: RoleDefinitionModelRoleType | None = "admin"
    user_ids: RoleDefinitionModelUserIds | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "description": "description",
            "group_ids": "group_ids",
            "name": "name",
            "role_type": "role_type",
            "user_ids": "user_ids",
        }
        key_transform_with_dump = {
            "description": "description",
            "group_ids": "group_ids",
            "name": "name",
            "role_type": "role_type",
            "user_ids": "user_ids",
        }
