from typing import cast
from uuid import UUID

from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport


class ShortTermStorageClient:
    """Client for short_term_storage endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def short_term_storage_serve_2_2(
        self,
        storage_request_id: UUID,
    ) -> None:
        """
        Serve the staged download specified by request ID.

        Args:
            storage_request_id (UUID):

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/short_term_storage/{storage_request_id}"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return None
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def short_term_storage_serve_2_2(
        self,
        storage_request_id: UUID,
    ) -> None:
        """
        Serve the staged download specified by request ID.

        Args:
            storage_request_id (UUID):

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/short_term_storage/{storage_request_id}"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return None
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def short_term_storage_ready_is_ready_2_2(
        self,
        storage_request_id: UUID,
    ) -> bool:
        """
        Determine if specified storage request ID is ready for download.

        Args:
            storage_request_id (UUID):

        Returns:
            bool: Boolean indicating if the storage is ready.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/short_term_storage/{storage_request_id}/ready"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(bool, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def short_term_storage_ready_is_ready_2_2(
        self,
        storage_request_id: UUID,
    ) -> bool:
        """
        Determine if specified storage request ID is ready for download.

        Args:
            storage_request_id (UUID):

        Returns:
            bool: Boolean indicating if the storage is ready.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/short_term_storage/{storage_request_id}/ready"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(bool, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover
