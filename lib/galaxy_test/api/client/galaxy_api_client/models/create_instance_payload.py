from dataclasses import dataclass

from .create_instance_payload_description import CreateInstancePayloadDescription
from .create_instance_payload_secrets import CreateInstancePayloadSecrets
from .create_instance_payload_variables import CreateInstancePayloadVariables
from .uuid__2 import Uuid2

__all__ = ["CreateInstancePayload"]


@dataclass
class CreateInstancePayload:
    """
    CreateInstancePayload dataclass

    Args:
        name (str)               :
        secrets (CreateInstancePayloadSecrets)
                                 :
        template_id (str)        :
        template_version (int)   :
        variables (CreateInstancePayloadVariables)
                                 :
        description (CreateInstancePayloadDescription | None)
                                 :
        uuid_ (Uuid2 | None)     : Maps from 'uuid'
    """

    name: str
    secrets: CreateInstancePayloadSecrets
    template_id: str
    template_version: int
    variables: CreateInstancePayloadVariables
    description: CreateInstancePayloadDescription | None = None
    uuid_: Uuid2 | None = None  # Maps from 'uuid'

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "description": "description",
            "name": "name",
            "secrets": "secrets",
            "template_id": "template_id",
            "template_version": "template_version",
            "uuid": "uuid_",
            "variables": "variables",
        }
        key_transform_with_dump = {
            "description": "description",
            "name": "name",
            "secrets": "secrets",
            "template_id": "template_id",
            "template_version": "template_version",
            "uuid_": "uuid",
            "variables": "variables",
        }
