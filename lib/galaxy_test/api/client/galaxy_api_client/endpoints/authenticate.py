from typing import Protocol, runtime_checkable

from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import structure_from_dict
from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport

from ..models.api_key_response_2 import ApiKeyResponse2


@runtime_checkable
class AuthenticateClientProtocol(Protocol):
    """Protocol defining the interface of AuthenticateClient for dependency injection."""

    async def authenticate_baseauth_get_api_key(
        self,
    ) -> ApiKeyResponse2: ...

    async def authenticate_baseauth_get_api_key(
        self,
    ) -> ApiKeyResponse2: ...


class AuthenticateClient(AuthenticateClientProtocol):
    """Client for authenticate endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def authenticate_baseauth_get_api_key(
        self,
    ) -> ApiKeyResponse2:
        """
        Returns returns an API key for authenticated user based on BaseAuth headers.

        Returns:
            ApiKeyResponse2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/authenticate/baseauth"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), ApiKeyResponse2)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def authenticate_baseauth_get_api_key(
        self,
    ) -> ApiKeyResponse2:
        """
        Returns returns an API key for authenticated user based on BaseAuth headers.

        Returns:
            ApiKeyResponse2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/authenticate/baseauth"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), ApiKeyResponse2)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover
