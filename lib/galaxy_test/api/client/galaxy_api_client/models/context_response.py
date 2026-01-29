from dataclasses import dataclass

from .config_ import Config_
from .session_csrf_token import SessionCsrfToken
from .user import User

__all__ = ["ContextResponse"]


@dataclass
class ContextResponse:
    """
    ContextResponse dataclass.

    Args:
        config_ (Config_)        :
        user (User)              :
        session_csrf_token (Optional[SessionCsrfToken])
                                 :
    """

    config_: Config_
    user: User
    session_csrf_token: SessionCsrfToken | None = None
