from typing import IO, TYPE_CHECKING, Any

from ...models.create_libraries_from_store import CreateLibrariesFromStore
from ...models.create_library_payload import CreateLibraryPayload
from ...models.libraries_contents_create_form_200_response import LibrariesContentsCreateForm200Response
from ...models.libraries_contents_create_form_param_run_as import LibrariesContentsCreateFormParamRunAs
from ...models.libraries_contents_delete_param_run_as import LibrariesContentsDeleteParamRunAs
from ...models.libraries_contents_delete_request_body import LibrariesContentsDeleteRequestBody
from ...models.libraries_contents_index_param_run_as import LibrariesContentsIndexParamRunAs
from ...models.libraries_contents_show_200_response import LibrariesContentsShow200Response
from ...models.libraries_contents_show_param_run_as import LibrariesContentsShowParamRunAs
from ...models.libraries_contents_update_param_run_as import LibrariesContentsUpdateParamRunAs
from ...models.libraries_create_param_run_as import LibrariesCreateParamRunAs
from ...models.libraries_delete_param_run_as import LibrariesDeleteParamRunAs
from ...models.libraries_delete_param_undelete import LibrariesDeleteParamUndelete
from ...models.libraries_delete_request_body import LibrariesDeleteRequestBody
from ...models.libraries_deleted_index_deleted_param_run_as import LibrariesDeletedIndexDeletedParamRunAs
from ...models.libraries_from_store_create_from_store_param_run_as import LibrariesFromStoreCreateFromStoreParamRunAs
from ...models.libraries_index_param_deleted import LibrariesIndexParamDeleted
from ...models.libraries_index_param_run_as import LibrariesIndexParamRunAs
from ...models.libraries_permissions_get_permissions_200_response import LibrariesPermissionsGetPermissions200Response
from ...models.libraries_permissions_get_permissions_param_is_library_access import (
    LibrariesPermissionsGetPermissionsParamIsLibraryAccess,
)
from ...models.libraries_permissions_get_permissions_param_q import LibrariesPermissionsGetPermissionsParamQ
from ...models.libraries_permissions_get_permissions_param_run_as import LibrariesPermissionsGetPermissionsParamRunAs
from ...models.libraries_permissions_get_permissions_param_scope import LibrariesPermissionsGetPermissionsParamScope
from ...models.libraries_permissions_set_permissions_200_response import LibrariesPermissionsSetPermissions200Response
from ...models.libraries_permissions_set_permissions_param_action import LibrariesPermissionsSetPermissionsParamAction
from ...models.libraries_permissions_set_permissions_param_run_as import LibrariesPermissionsSetPermissionsParamRunAs
from ...models.libraries_permissions_set_permissions_request_body import LibrariesPermissionsSetPermissionsRequestBody
from ...models.libraries_show_param_run_as import LibrariesShowParamRunAs
from ...models.libraries_update_param_run_as import LibrariesUpdateParamRunAs
from ...models.library_contents_delete_response import LibraryContentsDeleteResponse
from ...models.library_contents_index_list_response import LibraryContentsIndexListResponse
from ...models.library_summary import LibrarySummary
from ...models.library_summary_list import LibrarySummaryList
from ...models.update_library_payload import UpdateLibraryPayload

if TYPE_CHECKING:
    pass


class MockLibrariesClient:
    """
    Mock implementation of LibrariesClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestLibrariesClient(MockLibrariesClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def libraries_index(
        self,
        deleted: LibrariesIndexParamDeleted | None = None,
        run_as: LibrariesIndexParamRunAs | None = None,
    ) -> LibrarySummaryList:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockLibrariesClient.libraries_index() not implemented. Override this method in your test subclass."
        )

    async def libraries_create(
        self,
        body: CreateLibraryPayload,
        run_as: LibrariesCreateParamRunAs | None = None,
    ) -> LibrarySummary:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockLibrariesClient.libraries_create() not implemented. Override this method in your test subclass."
        )

    async def libraries_deleted_index_deleted(
        self,
        run_as: LibrariesDeletedIndexDeletedParamRunAs | None = None,
    ) -> LibrarySummaryList:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockLibrariesClient.libraries_deleted_index_deleted() not implemented. Override this method in your test subclass."
        )

    async def libraries_from_store_create_from_store(
        self,
        body: CreateLibrariesFromStore,
        run_as: LibrariesFromStoreCreateFromStoreParamRunAs | None = None,
    ) -> list[LibrarySummary]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockLibrariesClient.libraries_from_store_create_from_store() not implemented. Override this method in your test subclass."
        )

    async def libraries_delete(
        self,
        id_: str,
        undelete: LibrariesDeleteParamUndelete | None = None,
        run_as: LibrariesDeleteParamRunAs | None = None,
        body: LibrariesDeleteRequestBody | None = None,
    ) -> LibrarySummary:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockLibrariesClient.libraries_delete() not implemented. Override this method in your test subclass."
        )

    async def libraries_show(
        self,
        id_: str,
        run_as: LibrariesShowParamRunAs | None = None,
    ) -> LibrarySummary:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockLibrariesClient.libraries_show() not implemented. Override this method in your test subclass."
        )

    async def libraries_update(
        self,
        id_: str,
        body: UpdateLibraryPayload,
        run_as: LibrariesUpdateParamRunAs | None = None,
    ) -> LibrarySummary:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockLibrariesClient.libraries_update() not implemented. Override this method in your test subclass."
        )

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
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockLibrariesClient.libraries_permissions_get_permissions() not implemented. Override this method in your test subclass."
        )

    async def libraries_permissions_set_permissions(
        self,
        id_: str,
        body: LibrariesPermissionsSetPermissionsRequestBody,
        action: LibrariesPermissionsSetPermissionsParamAction | None = None,
        run_as: LibrariesPermissionsSetPermissionsParamRunAs | None = None,
    ) -> LibrariesPermissionsSetPermissions200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockLibrariesClient.libraries_permissions_set_permissions() not implemented. Override this method in your test subclass."
        )

    async def libraries_contents_index(
        self,
        library_id: str,
        run_as: LibrariesContentsIndexParamRunAs | None = None,
    ) -> LibraryContentsIndexListResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockLibrariesClient.libraries_contents_index() not implemented. Override this method in your test subclass."
        )

    async def libraries_contents_create_form(
        self,
        library_id: str,
        files: dict[str, IO[Any]],
        run_as: LibrariesContentsCreateFormParamRunAs | None = None,
    ) -> LibrariesContentsCreateForm200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockLibrariesClient.libraries_contents_create_form() not implemented. Override this method in your test subclass."
        )

    async def libraries_contents_delete(
        self,
        library_id: str,
        id_: str,
        run_as: LibrariesContentsDeleteParamRunAs | None = None,
        body: LibrariesContentsDeleteRequestBody | None = None,
    ) -> LibraryContentsDeleteResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockLibrariesClient.libraries_contents_delete() not implemented. Override this method in your test subclass."
        )

    async def libraries_contents_show(
        self,
        library_id: str,
        id_: str,
        run_as: LibrariesContentsShowParamRunAs | None = None,
    ) -> LibrariesContentsShow200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockLibrariesClient.libraries_contents_show() not implemented. Override this method in your test subclass."
        )

    async def libraries_contents_update(
        self,
        library_id: str,
        id_: str,
        payload: dict[str, Any],
        run_as: LibrariesContentsUpdateParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockLibrariesClient.libraries_contents_update() not implemented. Override this method in your test subclass."
        )
