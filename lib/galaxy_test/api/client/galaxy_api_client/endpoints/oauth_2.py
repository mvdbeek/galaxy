from typing import Any, Protocol, cast, runtime_checkable

from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.oauth_2_oauth_2_callback_param_code import Oauth2Oauth2CallbackParamCode
from ..models.oauth_2_oauth_2_callback_param_error import Oauth2Oauth2CallbackParamError
from ..models.oauth_2_oauth_2_callback_param_run_as import Oauth2Oauth2CallbackParamRunAs


@runtime_checkable
class Oauth2ClientProtocol(Protocol):
    """Protocol defining the interface of Oauth2Client for dependency injection."""

    async def oauth2_oauth2_callback(
        self,
        state: str,
        code: Oauth2Oauth2CallbackParamCode | None = None,
        error: Oauth2Oauth2CallbackParamError | None = None,
        run_as: Oauth2Oauth2CallbackParamRunAs | None = None,
    ) -> dict[str, Any]: ...

    async def oauth2_oauth2_callback(
        self,
        state: str,
        code: Oauth2Oauth2CallbackParamCode | None = None,
        error: Oauth2Oauth2CallbackParamError | None = None,
        run_as: Oauth2Oauth2CallbackParamRunAs | None = None,
    ) -> dict[str, Any]: ...


class Oauth2Client(Oauth2ClientProtocol):
    """Client for oauth2 endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def oauth2_oauth2_callback(
        self,
        state: str,
        code: Oauth2Oauth2CallbackParamCode | None = None,
        error: Oauth2Oauth2CallbackParamError | None = None,
        run_as: Oauth2Oauth2CallbackParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Callback entry point for remote resource responses with OAuth2 authorization codes

        Args:
            state (str)              : Base-64 encoded JSON used to route request within Galaxy.
            code (Oauth2Oauth2CallbackParamCode | None)
                                     :
            error (Oauth2Oauth2CallbackParamError | None)
                                     :
            run-as (Oauth2Oauth2CallbackParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/oauth2_callback"

        params: dict[str, Any] = {
            "state": DataclassSerializer.serialize(state),
            **({"code": DataclassSerializer.serialize(code)} if code is not None else {}),
            **({"error": DataclassSerializer.serialize(error)} if error is not None else {}),
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

    async def oauth2_oauth2_callback(
        self,
        state: str,
        code: Oauth2Oauth2CallbackParamCode | None = None,
        error: Oauth2Oauth2CallbackParamError | None = None,
        run_as: Oauth2Oauth2CallbackParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Callback entry point for remote resource responses with OAuth2 authorization codes

        Args:
            state (str)              : Base-64 encoded JSON used to route request within Galaxy.
            code (Oauth2Oauth2CallbackParamCode | None)
                                     :
            error (Oauth2Oauth2CallbackParamError | None)
                                     :
            run-as (Oauth2Oauth2CallbackParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/oauth2_callback"

        params: dict[str, Any] = {
            "state": DataclassSerializer.serialize(state),
            **({"code": DataclassSerializer.serialize(code)} if code is not None else {}),
            **({"error": DataclassSerializer.serialize(error)} if error is not None else {}),
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
