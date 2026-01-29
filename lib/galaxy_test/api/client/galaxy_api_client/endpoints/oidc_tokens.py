from typing import Any, Protocol, cast, runtime_checkable

from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.remote_files_oidc_tokens_get_token_param_run_as import RemoteFilesOidcTokensGetTokenParamRunAs


@runtime_checkable
class OidcTokensClientProtocol(Protocol):
    """Protocol defining the interface of OidcTokensClient for dependency injection."""

    async def remote_files_oidc_tokens_get_token(
        self,
        job_id: str,
        job_key: str,
        provider: str,
        run_as: RemoteFilesOidcTokensGetTokenParamRunAs | None = None,
    ) -> str: ...


class OidcTokensClient(OidcTokensClientProtocol):
    """Client for oidc_tokens endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def remote_files_oidc_tokens_get_token(
        self,
        job_id: str,
        job_key: str,
        provider: str,
        run_as: RemoteFilesOidcTokensGetTokenParamRunAs | None = None,
    ) -> str:
        """
        Get a fresh OIDC token

        Allows remote job running mechanisms to get a fresh OIDC token that can be used on
        remote side to authorize user. It is not meant to represent part of Galaxy's stable,
        user facing API

        Args:
            job_id (str)             :
            job_key (str)            : A key used to authenticate this request as acting on
                                       behalf or a job runner for the specified job
            provider (str)           : OIDC provider name
            run-as (RemoteFilesOidcTokensGetTokenParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            str: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        job_id = DataclassSerializer.serialize(job_id)

        url = f"{self.base_url}/api/jobs/{job_id}/oidc-tokens"

        params: dict[str, Any] = {
            "job_key": DataclassSerializer.serialize(job_key),
            "provider": DataclassSerializer.serialize(provider),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(str, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover
