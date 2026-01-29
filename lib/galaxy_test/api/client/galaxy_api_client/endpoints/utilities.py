from typing import Any

from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport

from ..models.utilities_proxy_param_run_as import UtilitiesProxyParamRunAs


class UtilitiesClient:
    """Client for utilities endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def utilities_proxy_2_2(
        self,
        url: str,
        run_as: UtilitiesProxyParamRunAs | None = None,
    ) -> Any:
        """
        Proxy

        Proxy a remote file to the client to avoid CORS issues.

        Args:
            url (str)                : The URL of the remote file
            run-as (Optional[UtilitiesProxyParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/proxy"

        params: dict[str, Any] = {
            "url": url,
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def utilities_proxy_2_2(
        self,
        url: str,
        run_as: UtilitiesProxyParamRunAs | None = None,
    ) -> Any:
        """
        Proxy

        Proxy a remote file to the client to avoid CORS issues.

        Args:
            url (str)                : The URL of the remote file
            run-as (Optional[UtilitiesProxyParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/proxy"

        params: dict[str, Any] = {
            "url": url,
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def utilities_proxy_3_2(
        self,
        url: str,
        run_as: UtilitiesProxyParamRunAs | None = None,
    ) -> Any:
        """
        Proxy

        Proxy a remote file to the client to avoid CORS issues.

        Args:
            url (str)                : The URL of the remote file
            run-as (Optional[UtilitiesProxyParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/proxy"

        params: dict[str, Any] = {
            "url": url,
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("HEAD", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def utilities_proxy_3_2(
        self,
        url: str,
        run_as: UtilitiesProxyParamRunAs | None = None,
    ) -> Any:
        """
        Proxy

        Proxy a remote file to the client to avoid CORS issues.

        Args:
            url (str)                : The URL of the remote file
            run-as (Optional[UtilitiesProxyParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/proxy"

        params: dict[str, Any] = {
            "url": url,
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("HEAD", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover
