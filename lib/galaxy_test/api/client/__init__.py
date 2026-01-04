"""Galaxy API Client for testing.

This package provides a typed Python client for the Galaxy API, generated from
the OpenAPI schema using openapi-python-client.

To generate/update the client, run:
    make update-python-api-client

Usage:
    from galaxy_test.api.client import create_client

    client = create_client(base_url="http://localhost:8080", api_key="...")

    # Use typed API methods
    from galaxy_test.api.client.galaxy_api_client.api.histories import create, index, show
    history = create.sync(client=client, body=CreateHistoryPayload(name="Test"))
"""

from .factory import create_client

__all__ = ["create_client"]
