from dataclasses import dataclass

from .config_ import Config_
from .context_response_session_csrf_token import ContextResponseSessionCsrfToken
from .context_response_user import ContextResponseUser

__all__ = ["ContextResponse"]


@dataclass
class ContextResponse:
    """
    ContextResponse dataclass

    Args:
        config_ (Config_)        : Maps from 'config'
        user (ContextResponseUser):
        session_csrf_token (ContextResponseSessionCsrfToken | None)
                                 :
    """

    config_: Config_  # Maps from 'config'
    user: ContextResponseUser
    session_csrf_token: ContextResponseSessionCsrfToken | None = None

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "config": "config_",
            "session_csrf_token": "session_csrf_token",
            "user": "user",
        }
        key_transform_with_dump = {
            "config_": "config",
            "session_csrf_token": "session_csrf_token",
            "user": "user",
        }
