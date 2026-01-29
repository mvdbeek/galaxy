from dataclasses import dataclass

from .update_instance_payload_active import UpdateInstancePayloadActive
from .update_instance_payload_description import UpdateInstancePayloadDescription
from .update_instance_payload_hidden import UpdateInstancePayloadHidden
from .update_instance_payload_name import UpdateInstancePayloadName
from .update_instance_payload_variables import UpdateInstancePayloadVariables

__all__ = ["UpdateInstancePayload"]


@dataclass
class UpdateInstancePayload:
    """
    UpdateInstancePayload dataclass

    Args:
        active (UpdateInstancePayloadActive | None)
                                 :
        description (UpdateInstancePayloadDescription | None)
                                 :
        hidden (UpdateInstancePayloadHidden | None)
                                 :
        name (UpdateInstancePayloadName | None)
                                 :
        variables (UpdateInstancePayloadVariables | None)
                                 :
    """

    active: UpdateInstancePayloadActive | None = None
    description: UpdateInstancePayloadDescription | None = None
    hidden: UpdateInstancePayloadHidden | None = None
    name: UpdateInstancePayloadName | None = None
    variables: UpdateInstancePayloadVariables | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "active": "active",
            "description": "description",
            "hidden": "hidden",
            "name": "name",
            "variables": "variables",
        }
        key_transform_with_dump = {
            "active": "active",
            "description": "description",
            "hidden": "hidden",
            "name": "name",
            "variables": "variables",
        }
