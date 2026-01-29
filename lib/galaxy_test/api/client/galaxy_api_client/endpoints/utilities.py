from typing import Any, Protocol, cast, runtime_checkable

from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.utilities_proxy_param_run_as import UtilitiesProxyParamRunAs
from ..models.utilities_proxy_param_run_as_2 import UtilitiesProxyParamRunAs2


@runtime_checkable
class UtilitiesClientProtocol(Protocol):
    """Protocol defining the interface of UtilitiesClient for dependency injection."""

    async def utilities_proxy(
        self,
        url: str,
        run_as: UtilitiesProxyParamRunAs | None = None,
    ) -> dict[str, Any]: ...

    async def utilities_proxy(
        self,
        url: str,
        run_as: UtilitiesProxyParamRunAs | None = None,
    ) -> dict[str, Any]: ...

    async def utilities_proxy_2(
        self,
        url: str,
        run_as: UtilitiesProxyParamRunAs2 | None = None,
    ) -> dict[str, Any]: ...

    async def utilities_proxy_2(
        self,
        url: str,
        run_as: UtilitiesProxyParamRunAs2 | None = None,
    ) -> dict[str, Any]: ...


class UtilitiesClient(UtilitiesClientProtocol):
    """Client for utilities endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def utilities_proxy(
        self,
        url: str,
        run_as: UtilitiesProxyParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Proxy

        Proxy a remote file to the client to avoid CORS issues.

        Args:
            url (str)                : The URL of the remote file
            run-as (UtilitiesProxyParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/proxy"

        params: dict[str, Any] = {
            "url": DataclassSerializer.serialize(url),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def utilities_proxy(
        self,
        url: str,
        run_as: UtilitiesProxyParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Proxy

        Proxy a remote file to the client to avoid CORS issues.

        Args:
            url (str)                : The URL of the remote file
            run-as (UtilitiesProxyParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/proxy"

        params: dict[str, Any] = {
            "url": DataclassSerializer.serialize(url),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def utilities_proxy_2(
        self,
        url: str,
        run_as: UtilitiesProxyParamRunAs2 | None = None,
    ) -> dict[str, Any]:
        """
        Proxy

        Proxy a remote file to the client to avoid CORS issues.

        Args:
            url (str)                : The URL of the remote file
            run-as (UtilitiesProxyParamRunAs2 | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/proxy"

        params: dict[str, Any] = {
            "url": DataclassSerializer.serialize(url),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("HEAD", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def utilities_proxy_2(
        self,
        url: str,
        run_as: UtilitiesProxyParamRunAs2 | None = None,
    ) -> dict[str, Any]:
        """
        Proxy

        Proxy a remote file to the client to avoid CORS issues.

        Args:
            url (str)                : The URL of the remote file
            run-as (UtilitiesProxyParamRunAs2 | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/proxy"

        params: dict[str, Any] = {
            "url": DataclassSerializer.serialize(url),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("HEAD", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover
