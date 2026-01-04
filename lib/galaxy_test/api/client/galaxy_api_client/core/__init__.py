# Re-export core exceptions and generated aliases
from .auth.base import BaseAuth
from .auth.plugins import ApiKeyAuth, BearerAuth, OAuth2Auth
from .config import ClientConfig
from .exception_aliases import *  # noqa: F403
from .exceptions import ClientError, HTTPError, ServerError

# Re-export other commonly used core components
from .http_transport import HttpTransport, HttpxTransport
from .schemas import BaseSchema
from .utils import DataclassSerializer

__all__ = [
    # Base exceptions
    "HTTPError",
    "ClientError",
    "ServerError",
    # All ErrorXXX from exception_aliases are implicitly in __all__ due to star import
    # Transport layer
    "HttpTransport",
    "HttpxTransport",
    # Configuration
    "ClientConfig",
    # Schemas
    "BaseSchema",
    # Utilities
    "DataclassSerializer",
    # Authentication
    "BaseAuth",
    "ApiKeyAuth",
    "BearerAuth",
    "OAuth2Auth",
    # Generated exception aliases
    "Error200",
    "Error202",
    "Error204",
    "Error304",
    "Error404",
    "Error501",
]
