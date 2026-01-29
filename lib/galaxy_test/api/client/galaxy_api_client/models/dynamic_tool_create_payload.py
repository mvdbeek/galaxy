from dataclasses import dataclass

from .dynamic_tool_create_payload_active import DynamicToolCreatePayloadActive
from .dynamic_tool_create_payload_hidden import DynamicToolCreatePayloadHidden
from .dynamic_tool_create_payload_representation import DynamicToolCreatePayloadRepresentation

__all__ = ["DynamicToolCreatePayload"]


@dataclass
class DynamicToolCreatePayload:
    """
    DynamicToolCreatePayload dataclass

    Args:
        representation (DynamicToolCreatePayloadRepresentation)
                                 :
        active (DynamicToolCreatePayloadActive | None)
                                 :
        hidden (DynamicToolCreatePayloadHidden | None)
                                 :
        src (str | None)         :
    """

    representation: DynamicToolCreatePayloadRepresentation
    active: DynamicToolCreatePayloadActive | None = True
    hidden: DynamicToolCreatePayloadHidden | None = False
    src: str | None = "representation"

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "active": "active",
            "hidden": "hidden",
            "representation": "representation",
            "src": "src",
        }
        key_transform_with_dump = {
            "active": "active",
            "hidden": "hidden",
            "representation": "representation",
            "src": "src",
        }
