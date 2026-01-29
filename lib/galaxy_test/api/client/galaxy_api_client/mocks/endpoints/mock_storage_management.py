from typing import TYPE_CHECKING

from ...models.cleanable_items_summary import CleanableItemsSummary
from ...models.cleanup_storage_items_request import CleanupStorageItemsRequest
from ...models.storage_items_cleanup_result import StorageItemsCleanupResult
from ...models.storage_management_datasets_cleanup_datasets_param_run_as import (
    StorageManagementDatasetsCleanupDatasetsParamRunAs,
)
from ...models.storage_management_datasets_discarded_discarded_datasets_param_limit import (
    StorageManagementDatasetsDiscardedDiscardedDatasetsParamLimit,
)
from ...models.storage_management_datasets_discarded_discarded_datasets_param_offset import (
    StorageManagementDatasetsDiscardedDiscardedDatasetsParamOffset,
)
from ...models.storage_management_datasets_discarded_discarded_datasets_param_order import (
    StorageManagementDatasetsDiscardedDiscardedDatasetsParamOrder,
)
from ...models.storage_management_datasets_discarded_discarded_datasets_param_run_as import (
    StorageManagementDatasetsDiscardedDiscardedDatasetsParamRunAs,
)
from ...models.storage_management_datasets_discarded_summary_discarded_datasets_summary_param_run_as import (
    StorageManagementDatasetsDiscardedSummaryDiscardedDatasetsSummaryParamRunAs,
)
from ...models.storage_management_histories_archived_archived_histories_param_limit import (
    StorageManagementHistoriesArchivedArchivedHistoriesParamLimit,
)
from ...models.storage_management_histories_archived_archived_histories_param_offset import (
    StorageManagementHistoriesArchivedArchivedHistoriesParamOffset,
)
from ...models.storage_management_histories_archived_archived_histories_param_order import (
    StorageManagementHistoriesArchivedArchivedHistoriesParamOrder,
)
from ...models.storage_management_histories_archived_archived_histories_param_run_as import (
    StorageManagementHistoriesArchivedArchivedHistoriesParamRunAs,
)
from ...models.storage_management_histories_archived_summary_archived_histories_summary_param_run_as import (
    StorageManagementHistoriesArchivedSummaryArchivedHistoriesSummaryParamRunAs,
)
from ...models.storage_management_histories_cleanup_histories_param_run_as import (
    StorageManagementHistoriesCleanupHistoriesParamRunAs,
)
from ...models.storage_management_histories_discarded_discarded_histories_param_limit import (
    StorageManagementHistoriesDiscardedDiscardedHistoriesParamLimit,
)
from ...models.storage_management_histories_discarded_discarded_histories_param_offset import (
    StorageManagementHistoriesDiscardedDiscardedHistoriesParamOffset,
)
from ...models.storage_management_histories_discarded_discarded_histories_param_order import (
    StorageManagementHistoriesDiscardedDiscardedHistoriesParamOrder,
)
from ...models.storage_management_histories_discarded_discarded_histories_param_run_as import (
    StorageManagementHistoriesDiscardedDiscardedHistoriesParamRunAs,
)
from ...models.storage_management_histories_discarded_summary_discarded_histories_summary_param_run_as import (
    StorageManagementHistoriesDiscardedSummaryDiscardedHistoriesSummaryParamRunAs,
)
from ...models.stored_item import StoredItem

if TYPE_CHECKING:
    pass


class MockStorageManagementClient:
    """
    Mock implementation of StorageManagementClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestStorageManagementClient(MockStorageManagementClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def storage_management_datasets_cleanup_datasets(
        self,
        body: CleanupStorageItemsRequest,
        run_as: StorageManagementDatasetsCleanupDatasetsParamRunAs | None = None,
    ) -> StorageItemsCleanupResult:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockStorageManagementClient.storage_management_datasets_cleanup_datasets() not implemented. Override this method in your test subclass."
        )

    async def storage_management_datasets_discarded_discarded_datasets(
        self,
        offset: StorageManagementDatasetsDiscardedDiscardedDatasetsParamOffset | None = None,
        limit: StorageManagementDatasetsDiscardedDiscardedDatasetsParamLimit | None = None,
        order: StorageManagementDatasetsDiscardedDiscardedDatasetsParamOrder | None = None,
        run_as: StorageManagementDatasetsDiscardedDiscardedDatasetsParamRunAs | None = None,
    ) -> list[StoredItem]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockStorageManagementClient.storage_management_datasets_discarded_discarded_datasets() not implemented. Override this method in your test subclass."
        )

    async def storage_management_datasets_discarded_summary_discarded_datasets_summary(
        self,
        run_as: StorageManagementDatasetsDiscardedSummaryDiscardedDatasetsSummaryParamRunAs | None = None,
    ) -> CleanableItemsSummary:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockStorageManagementClient.storage_management_datasets_discarded_summary_discarded_datasets_summary() not implemented. Override this method in your test subclass."
        )

    async def storage_management_histories_cleanup_histories(
        self,
        body: CleanupStorageItemsRequest,
        run_as: StorageManagementHistoriesCleanupHistoriesParamRunAs | None = None,
    ) -> StorageItemsCleanupResult:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockStorageManagementClient.storage_management_histories_cleanup_histories() not implemented. Override this method in your test subclass."
        )

    async def storage_management_histories_archived_archived_histories(
        self,
        offset: StorageManagementHistoriesArchivedArchivedHistoriesParamOffset | None = None,
        limit: StorageManagementHistoriesArchivedArchivedHistoriesParamLimit | None = None,
        order: StorageManagementHistoriesArchivedArchivedHistoriesParamOrder | None = None,
        run_as: StorageManagementHistoriesArchivedArchivedHistoriesParamRunAs | None = None,
    ) -> list[StoredItem]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockStorageManagementClient.storage_management_histories_archived_archived_histories() not implemented. Override this method in your test subclass."
        )

    async def storage_management_histories_archived_summary_archived_histories_summary(
        self,
        run_as: StorageManagementHistoriesArchivedSummaryArchivedHistoriesSummaryParamRunAs | None = None,
    ) -> CleanableItemsSummary:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockStorageManagementClient.storage_management_histories_archived_summary_archived_histories_summary() not implemented. Override this method in your test subclass."
        )

    async def storage_management_histories_discarded_discarded_histories(
        self,
        offset: StorageManagementHistoriesDiscardedDiscardedHistoriesParamOffset | None = None,
        limit: StorageManagementHistoriesDiscardedDiscardedHistoriesParamLimit | None = None,
        order: StorageManagementHistoriesDiscardedDiscardedHistoriesParamOrder | None = None,
        run_as: StorageManagementHistoriesDiscardedDiscardedHistoriesParamRunAs | None = None,
    ) -> list[StoredItem]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockStorageManagementClient.storage_management_histories_discarded_discarded_histories() not implemented. Override this method in your test subclass."
        )

    async def storage_management_histories_discarded_summary_discarded_histories_summary(
        self,
        run_as: StorageManagementHistoriesDiscardedSummaryDiscardedHistoriesSummaryParamRunAs | None = None,
    ) -> CleanableItemsSummary:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockStorageManagementClient.storage_management_histories_discarded_summary_discarded_histories_summary() not implemented. Override this method in your test subclass."
        )
