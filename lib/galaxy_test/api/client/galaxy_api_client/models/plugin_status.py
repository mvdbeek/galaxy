from dataclasses import dataclass

from .connection import Connection
from .oauth_2_access_token_generation import Oauth2AccessTokenGeneration
from .plugin_aspect_status import PluginAspectStatus
from .template_settings import TemplateSettings

__all__ = ["PluginStatus"]


@dataclass
class PluginStatus:
    """
    PluginStatus dataclass.

    Args:
        template_definition (PluginAspectStatus)
                                 :
        connection (Optional[Connection])
                                 :
        oauth2_access_token_generation (Optional[Oauth2AccessTokenGeneration])
                                 :
        template_settings (Optional[TemplateSettings])
                                 :
    """

    template_definition: PluginAspectStatus
    connection: Connection | None = None
    oauth2_access_token_generation: Oauth2AccessTokenGeneration | None = None
    template_settings: TemplateSettings | None = None
