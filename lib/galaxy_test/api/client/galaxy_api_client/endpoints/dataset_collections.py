from typing import Any, cast

from galaxy_test.api.client.galaxy_api_client.core import Error501
from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.async_file import AsyncFile
from ..models.create_new_collection_payload import CreateNewCollectionPayload
from ..models.create_workbook_for_collection_api import CreateWorkbookForCollectionApi
from ..models.create_workbook_request import CreateWorkbookRequest
from ..models.dataset_collection_attributes_result import DatasetCollectionAttributesResult
from ..models.dataset_collection_content_elements import DatasetCollectionContentElements
from ..models.dataset_collections_attributes_attributes_param_run_as import (
    DatasetCollectionsAttributesAttributesParamRunAs,
)
from ..models.dataset_collections_content_param_run_as import DatasetCollectionsContentParamRunAs
from ..models.dataset_collections_contents_contents_param_limit import DatasetCollectionsContentsContentsParamLimit
from ..models.dataset_collections_contents_contents_param_offset import DatasetCollectionsContentsContentsParamOffset
from ..models.dataset_collections_contents_contents_param_run_as import DatasetCollectionsContentsContentsParamRunAs
from ..models.dataset_collections_copy_copy_param_run_as import DatasetCollectionsCopyCopyParamRunAs
from ..models.dataset_collections_create_param_run_as import DatasetCollectionsCreateParamRunAs
from ..models.dataset_collections_download_param_run_as import DatasetCollectionsDownloadParamRunAs
from ..models.dataset_collections_show_200_response_2 import DatasetCollectionsShow200Response2
from ..models.dataset_collections_show_param_run_as import DatasetCollectionsShowParamRunAs
from ..models.dataset_collections_suitable_converters_suitable_converters_param_run_as import (
    DatasetCollectionsSuitableConvertersSuitableConvertersParamRunAs,
)
from ..models.dataset_collections_workbook_download_for_collection_param_filename import (
    DatasetCollectionsWorkbookDownloadForCollectionParamFilename,
)
from ..models.dataset_collections_workbook_download_for_collection_param_run_as import (
    DatasetCollectionsWorkbookDownloadForCollectionParamRunAs,
)
from ..models.dataset_collections_workbook_download_param_filename import (
    DatasetCollectionsWorkbookDownloadParamFilename,
)
from ..models.dataset_collections_workbook_download_param_run_as import DatasetCollectionsWorkbookDownloadParamRunAs
from ..models.dataset_collections_workbook_parse_for_collection_param_run_as import (
    DatasetCollectionsWorkbookParseForCollectionParamRunAs,
)
from ..models.dataset_collections_workbook_parse_param_run_as import DatasetCollectionsWorkbookParseParamRunAs
from ..models.dce_summary_9 import DceSummary9
from ..models.hdca_detailed_2 import HdcaDetailed2
from ..models.histories_prepare_download_prepare_collection_download_param_run_as import (
    HistoriesPrepareDownloadPrepareCollectionDownloadParamRunAs,
)
from ..models.parse_workbook import ParseWorkbook
from ..models.parse_workbook_for_collection_api import ParseWorkbookForCollectionApi
from ..models.parsed_workbook import ParsedWorkbook
from ..models.parsed_workbook_for_collection import ParsedWorkbookForCollection
from ..models.suitable_converters import SuitableConverters
from ..models.update_collection_attribute_payload import UpdateCollectionAttributePayload


class DatasetCollectionsClient:
    """Client for dataset collections endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def dataset_collections_content_2_2(
        self,
        dce_id: str,
        run_as: DatasetCollectionsContentParamRunAs | None = None,
    ) -> DceSummary9:
        """
        Content

        Args:
            dce_id (str)             : The encoded ID of the dataset collection element.
            run-as (Optional[DatasetCollectionsContentParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DceSummary9: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/dataset_collection_element/{dce_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DceSummary9, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dataset_collections_content_2_2(
        self,
        dce_id: str,
        run_as: DatasetCollectionsContentParamRunAs | None = None,
    ) -> DceSummary9:
        """
        Content

        Args:
            dce_id (str)             : The encoded ID of the dataset collection element.
            run-as (Optional[DatasetCollectionsContentParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DceSummary9: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/dataset_collection_element/{dce_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DceSummary9, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dataset_collections_create_2_2(
        self,
        body: CreateNewCollectionPayload,
        run_as: DatasetCollectionsCreateParamRunAs | None = None,
    ) -> HdcaDetailed2:
        """
        Create a new dataset collection instance.

        Args:
            run-as (Optional[DatasetCollectionsCreateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateNewCollectionPayload)
                                     : Request body. (json)

        Returns:
            HdcaDetailed2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/dataset_collections"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateNewCollectionPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(HdcaDetailed2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dataset_collections_create_2_2(
        self,
        body: CreateNewCollectionPayload,
        run_as: DatasetCollectionsCreateParamRunAs | None = None,
    ) -> HdcaDetailed2:
        """
        Create a new dataset collection instance.

        Args:
            run-as (Optional[DatasetCollectionsCreateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateNewCollectionPayload)
                                     : Request body. (json)

        Returns:
            HdcaDetailed2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/dataset_collections"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateNewCollectionPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(HdcaDetailed2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dataset_collections_show_2_2(
        self,
        hdca_id: str,
        instance_type: str | None = "history",
        view: str | None = "element",
        run_as: DatasetCollectionsShowParamRunAs | None = None,
    ) -> DatasetCollectionsShow200Response2:
        """
        Returns detailed information about the given collection.

        Args:
            hdca_id (str)            : The ID of the `HDCA`.
            instance_type (Optional[str])
                                     : The type of collection instance. Either `history`
                                       (default) or `library`.
            view (Optional[str])     : The view of collection instance to return.
            run-as (Optional[DatasetCollectionsShowParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DatasetCollectionsShow200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/dataset_collections/{hdca_id}"

        params: dict[str, Any] = {
            **({"instance_type": instance_type} if instance_type is not None else {}),
            **({"view": view} if view is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DatasetCollectionsShow200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dataset_collections_show_2_2(
        self,
        hdca_id: str,
        instance_type: str | None = "history",
        view: str | None = "element",
        run_as: DatasetCollectionsShowParamRunAs | None = None,
    ) -> DatasetCollectionsShow200Response2:
        """
        Returns detailed information about the given collection.

        Args:
            hdca_id (str)            : The ID of the `HDCA`.
            instance_type (Optional[str])
                                     : The type of collection instance. Either `history`
                                       (default) or `library`.
            view (Optional[str])     : The view of collection instance to return.
            run-as (Optional[DatasetCollectionsShowParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DatasetCollectionsShow200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/dataset_collections/{hdca_id}"

        params: dict[str, Any] = {
            **({"instance_type": instance_type} if instance_type is not None else {}),
            **({"view": view} if view is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DatasetCollectionsShow200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dataset_collections_attributes_attributes_2_2(
        self,
        hdca_id: str,
        instance_type: str | None = "history",
        run_as: DatasetCollectionsAttributesAttributesParamRunAs | None = None,
    ) -> DatasetCollectionAttributesResult:
        """
        Returns `dbkey`/`extension` attributes for all the collection elements.

        Args:
            hdca_id (str)            : The ID of the `HDCA`.
            instance_type (Optional[str])
                                     : The type of collection instance. Either `history`
                                       (default) or `library`.
            run-as (Optional[DatasetCollectionsAttributesAttributesParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DatasetCollectionAttributesResult: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/dataset_collections/{hdca_id}/attributes"

        params: dict[str, Any] = {
            **({"instance_type": instance_type} if instance_type is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DatasetCollectionAttributesResult, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dataset_collections_attributes_attributes_2_2(
        self,
        hdca_id: str,
        instance_type: str | None = "history",
        run_as: DatasetCollectionsAttributesAttributesParamRunAs | None = None,
    ) -> DatasetCollectionAttributesResult:
        """
        Returns `dbkey`/`extension` attributes for all the collection elements.

        Args:
            hdca_id (str)            : The ID of the `HDCA`.
            instance_type (Optional[str])
                                     : The type of collection instance. Either `history`
                                       (default) or `library`.
            run-as (Optional[DatasetCollectionsAttributesAttributesParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DatasetCollectionAttributesResult: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/dataset_collections/{hdca_id}/attributes"

        params: dict[str, Any] = {
            **({"instance_type": instance_type} if instance_type is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DatasetCollectionAttributesResult, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dataset_collections_contents_contents_2_2(
        self,
        hdca_id: str,
        parent_id: str,
        instance_type: str | None = "history",
        limit: DatasetCollectionsContentsContentsParamLimit | None = None,
        offset: DatasetCollectionsContentsContentsParamOffset | None = None,
        run_as: DatasetCollectionsContentsContentsParamRunAs | None = None,
    ) -> DatasetCollectionContentElements:
        """
        Returns direct child contents of indicated dataset collection parent ID.

        Args:
            hdca_id (str)            : The ID of the `HDCA`.
            parent_id (str)          : Parent collection ID describing what collection the
                                       contents belongs to.
            instance_type (Optional[str])
                                     : The type of collection instance. Either `history`
                                       (default) or `library`.
            limit (Optional[DatasetCollectionsContentsContentsParamLimit])
                                     : The maximum number of content elements to return.
            offset (Optional[DatasetCollectionsContentsContentsParamOffset])
                                     : The number of content elements that will be skipped
                                       before returning.
            run-as (Optional[DatasetCollectionsContentsContentsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DatasetCollectionContentElements: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/dataset_collections/{hdca_id}/contents/{parent_id}"

        params: dict[str, Any] = {
            **({"instance_type": instance_type} if instance_type is not None else {}),
            **({"limit": limit} if limit is not None else {}),
            **({"offset": offset} if offset is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DatasetCollectionContentElements, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dataset_collections_contents_contents_2_2(
        self,
        hdca_id: str,
        parent_id: str,
        instance_type: str | None = "history",
        limit: DatasetCollectionsContentsContentsParamLimit | None = None,
        offset: DatasetCollectionsContentsContentsParamOffset | None = None,
        run_as: DatasetCollectionsContentsContentsParamRunAs | None = None,
    ) -> DatasetCollectionContentElements:
        """
        Returns direct child contents of indicated dataset collection parent ID.

        Args:
            hdca_id (str)            : The ID of the `HDCA`.
            parent_id (str)          : Parent collection ID describing what collection the
                                       contents belongs to.
            instance_type (Optional[str])
                                     : The type of collection instance. Either `history`
                                       (default) or `library`.
            limit (Optional[DatasetCollectionsContentsContentsParamLimit])
                                     : The maximum number of content elements to return.
            offset (Optional[DatasetCollectionsContentsContentsParamOffset])
                                     : The number of content elements that will be skipped
                                       before returning.
            run-as (Optional[DatasetCollectionsContentsContentsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DatasetCollectionContentElements: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/dataset_collections/{hdca_id}/contents/{parent_id}"

        params: dict[str, Any] = {
            **({"instance_type": instance_type} if instance_type is not None else {}),
            **({"limit": limit} if limit is not None else {}),
            **({"offset": offset} if offset is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DatasetCollectionContentElements, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dataset_collections_copy_copy_2_2(
        self,
        hdca_id: str,
        body: UpdateCollectionAttributePayload,
        run_as: DatasetCollectionsCopyCopyParamRunAs | None = None,
    ) -> None:
        """
        Copy the given collection datasets to a new collection using a new `dbkey` attribute.

        Args:
            hdca_id (str)            : The ID of the `HDCA`.
            run-as (Optional[DatasetCollectionsCopyCopyParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UpdateCollectionAttributePayload)
                                     : Request body. (json)

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/dataset_collections/{hdca_id}/copy"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: UpdateCollectionAttributePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dataset_collections_copy_copy_2_2(
        self,
        hdca_id: str,
        body: UpdateCollectionAttributePayload,
        run_as: DatasetCollectionsCopyCopyParamRunAs | None = None,
    ) -> None:
        """
        Copy the given collection datasets to a new collection using a new `dbkey` attribute.

        Args:
            hdca_id (str)            : The ID of the `HDCA`.
            run-as (Optional[DatasetCollectionsCopyCopyParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UpdateCollectionAttributePayload)
                                     : Request body. (json)

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/dataset_collections/{hdca_id}/copy"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: UpdateCollectionAttributePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dataset_collections_download_2(
        self,
        hdca_id: str,
        run_as: DatasetCollectionsDownloadParamRunAs | None = None,
    ) -> None:
        """
        Download the content of a dataset collection as a `zip` archive.

        Download the content of a history dataset collection as a `zip` archive while
        maintaining approximate collection structure.

        Args:
            hdca_id (str)            : The ID of the `HDCA`.
            run-as (Optional[DatasetCollectionsDownloadParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/dataset_collections/{hdca_id}/download"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_prepare_download_prepare_collection_download_2(
        self,
        hdca_id: str,
        run_as: HistoriesPrepareDownloadPrepareCollectionDownloadParamRunAs | None = None,
    ) -> AsyncFile:
        """
        Prepare an short term storage object that the collection will be downloaded to.

        The history dataset collection will be written as a `zip` archive to the returned short
        term storage object. Progress tracking this file's creation can be tracked with the
        short_term_storage API.

        Args:
            hdca_id (str)            : The ID of the `HDCA`.
            run-as (Optional[HistoriesPrepareDownloadPrepareCollectionDownloadParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            AsyncFile: Short term storage reference for async monitoring of this download.

        Raises:
            HttpError:
                HTTPError: 501: Required asynchronous tasks required for this operation not
                           available.
        """
        url = f"{self.base_url}/api/dataset_collections/{hdca_id}/prepare_download"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(AsyncFile, response.json())
            case 501:
                raise Error501(response=response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dataset_collections_workbook_download_for_collection_2_2(
        self,
        hdca_id: str,
        body: CreateWorkbookForCollectionApi,
        filename: DatasetCollectionsWorkbookDownloadForCollectionParamFilename | None = None,
        run_as: DatasetCollectionsWorkbookDownloadForCollectionParamRunAs | None = None,
    ) -> None:
        """
        Create an XLSX workbook for a sample sheet definition targeting an existing collection.

        Args:
            hdca_id (str)            : The ID of the `HDCA`.
            filename (Optional[DatasetCollectionsWorkbookDownloadForCollectionParamFilename])
                                     : Filename of the workbook download to generate
            run-as (Optional[DatasetCollectionsWorkbookDownloadForCollectionParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateWorkbookForCollectionApi)
                                     : Request body. (json)

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/dataset_collections/{hdca_id}/sample_sheet_workbook"

        params: dict[str, Any] = {
            **({"filename": filename} if filename is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateWorkbookForCollectionApi = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dataset_collections_workbook_download_for_collection_2_2(
        self,
        hdca_id: str,
        body: CreateWorkbookForCollectionApi,
        filename: DatasetCollectionsWorkbookDownloadForCollectionParamFilename | None = None,
        run_as: DatasetCollectionsWorkbookDownloadForCollectionParamRunAs | None = None,
    ) -> None:
        """
        Create an XLSX workbook for a sample sheet definition targeting an existing collection.

        Args:
            hdca_id (str)            : The ID of the `HDCA`.
            filename (Optional[DatasetCollectionsWorkbookDownloadForCollectionParamFilename])
                                     : Filename of the workbook download to generate
            run-as (Optional[DatasetCollectionsWorkbookDownloadForCollectionParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateWorkbookForCollectionApi)
                                     : Request body. (json)

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/dataset_collections/{hdca_id}/sample_sheet_workbook"

        params: dict[str, Any] = {
            **({"filename": filename} if filename is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateWorkbookForCollectionApi = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dataset_collections_workbook_parse_for_collection_2_2(
        self,
        hdca_id: str,
        body: ParseWorkbookForCollectionApi,
        run_as: DatasetCollectionsWorkbookParseForCollectionParamRunAs | None = None,
    ) -> ParsedWorkbookForCollection:
        """
        Parse an XLSX workbook for a sample sheet definition and supplied file contents.

        Args:
            hdca_id (str)            : The ID of the `HDCA`.
            run-as (Optional[DatasetCollectionsWorkbookParseForCollectionParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (ParseWorkbookForCollectionApi)
                                     : Request body. (json)

        Returns:
            ParsedWorkbookForCollection: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/dataset_collections/{hdca_id}/sample_sheet_workbook/parse"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: ParseWorkbookForCollectionApi = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ParsedWorkbookForCollection, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dataset_collections_workbook_parse_for_collection_2_2(
        self,
        hdca_id: str,
        body: ParseWorkbookForCollectionApi,
        run_as: DatasetCollectionsWorkbookParseForCollectionParamRunAs | None = None,
    ) -> ParsedWorkbookForCollection:
        """
        Parse an XLSX workbook for a sample sheet definition and supplied file contents.

        Args:
            hdca_id (str)            : The ID of the `HDCA`.
            run-as (Optional[DatasetCollectionsWorkbookParseForCollectionParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (ParseWorkbookForCollectionApi)
                                     : Request body. (json)

        Returns:
            ParsedWorkbookForCollection: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/dataset_collections/{hdca_id}/sample_sheet_workbook/parse"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: ParseWorkbookForCollectionApi = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ParsedWorkbookForCollection, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dataset_collections_suitable_converters_suitable_converters_2_2(
        self,
        hdca_id: str,
        instance_type: str | None = "history",
        run_as: DatasetCollectionsSuitableConvertersSuitableConvertersParamRunAs | None = None,
    ) -> SuitableConverters:
        """
        Returns a list of applicable converters for all datatypes in the given collection.

        Args:
            hdca_id (str)            : The ID of the `HDCA`.
            instance_type (Optional[str])
                                     : The type of collection instance. Either `history`
                                       (default) or `library`.
            run-as (Optional[DatasetCollectionsSuitableConvertersSuitableConvertersParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            SuitableConverters: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/dataset_collections/{hdca_id}/suitable_converters"

        params: dict[str, Any] = {
            **({"instance_type": instance_type} if instance_type is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(SuitableConverters, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dataset_collections_suitable_converters_suitable_converters_2_2(
        self,
        hdca_id: str,
        instance_type: str | None = "history",
        run_as: DatasetCollectionsSuitableConvertersSuitableConvertersParamRunAs | None = None,
    ) -> SuitableConverters:
        """
        Returns a list of applicable converters for all datatypes in the given collection.

        Args:
            hdca_id (str)            : The ID of the `HDCA`.
            instance_type (Optional[str])
                                     : The type of collection instance. Either `history`
                                       (default) or `library`.
            run-as (Optional[DatasetCollectionsSuitableConvertersSuitableConvertersParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            SuitableConverters: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/dataset_collections/{hdca_id}/suitable_converters"

        params: dict[str, Any] = {
            **({"instance_type": instance_type} if instance_type is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(SuitableConverters, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dataset_collections_workbook_download_2_2(
        self,
        body: CreateWorkbookRequest,
        filename: DatasetCollectionsWorkbookDownloadParamFilename | None = None,
        run_as: DatasetCollectionsWorkbookDownloadParamRunAs | None = None,
    ) -> None:
        """
        Create an XLSX workbook for a sample sheet definition.

        Args:
            filename (Optional[DatasetCollectionsWorkbookDownloadParamFilename])
                                     : Filename of the workbook download to generate
            run-as (Optional[DatasetCollectionsWorkbookDownloadParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateWorkbookRequest)
                                     : Request body. (json)

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/sample_sheet_workbook"

        params: dict[str, Any] = {
            **({"filename": filename} if filename is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateWorkbookRequest = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dataset_collections_workbook_download_2_2(
        self,
        body: CreateWorkbookRequest,
        filename: DatasetCollectionsWorkbookDownloadParamFilename | None = None,
        run_as: DatasetCollectionsWorkbookDownloadParamRunAs | None = None,
    ) -> None:
        """
        Create an XLSX workbook for a sample sheet definition.

        Args:
            filename (Optional[DatasetCollectionsWorkbookDownloadParamFilename])
                                     : Filename of the workbook download to generate
            run-as (Optional[DatasetCollectionsWorkbookDownloadParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateWorkbookRequest)
                                     : Request body. (json)

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/sample_sheet_workbook"

        params: dict[str, Any] = {
            **({"filename": filename} if filename is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateWorkbookRequest = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dataset_collections_workbook_parse_2_2(
        self,
        body: ParseWorkbook,
        run_as: DatasetCollectionsWorkbookParseParamRunAs | None = None,
    ) -> ParsedWorkbook:
        """
        Parse an XLSX workbook for a sample sheet definition and supplied file contents.

        Args:
            run-as (Optional[DatasetCollectionsWorkbookParseParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (ParseWorkbook)     : Request body. (json)

        Returns:
            ParsedWorkbook: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/sample_sheet_workbook/parse"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: ParseWorkbook = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ParsedWorkbook, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dataset_collections_workbook_parse_2_2(
        self,
        body: ParseWorkbook,
        run_as: DatasetCollectionsWorkbookParseParamRunAs | None = None,
    ) -> ParsedWorkbook:
        """
        Parse an XLSX workbook for a sample sheet definition and supplied file contents.

        Args:
            run-as (Optional[DatasetCollectionsWorkbookParseParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (ParseWorkbook)     : Request body. (json)

        Returns:
            ParsedWorkbook: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/sample_sheet_workbook/parse"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: ParseWorkbook = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ParsedWorkbook, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover
