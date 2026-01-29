from typing import Any, Protocol, runtime_checkable

from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import structure_from_dict
from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.role_definition_model import RoleDefinitionModel
from ..models.role_list_response import RoleListResponse
from ..models.role_model_response import RoleModelResponse
from ..models.roles_create_param_run_as import RolesCreateParamRunAs
from ..models.roles_delete_param_run_as import RolesDeleteParamRunAs
from ..models.roles_index_param_run_as import RolesIndexParamRunAs
from ..models.roles_purge_purge_param_run_as import RolesPurgePurgeParamRunAs
from ..models.roles_show_param_run_as import RolesShowParamRunAs
from ..models.roles_undelete_undelete_param_run_as import RolesUndeleteUndeleteParamRunAs


@runtime_checkable
class RolesClientProtocol(Protocol):
    """Protocol defining the interface of RolesClient for dependency injection."""

    async def roles_index(
        self,
        run_as: RolesIndexParamRunAs | None = None,
    ) -> RoleListResponse: ...

    async def roles_index(
        self,
        run_as: RolesIndexParamRunAs | None = None,
    ) -> RoleListResponse: ...

    async def roles_create(
        self,
        body: RoleDefinitionModel,
        run_as: RolesCreateParamRunAs | None = None,
    ) -> RoleModelResponse: ...

    async def roles_create(
        self,
        body: RoleDefinitionModel,
        run_as: RolesCreateParamRunAs | None = None,
    ) -> RoleModelResponse: ...

    async def roles_delete(
        self,
        id_: str,
        run_as: RolesDeleteParamRunAs | None = None,
    ) -> RoleModelResponse: ...

    async def roles_delete(
        self,
        id_: str,
        run_as: RolesDeleteParamRunAs | None = None,
    ) -> RoleModelResponse: ...

    async def roles_show(
        self,
        id_: str,
        run_as: RolesShowParamRunAs | None = None,
    ) -> RoleModelResponse: ...

    async def roles_show(
        self,
        id_: str,
        run_as: RolesShowParamRunAs | None = None,
    ) -> RoleModelResponse: ...

    async def roles_purge_purge(
        self,
        id_: str,
        run_as: RolesPurgePurgeParamRunAs | None = None,
    ) -> RoleModelResponse: ...

    async def roles_purge_purge(
        self,
        id_: str,
        run_as: RolesPurgePurgeParamRunAs | None = None,
    ) -> RoleModelResponse: ...

    async def roles_undelete_undelete(
        self,
        id_: str,
        run_as: RolesUndeleteUndeleteParamRunAs | None = None,
    ) -> RoleModelResponse: ...

    async def roles_undelete_undelete(
        self,
        id_: str,
        run_as: RolesUndeleteUndeleteParamRunAs | None = None,
    ) -> RoleModelResponse: ...


class RolesClient(RolesClientProtocol):
    """Client for roles endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def roles_index(
        self,
        run_as: RolesIndexParamRunAs | None = None,
    ) -> RoleListResponse:
        """
        Index

        Args:
            run-as (RolesIndexParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            RoleListResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/roles"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), RoleListResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def roles_index(
        self,
        run_as: RolesIndexParamRunAs | None = None,
    ) -> RoleListResponse:
        """
        Index

        Args:
            run-as (RolesIndexParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            RoleListResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/roles"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), RoleListResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def roles_create(
        self,
        body: RoleDefinitionModel,
        run_as: RolesCreateParamRunAs | None = None,
    ) -> RoleModelResponse:
        """
        Create

        Args:
            run-as (RolesCreateParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (RoleDefinitionModel): Request body. (json)

        Returns:
            RoleModelResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/roles"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: RoleDefinitionModel = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), RoleModelResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def roles_create(
        self,
        body: RoleDefinitionModel,
        run_as: RolesCreateParamRunAs | None = None,
    ) -> RoleModelResponse:
        """
        Create

        Args:
            run-as (RolesCreateParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (RoleDefinitionModel): Request body. (json)

        Returns:
            RoleModelResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/roles"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: RoleDefinitionModel = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), RoleModelResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def roles_delete(
        self,
        id_: str,
        run_as: RolesDeleteParamRunAs | None = None,
    ) -> RoleModelResponse:
        """
        Delete

        Args:
            id (str)                 : The ID of the role.
            run-as (RolesDeleteParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            RoleModelResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/roles/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), RoleModelResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def roles_delete(
        self,
        id_: str,
        run_as: RolesDeleteParamRunAs | None = None,
    ) -> RoleModelResponse:
        """
        Delete

        Args:
            id (str)                 : The ID of the role.
            run-as (RolesDeleteParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            RoleModelResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/roles/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), RoleModelResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def roles_show(
        self,
        id_: str,
        run_as: RolesShowParamRunAs | None = None,
    ) -> RoleModelResponse:
        """
        Show

        Args:
            id (str)                 : The ID of the role.
            run-as (RolesShowParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            RoleModelResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/roles/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), RoleModelResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def roles_show(
        self,
        id_: str,
        run_as: RolesShowParamRunAs | None = None,
    ) -> RoleModelResponse:
        """
        Show

        Args:
            id (str)                 : The ID of the role.
            run-as (RolesShowParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            RoleModelResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/roles/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), RoleModelResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def roles_purge_purge(
        self,
        id_: str,
        run_as: RolesPurgePurgeParamRunAs | None = None,
    ) -> RoleModelResponse:
        """
        Purge

        Args:
            id (str)                 : The ID of the role.
            run-as (RolesPurgePurgeParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            RoleModelResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/roles/{id_}/purge"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), RoleModelResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def roles_purge_purge(
        self,
        id_: str,
        run_as: RolesPurgePurgeParamRunAs | None = None,
    ) -> RoleModelResponse:
        """
        Purge

        Args:
            id (str)                 : The ID of the role.
            run-as (RolesPurgePurgeParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            RoleModelResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/roles/{id_}/purge"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), RoleModelResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def roles_undelete_undelete(
        self,
        id_: str,
        run_as: RolesUndeleteUndeleteParamRunAs | None = None,
    ) -> RoleModelResponse:
        """
        Undelete

        Args:
            id (str)                 : The ID of the role.
            run-as (RolesUndeleteUndeleteParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            RoleModelResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/roles/{id_}/undelete"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), RoleModelResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def roles_undelete_undelete(
        self,
        id_: str,
        run_as: RolesUndeleteUndeleteParamRunAs | None = None,
    ) -> RoleModelResponse:
        """
        Undelete

        Args:
            id (str)                 : The ID of the role.
            run-as (RolesUndeleteUndeleteParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            RoleModelResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/roles/{id_}/undelete"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), RoleModelResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover
