from dataclasses import dataclass

from .plugin_aspect_status_state import PluginAspectStatusState

__all__ = ["PluginAspectStatus"]


@dataclass
class PluginAspectStatus:
    """
    PluginAspectStatus dataclass

    Args:
        message (str)            :
        state (PluginAspectStatusState)
                                 :
    """

    message: str
    state: PluginAspectStatusState

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "message": "message",
            "state": "state",
        }
        key_transform_with_dump = {
            "message": "message",
            "state": "state",
        }
