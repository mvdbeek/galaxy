from dataclasses import dataclass

from .type__13 import Type13
from .user_file_source_model_description import UserFileSourceModelDescription
from .user_file_source_model_variables import UserFileSourceModelVariables

__all__ = ["UserFileSourceModel"]


@dataclass
class UserFileSourceModel:
    """
    UserFileSourceModel dataclass

    Args:
        active (bool)            :
        description (UserFileSourceModelDescription)
                                 :
        hidden (bool)            :
        name (str)               :
        purged (bool)            :
        secrets (List[str])      :
        template_id (str)        :
        template_version (int)   :
        type_ (Type13)           : Maps from 'type'
        uri_root (str)           :
        uuid_ (str)              : Maps from 'uuid'
        variables (UserFileSourceModelVariables)
                                 :
    """

    active: bool
    description: UserFileSourceModelDescription
    hidden: bool
    name: str
    purged: bool
    secrets: list[str]
    template_id: str
    template_version: int
    type_: Type13  # Maps from 'type'
    uri_root: str
    uuid_: str  # Maps from 'uuid'
    variables: UserFileSourceModelVariables

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "active": "active",
            "description": "description",
            "hidden": "hidden",
            "name": "name",
            "purged": "purged",
            "secrets": "secrets",
            "template_id": "template_id",
            "template_version": "template_version",
            "type": "type_",
            "uri_root": "uri_root",
            "uuid": "uuid_",
            "variables": "variables",
        }
        key_transform_with_dump = {
            "active": "active",
            "description": "description",
            "hidden": "hidden",
            "name": "name",
            "purged": "purged",
            "secrets": "secrets",
            "template_id": "template_id",
            "template_version": "template_version",
            "type_": "type",
            "uri_root": "uri_root",
            "uuid_": "uuid",
            "variables": "variables",
        }
