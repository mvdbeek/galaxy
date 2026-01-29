from typing import TYPE_CHECKING

from ...models.create_quota_params import CreateQuotaParams
from ...models.create_quota_result import CreateQuotaResult
from ...models.delete_quota_payload import DeleteQuotaPayload
from ...models.quota_details import QuotaDetails
from ...models.quota_summary_list import QuotaSummaryList
from ...models.quotas_create_param_run_as import QuotasCreateParamRunAs
from ...models.quotas_delete_param_run_as import QuotasDeleteParamRunAs
from ...models.quotas_deleted_index_deleted_param_run_as import QuotasDeletedIndexDeletedParamRunAs
from ...models.quotas_deleted_show_deleted_param_run_as import QuotasDeletedShowDeletedParamRunAs
from ...models.quotas_deleted_undelete_undelete_param_run_as import QuotasDeletedUndeleteUndeleteParamRunAs
from ...models.quotas_index_param_run_as import QuotasIndexParamRunAs
from ...models.quotas_purge_purge_param_run_as import QuotasPurgePurgeParamRunAs
from ...models.quotas_show_param_run_as import QuotasShowParamRunAs
from ...models.quotas_update_param_run_as import QuotasUpdateParamRunAs
from ...models.update_quota_params import UpdateQuotaParams

if TYPE_CHECKING:
    pass


class MockQuotasClient:
    """
    Mock implementation of QuotasClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestQuotasClient(MockQuotasClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def quotas_index(
        self,
        run_as: QuotasIndexParamRunAs | None = None,
    ) -> QuotaSummaryList:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockQuotasClient.quotas_index() not implemented. Override this method in your test subclass."
        )

    async def quotas_create(
        self,
        body: CreateQuotaParams,
        run_as: QuotasCreateParamRunAs | None = None,
    ) -> CreateQuotaResult:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockQuotasClient.quotas_create() not implemented. Override this method in your test subclass."
        )

    async def quotas_deleted_index_deleted(
        self,
        run_as: QuotasDeletedIndexDeletedParamRunAs | None = None,
    ) -> QuotaSummaryList:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockQuotasClient.quotas_deleted_index_deleted() not implemented. Override this method in your test subclass."
        )

    async def quotas_deleted_show_deleted(
        self,
        id_: str,
        run_as: QuotasDeletedShowDeletedParamRunAs | None = None,
    ) -> QuotaDetails:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockQuotasClient.quotas_deleted_show_deleted() not implemented. Override this method in your test subclass."
        )

    async def quotas_deleted_undelete_undelete(
        self,
        id_: str,
        run_as: QuotasDeletedUndeleteUndeleteParamRunAs | None = None,
    ) -> str:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockQuotasClient.quotas_deleted_undelete_undelete() not implemented. Override this method in your test subclass."
        )

    async def quotas_delete(
        self,
        id_: str,
        run_as: QuotasDeleteParamRunAs | None = None,
        body: DeleteQuotaPayload | None = None,
    ) -> str:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockQuotasClient.quotas_delete() not implemented. Override this method in your test subclass."
        )

    async def quotas_show(
        self,
        id_: str,
        run_as: QuotasShowParamRunAs | None = None,
    ) -> QuotaDetails:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockQuotasClient.quotas_show() not implemented. Override this method in your test subclass."
        )

    async def quotas_update(
        self,
        id_: str,
        body: UpdateQuotaParams,
        run_as: QuotasUpdateParamRunAs | None = None,
    ) -> str:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockQuotasClient.quotas_update() not implemented. Override this method in your test subclass."
        )

    async def quotas_purge_purge(
        self,
        id_: str,
        run_as: QuotasPurgePurgeParamRunAs | None = None,
    ) -> str:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockQuotasClient.quotas_purge_purge() not implemented. Override this method in your test subclass."
        )
