from dataclasses import dataclass

from .path_based_dynamic_tool_create_payload_active import PathBasedDynamicToolCreatePayloadActive
from .path_based_dynamic_tool_create_payload_hidden import PathBasedDynamicToolCreatePayloadHidden
from .path_based_dynamic_tool_create_payload_tool_directory import PathBasedDynamicToolCreatePayloadToolDirectory

__all__ = ["PathBasedDynamicToolCreatePayload"]


@dataclass
class PathBasedDynamicToolCreatePayload:
    """
    PathBasedDynamicToolCreatePayload dataclass

    Args:
        path (str)               :
        src (str)                :
        active (PathBasedDynamicToolCreatePayloadActive | None)
                                 :
        hidden (PathBasedDynamicToolCreatePayloadHidden | None)
                                 :
        tool_directory (PathBasedDynamicToolCreatePayloadToolDirectory | None)
                                 :
    """

    path: str
    src: str
    active: PathBasedDynamicToolCreatePayloadActive | None = None
    hidden: PathBasedDynamicToolCreatePayloadHidden | None = None
    tool_directory: PathBasedDynamicToolCreatePayloadToolDirectory | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "active": "active",
            "hidden": "hidden",
            "path": "path",
            "src": "src",
            "tool_directory": "tool_directory",
        }
        key_transform_with_dump = {
            "active": "active",
            "hidden": "hidden",
            "path": "path",
            "src": "src",
            "tool_directory": "tool_directory",
        }
