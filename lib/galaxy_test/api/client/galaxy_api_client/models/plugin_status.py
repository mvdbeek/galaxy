from dataclasses import dataclass

from .plugin_aspect_status import PluginAspectStatus
from .plugin_status_connection import PluginStatusConnection
from .plugin_status_oauth_2_access_token_generation import PluginStatusOauth2AccessTokenGeneration
from .plugin_status_template_settings import PluginStatusTemplateSettings

__all__ = ["PluginStatus"]


@dataclass
class PluginStatus:
    """
    PluginStatus dataclass

    Args:
        template_definition (PluginAspectStatus)
                                 :
        connection (PluginStatusConnection | None)
                                 :
        oauth2_access_token_generation (PluginStatusOauth2AccessTokenGeneration | None)
                                 :
        template_settings (PluginStatusTemplateSettings | None)
                                 :
    """

    template_definition: PluginAspectStatus
    connection: PluginStatusConnection | None = None
    oauth2_access_token_generation: PluginStatusOauth2AccessTokenGeneration | None = None
    template_settings: PluginStatusTemplateSettings | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "connection": "connection",
            "oauth2_access_token_generation": "oauth2_access_token_generation",
            "template_definition": "template_definition",
            "template_settings": "template_settings",
        }
        key_transform_with_dump = {
            "connection": "connection",
            "oauth2_access_token_generation": "oauth2_access_token_generation",
            "template_definition": "template_definition",
            "template_settings": "template_settings",
        }
