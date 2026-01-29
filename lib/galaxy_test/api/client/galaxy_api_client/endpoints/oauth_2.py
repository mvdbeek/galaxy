from typing import Any

from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport

from ..models.oauth_2_oauth_2_callback_param_code import Oauth2Oauth2CallbackParamCode
from ..models.oauth_2_oauth_2_callback_param_error import Oauth2Oauth2CallbackParamError
from ..models.oauth_2_oauth_2_callback_param_run_as import Oauth2Oauth2CallbackParamRunAs


class Oauth2Client:
    """Client for oauth2 endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def oauth2_oauth2_callback_2_2(
        self,
        state: str,
        code: Oauth2Oauth2CallbackParamCode | None = None,
        error: Oauth2Oauth2CallbackParamError | None = None,
        run_as: Oauth2Oauth2CallbackParamRunAs | None = None,
    ) -> Any:
        """
        Callback entry point for remote resource responses with OAuth2 authorization codes

        Args:
            state (str)              : Base-64 encoded JSON used to route request within Galaxy.
            code (Optional[Oauth2Oauth2CallbackParamCode])
                                     :
            error (Optional[Oauth2Oauth2CallbackParamError])
                                     :
            run-as (Optional[Oauth2Oauth2CallbackParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/oauth2_callback"

        params: dict[str, Any] = {
            "state": state,
            **({"code": code} if code is not None else {}),
            **({"error": error} if error is not None else {}),
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

    async def oauth2_oauth2_callback_2_2(
        self,
        state: str,
        code: Oauth2Oauth2CallbackParamCode | None = None,
        error: Oauth2Oauth2CallbackParamError | None = None,
        run_as: Oauth2Oauth2CallbackParamRunAs | None = None,
    ) -> Any:
        """
        Callback entry point for remote resource responses with OAuth2 authorization codes

        Args:
            state (str)              : Base-64 encoded JSON used to route request within Galaxy.
            code (Optional[Oauth2Oauth2CallbackParamCode])
                                     :
            error (Optional[Oauth2Oauth2CallbackParamError])
                                     :
            run-as (Optional[Oauth2Oauth2CallbackParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/oauth2_callback"

        params: dict[str, Any] = {
            "state": state,
            **({"code": code} if code is not None else {}),
            **({"error": error} if error is not None else {}),
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
