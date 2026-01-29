from typing import TYPE_CHECKING, Any

from ...models.anonymous_array_item_85 import AnonymousArrayItem85
from ...models.async_task_result_summary import AsyncTaskResultSummary
from ...models.compute_dataset_hash_payload import ComputeDatasetHashPayload
from ...models.converted_datasets_map import ConvertedDatasetsMap
from ...models.dataset_association_roles import DatasetAssociationRoles
from ...models.dataset_content_type import DatasetContentType
from ...models.dataset_extra_files import DatasetExtraFiles
from ...models.dataset_inheritance_chain import DatasetInheritanceChain
from ...models.dataset_source_type import DatasetSourceType
from ...models.dataset_storage_details import DatasetStorageDetails
from ...models.dataset_text_content_details import DatasetTextContentDetails
from ...models.datasets_content_get_structured_content_param_run_as import DatasetsContentGetStructuredContentParamRunAs
from ...models.datasets_contents_display_display_history_content_param_ck_size import (
    DatasetsContentsDisplayDisplayHistoryContentParamCkSize,
)
from ...models.datasets_contents_display_display_history_content_param_ck_size_2 import (
    DatasetsContentsDisplayDisplayHistoryContentParamCkSize2,
)
from ...models.datasets_contents_display_display_history_content_param_filename import (
    DatasetsContentsDisplayDisplayHistoryContentParamFilename,
)
from ...models.datasets_contents_display_display_history_content_param_filename_2 import (
    DatasetsContentsDisplayDisplayHistoryContentParamFilename2,
)
from ...models.datasets_contents_display_display_history_content_param_history_id import (
    DatasetsContentsDisplayDisplayHistoryContentParamHistoryId,
)
from ...models.datasets_contents_display_display_history_content_param_history_id_2 import (
    DatasetsContentsDisplayDisplayHistoryContentParamHistoryId2,
)
from ...models.datasets_contents_display_display_history_content_param_offset import (
    DatasetsContentsDisplayDisplayHistoryContentParamOffset,
)
from ...models.datasets_contents_display_display_history_content_param_offset_2 import (
    DatasetsContentsDisplayDisplayHistoryContentParamOffset2,
)
from ...models.datasets_contents_display_display_history_content_param_run_as import (
    DatasetsContentsDisplayDisplayHistoryContentParamRunAs,
)
from ...models.datasets_contents_display_display_history_content_param_run_as_2 import (
    DatasetsContentsDisplayDisplayHistoryContentParamRunAs2,
)
from ...models.datasets_contents_display_display_history_content_param_to_ext import (
    DatasetsContentsDisplayDisplayHistoryContentParamToExt,
)
from ...models.datasets_contents_display_display_history_content_param_to_ext_2 import (
    DatasetsContentsDisplayDisplayHistoryContentParamToExt2,
)
from ...models.datasets_contents_extra_files_extra_files_history_param_run_as import (
    DatasetsContentsExtraFilesExtraFilesHistoryParamRunAs,
)
from ...models.datasets_converted_converted_ext_200_response import DatasetsConvertedConvertedExt200Response
from ...models.datasets_converted_converted_ext_param_keys import DatasetsConvertedConvertedExtParamKeys
from ...models.datasets_converted_converted_ext_param_run_as import DatasetsConvertedConvertedExtParamRunAs
from ...models.datasets_converted_converted_ext_param_view import DatasetsConvertedConvertedExtParamView
from ...models.datasets_converted_converted_param_run_as import DatasetsConvertedConvertedParamRunAs
from ...models.datasets_delete_batch_param_run_as import DatasetsDeleteBatchParamRunAs
from ...models.datasets_display_display_param_ck_size import DatasetsDisplayDisplayParamCkSize
from ...models.datasets_display_display_param_ck_size_2 import DatasetsDisplayDisplayParamCkSize2
from ...models.datasets_display_display_param_filename import DatasetsDisplayDisplayParamFilename
from ...models.datasets_display_display_param_filename_2 import DatasetsDisplayDisplayParamFilename2
from ...models.datasets_display_display_param_offset import DatasetsDisplayDisplayParamOffset
from ...models.datasets_display_display_param_offset_2 import DatasetsDisplayDisplayParamOffset2
from ...models.datasets_display_display_param_run_as import DatasetsDisplayDisplayParamRunAs
from ...models.datasets_display_display_param_run_as_2 import DatasetsDisplayDisplayParamRunAs2
from ...models.datasets_display_display_param_to_ext import DatasetsDisplayDisplayParamToExt
from ...models.datasets_display_display_param_to_ext_2 import DatasetsDisplayDisplayParamToExt2
from ...models.datasets_extra_files_extra_files_param_run_as import DatasetsExtraFilesExtraFilesParamRunAs
from ...models.datasets_extra_files_raw_extra_file_raw_param_run_as import DatasetsExtraFilesRawExtraFileRawParamRunAs
from ...models.datasets_get_content_as_text_get_content_as_text_param_filename import (
    DatasetsGetContentAsTextGetContentAsTextParamFilename,
)
from ...models.datasets_get_content_as_text_get_content_as_text_param_run_as import (
    DatasetsGetContentAsTextGetContentAsTextParamRunAs,
)
from ...models.datasets_get_metadata_file_param_run_as import DatasetsGetMetadataFileParamRunAs
from ...models.datasets_hash_compute_hash_param_run_as import DatasetsHashComputeHashParamRunAs
from ...models.datasets_index_param_history_id import DatasetsIndexParamHistoryId
from ...models.datasets_index_param_keys import DatasetsIndexParamKeys
from ...models.datasets_index_param_limit import DatasetsIndexParamLimit
from ...models.datasets_index_param_offset import DatasetsIndexParamOffset
from ...models.datasets_index_param_order import DatasetsIndexParamOrder
from ...models.datasets_index_param_q import DatasetsIndexParamQ
from ...models.datasets_index_param_qv import DatasetsIndexParamQv
from ...models.datasets_index_param_run_as import DatasetsIndexParamRunAs
from ...models.datasets_index_param_view import DatasetsIndexParamView
from ...models.datasets_inheritance_chain_show_inheritance_chain_param_run_as import (
    DatasetsInheritanceChainShowInheritanceChainParamRunAs,
)
from ...models.datasets_metadata_file_get_metadata_file_datasets_param_run_as import (
    DatasetsMetadataFileGetMetadataFileDatasetsParamRunAs,
)
from ...models.datasets_permissions_update_permissions_param_run_as import (
    DatasetsPermissionsUpdatePermissionsParamRunAs,
)
from ...models.datasets_permissions_update_permissions_request_body import (
    DatasetsPermissionsUpdatePermissionsRequestBody,
)
from ...models.datasets_report_report_param_run_as import DatasetsReportReportParamRunAs
from ...models.datasets_show_param_data_type import DatasetsShowParamDataType
from ...models.datasets_show_param_keys import DatasetsShowParamKeys
from ...models.datasets_show_param_limit import DatasetsShowParamLimit
from ...models.datasets_show_param_offset import DatasetsShowParamOffset
from ...models.datasets_show_param_run_as import DatasetsShowParamRunAs
from ...models.datasets_show_param_view import DatasetsShowParamView
from ...models.datasets_storage_show_storage_param_run_as import DatasetsStorageShowStorageParamRunAs
from ...models.datasets_update_object_store_id_param_run_as import DatasetsUpdateObjectStoreIdParamRunAs
from ...models.delete_dataset_batch_payload import DeleteDatasetBatchPayload
from ...models.delete_dataset_batch_result import DeleteDatasetBatchResult
from ...models.history_contents_get_metadata_file_param_run_as import HistoryContentsGetMetadataFileParamRunAs
from ...models.tool_report_for_dataset import ToolReportForDataset
from ...models.update_object_store_id_payload import UpdateObjectStoreIdPayload

if TYPE_CHECKING:
    pass


class MockDatasetsClient:
    """
    Mock implementation of DatasetsClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestDatasetsClient(MockDatasetsClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def datasets_delete_batch(
        self,
        body: DeleteDatasetBatchPayload,
        run_as: DatasetsDeleteBatchParamRunAs | None = None,
    ) -> DeleteDatasetBatchResult:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatasetsClient.datasets_delete_batch() not implemented. Override this method in your test subclass."
        )

    async def datasets_index(
        self,
        history_id: DatasetsIndexParamHistoryId | None = None,
        view: DatasetsIndexParamView | None = None,
        keys: DatasetsIndexParamKeys | None = None,
        q: DatasetsIndexParamQ | None = None,
        qv: DatasetsIndexParamQv | None = None,
        offset: DatasetsIndexParamOffset | None = None,
        limit: DatasetsIndexParamLimit | None = None,
        order: DatasetsIndexParamOrder | None = None,
        run_as: DatasetsIndexParamRunAs | None = None,
    ) -> list[AnonymousArrayItem85]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatasetsClient.datasets_index() not implemented. Override this method in your test subclass."
        )

    async def datasets_show(
        self,
        dataset_id: str,
        hda_ldda: DatasetSourceType | None = None,
        data_type: DatasetsShowParamDataType | None = None,
        limit: DatasetsShowParamLimit | None = None,
        offset: DatasetsShowParamOffset | None = None,
        view: DatasetsShowParamView | None = None,
        keys: DatasetsShowParamKeys | None = None,
        run_as: DatasetsShowParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatasetsClient.datasets_show() not implemented. Override this method in your test subclass."
        )

    async def datasets_content_get_structured_content(
        self,
        dataset_id: str,
        content_type: DatasetContentType,
        run_as: DatasetsContentGetStructuredContentParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatasetsClient.datasets_content_get_structured_content() not implemented. Override this method in your test subclass."
        )

    async def datasets_converted_converted(
        self,
        dataset_id: str,
        run_as: DatasetsConvertedConvertedParamRunAs | None = None,
    ) -> ConvertedDatasetsMap:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatasetsClient.datasets_converted_converted() not implemented. Override this method in your test subclass."
        )

    async def datasets_converted_converted_ext(
        self,
        dataset_id: str,
        ext: str,
        view: DatasetsConvertedConvertedExtParamView | None = None,
        keys: DatasetsConvertedConvertedExtParamKeys | None = None,
        run_as: DatasetsConvertedConvertedExtParamRunAs | None = None,
    ) -> DatasetsConvertedConvertedExt200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatasetsClient.datasets_converted_converted_ext() not implemented. Override this method in your test subclass."
        )

    async def datasets_extra_files_extra_files(
        self,
        dataset_id: str,
        run_as: DatasetsExtraFilesExtraFilesParamRunAs | None = None,
    ) -> DatasetExtraFiles:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatasetsClient.datasets_extra_files_extra_files() not implemented. Override this method in your test subclass."
        )

    async def datasets_extra_files_raw_extra_file_raw(
        self,
        dataset_id: str,
        filename: str,
        run_as: DatasetsExtraFilesRawExtraFileRawParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatasetsClient.datasets_extra_files_raw_extra_file_raw() not implemented. Override this method in your test subclass."
        )

    async def datasets_get_content_as_text_get_content_as_text(
        self,
        dataset_id: str,
        filename: DatasetsGetContentAsTextGetContentAsTextParamFilename | None = None,
        run_as: DatasetsGetContentAsTextGetContentAsTextParamRunAs | None = None,
    ) -> DatasetTextContentDetails:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatasetsClient.datasets_get_content_as_text_get_content_as_text() not implemented. Override this method in your test subclass."
        )

    async def datasets_hash_compute_hash(
        self,
        dataset_id: str,
        body: ComputeDatasetHashPayload,
        hda_ldda: DatasetSourceType | None = None,
        run_as: DatasetsHashComputeHashParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatasetsClient.datasets_hash_compute_hash() not implemented. Override this method in your test subclass."
        )

    async def datasets_inheritance_chain_show_inheritance_chain(
        self,
        dataset_id: str,
        hda_ldda: DatasetSourceType | None = None,
        run_as: DatasetsInheritanceChainShowInheritanceChainParamRunAs | None = None,
    ) -> DatasetInheritanceChain:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatasetsClient.datasets_inheritance_chain_show_inheritance_chain() not implemented. Override this method in your test subclass."
        )

    async def datasets_update_object_store_id(
        self,
        dataset_id: str,
        body: UpdateObjectStoreIdPayload,
        run_as: DatasetsUpdateObjectStoreIdParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatasetsClient.datasets_update_object_store_id() not implemented. Override this method in your test subclass."
        )

    async def datasets_permissions_update_permissions(
        self,
        dataset_id: str,
        body: DatasetsPermissionsUpdatePermissionsRequestBody,
        run_as: DatasetsPermissionsUpdatePermissionsParamRunAs | None = None,
    ) -> DatasetAssociationRoles:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatasetsClient.datasets_permissions_update_permissions() not implemented. Override this method in your test subclass."
        )

    async def datasets_report_report(
        self,
        dataset_id: str,
        run_as: DatasetsReportReportParamRunAs | None = None,
    ) -> ToolReportForDataset:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatasetsClient.datasets_report_report() not implemented. Override this method in your test subclass."
        )

    async def datasets_storage_show_storage(
        self,
        dataset_id: str,
        hda_ldda: DatasetSourceType | None = None,
        run_as: DatasetsStorageShowStorageParamRunAs | None = None,
    ) -> DatasetStorageDetails:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatasetsClient.datasets_storage_show_storage() not implemented. Override this method in your test subclass."
        )

    async def datasets_display_display(
        self,
        history_content_id: str,
        preview: bool | None = None,
        filename: DatasetsDisplayDisplayParamFilename | None = None,
        to_ext: DatasetsDisplayDisplayParamToExt | None = None,
        raw: bool | None = None,
        offset: DatasetsDisplayDisplayParamOffset | None = None,
        ck_size: DatasetsDisplayDisplayParamCkSize | None = None,
        run_as: DatasetsDisplayDisplayParamRunAs | None = None,
    ) -> None:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatasetsClient.datasets_display_display() not implemented. Override this method in your test subclass."
        )

    async def datasets_display_display_2(
        self,
        history_content_id: str,
        preview: bool | None = None,
        filename: DatasetsDisplayDisplayParamFilename2 | None = None,
        to_ext: DatasetsDisplayDisplayParamToExt2 | None = None,
        raw: bool | None = None,
        offset: DatasetsDisplayDisplayParamOffset2 | None = None,
        ck_size: DatasetsDisplayDisplayParamCkSize2 | None = None,
        run_as: DatasetsDisplayDisplayParamRunAs2 | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatasetsClient.datasets_display_display_2() not implemented. Override this method in your test subclass."
        )

    async def datasets_get_metadata_file(
        self,
        history_content_id: str,
        metadata_file: str,
        run_as: DatasetsGetMetadataFileParamRunAs | None = None,
    ) -> None:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatasetsClient.datasets_get_metadata_file() not implemented. Override this method in your test subclass."
        )

    async def datasets_metadata_file_get_metadata_file_datasets(
        self,
        history_content_id: str,
        metadata_file: str,
        run_as: DatasetsMetadataFileGetMetadataFileDatasetsParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatasetsClient.datasets_metadata_file_get_metadata_file_datasets() not implemented. Override this method in your test subclass."
        )

    async def datasets_contents_display_display_history_content(
        self,
        history_content_id: str,
        history_id: DatasetsContentsDisplayDisplayHistoryContentParamHistoryId | None,
        preview: bool | None = None,
        filename: DatasetsContentsDisplayDisplayHistoryContentParamFilename | None = None,
        to_ext: DatasetsContentsDisplayDisplayHistoryContentParamToExt | None = None,
        raw: bool | None = None,
        offset: DatasetsContentsDisplayDisplayHistoryContentParamOffset | None = None,
        ck_size: DatasetsContentsDisplayDisplayHistoryContentParamCkSize | None = None,
        run_as: DatasetsContentsDisplayDisplayHistoryContentParamRunAs | None = None,
    ) -> None:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatasetsClient.datasets_contents_display_display_history_content() not implemented. Override this method in your test subclass."
        )

    async def datasets_contents_display_display_history_content_2(
        self,
        history_content_id: str,
        history_id: DatasetsContentsDisplayDisplayHistoryContentParamHistoryId2 | None,
        preview: bool | None = None,
        filename: DatasetsContentsDisplayDisplayHistoryContentParamFilename2 | None = None,
        to_ext: DatasetsContentsDisplayDisplayHistoryContentParamToExt2 | None = None,
        raw: bool | None = None,
        offset: DatasetsContentsDisplayDisplayHistoryContentParamOffset2 | None = None,
        ck_size: DatasetsContentsDisplayDisplayHistoryContentParamCkSize2 | None = None,
        run_as: DatasetsContentsDisplayDisplayHistoryContentParamRunAs2 | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatasetsClient.datasets_contents_display_display_history_content_2() not implemented. Override this method in your test subclass."
        )

    async def datasets_contents_extra_files_extra_files_history(
        self,
        history_id: str,
        history_content_id: str,
        run_as: DatasetsContentsExtraFilesExtraFilesHistoryParamRunAs | None = None,
    ) -> DatasetExtraFiles:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatasetsClient.datasets_contents_extra_files_extra_files_history() not implemented. Override this method in your test subclass."
        )

    async def history_contents_get_metadata_file(
        self,
        history_id: str,
        history_content_id: str,
        metadata_file: str,
        run_as: HistoryContentsGetMetadataFileParamRunAs | None = None,
    ) -> None:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockDatasetsClient.history_contents_get_metadata_file() not implemented. Override this method in your test subclass."
        )
