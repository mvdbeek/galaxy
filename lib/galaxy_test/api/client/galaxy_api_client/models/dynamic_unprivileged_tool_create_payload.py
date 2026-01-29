from dataclasses import dataclass

from .dynamic_unprivileged_tool_create_payload_active import DynamicUnprivilegedToolCreatePayloadActive
from .dynamic_unprivileged_tool_create_payload_hidden import DynamicUnprivilegedToolCreatePayloadHidden
from .user_tool_source_input_2 import UserToolSourceInput2

__all__ = ["DynamicUnprivilegedToolCreatePayload"]


@dataclass
class DynamicUnprivilegedToolCreatePayload:
    """
    DynamicUnprivilegedToolCreatePayload dataclass

    Args:
        representation (UserToolSourceInput2)
                                 :
        active (DynamicUnprivilegedToolCreatePayloadActive | None)
                                 :
        hidden (DynamicUnprivilegedToolCreatePayloadHidden | None)
                                 :
        src (str | None)         :
    """

    representation: UserToolSourceInput2
    active: DynamicUnprivilegedToolCreatePayloadActive | None = True
    hidden: DynamicUnprivilegedToolCreatePayloadHidden | None = False
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
