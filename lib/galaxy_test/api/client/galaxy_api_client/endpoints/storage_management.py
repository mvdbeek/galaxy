from typing import Any, Protocol, runtime_checkable

from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import structure_from_dict
from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.cleanable_items_summary import CleanableItemsSummary
from ..models.cleanup_storage_items_request import CleanupStorageItemsRequest
from ..models.storage_items_cleanup_result import StorageItemsCleanupResult
from ..models.storage_management_datasets_cleanup_datasets_param_run_as import (
    StorageManagementDatasetsCleanupDatasetsParamRunAs,
)
from ..models.storage_management_datasets_discarded_discarded_datasets_param_limit import (
    StorageManagementDatasetsDiscardedDiscardedDatasetsParamLimit,
)
from ..models.storage_management_datasets_discarded_discarded_datasets_param_offset import (
    StorageManagementDatasetsDiscardedDiscardedDatasetsParamOffset,
)
from ..models.storage_management_datasets_discarded_discarded_datasets_param_order import (
    StorageManagementDatasetsDiscardedDiscardedDatasetsParamOrder,
)
from ..models.storage_management_datasets_discarded_discarded_datasets_param_run_as import (
    StorageManagementDatasetsDiscardedDiscardedDatasetsParamRunAs,
)
from ..models.storage_management_datasets_discarded_summary_discarded_datasets_summary_param_run_as import (
    StorageManagementDatasetsDiscardedSummaryDiscardedDatasetsSummaryParamRunAs,
)
from ..models.storage_management_histories_archived_archived_histories_param_limit import (
    StorageManagementHistoriesArchivedArchivedHistoriesParamLimit,
)
from ..models.storage_management_histories_archived_archived_histories_param_offset import (
    StorageManagementHistoriesArchivedArchivedHistoriesParamOffset,
)
from ..models.storage_management_histories_archived_archived_histories_param_order import (
    StorageManagementHistoriesArchivedArchivedHistoriesParamOrder,
)
from ..models.storage_management_histories_archived_archived_histories_param_run_as import (
    StorageManagementHistoriesArchivedArchivedHistoriesParamRunAs,
)
from ..models.storage_management_histories_archived_summary_archived_histories_summary_param_run_as import (
    StorageManagementHistoriesArchivedSummaryArchivedHistoriesSummaryParamRunAs,
)
from ..models.storage_management_histories_cleanup_histories_param_run_as import (
    StorageManagementHistoriesCleanupHistoriesParamRunAs,
)
from ..models.storage_management_histories_discarded_discarded_histories_param_limit import (
    StorageManagementHistoriesDiscardedDiscardedHistoriesParamLimit,
)
from ..models.storage_management_histories_discarded_discarded_histories_param_offset import (
    StorageManagementHistoriesDiscardedDiscardedHistoriesParamOffset,
)
from ..models.storage_management_histories_discarded_discarded_histories_param_order import (
    StorageManagementHistoriesDiscardedDiscardedHistoriesParamOrder,
)
from ..models.storage_management_histories_discarded_discarded_histories_param_run_as import (
    StorageManagementHistoriesDiscardedDiscardedHistoriesParamRunAs,
)
from ..models.storage_management_histories_discarded_summary_discarded_histories_summary_param_run_as import (
    StorageManagementHistoriesDiscardedSummaryDiscardedHistoriesSummaryParamRunAs,
)
from ..models.stored_item import StoredItem


@runtime_checkable
class StorageManagementClientProtocol(Protocol):
    """Protocol defining the interface of StorageManagementClient for dependency injection."""

    async def storage_management_datasets_cleanup_datasets(
        self,
        body: CleanupStorageItemsRequest,
        run_as: StorageManagementDatasetsCleanupDatasetsParamRunAs | None = None,
    ) -> StorageItemsCleanupResult: ...

    async def storage_management_datasets_cleanup_datasets(
        self,
        body: CleanupStorageItemsRequest,
        run_as: StorageManagementDatasetsCleanupDatasetsParamRunAs | None = None,
    ) -> StorageItemsCleanupResult: ...

    async def storage_management_datasets_discarded_discarded_datasets(
        self,
        offset: StorageManagementDatasetsDiscardedDiscardedDatasetsParamOffset | None = None,
        limit: StorageManagementDatasetsDiscardedDiscardedDatasetsParamLimit | None = None,
        order: StorageManagementDatasetsDiscardedDiscardedDatasetsParamOrder | None = None,
        run_as: StorageManagementDatasetsDiscardedDiscardedDatasetsParamRunAs | None = None,
    ) -> list[StoredItem]: ...

    async def storage_management_datasets_discarded_discarded_datasets(
        self,
        offset: StorageManagementDatasetsDiscardedDiscardedDatasetsParamOffset | None = None,
        limit: StorageManagementDatasetsDiscardedDiscardedDatasetsParamLimit | None = None,
        order: StorageManagementDatasetsDiscardedDiscardedDatasetsParamOrder | None = None,
        run_as: StorageManagementDatasetsDiscardedDiscardedDatasetsParamRunAs | None = None,
    ) -> list[StoredItem]: ...

    async def storage_management_datasets_discarded_summary_discarded_datasets_summary(
        self,
        run_as: StorageManagementDatasetsDiscardedSummaryDiscardedDatasetsSummaryParamRunAs | None = None,
    ) -> CleanableItemsSummary: ...

    async def storage_management_datasets_discarded_summary_discarded_datasets_summary(
        self,
        run_as: StorageManagementDatasetsDiscardedSummaryDiscardedDatasetsSummaryParamRunAs | None = None,
    ) -> CleanableItemsSummary: ...

    async def storage_management_histories_cleanup_histories(
        self,
        body: CleanupStorageItemsRequest,
        run_as: StorageManagementHistoriesCleanupHistoriesParamRunAs | None = None,
    ) -> StorageItemsCleanupResult: ...

    async def storage_management_histories_cleanup_histories(
        self,
        body: CleanupStorageItemsRequest,
        run_as: StorageManagementHistoriesCleanupHistoriesParamRunAs | None = None,
    ) -> StorageItemsCleanupResult: ...

    async def storage_management_histories_archived_archived_histories(
        self,
        offset: StorageManagementHistoriesArchivedArchivedHistoriesParamOffset | None = None,
        limit: StorageManagementHistoriesArchivedArchivedHistoriesParamLimit | None = None,
        order: StorageManagementHistoriesArchivedArchivedHistoriesParamOrder | None = None,
        run_as: StorageManagementHistoriesArchivedArchivedHistoriesParamRunAs | None = None,
    ) -> list[StoredItem]: ...

    async def storage_management_histories_archived_archived_histories(
        self,
        offset: StorageManagementHistoriesArchivedArchivedHistoriesParamOffset | None = None,
        limit: StorageManagementHistoriesArchivedArchivedHistoriesParamLimit | None = None,
        order: StorageManagementHistoriesArchivedArchivedHistoriesParamOrder | None = None,
        run_as: StorageManagementHistoriesArchivedArchivedHistoriesParamRunAs | None = None,
    ) -> list[StoredItem]: ...

    async def storage_management_histories_archived_summary_archived_histories_summary(
        self,
        run_as: StorageManagementHistoriesArchivedSummaryArchivedHistoriesSummaryParamRunAs | None = None,
    ) -> CleanableItemsSummary: ...

    async def storage_management_histories_archived_summary_archived_histories_summary(
        self,
        run_as: StorageManagementHistoriesArchivedSummaryArchivedHistoriesSummaryParamRunAs | None = None,
    ) -> CleanableItemsSummary: ...

    async def storage_management_histories_discarded_discarded_histories(
        self,
        offset: StorageManagementHistoriesDiscardedDiscardedHistoriesParamOffset | None = None,
        limit: StorageManagementHistoriesDiscardedDiscardedHistoriesParamLimit | None = None,
        order: StorageManagementHistoriesDiscardedDiscardedHistoriesParamOrder | None = None,
        run_as: StorageManagementHistoriesDiscardedDiscardedHistoriesParamRunAs | None = None,
    ) -> list[StoredItem]: ...

    async def storage_management_histories_discarded_discarded_histories(
        self,
        offset: StorageManagementHistoriesDiscardedDiscardedHistoriesParamOffset | None = None,
        limit: StorageManagementHistoriesDiscardedDiscardedHistoriesParamLimit | None = None,
        order: StorageManagementHistoriesDiscardedDiscardedHistoriesParamOrder | None = None,
        run_as: StorageManagementHistoriesDiscardedDiscardedHistoriesParamRunAs | None = None,
    ) -> list[StoredItem]: ...

    async def storage_management_histories_discarded_summary_discarded_histories_summary(
        self,
        run_as: StorageManagementHistoriesDiscardedSummaryDiscardedHistoriesSummaryParamRunAs | None = None,
    ) -> CleanableItemsSummary: ...

    async def storage_management_histories_discarded_summary_discarded_histories_summary(
        self,
        run_as: StorageManagementHistoriesDiscardedSummaryDiscardedHistoriesSummaryParamRunAs | None = None,
    ) -> CleanableItemsSummary: ...


class StorageManagementClient(StorageManagementClientProtocol):
    """Client for storage management endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def storage_management_datasets_cleanup_datasets(
        self,
        body: CleanupStorageItemsRequest,
        run_as: StorageManagementDatasetsCleanupDatasetsParamRunAs | None = None,
    ) -> StorageItemsCleanupResult:
        """
        Purges a set of datasets by ID from disk. The datasets must be owned by the user.

        **Warning**: This operation cannot be undone. All objects will be deleted permanently
        from the disk.

        Args:
            run-as (StorageManagementDatasetsCleanupDatasetsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CleanupStorageItemsRequest)
                                     : Request body. (json)

        Returns:
            StorageItemsCleanupResult: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/storage/datasets"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: CleanupStorageItemsRequest = DataclassSerializer.serialize(body)

        response = await self._transport.request("DELETE", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), StorageItemsCleanupResult)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def storage_management_datasets_cleanup_datasets(
        self,
        body: CleanupStorageItemsRequest,
        run_as: StorageManagementDatasetsCleanupDatasetsParamRunAs | None = None,
    ) -> StorageItemsCleanupResult:
        """
        Purges a set of datasets by ID from disk. The datasets must be owned by the user.

        **Warning**: This operation cannot be undone. All objects will be deleted permanently
        from the disk.

        Args:
            run-as (StorageManagementDatasetsCleanupDatasetsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CleanupStorageItemsRequest)
                                     : Request body. (json)

        Returns:
            StorageItemsCleanupResult: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/storage/datasets"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: CleanupStorageItemsRequest = DataclassSerializer.serialize(body)

        response = await self._transport.request("DELETE", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), StorageItemsCleanupResult)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def storage_management_datasets_discarded_discarded_datasets(
        self,
        offset: StorageManagementDatasetsDiscardedDiscardedDatasetsParamOffset | None = None,
        limit: StorageManagementDatasetsDiscardedDiscardedDatasetsParamLimit | None = None,
        order: StorageManagementDatasetsDiscardedDiscardedDatasetsParamOrder | None = None,
        run_as: StorageManagementDatasetsDiscardedDiscardedDatasetsParamRunAs | None = None,
    ) -> list[StoredItem]:
        """
        Returns discarded datasets owned by the given user. The results can be paginated.

        Args:
            offset (StorageManagementDatasetsDiscardedDiscardedDatasetsParamOffset | None)
                                     : Starts at the beginning skip the first ( offset - 1 )
                                       items and begin returning at the Nth item
            limit (StorageManagementDatasetsDiscardedDiscardedDatasetsParamLimit | None)
                                     : The maximum number of items to return.
            order (StorageManagementDatasetsDiscardedDiscardedDatasetsParamOrder | None)
                                     : String containing one of the valid ordering attributes
                                       followed by '-asc' or '-dsc' for ascending and descending
                                       order respectively.
            run-as (StorageManagementDatasetsDiscardedDiscardedDatasetsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[StoredItem]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/storage/datasets/discarded"

        params: dict[str, Any] = {
            **({"offset": DataclassSerializer.serialize(offset)} if offset is not None else {}),
            **({"limit": DataclassSerializer.serialize(limit)} if limit is not None else {}),
            **({"order": DataclassSerializer.serialize(order)} if order is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[StoredItem])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def storage_management_datasets_discarded_discarded_datasets(
        self,
        offset: StorageManagementDatasetsDiscardedDiscardedDatasetsParamOffset | None = None,
        limit: StorageManagementDatasetsDiscardedDiscardedDatasetsParamLimit | None = None,
        order: StorageManagementDatasetsDiscardedDiscardedDatasetsParamOrder | None = None,
        run_as: StorageManagementDatasetsDiscardedDiscardedDatasetsParamRunAs | None = None,
    ) -> list[StoredItem]:
        """
        Returns discarded datasets owned by the given user. The results can be paginated.

        Args:
            offset (StorageManagementDatasetsDiscardedDiscardedDatasetsParamOffset | None)
                                     : Starts at the beginning skip the first ( offset - 1 )
                                       items and begin returning at the Nth item
            limit (StorageManagementDatasetsDiscardedDiscardedDatasetsParamLimit | None)
                                     : The maximum number of items to return.
            order (StorageManagementDatasetsDiscardedDiscardedDatasetsParamOrder | None)
                                     : String containing one of the valid ordering attributes
                                       followed by '-asc' or '-dsc' for ascending and descending
                                       order respectively.
            run-as (StorageManagementDatasetsDiscardedDiscardedDatasetsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[StoredItem]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/storage/datasets/discarded"

        params: dict[str, Any] = {
            **({"offset": DataclassSerializer.serialize(offset)} if offset is not None else {}),
            **({"limit": DataclassSerializer.serialize(limit)} if limit is not None else {}),
            **({"order": DataclassSerializer.serialize(order)} if order is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[StoredItem])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def storage_management_datasets_discarded_summary_discarded_datasets_summary(
        self,
        run_as: StorageManagementDatasetsDiscardedSummaryDiscardedDatasetsSummaryParamRunAs | None = None,
    ) -> CleanableItemsSummary:
        """
        Returns information with the total storage space taken by discarded datasets owned by
        the given user.

        Args:
            run-as (StorageManagementDatasetsDiscardedSummaryDiscardedDatasetsSummaryParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            CleanableItemsSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/storage/datasets/discarded/summary"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), CleanableItemsSummary)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def storage_management_datasets_discarded_summary_discarded_datasets_summary(
        self,
        run_as: StorageManagementDatasetsDiscardedSummaryDiscardedDatasetsSummaryParamRunAs | None = None,
    ) -> CleanableItemsSummary:
        """
        Returns information with the total storage space taken by discarded datasets owned by
        the given user.

        Args:
            run-as (StorageManagementDatasetsDiscardedSummaryDiscardedDatasetsSummaryParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            CleanableItemsSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/storage/datasets/discarded/summary"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), CleanableItemsSummary)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def storage_management_histories_cleanup_histories(
        self,
        body: CleanupStorageItemsRequest,
        run_as: StorageManagementHistoriesCleanupHistoriesParamRunAs | None = None,
    ) -> StorageItemsCleanupResult:
        """
        Purges a set of histories by ID. The histories must be owned by the user.

        **Warning**: This operation cannot be undone. All objects will be deleted permanently
        from the disk.

        Args:
            run-as (StorageManagementHistoriesCleanupHistoriesParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CleanupStorageItemsRequest)
                                     : Request body. (json)

        Returns:
            StorageItemsCleanupResult: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/storage/histories"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: CleanupStorageItemsRequest = DataclassSerializer.serialize(body)

        response = await self._transport.request("DELETE", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), StorageItemsCleanupResult)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def storage_management_histories_cleanup_histories(
        self,
        body: CleanupStorageItemsRequest,
        run_as: StorageManagementHistoriesCleanupHistoriesParamRunAs | None = None,
    ) -> StorageItemsCleanupResult:
        """
        Purges a set of histories by ID. The histories must be owned by the user.

        **Warning**: This operation cannot be undone. All objects will be deleted permanently
        from the disk.

        Args:
            run-as (StorageManagementHistoriesCleanupHistoriesParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CleanupStorageItemsRequest)
                                     : Request body. (json)

        Returns:
            StorageItemsCleanupResult: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/storage/histories"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: CleanupStorageItemsRequest = DataclassSerializer.serialize(body)

        response = await self._transport.request("DELETE", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), StorageItemsCleanupResult)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def storage_management_histories_archived_archived_histories(
        self,
        offset: StorageManagementHistoriesArchivedArchivedHistoriesParamOffset | None = None,
        limit: StorageManagementHistoriesArchivedArchivedHistoriesParamLimit | None = None,
        order: StorageManagementHistoriesArchivedArchivedHistoriesParamOrder | None = None,
        run_as: StorageManagementHistoriesArchivedArchivedHistoriesParamRunAs | None = None,
    ) -> list[StoredItem]:
        """
        Returns archived histories owned by the given user that are not purged. The results can
        be paginated.

        Args:
            offset (StorageManagementHistoriesArchivedArchivedHistoriesParamOffset | None)
                                     : Starts at the beginning skip the first ( offset - 1 )
                                       items and begin returning at the Nth item
            limit (StorageManagementHistoriesArchivedArchivedHistoriesParamLimit | None)
                                     : The maximum number of items to return.
            order (StorageManagementHistoriesArchivedArchivedHistoriesParamOrder | None)
                                     : String containing one of the valid ordering attributes
                                       followed by '-asc' or '-dsc' for ascending and descending
                                       order respectively.
            run-as (StorageManagementHistoriesArchivedArchivedHistoriesParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[StoredItem]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/storage/histories/archived"

        params: dict[str, Any] = {
            **({"offset": DataclassSerializer.serialize(offset)} if offset is not None else {}),
            **({"limit": DataclassSerializer.serialize(limit)} if limit is not None else {}),
            **({"order": DataclassSerializer.serialize(order)} if order is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[StoredItem])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def storage_management_histories_archived_archived_histories(
        self,
        offset: StorageManagementHistoriesArchivedArchivedHistoriesParamOffset | None = None,
        limit: StorageManagementHistoriesArchivedArchivedHistoriesParamLimit | None = None,
        order: StorageManagementHistoriesArchivedArchivedHistoriesParamOrder | None = None,
        run_as: StorageManagementHistoriesArchivedArchivedHistoriesParamRunAs | None = None,
    ) -> list[StoredItem]:
        """
        Returns archived histories owned by the given user that are not purged. The results can
        be paginated.

        Args:
            offset (StorageManagementHistoriesArchivedArchivedHistoriesParamOffset | None)
                                     : Starts at the beginning skip the first ( offset - 1 )
                                       items and begin returning at the Nth item
            limit (StorageManagementHistoriesArchivedArchivedHistoriesParamLimit | None)
                                     : The maximum number of items to return.
            order (StorageManagementHistoriesArchivedArchivedHistoriesParamOrder | None)
                                     : String containing one of the valid ordering attributes
                                       followed by '-asc' or '-dsc' for ascending and descending
                                       order respectively.
            run-as (StorageManagementHistoriesArchivedArchivedHistoriesParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[StoredItem]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/storage/histories/archived"

        params: dict[str, Any] = {
            **({"offset": DataclassSerializer.serialize(offset)} if offset is not None else {}),
            **({"limit": DataclassSerializer.serialize(limit)} if limit is not None else {}),
            **({"order": DataclassSerializer.serialize(order)} if order is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[StoredItem])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def storage_management_histories_archived_summary_archived_histories_summary(
        self,
        run_as: StorageManagementHistoriesArchivedSummaryArchivedHistoriesSummaryParamRunAs | None = None,
    ) -> CleanableItemsSummary:
        """
        Returns information with the total storage space taken by non-purged archived histories
        associated with the given user.

        Args:
            run-as (StorageManagementHistoriesArchivedSummaryArchivedHistoriesSummaryParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            CleanableItemsSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/storage/histories/archived/summary"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), CleanableItemsSummary)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def storage_management_histories_archived_summary_archived_histories_summary(
        self,
        run_as: StorageManagementHistoriesArchivedSummaryArchivedHistoriesSummaryParamRunAs | None = None,
    ) -> CleanableItemsSummary:
        """
        Returns information with the total storage space taken by non-purged archived histories
        associated with the given user.

        Args:
            run-as (StorageManagementHistoriesArchivedSummaryArchivedHistoriesSummaryParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            CleanableItemsSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/storage/histories/archived/summary"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), CleanableItemsSummary)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def storage_management_histories_discarded_discarded_histories(
        self,
        offset: StorageManagementHistoriesDiscardedDiscardedHistoriesParamOffset | None = None,
        limit: StorageManagementHistoriesDiscardedDiscardedHistoriesParamLimit | None = None,
        order: StorageManagementHistoriesDiscardedDiscardedHistoriesParamOrder | None = None,
        run_as: StorageManagementHistoriesDiscardedDiscardedHistoriesParamRunAs | None = None,
    ) -> list[StoredItem]:
        """
        Returns all discarded histories associated with the given user.

        Args:
            offset (StorageManagementHistoriesDiscardedDiscardedHistoriesParamOffset | None)
                                     : Starts at the beginning skip the first ( offset - 1 )
                                       items and begin returning at the Nth item
            limit (StorageManagementHistoriesDiscardedDiscardedHistoriesParamLimit | None)
                                     : The maximum number of items to return.
            order (StorageManagementHistoriesDiscardedDiscardedHistoriesParamOrder | None)
                                     : String containing one of the valid ordering attributes
                                       followed by '-asc' or '-dsc' for ascending and descending
                                       order respectively.
            run-as (StorageManagementHistoriesDiscardedDiscardedHistoriesParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[StoredItem]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/storage/histories/discarded"

        params: dict[str, Any] = {
            **({"offset": DataclassSerializer.serialize(offset)} if offset is not None else {}),
            **({"limit": DataclassSerializer.serialize(limit)} if limit is not None else {}),
            **({"order": DataclassSerializer.serialize(order)} if order is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[StoredItem])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def storage_management_histories_discarded_discarded_histories(
        self,
        offset: StorageManagementHistoriesDiscardedDiscardedHistoriesParamOffset | None = None,
        limit: StorageManagementHistoriesDiscardedDiscardedHistoriesParamLimit | None = None,
        order: StorageManagementHistoriesDiscardedDiscardedHistoriesParamOrder | None = None,
        run_as: StorageManagementHistoriesDiscardedDiscardedHistoriesParamRunAs | None = None,
    ) -> list[StoredItem]:
        """
        Returns all discarded histories associated with the given user.

        Args:
            offset (StorageManagementHistoriesDiscardedDiscardedHistoriesParamOffset | None)
                                     : Starts at the beginning skip the first ( offset - 1 )
                                       items and begin returning at the Nth item
            limit (StorageManagementHistoriesDiscardedDiscardedHistoriesParamLimit | None)
                                     : The maximum number of items to return.
            order (StorageManagementHistoriesDiscardedDiscardedHistoriesParamOrder | None)
                                     : String containing one of the valid ordering attributes
                                       followed by '-asc' or '-dsc' for ascending and descending
                                       order respectively.
            run-as (StorageManagementHistoriesDiscardedDiscardedHistoriesParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[StoredItem]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/storage/histories/discarded"

        params: dict[str, Any] = {
            **({"offset": DataclassSerializer.serialize(offset)} if offset is not None else {}),
            **({"limit": DataclassSerializer.serialize(limit)} if limit is not None else {}),
            **({"order": DataclassSerializer.serialize(order)} if order is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[StoredItem])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def storage_management_histories_discarded_summary_discarded_histories_summary(
        self,
        run_as: StorageManagementHistoriesDiscardedSummaryDiscardedHistoriesSummaryParamRunAs | None = None,
    ) -> CleanableItemsSummary:
        """
        Returns information with the total storage space taken by discarded histories associated
        with the given user.

        Args:
            run-as (StorageManagementHistoriesDiscardedSummaryDiscardedHistoriesSummaryParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            CleanableItemsSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/storage/histories/discarded/summary"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), CleanableItemsSummary)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def storage_management_histories_discarded_summary_discarded_histories_summary(
        self,
        run_as: StorageManagementHistoriesDiscardedSummaryDiscardedHistoriesSummaryParamRunAs | None = None,
    ) -> CleanableItemsSummary:
        """
        Returns information with the total storage space taken by discarded histories associated
        with the given user.

        Args:
            run-as (StorageManagementHistoriesDiscardedSummaryDiscardedHistoriesSummaryParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            CleanableItemsSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/storage/histories/discarded/summary"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), CleanableItemsSummary)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover
