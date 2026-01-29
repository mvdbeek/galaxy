from typing import Any, Protocol, cast, runtime_checkable

from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.forms_delete_param_run_as import FormsDeleteParamRunAs
from ..models.forms_undelete_undelete_param_run_as import FormsUndeleteUndeleteParamRunAs


@runtime_checkable
class FormsClientProtocol(Protocol):
    """Protocol defining the interface of FormsClient for dependency injection."""

    async def forms_delete(
        self,
        id_: str,
        run_as: FormsDeleteParamRunAs | None = None,
    ) -> dict[str, Any]: ...

    async def forms_delete(
        self,
        id_: str,
        run_as: FormsDeleteParamRunAs | None = None,
    ) -> dict[str, Any]: ...

    async def forms_undelete_undelete(
        self,
        id_: str,
        run_as: FormsUndeleteUndeleteParamRunAs | None = None,
    ) -> dict[str, Any]: ...

    async def forms_undelete_undelete(
        self,
        id_: str,
        run_as: FormsUndeleteUndeleteParamRunAs | None = None,
    ) -> dict[str, Any]: ...


class FormsClient(FormsClientProtocol):
    """Client for forms endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def forms_delete(
        self,
        id_: str,
        run_as: FormsDeleteParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Delete

        Args:
            id (str)                 : The encoded database identifier of the form.
            run-as (FormsDeleteParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/forms/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def forms_delete(
        self,
        id_: str,
        run_as: FormsDeleteParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Delete

        Args:
            id (str)                 : The encoded database identifier of the form.
            run-as (FormsDeleteParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/forms/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def forms_undelete_undelete(
        self,
        id_: str,
        run_as: FormsUndeleteUndeleteParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Undelete

        Args:
            id (str)                 : The encoded database identifier of the form.
            run-as (FormsUndeleteUndeleteParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/forms/{id_}/undelete"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def forms_undelete_undelete(
        self,
        id_: str,
        run_as: FormsUndeleteUndeleteParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Undelete

        Args:
            id (str)                 : The encoded database identifier of the form.
            run-as (FormsUndeleteUndeleteParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/forms/{id_}/undelete"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover
