# Client package __init__.py
# Re-exports from core and local client.

from .client import APIClient
from .core.auth import ApiKeyAuth, BaseAuth, BearerAuth, OAuth2Auth
from .core.cattrs_converter import converter, structure_from_dict, unstructure_to_dict
from .core.config import ClientConfig
from .core.exceptions import ClientError, HTTPError, ServerError
from .core.http_transport import HttpTransport, HttpxTransport

__all__ = [
    "APIClient",
    "BaseAuth",
    "ApiKeyAuth",
    "BearerAuth",
    "OAuth2Auth",
    "ClientConfig",
    "HTTPError",
    "ClientError",
    "ServerError",
    "HttpTransport",
    "HttpxTransport",
    "structure_from_dict",
    "unstructure_to_dict",
    "converter",
]
