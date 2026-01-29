from typing import IO, Any, cast

from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.create_libraries_from_store import CreateLibrariesFromStore
from ..models.create_library_payload import CreateLibraryPayload
from ..models.libraries_contents_create_form_200_response_2 import LibrariesContentsCreateForm200Response2
from ..models.libraries_contents_create_form_param_run_as import LibrariesContentsCreateFormParamRunAs
from ..models.libraries_contents_delete_param_run_as import LibrariesContentsDeleteParamRunAs
from ..models.libraries_contents_delete_request_body_2 import LibrariesContentsDeleteRequestBody2
from ..models.libraries_contents_index_param_run_as import LibrariesContentsIndexParamRunAs
from ..models.libraries_contents_show_200_response_2 import LibrariesContentsShow200Response2
from ..models.libraries_contents_show_param_run_as import LibrariesContentsShowParamRunAs
from ..models.libraries_contents_update_param_run_as import LibrariesContentsUpdateParamRunAs
from ..models.libraries_create_param_run_as import LibrariesCreateParamRunAs
from ..models.libraries_delete_param_run_as import LibrariesDeleteParamRunAs
from ..models.libraries_delete_param_undelete import LibrariesDeleteParamUndelete
from ..models.libraries_delete_request_body_2 import LibrariesDeleteRequestBody2
from ..models.libraries_deleted_index_deleted_param_run_as import LibrariesDeletedIndexDeletedParamRunAs
from ..models.libraries_from_store_create_from_store_param_run_as import LibrariesFromStoreCreateFromStoreParamRunAs
from ..models.libraries_index_param_deleted import LibrariesIndexParamDeleted
from ..models.libraries_index_param_run_as import LibrariesIndexParamRunAs
from ..models.libraries_permissions_get_permissions_200_response_2 import LibrariesPermissionsGetPermissions200Response2
from ..models.libraries_permissions_get_permissions_param_is_library_access import (
    LibrariesPermissionsGetPermissionsParamIsLibraryAccess,
)
from ..models.libraries_permissions_get_permissions_param_q import LibrariesPermissionsGetPermissionsParamQ
from ..models.libraries_permissions_get_permissions_param_run_as import LibrariesPermissionsGetPermissionsParamRunAs
from ..models.libraries_permissions_get_permissions_param_scope import LibrariesPermissionsGetPermissionsParamScope
from ..models.libraries_permissions_set_permissions_200_response_2 import LibrariesPermissionsSetPermissions200Response2
from ..models.libraries_permissions_set_permissions_param_action import LibrariesPermissionsSetPermissionsParamAction
from ..models.libraries_permissions_set_permissions_param_run_as import LibrariesPermissionsSetPermissionsParamRunAs
from ..models.libraries_permissions_set_permissions_request_body_2 import LibrariesPermissionsSetPermissionsRequestBody2
from ..models.libraries_show_param_run_as import LibrariesShowParamRunAs
from ..models.libraries_update_param_run_as import LibrariesUpdateParamRunAs
from ..models.library_contents_delete_response import LibraryContentsDeleteResponse
from ..models.library_contents_index_list_response import LibraryContentsIndexListResponse
from ..models.library_summary import LibrarySummary
from ..models.library_summary_list import LibrarySummaryList
from ..models.update_library_payload import UpdateLibraryPayload


class LibrariesClient:
    """Client for libraries endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def libraries_index_2_2(
        self,
        deleted: LibrariesIndexParamDeleted | None = None,
        run_as: LibrariesIndexParamRunAs | None = None,
    ) -> LibrarySummaryList:
        """
        Returns a list of summary data for all libraries.

        Returns a list of summary data for all libraries.

        Args:
            deleted (Optional[LibrariesIndexParamDeleted])
                                     : Whether to include deleted libraries in the result.
            run-as (Optional[LibrariesIndexParamRunAs])
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
            **({"deleted": deleted} if deleted is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(LibrarySummaryList, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def libraries_index_2_2(
        self,
        deleted: LibrariesIndexParamDeleted | None = None,
        run_as: LibrariesIndexParamRunAs | None = None,
    ) -> LibrarySummaryList:
        """
        Returns a list of summary data for all libraries.

        Returns a list of summary data for all libraries.

        Args:
            deleted (Optional[LibrariesIndexParamDeleted])
                                     : Whether to include deleted libraries in the result.
            run-as (Optional[LibrariesIndexParamRunAs])
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
            **({"deleted": deleted} if deleted is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(LibrarySummaryList, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def libraries_create_2_2(
        self,
        body: CreateLibraryPayload,
        run_as: LibrariesCreateParamRunAs | None = None,
    ) -> LibrarySummary:
        """
        Creates a new library and returns its summary information.

        Creates a new library and returns its summary information. Currently, only admin users
        can create libraries.

        Args:
            run-as (Optional[LibrariesCreateParamRunAs])
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
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateLibraryPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(LibrarySummary, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def libraries_create_2_2(
        self,
        body: CreateLibraryPayload,
        run_as: LibrariesCreateParamRunAs | None = None,
    ) -> LibrarySummary:
        """
        Creates a new library and returns its summary information.

        Creates a new library and returns its summary information. Currently, only admin users
        can create libraries.

        Args:
            run-as (Optional[LibrariesCreateParamRunAs])
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
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateLibraryPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(LibrarySummary, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def libraries_deleted_index_deleted_2_2(
        self,
        run_as: LibrariesDeletedIndexDeletedParamRunAs | None = None,
    ) -> LibrarySummaryList:
        """
        Returns a list of summary data for all libraries marked as deleted.

        Returns a list of summary data for all libraries marked as deleted.

        Args:
            run-as (Optional[LibrariesDeletedIndexDeletedParamRunAs])
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
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(LibrarySummaryList, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def libraries_deleted_index_deleted_2_2(
        self,
        run_as: LibrariesDeletedIndexDeletedParamRunAs | None = None,
    ) -> LibrarySummaryList:
        """
        Returns a list of summary data for all libraries marked as deleted.

        Returns a list of summary data for all libraries marked as deleted.

        Args:
            run-as (Optional[LibrariesDeletedIndexDeletedParamRunAs])
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
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(LibrarySummaryList, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def libraries_from_store_create_from_store_2_2(
        self,
        body: CreateLibrariesFromStore,
        run_as: LibrariesFromStoreCreateFromStoreParamRunAs | None = None,
    ) -> list[LibrarySummary]:
        """
        Create libraries from a model store.

        Args:
            run-as (Optional[LibrariesFromStoreCreateFromStoreParamRunAs])
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
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateLibrariesFromStore = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[LibrarySummary], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def libraries_from_store_create_from_store_2_2(
        self,
        body: CreateLibrariesFromStore,
        run_as: LibrariesFromStoreCreateFromStoreParamRunAs | None = None,
    ) -> list[LibrarySummary]:
        """
        Create libraries from a model store.

        Args:
            run-as (Optional[LibrariesFromStoreCreateFromStoreParamRunAs])
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
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateLibrariesFromStore = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[LibrarySummary], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def libraries_delete_2_2(
        self,
        id_: str,
        undelete: LibrariesDeleteParamUndelete | None = None,
        run_as: LibrariesDeleteParamRunAs | None = None,
        body: LibrariesDeleteRequestBody2 | None = None,
    ) -> LibrarySummary:
        """
        Marks the specified library as deleted (or undeleted).

        Marks the specified library as deleted (or undeleted). Currently, only admin users can
        delete or restore libraries.

        Args:
            id (str)                 : The ID of the Library.
            undelete (Optional[LibrariesDeleteParamUndelete])
                                     : Whether to restore a deleted library.
            run-as (Optional[LibrariesDeleteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (Optional[LibrariesDeleteRequestBody2])
                                     : Request body. (json)

        Returns:
            LibrarySummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/libraries/{id_}"

        params: dict[str, Any] = {
            **({"undelete": undelete} if undelete is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: LibrariesDeleteRequestBody2 | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("DELETE", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(LibrarySummary, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def libraries_delete_2_2(
        self,
        id_: str,
        undelete: LibrariesDeleteParamUndelete | None = None,
        run_as: LibrariesDeleteParamRunAs | None = None,
        body: LibrariesDeleteRequestBody2 | None = None,
    ) -> LibrarySummary:
        """
        Marks the specified library as deleted (or undeleted).

        Marks the specified library as deleted (or undeleted). Currently, only admin users can
        delete or restore libraries.

        Args:
            id (str)                 : The ID of the Library.
            undelete (Optional[LibrariesDeleteParamUndelete])
                                     : Whether to restore a deleted library.
            run-as (Optional[LibrariesDeleteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (Optional[LibrariesDeleteRequestBody2])
                                     : Request body. (json)

        Returns:
            LibrarySummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/libraries/{id_}"

        params: dict[str, Any] = {
            **({"undelete": undelete} if undelete is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: LibrariesDeleteRequestBody2 | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("DELETE", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(LibrarySummary, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def libraries_show_2_2(
        self,
        id_: str,
        run_as: LibrariesShowParamRunAs | None = None,
    ) -> LibrarySummary:
        """
        Returns summary information about a particular library.

        Returns summary information about a particular library.

        Args:
            id (str)                 : The ID of the Library.
            run-as (Optional[LibrariesShowParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            LibrarySummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/libraries/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(LibrarySummary, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def libraries_show_2_2(
        self,
        id_: str,
        run_as: LibrariesShowParamRunAs | None = None,
    ) -> LibrarySummary:
        """
        Returns summary information about a particular library.

        Returns summary information about a particular library.

        Args:
            id (str)                 : The ID of the Library.
            run-as (Optional[LibrariesShowParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            LibrarySummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/libraries/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(LibrarySummary, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def libraries_update_2_2(
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
            run-as (Optional[LibrariesUpdateParamRunAs])
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
        url = f"{self.base_url}/api/libraries/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: UpdateLibraryPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PATCH", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(LibrarySummary, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def libraries_update_2_2(
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
            run-as (Optional[LibrariesUpdateParamRunAs])
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
        url = f"{self.base_url}/api/libraries/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: UpdateLibraryPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PATCH", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(LibrarySummary, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def libraries_permissions_get_permissions_2_2(
        self,
        id_: str,
        scope: LibrariesPermissionsGetPermissionsParamScope | None = None,
        is_library_access: LibrariesPermissionsGetPermissionsParamIsLibraryAccess | None = None,
        page: int | None = 1,
        page_limit: int | None = 10,
        q: LibrariesPermissionsGetPermissionsParamQ | None = None,
        run_as: LibrariesPermissionsGetPermissionsParamRunAs | None = None,
    ) -> LibrariesPermissionsGetPermissions200Response2:
        """
        Gets the current or available permissions of a particular library.

        Gets the current or available permissions of a particular library. The results can be
        paginated and additionally filtered by a query.

        Args:
            id (str)                 : The ID of the Library.
            scope (Optional[LibrariesPermissionsGetPermissionsParamScope])
                                     : The scope of the permissions to retrieve. Either the
                                       `current` permissions or the `available`.
            is_library_access (Optional[LibrariesPermissionsGetPermissionsParamIsLibraryAccess])
                                     : Indicates whether the roles available for the library
                                       access are requested.
            page (Optional[int])     : The page number to retrieve when paginating the available
                                       roles.
            page_limit (Optional[int]): The maximum number of permissions per page when
                                        paginating.
            q (Optional[LibrariesPermissionsGetPermissionsParamQ])
                                     : Optional search text to retrieve only the roles matching
                                       this query.
            run-as (Optional[LibrariesPermissionsGetPermissionsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            LibrariesPermissionsGetPermissions200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/libraries/{id_}/permissions"

        params: dict[str, Any] = {
            **({"scope": scope} if scope is not None else {}),
            **({"is_library_access": is_library_access} if is_library_access is not None else {}),
            **({"page": page} if page is not None else {}),
            **({"page_limit": page_limit} if page_limit is not None else {}),
            **({"q": q} if q is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(LibrariesPermissionsGetPermissions200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def libraries_permissions_get_permissions_2_2(
        self,
        id_: str,
        scope: LibrariesPermissionsGetPermissionsParamScope | None = None,
        is_library_access: LibrariesPermissionsGetPermissionsParamIsLibraryAccess | None = None,
        page: int | None = 1,
        page_limit: int | None = 10,
        q: LibrariesPermissionsGetPermissionsParamQ | None = None,
        run_as: LibrariesPermissionsGetPermissionsParamRunAs | None = None,
    ) -> LibrariesPermissionsGetPermissions200Response2:
        """
        Gets the current or available permissions of a particular library.

        Gets the current or available permissions of a particular library. The results can be
        paginated and additionally filtered by a query.

        Args:
            id (str)                 : The ID of the Library.
            scope (Optional[LibrariesPermissionsGetPermissionsParamScope])
                                     : The scope of the permissions to retrieve. Either the
                                       `current` permissions or the `available`.
            is_library_access (Optional[LibrariesPermissionsGetPermissionsParamIsLibraryAccess])
                                     : Indicates whether the roles available for the library
                                       access are requested.
            page (Optional[int])     : The page number to retrieve when paginating the available
                                       roles.
            page_limit (Optional[int]): The maximum number of permissions per page when
                                        paginating.
            q (Optional[LibrariesPermissionsGetPermissionsParamQ])
                                     : Optional search text to retrieve only the roles matching
                                       this query.
            run-as (Optional[LibrariesPermissionsGetPermissionsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            LibrariesPermissionsGetPermissions200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/libraries/{id_}/permissions"

        params: dict[str, Any] = {
            **({"scope": scope} if scope is not None else {}),
            **({"is_library_access": is_library_access} if is_library_access is not None else {}),
            **({"page": page} if page is not None else {}),
            **({"page_limit": page_limit} if page_limit is not None else {}),
            **({"q": q} if q is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(LibrariesPermissionsGetPermissions200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def libraries_permissions_set_permissions_2_2(
        self,
        id_: str,
        body: LibrariesPermissionsSetPermissionsRequestBody2,
        action: LibrariesPermissionsSetPermissionsParamAction | None = None,
        run_as: LibrariesPermissionsSetPermissionsParamRunAs | None = None,
    ) -> LibrariesPermissionsSetPermissions200Response2:
        """
        Sets the permissions to access and manipulate a library.

        Sets the permissions to access and manipulate a library.

        Args:
            id (str)                 : The ID of the Library.
            action (Optional[LibrariesPermissionsSetPermissionsParamAction])
                                     : Indicates what action should be performed on the Library.
            run-as (Optional[LibrariesPermissionsSetPermissionsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (LibrariesPermissionsSetPermissionsRequestBody2)
                                     : Request body. (json)

        Returns:
            LibrariesPermissionsSetPermissions200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/libraries/{id_}/permissions"

        params: dict[str, Any] = {
            **({"action": action} if action is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: LibrariesPermissionsSetPermissionsRequestBody2 = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(LibrariesPermissionsSetPermissions200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def libraries_permissions_set_permissions_2_2(
        self,
        id_: str,
        body: LibrariesPermissionsSetPermissionsRequestBody2,
        action: LibrariesPermissionsSetPermissionsParamAction | None = None,
        run_as: LibrariesPermissionsSetPermissionsParamRunAs | None = None,
    ) -> LibrariesPermissionsSetPermissions200Response2:
        """
        Sets the permissions to access and manipulate a library.

        Sets the permissions to access and manipulate a library.

        Args:
            id (str)                 : The ID of the Library.
            action (Optional[LibrariesPermissionsSetPermissionsParamAction])
                                     : Indicates what action should be performed on the Library.
            run-as (Optional[LibrariesPermissionsSetPermissionsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (LibrariesPermissionsSetPermissionsRequestBody2)
                                     : Request body. (json)

        Returns:
            LibrariesPermissionsSetPermissions200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/libraries/{id_}/permissions"

        params: dict[str, Any] = {
            **({"action": action} if action is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: LibrariesPermissionsSetPermissionsRequestBody2 = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(LibrariesPermissionsSetPermissions200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def libraries_contents_index_2_2(
        self,
        library_id: str,
        run_as: LibrariesContentsIndexParamRunAs | None = None,
    ) -> LibraryContentsIndexListResponse:
        """
        Return a list of library files and folders.

        This endpoint is deprecated. Please use GET /api/folders/{folder_id}/contents instead.

        Args:
            library_id (str)         : The ID of the Library.
            run-as (Optional[LibrariesContentsIndexParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            LibraryContentsIndexListResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/libraries/{library_id}/contents"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(LibraryContentsIndexListResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def libraries_contents_index_2_2(
        self,
        library_id: str,
        run_as: LibrariesContentsIndexParamRunAs | None = None,
    ) -> LibraryContentsIndexListResponse:
        """
        Return a list of library files and folders.

        This endpoint is deprecated. Please use GET /api/folders/{folder_id}/contents instead.

        Args:
            library_id (str)         : The ID of the Library.
            run-as (Optional[LibrariesContentsIndexParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            LibraryContentsIndexListResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/libraries/{library_id}/contents"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(LibraryContentsIndexListResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def libraries_contents_create_form_2_2(
        self,
        library_id: str,
        files: dict[str, IO[Any]],
        run_as: LibrariesContentsCreateFormParamRunAs | None = None,
    ) -> LibrariesContentsCreateForm200Response2:
        """
        Create a new library file or folder.

        This endpoint is deprecated. Please use POST /api/folders/{folder_id} or POST
        /api/folders/{folder_id}/contents instead.

        Args:
            library_id (str)         : The ID of the Library.
            run-as (Optional[LibrariesContentsCreateFormParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            files (Dict[str, IO[Any]]): Request body. (multipart/form-data)

        Returns:
            LibrariesContentsCreateForm200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/libraries/{library_id}/contents"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        files_data: dict[str, IO[Any]] = DataclassSerializer.serialize(files)

        response = await self._transport.request("POST", url, params=None, files=files_data, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(LibrariesContentsCreateForm200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def libraries_contents_create_form_2_2(
        self,
        library_id: str,
        files: dict[str, IO[Any]],
        run_as: LibrariesContentsCreateFormParamRunAs | None = None,
    ) -> LibrariesContentsCreateForm200Response2:
        """
        Create a new library file or folder.

        This endpoint is deprecated. Please use POST /api/folders/{folder_id} or POST
        /api/folders/{folder_id}/contents instead.

        Args:
            library_id (str)         : The ID of the Library.
            run-as (Optional[LibrariesContentsCreateFormParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            files (Dict[str, IO[Any]]): Request body. (multipart/form-data)

        Returns:
            LibrariesContentsCreateForm200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/libraries/{library_id}/contents"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        files_data: dict[str, IO[Any]] = DataclassSerializer.serialize(files)

        response = await self._transport.request("POST", url, params=None, files=files_data, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(LibrariesContentsCreateForm200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def libraries_contents_delete_2_2(
        self,
        library_id: str,
        id_: str,
        run_as: LibrariesContentsDeleteParamRunAs | None = None,
        body: LibrariesContentsDeleteRequestBody2 | None = None,
    ) -> LibraryContentsDeleteResponse:
        """
        Delete a library file or folder.

        This endpoint is deprecated. Please use DELETE /api/libraries/datasets/{id} instead.

        Args:
            library_id (str)         : The ID of the Library.
            id (str)                 : The encoded ID of the library dataset.
            run-as (Optional[LibrariesContentsDeleteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (Optional[LibrariesContentsDeleteRequestBody2])
                                     : Request body. (json)

        Returns:
            LibraryContentsDeleteResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/libraries/{library_id}/contents/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: LibrariesContentsDeleteRequestBody2 | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("DELETE", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(LibraryContentsDeleteResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def libraries_contents_delete_2_2(
        self,
        library_id: str,
        id_: str,
        run_as: LibrariesContentsDeleteParamRunAs | None = None,
        body: LibrariesContentsDeleteRequestBody2 | None = None,
    ) -> LibraryContentsDeleteResponse:
        """
        Delete a library file or folder.

        This endpoint is deprecated. Please use DELETE /api/libraries/datasets/{id} instead.

        Args:
            library_id (str)         : The ID of the Library.
            id (str)                 : The encoded ID of the library dataset.
            run-as (Optional[LibrariesContentsDeleteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (Optional[LibrariesContentsDeleteRequestBody2])
                                     : Request body. (json)

        Returns:
            LibraryContentsDeleteResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/libraries/{library_id}/contents/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: LibrariesContentsDeleteRequestBody2 | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("DELETE", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(LibraryContentsDeleteResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def libraries_contents_show_2_2(
        self,
        library_id: str,
        id_: str,
        run_as: LibrariesContentsShowParamRunAs | None = None,
    ) -> LibrariesContentsShow200Response2:
        """
        Return a library file or folder.

        This endpoint is deprecated. Please use GET /api/libraries/datasets/{id} instead.

        Args:
            library_id (str)         : The ID of the Library.
            id (str)                 :
            run-as (Optional[LibrariesContentsShowParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            LibrariesContentsShow200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/libraries/{library_id}/contents/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(LibrariesContentsShow200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def libraries_contents_show_2_2(
        self,
        library_id: str,
        id_: str,
        run_as: LibrariesContentsShowParamRunAs | None = None,
    ) -> LibrariesContentsShow200Response2:
        """
        Return a library file or folder.

        This endpoint is deprecated. Please use GET /api/libraries/datasets/{id} instead.

        Args:
            library_id (str)         : The ID of the Library.
            id (str)                 :
            run-as (Optional[LibrariesContentsShowParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            LibrariesContentsShow200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/libraries/{library_id}/contents/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(LibrariesContentsShow200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def libraries_contents_update_2_2(
        self,
        library_id: str,
        id_: str,
        payload: Any,
        run_as: LibrariesContentsUpdateParamRunAs | None = None,
    ) -> Any:
        """
        Update a library file or folder.

        This endpoint is deprecated. Please use PATCH /api/libraries/datasets/{id} instead.

        Args:
            library_id (str)         : The ID of the Library.
            id (str)                 : The encoded ID of the library dataset.
            payload (Any)            :
            run-as (Optional[LibrariesContentsUpdateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/libraries/{library_id}/contents/{id_}"

        params: dict[str, Any] = {
            "payload": payload,
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def libraries_contents_update_2_2(
        self,
        library_id: str,
        id_: str,
        payload: Any,
        run_as: LibrariesContentsUpdateParamRunAs | None = None,
    ) -> Any:
        """
        Update a library file or folder.

        This endpoint is deprecated. Please use PATCH /api/libraries/datasets/{id} instead.

        Args:
            library_id (str)         : The ID of the Library.
            id (str)                 : The encoded ID of the library dataset.
            payload (Any)            :
            run-as (Optional[LibrariesContentsUpdateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/libraries/{library_id}/contents/{id_}"

        params: dict[str, Any] = {
            "payload": payload,
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover
