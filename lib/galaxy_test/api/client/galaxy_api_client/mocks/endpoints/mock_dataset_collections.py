from typing import TYPE_CHECKING

from ...models.create_new_collection_payload import CreateNewCollectionPayload
from ...models.create_workbook_for_collection_api import CreateWorkbookForCollectionApi
from ...models.create_workbook_request import CreateWorkbookRequest
from ...models.dataset_collection_attributes_result import DatasetCollectionAttributesResult
from ...models.dataset_collection_content_elements import DatasetCollectionContentElements
from ...models.dataset_collections_attributes_attributes_param_run_as import (
    DatasetCollectionsAttributesAttributesParamRunAs,
)
from ...models.dataset_collections_content_param_run_as import DatasetCollectionsContentParamRunAs
from ...models.dataset_collections_contents_contents_param_limit import DatasetCollectionsContentsContentsParamLimit
from ...models.dataset_collections_contents_contents_param_offset import DatasetCollectionsContentsContentsParamOffset
from ...models.dataset_collections_contents_contents_param_run_as import DatasetCollectionsContentsContentsParamRunAs
from ...models.dataset_collections_copy_copy_param_run_as import DatasetCollectionsCopyCopyParamRunAs
from ...models.dataset_collections_create_param_run_as import DatasetCollectionsCreateParamRunAs
from ...models.dataset_collections_show_200_response import DatasetCollectionsShow200Response
from ...models.dataset_collections_show_param_run_as import DatasetCollectionsShowParamRunAs
from ...models.dataset_collections_suitable_converters_suitable_converters_param_run_as import (
    DatasetCollectionsSuitableConvertersSuitableConvertersParamRunAs,
)
from ...models.dataset_collections_workbook_download_for_collection_param_filename import (
    DatasetCollectionsWorkbookDownloadForCollectionParamFilename,
)
from ...models.dataset_collections_workbook_download_for_collection_param_run_as import (
    DatasetCollectionsWorkbookDownloadForCollectionParamRunAs,
)
from ...models.dataset_collections_workbook_download_param_filename import (
    DatasetCollectionsWorkbookDownloadParamFilename,
)
from ...models.dataset_collections_workbook_download_param_run_as import DatasetCollectionsWorkbookDownloadParamRunAs
from ...models.dataset_collections_workbook_parse_for_collection_param_run_as import (
    DatasetCollectionsWorkbookParseForCollectionParamRunAs,
)
from ...models.dataset_collections_workbook_parse_param_run_as import DatasetCollectionsWorkbookParseParamRunAs
from ...models.dce_summary_2 import DceSummary2
from ...models.hdca_detailed_2 import HdcaDetailed2
from ...models.parse_workbook import ParseWorkbook
from ...models.parse_workbook_for_collection_api import ParseWorkbookForCollectionApi
from ...models.parsed_workbook import ParsedWorkbook
from ...models.parsed_workbook_for_collection import ParsedWorkbookForCollection
from ...models.suitable_converters import SuitableConverters
from ...models.update_collection_attribute_payload import UpdateCollectionAttributePayload

if TYPE_CHECKING:
    pass


class MockDatasetCollectionsClient:
    """
    Mock implementation of DatasetCollectionsClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestDatasetCollectionsClient(MockDatasetCollectionsClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def dataset_collections_content(
        self,
        dce_id: str,
        run_as: DatasetCollectionsContentParamRunAs | None = None,
    ) -> DceSummary2:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatasetCollectionsClient.dataset_collections_content() not implemented. Override this method in your test subclass."
        )

    async def dataset_collections_create(
        self,
        body: CreateNewCollectionPayload,
        run_as: DatasetCollectionsCreateParamRunAs | None = None,
    ) -> HdcaDetailed2:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatasetCollectionsClient.dataset_collections_create() not implemented. Override this method in your test subclass."
        )

    async def dataset_collections_show(
        self,
        hdca_id: str,
        instance_type: str | None = None,
        view: str | None = None,
        run_as: DatasetCollectionsShowParamRunAs | None = None,
    ) -> DatasetCollectionsShow200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatasetCollectionsClient.dataset_collections_show() not implemented. Override this method in your test subclass."
        )

    async def dataset_collections_attributes_attributes(
        self,
        hdca_id: str,
        instance_type: str | None = None,
        run_as: DatasetCollectionsAttributesAttributesParamRunAs | None = None,
    ) -> DatasetCollectionAttributesResult:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatasetCollectionsClient.dataset_collections_attributes_attributes() not implemented. Override this method in your test subclass."
        )

    async def dataset_collections_contents_contents(
        self,
        hdca_id: str,
        parent_id: str,
        instance_type: str | None = None,
        limit: DatasetCollectionsContentsContentsParamLimit | None = None,
        offset: DatasetCollectionsContentsContentsParamOffset | None = None,
        run_as: DatasetCollectionsContentsContentsParamRunAs | None = None,
    ) -> DatasetCollectionContentElements:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatasetCollectionsClient.dataset_collections_contents_contents() not implemented. Override this method in your test subclass."
        )

    async def dataset_collections_copy_copy(
        self,
        hdca_id: str,
        body: UpdateCollectionAttributePayload,
        run_as: DatasetCollectionsCopyCopyParamRunAs | None = None,
    ) -> None:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatasetCollectionsClient.dataset_collections_copy_copy() not implemented. Override this method in your test subclass."
        )

    async def dataset_collections_workbook_download_for_collection(
        self,
        hdca_id: str,
        body: CreateWorkbookForCollectionApi,
        filename: DatasetCollectionsWorkbookDownloadForCollectionParamFilename | None = None,
        run_as: DatasetCollectionsWorkbookDownloadForCollectionParamRunAs | None = None,
    ) -> None:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatasetCollectionsClient.dataset_collections_workbook_download_for_collection() not implemented. Override this method in your test subclass."
        )

    async def dataset_collections_workbook_parse_for_collection(
        self,
        hdca_id: str,
        body: ParseWorkbookForCollectionApi,
        run_as: DatasetCollectionsWorkbookParseForCollectionParamRunAs | None = None,
    ) -> ParsedWorkbookForCollection:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatasetCollectionsClient.dataset_collections_workbook_parse_for_collection() not implemented. Override this method in your test subclass."
        )

    async def dataset_collections_suitable_converters_suitable_converters(
        self,
        hdca_id: str,
        instance_type: str | None = None,
        run_as: DatasetCollectionsSuitableConvertersSuitableConvertersParamRunAs | None = None,
    ) -> SuitableConverters:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatasetCollectionsClient.dataset_collections_suitable_converters_suitable_converters() not implemented. Override this method in your test subclass."
        )

    async def dataset_collections_workbook_download(
        self,
        body: CreateWorkbookRequest,
        filename: DatasetCollectionsWorkbookDownloadParamFilename | None = None,
        run_as: DatasetCollectionsWorkbookDownloadParamRunAs | None = None,
    ) -> None:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatasetCollectionsClient.dataset_collections_workbook_download() not implemented. Override this method in your test subclass."
        )

    async def dataset_collections_workbook_parse(
        self,
        body: ParseWorkbook,
        run_as: DatasetCollectionsWorkbookParseParamRunAs | None = None,
    ) -> ParsedWorkbook:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatasetCollectionsClient.dataset_collections_workbook_parse() not implemented. Override this method in your test subclass."
        )
