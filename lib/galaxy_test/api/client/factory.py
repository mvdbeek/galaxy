"""Factory for creating Galaxy API client instances.

This module provides a factory function for creating typed API clients
for testing purposes. The client is generated from the Galaxy OpenAPI
schema using openapi-python-client.

To generate the client, run: make update-python-api-client
"""

# Import the generated client (will be available after running make update-python-api-client)
try:
    from galaxy_test.api.client.galaxy_api_client import AuthenticatedClient, Client

    CLIENT_AVAILABLE = True
except ImportError:
    CLIENT_AVAILABLE = False
    AuthenticatedClient = None  # type: ignore[misc, assignment]
    Client = None  # type: ignore[misc, assignment]


class ClientNotGeneratedError(Exception):
    """Raised when trying to use the API client before it has been generated."""

    def __init__(self):
        super().__init__(
            "The Galaxy API client has not been generated yet. Run 'make update-python-api-client' to generate it."
        )


def create_client(
    base_url: str,
    api_key: str | None = None,
    timeout: float = 60.0,
):
    """Create a Galaxy API client for testing.

    Args:
        base_url: Galaxy server URL (e.g., "http://localhost:8080")
        api_key: Optional API key for authentication
        timeout: Request timeout in seconds

    Returns:
        An authenticated or anonymous client instance

    Raises:
        ClientNotGeneratedError: If the client hasn't been generated yet

    Example:
        >>> client = create_client("http://localhost:8080", api_key="...")
        >>> from galaxy_test.api.client.galaxy_api_client.api.histories import create
        >>> from galaxy_test.api.client.galaxy_api_client.models import CreateHistoryPayload
        >>> history = create.sync(client=client, body=CreateHistoryPayload(name="Test"))
    """
    if not CLIENT_AVAILABLE:
        raise ClientNotGeneratedError()

    if api_key:
        return AuthenticatedClient(
            base_url=base_url,
            headers={"x-api-key": api_key},
            timeout=timeout,
        )
    return Client(base_url=base_url, timeout=timeout)


def is_client_available() -> bool:
    """Check if the API client has been generated.

    Returns:
        True if the client is available, False otherwise
    """
    return CLIENT_AVAILABLE
