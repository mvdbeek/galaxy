from typing import IO, Any, Protocol, cast, runtime_checkable

from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import structure_from_dict
from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.create_libraries_from_store import CreateLibrariesFromStore
from ..models.create_library_payload import CreateLibraryPayload
from ..models.libraries_contents_create_form_200_response import LibrariesContentsCreateForm200Response
from ..models.libraries_contents_create_form_param_run_as import LibrariesContentsCreateFormParamRunAs
from ..models.libraries_contents_delete_param_run_as import LibrariesContentsDeleteParamRunAs
from ..models.libraries_contents_delete_request_body import LibrariesContentsDeleteRequestBody
from ..models.libraries_contents_index_param_run_as import LibrariesContentsIndexParamRunAs
from ..models.libraries_contents_show_200_response import LibrariesContentsShow200Response
from ..models.libraries_contents_show_param_run_as import LibrariesContentsShowParamRunAs
from ..models.libraries_contents_update_param_run_as import LibrariesContentsUpdateParamRunAs
from ..models.libraries_create_param_run_as import LibrariesCreateParamRunAs
from ..models.libraries_delete_param_run_as import LibrariesDeleteParamRunAs
from ..models.libraries_delete_param_undelete import LibrariesDeleteParamUndelete
from ..models.libraries_delete_request_body import LibrariesDeleteRequestBody
from ..models.libraries_deleted_index_deleted_param_run_as import LibrariesDeletedIndexDeletedParamRunAs
from ..models.libraries_from_store_create_from_store_param_run_as import LibrariesFromStoreCreateFromStoreParamRunAs
from ..models.libraries_index_param_deleted import LibrariesIndexParamDeleted
from ..models.libraries_index_param_run_as import LibrariesIndexParamRunAs
from ..models.libraries_permissions_get_permissions_200_response import LibrariesPermissionsGetPermissions200Response
from ..models.libraries_permissions_get_permissions_param_is_library_access import (
    LibrariesPermissionsGetPermissionsParamIsLibraryAccess,
)
from ..models.libraries_permissions_get_permissions_param_q import LibrariesPermissionsGetPermissionsParamQ
from ..models.libraries_permissions_get_permissions_param_run_as import LibrariesPermissionsGetPermissionsParamRunAs
from ..models.libraries_permissions_get_permissions_param_scope import LibrariesPermissionsGetPermissionsParamScope
from ..models.libraries_permissions_set_permissions_200_response import LibrariesPermissionsSetPermissions200Response
from ..models.libraries_permissions_set_permissions_param_action import LibrariesPermissionsSetPermissionsParamAction
from ..models.libraries_permissions_set_permissions_param_run_as import LibrariesPermissionsSetPermissionsParamRunAs
from ..models.libraries_permissions_set_permissions_request_body import LibrariesPermissionsSetPermissionsRequestBody
from ..models.libraries_show_param_run_as import LibrariesShowParamRunAs
from ..models.libraries_update_param_run_as import LibrariesUpdateParamRunAs
from ..models.library_contents_delete_response import LibraryContentsDeleteResponse
from ..models.library_contents_index_list_response import LibraryContentsIndexListResponse
from ..models.library_summary import LibrarySummary
from ..models.library_summary_list import LibrarySummaryList
from ..models.update_library_payload import UpdateLibraryPayload


@runtime_checkable
class LibrariesClientProtocol(Protocol):
    """Protocol defining the interface of LibrariesClient for dependency injection."""

    async def libraries_index(
        self,
        deleted: LibrariesIndexParamDeleted | None = None,
        run_as: LibrariesIndexParamRunAs | None = None,
    ) -> LibrarySummaryList: ...

    async def libraries_index(
        self,
        deleted: LibrariesIndexParamDeleted | None = None,
        run_as: LibrariesIndexParamRunAs | None = None,
    ) -> LibrarySummaryList: ...

    async def libraries_create(
        self,
        body: CreateLibraryPayload,
        run_as: LibrariesCreateParamRunAs | None = None,
    ) -> LibrarySummary: ...

    async def libraries_create(
        self,
        body: CreateLibraryPayload,
        run_as: LibrariesCreateParamRunAs | None = None,
    ) -> LibrarySummary: ...

    async def libraries_deleted_index_deleted(
        self,
        run_as: LibrariesDeletedIndexDeletedParamRunAs | None = None,
    ) -> LibrarySummaryList: ...

    async def libraries_deleted_index_deleted(
        self,
        run_as: LibrariesDeletedIndexDeletedParamRunAs | None = None,
    ) -> LibrarySummaryList: ...

    async def libraries_from_store_create_from_store(
        self,
        body: CreateLibrariesFromStore,
        run_as: LibrariesFromStoreCreateFromStoreParamRunAs | None = None,
    ) -> list[LibrarySummary]: ...

    async def libraries_from_store_create_from_store(
        self,
        body: CreateLibrariesFromStore,
        run_as: LibrariesFromStoreCreateFromStoreParamRunAs | None = None,
    ) -> list[LibrarySummary]: ...

    async def libraries_delete(
        self,
        id_: str,
        undelete: LibrariesDeleteParamUndelete | None = None,
        run_as: LibrariesDeleteParamRunAs | None = None,
        body: LibrariesDeleteRequestBody | None = None,
    ) -> LibrarySummary: ...

    async def libraries_delete(
        self,
        id_: str,
        undelete: LibrariesDeleteParamUndelete | None = None,
        run_as: LibrariesDeleteParamRunAs | None = None,
        body: LibrariesDeleteRequestBody | None = None,
    ) -> LibrarySummary: ...

    async def libraries_show(
        self,
        id_: str,
        run_as: LibrariesShowParamRunAs | None = None,
    ) -> LibrarySummary: ...

    async def libraries_show(
        self,
        id_: str,
        run_as: LibrariesShowParamRunAs | None = None,
    ) -> LibrarySummary: ...

    async def libraries_update(
        self,
        id_: str,
        body: UpdateLibraryPayload,
        run_as: LibrariesUpdateParamRunAs | None = None,
    ) -> LibrarySummary: ...

    async def libraries_update(
        self,
        id_: str,
        body: UpdateLibraryPayload,
        run_as: LibrariesUpdateParamRunAs | None = None,
    ) -> LibrarySummary: ...

    async def libraries_permissions_get_permissions(
        self,
        id_: str,
        scope: LibrariesPermissionsGetPermissionsParamScope | None = None,
        is_library_access: LibrariesPermissionsGetPermissionsParamIsLibraryAccess | None = None,
        page: int | None = None,
        page_limit: int | None = None,
        q: LibrariesPermissionsGetPermissionsParamQ | None = None,
        run_as: LibrariesPermissionsGetPermissionsParamRunAs | None = None,
    ) -> LibrariesPermissionsGetPermissions200Response: ...

    async def libraries_permissions_get_permissions(
        self,
        id_: str,
        scope: LibrariesPermissionsGetPermissionsParamScope | None = None,
        is_library_access: LibrariesPermissionsGetPermissionsParamIsLibraryAccess | None = None,
        page: int | None = None,
        page_limit: int | None = None,
        q: LibrariesPermissionsGetPermissionsParamQ | None = None,
        run_as: LibrariesPermissionsGetPermissionsParamRunAs | None = None,
    ) -> LibrariesPermissionsGetPermissions200Response: ...

    async def libraries_permissions_set_permissions(
        self,
        id_: str,
        body: LibrariesPermissionsSetPermissionsRequestBody,
        action: LibrariesPermissionsSetPermissionsParamAction | None = None,
        run_as: LibrariesPermissionsSetPermissionsParamRunAs | None = None,
    ) -> LibrariesPermissionsSetPermissions200Response: ...

    async def libraries_permissions_set_permissions(
        self,
        id_: str,
        body: LibrariesPermissionsSetPermissionsRequestBody,
        action: LibrariesPermissionsSetPermissionsParamAction | None = None,
        run_as: LibrariesPermissionsSetPermissionsParamRunAs | None = None,
    ) -> LibrariesPermissionsSetPermissions200Response: ...

    async def libraries_contents_index(
        self,
        library_id: str,
        run_as: LibrariesContentsIndexParamRunAs | None = None,
    ) -> LibraryContentsIndexListResponse: ...

    async def libraries_contents_index(
        self,
        library_id: str,
        run_as: LibrariesContentsIndexParamRunAs | None = None,
    ) -> LibraryContentsIndexListResponse: ...

    async def libraries_contents_create_form(
        self,
        library_id: str,
        files: dict[str, IO[Any]],
        run_as: LibrariesContentsCreateFormParamRunAs | None = None,
    ) -> LibrariesContentsCreateForm200Response: ...

    async def libraries_contents_create_form(
        self,
        library_id: str,
        files: dict[str, IO[Any]],
        run_as: LibrariesContentsCreateFormParamRunAs | None = None,
    ) -> LibrariesContentsCreateForm200Response: ...

    async def libraries_contents_delete(
        self,
        library_id: str,
        id_: str,
        run_as: LibrariesContentsDeleteParamRunAs | None = None,
        body: LibrariesContentsDeleteRequestBody | None = None,
    ) -> LibraryContentsDeleteResponse: ...

    async def libraries_contents_delete(
        self,
        library_id: str,
        id_: str,
        run_as: LibrariesContentsDeleteParamRunAs | None = None,
        body: LibrariesContentsDeleteRequestBody | None = None,
    ) -> LibraryContentsDeleteResponse: ...

    async def libraries_contents_show(
        self,
        library_id: str,
        id_: str,
        run_as: LibrariesContentsShowParamRunAs | None = None,
    ) -> LibrariesContentsShow200Response: ...

    async def libraries_contents_show(
        self,
        library_id: str,
        id_: str,
        run_as: LibrariesContentsShowParamRunAs | None = None,
    ) -> LibrariesContentsShow200Response: ...

    async def libraries_contents_update(
        self,
        library_id: str,
        id_: str,
        payload: dict[str, Any],
        run_as: LibrariesContentsUpdateParamRunAs | None = None,
    ) -> dict[str, Any]: ...

    async def libraries_contents_update(
        self,
        library_id: str,
        id_: str,
        payload: dict[str, Any],
        run_as: LibrariesContentsUpdateParamRunAs | None = None,
    ) -> dict[str, Any]: ...


class LibrariesClient(LibrariesClientProtocol):
    """Client for libraries endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def libraries_index(
        self,
        deleted: LibrariesIndexParamDeleted | None = None,
        run_as: LibrariesIndexParamRunAs | None = None,
    ) -> LibrarySummaryList:
        """
        Returns a list of summary data for all libraries.

        Returns a list of summary data for all libraries.

        Args:
            deleted (LibrariesIndexParamDeleted | None)
                                     : Whether to include deleted libraries in the result.
            run-as (LibrariesIndexParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            LibrarySummaryList: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/libraries"

        params: dict[str, Any] = {
            **({"deleted": DataclassSerializer.serialize(deleted)} if deleted is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), LibrarySummaryList)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def libraries_index(
        self,
        deleted: LibrariesIndexParamDeleted | None = None,
        run_as: LibrariesIndexParamRunAs | None = None,
    ) -> LibrarySummaryList:
        """
        Returns a list of summary data for all libraries.

        Returns a list of summary data for all libraries.

        Args:
            deleted (LibrariesIndexParamDeleted | None)
                                     : Whether to include deleted libraries in the result.
            run-as (LibrariesIndexParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            LibrarySummaryList: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/libraries"

        params: dict[str, Any] = {
            **({"deleted": DataclassSerializer.serialize(deleted)} if deleted is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), LibrarySummaryList)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def libraries_create(
        self,
        body: CreateLibraryPayload,
        run_as: LibrariesCreateParamRunAs | None = None,
    ) -> LibrarySummary:
        """
        Creates a new library and returns its summary information.

        Creates a new library and returns its summary information. Currently, only admin users
        can create libraries.

        Args:
            run-as (LibrariesCreateParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateLibraryPayload)
                                     : Request body. (json)

        Returns:
            LibrarySummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/libraries"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: CreateLibraryPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), LibrarySummary)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def libraries_create(
        self,
        body: CreateLibraryPayload,
        run_as: LibrariesCreateParamRunAs | None = None,
    ) -> LibrarySummary:
        """
        Creates a new library and returns its summary information.

        Creates a new library and returns its summary information. Currently, only admin users
        can create libraries.

        Args:
            run-as (LibrariesCreateParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateLibraryPayload)
                                     : Request body. (json)

        Returns:
            LibrarySummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/libraries"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: CreateLibraryPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), LibrarySummary)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def libraries_deleted_index_deleted(
        self,
        run_as: LibrariesDeletedIndexDeletedParamRunAs | None = None,
    ) -> LibrarySummaryList:
        """
        Returns a list of summary data for all libraries marked as deleted.

        Returns a list of summary data for all libraries marked as deleted.

        Args:
            run-as (LibrariesDeletedIndexDeletedParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            LibrarySummaryList: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/libraries/deleted"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), LibrarySummaryList)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def libraries_deleted_index_deleted(
        self,
        run_as: LibrariesDeletedIndexDeletedParamRunAs | None = None,
    ) -> LibrarySummaryList:
        """
        Returns a list of summary data for all libraries marked as deleted.

        Returns a list of summary data for all libraries marked as deleted.

        Args:
            run-as (LibrariesDeletedIndexDeletedParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            LibrarySummaryList: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/libraries/deleted"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), LibrarySummaryList)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def libraries_from_store_create_from_store(
        self,
        body: CreateLibrariesFromStore,
        run_as: LibrariesFromStoreCreateFromStoreParamRunAs | None = None,
    ) -> list[LibrarySummary]:
        """
        Create libraries from a model store.

        Args:
            run-as (LibrariesFromStoreCreateFromStoreParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateLibrariesFromStore)
                                     : Request body. (json)

        Returns:
            List[LibrarySummary]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/libraries/from_store"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: CreateLibrariesFromStore = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[LibrarySummary])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def libraries_from_store_create_from_store(
        self,
        body: CreateLibrariesFromStore,
        run_as: LibrariesFromStoreCreateFromStoreParamRunAs | None = None,
    ) -> list[LibrarySummary]:
        """
        Create libraries from a model store.

        Args:
            run-as (LibrariesFromStoreCreateFromStoreParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateLibrariesFromStore)
                                     : Request body. (json)

        Returns:
            List[LibrarySummary]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/libraries/from_store"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: CreateLibrariesFromStore = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[LibrarySummary])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def libraries_delete(
        self,
        id_: str,
        undelete: LibrariesDeleteParamUndelete | None = None,
        run_as: LibrariesDeleteParamRunAs | None = None,
        body: LibrariesDeleteRequestBody | None = None,
    ) -> LibrarySummary:
        """
        Marks the specified library as deleted (or undeleted).

        Marks the specified library as deleted (or undeleted). Currently, only admin users can
        delete or restore libraries.

        Args:
            id (str)                 : The ID of the Library.
            undelete (LibrariesDeleteParamUndelete | None)
                                     : Whether to restore a deleted library.
            run-as (LibrariesDeleteParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (LibrariesDeleteRequestBody | None)
                                     : Request body. (json)

        Returns:
            LibrarySummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/libraries/{id_}"

        params: dict[str, Any] = {
            **({"undelete": DataclassSerializer.serialize(undelete)} if undelete is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: LibrariesDeleteRequestBody | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("DELETE", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), LibrarySummary)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def libraries_delete(
        self,
        id_: str,
        undelete: LibrariesDeleteParamUndelete | None = None,
        run_as: LibrariesDeleteParamRunAs | None = None,
        body: LibrariesDeleteRequestBody | None = None,
    ) -> LibrarySummary:
        """
        Marks the specified library as deleted (or undeleted).

        Marks the specified library as deleted (or undeleted). Currently, only admin users can
        delete or restore libraries.

        Args:
            id (str)                 : The ID of the Library.
            undelete (LibrariesDeleteParamUndelete | None)
                                     : Whether to restore a deleted library.
            run-as (LibrariesDeleteParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (LibrariesDeleteRequestBody | None)
                                     : Request body. (json)

        Returns:
            LibrarySummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/libraries/{id_}"

        params: dict[str, Any] = {
            **({"undelete": DataclassSerializer.serialize(undelete)} if undelete is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: LibrariesDeleteRequestBody | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("DELETE", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), LibrarySummary)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def libraries_show(
        self,
        id_: str,
        run_as: LibrariesShowParamRunAs | None = None,
    ) -> LibrarySummary:
        """
        Returns summary information about a particular library.

        Returns summary information about a particular library.

        Args:
            id (str)                 : The ID of the Library.
            run-as (LibrariesShowParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            LibrarySummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/libraries/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), LibrarySummary)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def libraries_show(
        self,
        id_: str,
        run_as: LibrariesShowParamRunAs | None = None,
    ) -> LibrarySummary:
        """
        Returns summary information about a particular library.

        Returns summary information about a particular library.

        Args:
            id (str)                 : The ID of the Library.
            run-as (LibrariesShowParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            LibrarySummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/libraries/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), LibrarySummary)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def libraries_update(
        self,
        id_: str,
        body: UpdateLibraryPayload,
        run_as: LibrariesUpdateParamRunAs | None = None,
    ) -> LibrarySummary:
        """
        Updates the information of an existing library.

        Updates the information of an existing library.

        Args:
            id (str)                 : The ID of the Library.
            run-as (LibrariesUpdateParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UpdateLibraryPayload)
                                     : Request body. (json)

        Returns:
            LibrarySummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/libraries/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: UpdateLibraryPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PATCH", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), LibrarySummary)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def libraries_update(
        self,
        id_: str,
        body: UpdateLibraryPayload,
        run_as: LibrariesUpdateParamRunAs | None = None,
    ) -> LibrarySummary:
        """
        Updates the information of an existing library.

        Updates the information of an existing library.

        Args:
            id (str)                 : The ID of the Library.
            run-as (LibrariesUpdateParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UpdateLibraryPayload)
                                     : Request body. (json)

        Returns:
            LibrarySummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/libraries/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: UpdateLibraryPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PATCH", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), LibrarySummary)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def libraries_permissions_get_permissions(
        self,
        id_: str,
        scope: LibrariesPermissionsGetPermissionsParamScope | None = None,
        is_library_access: LibrariesPermissionsGetPermissionsParamIsLibraryAccess | None = None,
        page: int | None = None,
        page_limit: int | None = None,
        q: LibrariesPermissionsGetPermissionsParamQ | None = None,
        run_as: LibrariesPermissionsGetPermissionsParamRunAs | None = None,
    ) -> LibrariesPermissionsGetPermissions200Response:
        """
        Gets the current or available permissions of a particular library.

        Gets the current or available permissions of a particular library. The results can be
        paginated and additionally filtered by a query.

        Args:
            id (str)                 : The ID of the Library.
            scope (LibrariesPermissionsGetPermissionsParamScope | None)
                                     : The scope of the permissions to retrieve. Either the
                                       `current` permissions or the `available`.
            is_library_access (LibrariesPermissionsGetPermissionsParamIsLibraryAccess | None)
                                     : Indicates whether the roles available for the library
                                       access are requested.
            page (int | None)        : The page number to retrieve when paginating the available
                                       roles.
            page_limit (int | None)  : The maximum number of permissions per page when
                                       paginating.
            q (LibrariesPermissionsGetPermissionsParamQ | None)
                                     : Optional search text to retrieve only the roles matching
                                       this query.
            run-as (LibrariesPermissionsGetPermissionsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            LibrariesPermissionsGetPermissions200Response: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/libraries/{id_}/permissions"

        params: dict[str, Any] = {
            **({"scope": DataclassSerializer.serialize(scope)} if scope is not None else {}),
            **(
                {"is_library_access": DataclassSerializer.serialize(is_library_access)}
                if is_library_access is not None
                else {}
            ),
            **({"page": DataclassSerializer.serialize(page)} if page is not None else {}),
            **({"page_limit": DataclassSerializer.serialize(page_limit)} if page_limit is not None else {}),
            **({"q": DataclassSerializer.serialize(q)} if q is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), LibrariesPermissionsGetPermissions200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def libraries_permissions_get_permissions(
        self,
        id_: str,
        scope: LibrariesPermissionsGetPermissionsParamScope | None = None,
        is_library_access: LibrariesPermissionsGetPermissionsParamIsLibraryAccess | None = None,
        page: int | None = None,
        page_limit: int | None = None,
        q: LibrariesPermissionsGetPermissionsParamQ | None = None,
        run_as: LibrariesPermissionsGetPermissionsParamRunAs | None = None,
    ) -> LibrariesPermissionsGetPermissions200Response:
        """
        Gets the current or available permissions of a particular library.

        Gets the current or available permissions of a particular library. The results can be
        paginated and additionally filtered by a query.

        Args:
            id (str)                 : The ID of the Library.
            scope (LibrariesPermissionsGetPermissionsParamScope | None)
                                     : The scope of the permissions to retrieve. Either the
                                       `current` permissions or the `available`.
            is_library_access (LibrariesPermissionsGetPermissionsParamIsLibraryAccess | None)
                                     : Indicates whether the roles available for the library
                                       access are requested.
            page (int | None)        : The page number to retrieve when paginating the available
                                       roles.
            page_limit (int | None)  : The maximum number of permissions per page when
                                       paginating.
            q (LibrariesPermissionsGetPermissionsParamQ | None)
                                     : Optional search text to retrieve only the roles matching
                                       this query.
            run-as (LibrariesPermissionsGetPermissionsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            LibrariesPermissionsGetPermissions200Response: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/libraries/{id_}/permissions"

        params: dict[str, Any] = {
            **({"scope": DataclassSerializer.serialize(scope)} if scope is not None else {}),
            **(
                {"is_library_access": DataclassSerializer.serialize(is_library_access)}
                if is_library_access is not None
                else {}
            ),
            **({"page": DataclassSerializer.serialize(page)} if page is not None else {}),
            **({"page_limit": DataclassSerializer.serialize(page_limit)} if page_limit is not None else {}),
            **({"q": DataclassSerializer.serialize(q)} if q is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), LibrariesPermissionsGetPermissions200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def libraries_permissions_set_permissions(
        self,
        id_: str,
        body: LibrariesPermissionsSetPermissionsRequestBody,
        action: LibrariesPermissionsSetPermissionsParamAction | None = None,
        run_as: LibrariesPermissionsSetPermissionsParamRunAs | None = None,
    ) -> LibrariesPermissionsSetPermissions200Response:
        """
        Sets the permissions to access and manipulate a library.

        Sets the permissions to access and manipulate a library.

        Args:
            id (str)                 : The ID of the Library.
            action (LibrariesPermissionsSetPermissionsParamAction | None)
                                     : Indicates what action should be performed on the Library.
            run-as (LibrariesPermissionsSetPermissionsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (LibrariesPermissionsSetPermissionsRequestBody)
                                     : Request body. (json)

        Returns:
            LibrariesPermissionsSetPermissions200Response: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/libraries/{id_}/permissions"

        params: dict[str, Any] = {
            **({"action": DataclassSerializer.serialize(action)} if action is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: LibrariesPermissionsSetPermissionsRequestBody = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), LibrariesPermissionsSetPermissions200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def libraries_permissions_set_permissions(
        self,
        id_: str,
        body: LibrariesPermissionsSetPermissionsRequestBody,
        action: LibrariesPermissionsSetPermissionsParamAction | None = None,
        run_as: LibrariesPermissionsSetPermissionsParamRunAs | None = None,
    ) -> LibrariesPermissionsSetPermissions200Response:
        """
        Sets the permissions to access and manipulate a library.

        Sets the permissions to access and manipulate a library.

        Args:
            id (str)                 : The ID of the Library.
            action (LibrariesPermissionsSetPermissionsParamAction | None)
                                     : Indicates what action should be performed on the Library.
            run-as (LibrariesPermissionsSetPermissionsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (LibrariesPermissionsSetPermissionsRequestBody)
                                     : Request body. (json)

        Returns:
            LibrariesPermissionsSetPermissions200Response: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/libraries/{id_}/permissions"

        params: dict[str, Any] = {
            **({"action": DataclassSerializer.serialize(action)} if action is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: LibrariesPermissionsSetPermissionsRequestBody = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), LibrariesPermissionsSetPermissions200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def libraries_contents_index(
        self,
        library_id: str,
        run_as: LibrariesContentsIndexParamRunAs | None = None,
    ) -> LibraryContentsIndexListResponse:
        """
        Return a list of library files and folders.

        This endpoint is deprecated. Please use GET /api/folders/{folder_id}/contents instead.

        Args:
            library_id (str)         : The ID of the Library.
            run-as (LibrariesContentsIndexParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            LibraryContentsIndexListResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        library_id = DataclassSerializer.serialize(library_id)

        url = f"{self.base_url}/api/libraries/{library_id}/contents"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(LibraryContentsIndexListResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def libraries_contents_index(
        self,
        library_id: str,
        run_as: LibrariesContentsIndexParamRunAs | None = None,
    ) -> LibraryContentsIndexListResponse:
        """
        Return a list of library files and folders.

        This endpoint is deprecated. Please use GET /api/folders/{folder_id}/contents instead.

        Args:
            library_id (str)         : The ID of the Library.
            run-as (LibrariesContentsIndexParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            LibraryContentsIndexListResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        library_id = DataclassSerializer.serialize(library_id)

        url = f"{self.base_url}/api/libraries/{library_id}/contents"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(LibraryContentsIndexListResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def libraries_contents_create_form(
        self,
        library_id: str,
        files: dict[str, IO[Any]],
        run_as: LibrariesContentsCreateFormParamRunAs | None = None,
    ) -> LibrariesContentsCreateForm200Response:
        """
        Create a new library file or folder.

        This endpoint is deprecated. Please use POST /api/folders/{folder_id} or POST
        /api/folders/{folder_id}/contents instead.

        Args:
            library_id (str)         : The ID of the Library.
            run-as (LibrariesContentsCreateFormParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            files (dict[str, IO[Any]]): Request body. (multipart/form-data)

        Returns:
            LibrariesContentsCreateForm200Response: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        library_id = DataclassSerializer.serialize(library_id)

        url = f"{self.base_url}/api/libraries/{library_id}/contents"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        files_data: dict[str, IO[Any]] = DataclassSerializer.serialize(files)

        response = await self._transport.request("POST", url, params=None, files=files_data, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), LibrariesContentsCreateForm200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def libraries_contents_create_form(
        self,
        library_id: str,
        files: dict[str, IO[Any]],
        run_as: LibrariesContentsCreateFormParamRunAs | None = None,
    ) -> LibrariesContentsCreateForm200Response:
        """
        Create a new library file or folder.

        This endpoint is deprecated. Please use POST /api/folders/{folder_id} or POST
        /api/folders/{folder_id}/contents instead.

        Args:
            library_id (str)         : The ID of the Library.
            run-as (LibrariesContentsCreateFormParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            files (dict[str, IO[Any]]): Request body. (multipart/form-data)

        Returns:
            LibrariesContentsCreateForm200Response: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        library_id = DataclassSerializer.serialize(library_id)

        url = f"{self.base_url}/api/libraries/{library_id}/contents"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        files_data: dict[str, IO[Any]] = DataclassSerializer.serialize(files)

        response = await self._transport.request("POST", url, params=None, files=files_data, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), LibrariesContentsCreateForm200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def libraries_contents_delete(
        self,
        library_id: str,
        id_: str,
        run_as: LibrariesContentsDeleteParamRunAs | None = None,
        body: LibrariesContentsDeleteRequestBody | None = None,
    ) -> LibraryContentsDeleteResponse:
        """
        Delete a library file or folder.

        This endpoint is deprecated. Please use DELETE /api/libraries/datasets/{id} instead.

        Args:
            library_id (str)         : The ID of the Library.
            id (str)                 : The encoded ID of the library dataset.
            run-as (LibrariesContentsDeleteParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (LibrariesContentsDeleteRequestBody | None)
                                     : Request body. (json)

        Returns:
            LibraryContentsDeleteResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        library_id = DataclassSerializer.serialize(library_id)
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/libraries/{library_id}/contents/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: LibrariesContentsDeleteRequestBody | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("DELETE", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), LibraryContentsDeleteResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def libraries_contents_delete(
        self,
        library_id: str,
        id_: str,
        run_as: LibrariesContentsDeleteParamRunAs | None = None,
        body: LibrariesContentsDeleteRequestBody | None = None,
    ) -> LibraryContentsDeleteResponse:
        """
        Delete a library file or folder.

        This endpoint is deprecated. Please use DELETE /api/libraries/datasets/{id} instead.

        Args:
            library_id (str)         : The ID of the Library.
            id (str)                 : The encoded ID of the library dataset.
            run-as (LibrariesContentsDeleteParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (LibrariesContentsDeleteRequestBody | None)
                                     : Request body. (json)

        Returns:
            LibraryContentsDeleteResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        library_id = DataclassSerializer.serialize(library_id)
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/libraries/{library_id}/contents/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: LibrariesContentsDeleteRequestBody | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("DELETE", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), LibraryContentsDeleteResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def libraries_contents_show(
        self,
        library_id: str,
        id_: str,
        run_as: LibrariesContentsShowParamRunAs | None = None,
    ) -> LibrariesContentsShow200Response:
        """
        Return a library file or folder.

        This endpoint is deprecated. Please use GET /api/libraries/datasets/{id} instead.

        Args:
            library_id (str)         : The ID of the Library.
            id (str)                 :
            run-as (LibrariesContentsShowParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            LibrariesContentsShow200Response: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        library_id = DataclassSerializer.serialize(library_id)
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/libraries/{library_id}/contents/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), LibrariesContentsShow200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def libraries_contents_show(
        self,
        library_id: str,
        id_: str,
        run_as: LibrariesContentsShowParamRunAs | None = None,
    ) -> LibrariesContentsShow200Response:
        """
        Return a library file or folder.

        This endpoint is deprecated. Please use GET /api/libraries/datasets/{id} instead.

        Args:
            library_id (str)         : The ID of the Library.
            id (str)                 :
            run-as (LibrariesContentsShowParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            LibrariesContentsShow200Response: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        library_id = DataclassSerializer.serialize(library_id)
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/libraries/{library_id}/contents/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), LibrariesContentsShow200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def libraries_contents_update(
        self,
        library_id: str,
        id_: str,
        payload: dict[str, Any],
        run_as: LibrariesContentsUpdateParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Update a library file or folder.

        This endpoint is deprecated. Please use PATCH /api/libraries/datasets/{id} instead.

        Args:
            library_id (str)         : The ID of the Library.
            id (str)                 : The encoded ID of the library dataset.
            payload (dict[str, Any]) :
            run-as (LibrariesContentsUpdateParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        library_id = DataclassSerializer.serialize(library_id)
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/libraries/{library_id}/contents/{id_}"

        params: dict[str, Any] = {
            "payload": DataclassSerializer.serialize(payload),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def libraries_contents_update(
        self,
        library_id: str,
        id_: str,
        payload: dict[str, Any],
        run_as: LibrariesContentsUpdateParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Update a library file or folder.

        This endpoint is deprecated. Please use PATCH /api/libraries/datasets/{id} instead.

        Args:
            library_id (str)         : The ID of the Library.
            id (str)                 : The encoded ID of the library dataset.
            payload (dict[str, Any]) :
            run-as (LibrariesContentsUpdateParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        library_id = DataclassSerializer.serialize(library_id)
        id_ = DataclassSerializer.serialize(id_)

        url = f"{self.base_url}/api/libraries/{library_id}/contents/{id_}"

        params: dict[str, Any] = {
            "payload": DataclassSerializer.serialize(payload),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover
