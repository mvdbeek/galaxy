from typing import TYPE_CHECKING, Any

from ...models.async_file import AsyncFile
from ...models.create_page_payload import CreatePagePayload
from ...models.page_details import PageDetails
from ...models.page_summary import PageSummary
from ...models.page_summary_list import PageSummaryList
from ...models.pages_create_param_run_as import PagesCreateParamRunAs
from ...models.pages_delete_param_run_as import PagesDeleteParamRunAs
from ...models.pages_disable_link_access_disable_link_access_param_run_as import (
    PagesDisableLinkAccessDisableLinkAccessParamRunAs,
)
from ...models.pages_enable_link_access_enable_link_access_param_run_as import (
    PagesEnableLinkAccessEnableLinkAccessParamRunAs,
)
from ...models.pages_index_param_run_as import PagesIndexParamRunAs
from ...models.pages_index_param_search import PagesIndexParamSearch
from ...models.pages_index_param_user_id import PagesIndexParamUserId
from ...models.pages_prepare_download_prepare_pdf_param_run_as import PagesPrepareDownloadPreparePdfParamRunAs
from ...models.pages_publish_publish_param_run_as import PagesPublishPublishParamRunAs
from ...models.pages_share_with_users_share_with_users_param_run_as import PagesShareWithUsersShareWithUsersParamRunAs
from ...models.pages_sharing_sharing_param_run_as import PagesSharingSharingParamRunAs
from ...models.pages_show_param_run_as import PagesShowParamRunAs
from ...models.pages_show_pdf_param_run_as import PagesShowPdfParamRunAs
from ...models.pages_slug_set_slug_param_run_as import PagesSlugSetSlugParamRunAs
from ...models.pages_undelete_undelete_param_run_as import PagesUndeleteUndeleteParamRunAs
from ...models.pages_unpublish_unpublish_param_run_as import PagesUnpublishUnpublishParamRunAs
from ...models.pages_update_param_run_as import PagesUpdateParamRunAs
from ...models.set_slug_payload import SetSlugPayload
from ...models.share_with_payload import ShareWithPayload
from ...models.share_with_status import ShareWithStatus
from ...models.sharing_status import SharingStatus
from ...models.update_page_payload import UpdatePagePayload

if TYPE_CHECKING:
    pass


class MockPagesClient:
    """
    Mock implementation of PagesClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestPagesClient(MockPagesClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def pages_index(
        self,
        deleted: bool | None = None,
        limit: int | None = None,
        offset: int | None = None,
        search: PagesIndexParamSearch | None = None,
        show_own: bool | None = None,
        show_published: bool | None = None,
        show_shared: bool | None = None,
        sort_by: str | None = None,
        sort_desc: bool | None = None,
        user_id: PagesIndexParamUserId | None = None,
        run_as: PagesIndexParamRunAs | None = None,
    ) -> PageSummaryList:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockPagesClient.pages_index() not implemented. Override this method in your test subclass."
        )

    async def pages_create(
        self,
        body: CreatePagePayload,
        run_as: PagesCreateParamRunAs | None = None,
    ) -> PageSummary:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockPagesClient.pages_create() not implemented. Override this method in your test subclass."
        )

    async def pages_delete(
        self,
        id_: str,
        run_as: PagesDeleteParamRunAs | None = None,
    ) -> None:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockPagesClient.pages_delete() not implemented. Override this method in your test subclass."
        )

    async def pages_show(
        self,
        id_: str,
        run_as: PagesShowParamRunAs | None = None,
    ) -> PageDetails:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockPagesClient.pages_show() not implemented. Override this method in your test subclass."
        )

    async def pages_update(
        self,
        id_: str,
        body: UpdatePagePayload,
        run_as: PagesUpdateParamRunAs | None = None,
    ) -> PageSummary:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockPagesClient.pages_update() not implemented. Override this method in your test subclass."
        )

    async def pages_show_pdf(
        self,
        id_: str,
        run_as: PagesShowPdfParamRunAs | None = None,
    ) -> Any:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockPagesClient.pages_show_pdf() not implemented. Override this method in your test subclass."
        )

    async def pages_disable_link_access_disable_link_access(
        self,
        id_: str,
        run_as: PagesDisableLinkAccessDisableLinkAccessParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockPagesClient.pages_disable_link_access_disable_link_access() not implemented. Override this method in your test subclass."
        )

    async def pages_enable_link_access_enable_link_access(
        self,
        id_: str,
        run_as: PagesEnableLinkAccessEnableLinkAccessParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockPagesClient.pages_enable_link_access_enable_link_access() not implemented. Override this method in your test subclass."
        )

    async def pages_prepare_download_prepare_pdf(
        self,
        id_: str,
        run_as: PagesPrepareDownloadPreparePdfParamRunAs | None = None,
    ) -> AsyncFile:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockPagesClient.pages_prepare_download_prepare_pdf() not implemented. Override this method in your test subclass."
        )

    async def pages_publish_publish(
        self,
        id_: str,
        run_as: PagesPublishPublishParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockPagesClient.pages_publish_publish() not implemented. Override this method in your test subclass."
        )

    async def pages_share_with_users_share_with_users(
        self,
        id_: str,
        body: ShareWithPayload,
        run_as: PagesShareWithUsersShareWithUsersParamRunAs | None = None,
    ) -> ShareWithStatus:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockPagesClient.pages_share_with_users_share_with_users() not implemented. Override this method in your test subclass."
        )

    async def pages_sharing_sharing(
        self,
        id_: str,
        run_as: PagesSharingSharingParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockPagesClient.pages_sharing_sharing() not implemented. Override this method in your test subclass."
        )

    async def pages_slug_set_slug(
        self,
        id_: str,
        body: SetSlugPayload,
        run_as: PagesSlugSetSlugParamRunAs | None = None,
    ) -> None:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockPagesClient.pages_slug_set_slug() not implemented. Override this method in your test subclass."
        )

    async def pages_undelete_undelete(
        self,
        id_: str,
        run_as: PagesUndeleteUndeleteParamRunAs | None = None,
    ) -> None:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockPagesClient.pages_undelete_undelete() not implemented. Override this method in your test subclass."
        )

    async def pages_unpublish_unpublish(
        self,
        id_: str,
        run_as: PagesUnpublishUnpublishParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockPagesClient.pages_unpublish_unpublish() not implemented. Override this method in your test subclass."
        )
