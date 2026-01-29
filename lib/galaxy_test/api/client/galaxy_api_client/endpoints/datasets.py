from typing import Any, Protocol, cast, runtime_checkable

from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import structure_from_dict
from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.anonymous_array_item_85 import AnonymousArrayItem85
from ..models.async_task_result_summary import AsyncTaskResultSummary
from ..models.compute_dataset_hash_payload import ComputeDatasetHashPayload
from ..models.converted_datasets_map import ConvertedDatasetsMap
from ..models.dataset_association_roles import DatasetAssociationRoles
from ..models.dataset_content_type import DatasetContentType
from ..models.dataset_extra_files import DatasetExtraFiles
from ..models.dataset_inheritance_chain import DatasetInheritanceChain
from ..models.dataset_source_type import DatasetSourceType
from ..models.dataset_storage_details import DatasetStorageDetails
from ..models.dataset_text_content_details import DatasetTextContentDetails
from ..models.datasets_content_get_structured_content_param_run_as import DatasetsContentGetStructuredContentParamRunAs
from ..models.datasets_contents_display_display_history_content_param_ck_size import (
    DatasetsContentsDisplayDisplayHistoryContentParamCkSize,
)
from ..models.datasets_contents_display_display_history_content_param_ck_size_2 import (
    DatasetsContentsDisplayDisplayHistoryContentParamCkSize2,
)
from ..models.datasets_contents_display_display_history_content_param_filename import (
    DatasetsContentsDisplayDisplayHistoryContentParamFilename,
)
from ..models.datasets_contents_display_display_history_content_param_filename_2 import (
    DatasetsContentsDisplayDisplayHistoryContentParamFilename2,
)
from ..models.datasets_contents_display_display_history_content_param_history_id import (
    DatasetsContentsDisplayDisplayHistoryContentParamHistoryId,
)
from ..models.datasets_contents_display_display_history_content_param_history_id_2 import (
    DatasetsContentsDisplayDisplayHistoryContentParamHistoryId2,
)
from ..models.datasets_contents_display_display_history_content_param_offset import (
    DatasetsContentsDisplayDisplayHistoryContentParamOffset,
)
from ..models.datasets_contents_display_display_history_content_param_offset_2 import (
    DatasetsContentsDisplayDisplayHistoryContentParamOffset2,
)
from ..models.datasets_contents_display_display_history_content_param_run_as import (
    DatasetsContentsDisplayDisplayHistoryContentParamRunAs,
)
from ..models.datasets_contents_display_display_history_content_param_run_as_2 import (
    DatasetsContentsDisplayDisplayHistoryContentParamRunAs2,
)
from ..models.datasets_contents_display_display_history_content_param_to_ext import (
    DatasetsContentsDisplayDisplayHistoryContentParamToExt,
)
from ..models.datasets_contents_display_display_history_content_param_to_ext_2 import (
    DatasetsContentsDisplayDisplayHistoryContentParamToExt2,
)
from ..models.datasets_contents_extra_files_extra_files_history_param_run_as import (
    DatasetsContentsExtraFilesExtraFilesHistoryParamRunAs,
)
from ..models.datasets_converted_converted_ext_200_response import DatasetsConvertedConvertedExt200Response
from ..models.datasets_converted_converted_ext_param_keys import DatasetsConvertedConvertedExtParamKeys
from ..models.datasets_converted_converted_ext_param_run_as import DatasetsConvertedConvertedExtParamRunAs
from ..models.datasets_converted_converted_ext_param_view import DatasetsConvertedConvertedExtParamView
from ..models.datasets_converted_converted_param_run_as import DatasetsConvertedConvertedParamRunAs
from ..models.datasets_delete_batch_param_run_as import DatasetsDeleteBatchParamRunAs
from ..models.datasets_display_display_param_ck_size import DatasetsDisplayDisplayParamCkSize
from ..models.datasets_display_display_param_ck_size_2 import DatasetsDisplayDisplayParamCkSize2
from ..models.datasets_display_display_param_filename import DatasetsDisplayDisplayParamFilename
from ..models.datasets_display_display_param_filename_2 import DatasetsDisplayDisplayParamFilename2
from ..models.datasets_display_display_param_offset import DatasetsDisplayDisplayParamOffset
from ..models.datasets_display_display_param_offset_2 import DatasetsDisplayDisplayParamOffset2
from ..models.datasets_display_display_param_run_as import DatasetsDisplayDisplayParamRunAs
from ..models.datasets_display_display_param_run_as_2 import DatasetsDisplayDisplayParamRunAs2
from ..models.datasets_display_display_param_to_ext import DatasetsDisplayDisplayParamToExt
from ..models.datasets_display_display_param_to_ext_2 import DatasetsDisplayDisplayParamToExt2
from ..models.datasets_extra_files_extra_files_param_run_as import DatasetsExtraFilesExtraFilesParamRunAs
from ..models.datasets_extra_files_raw_extra_file_raw_param_run_as import DatasetsExtraFilesRawExtraFileRawParamRunAs
from ..models.datasets_get_content_as_text_get_content_as_text_param_filename import (
    DatasetsGetContentAsTextGetContentAsTextParamFilename,
)
from ..models.datasets_get_content_as_text_get_content_as_text_param_run_as import (
    DatasetsGetContentAsTextGetContentAsTextParamRunAs,
)
from ..models.datasets_get_metadata_file_param_run_as import DatasetsGetMetadataFileParamRunAs
from ..models.datasets_hash_compute_hash_param_run_as import DatasetsHashComputeHashParamRunAs
from ..models.datasets_index_param_history_id import DatasetsIndexParamHistoryId
from ..models.datasets_index_param_keys import DatasetsIndexParamKeys
from ..models.datasets_index_param_limit import DatasetsIndexParamLimit
from ..models.datasets_index_param_offset import DatasetsIndexParamOffset
from ..models.datasets_index_param_order import DatasetsIndexParamOrder
from ..models.datasets_index_param_q import DatasetsIndexParamQ
from ..models.datasets_index_param_qv import DatasetsIndexParamQv
from ..models.datasets_index_param_run_as import DatasetsIndexParamRunAs
from ..models.datasets_index_param_view import DatasetsIndexParamView
from ..models.datasets_inheritance_chain_show_inheritance_chain_param_run_as import (
    DatasetsInheritanceChainShowInheritanceChainParamRunAs,
)
from ..models.datasets_metadata_file_get_metadata_file_datasets_param_run_as import (
    DatasetsMetadataFileGetMetadataFileDatasetsParamRunAs,
)
from ..models.datasets_permissions_update_permissions_param_run_as import DatasetsPermissionsUpdatePermissionsParamRunAs
from ..models.datasets_permissions_update_permissions_request_body import (
    DatasetsPermissionsUpdatePermissionsRequestBody,
)
from ..models.datasets_report_report_param_run_as import DatasetsReportReportParamRunAs
from ..models.datasets_show_param_data_type import DatasetsShowParamDataType
from ..models.datasets_show_param_keys import DatasetsShowParamKeys
from ..models.datasets_show_param_limit import DatasetsShowParamLimit
from ..models.datasets_show_param_offset import DatasetsShowParamOffset
from ..models.datasets_show_param_run_as import DatasetsShowParamRunAs
from ..models.datasets_show_param_view import DatasetsShowParamView
from ..models.datasets_storage_show_storage_param_run_as import DatasetsStorageShowStorageParamRunAs
from ..models.datasets_update_object_store_id_param_run_as import DatasetsUpdateObjectStoreIdParamRunAs
from ..models.delete_dataset_batch_payload import DeleteDatasetBatchPayload
from ..models.delete_dataset_batch_result import DeleteDatasetBatchResult
from ..models.history_contents_get_metadata_file_param_run_as import HistoryContentsGetMetadataFileParamRunAs
from ..models.tool_report_for_dataset import ToolReportForDataset
from ..models.update_object_store_id_payload import UpdateObjectStoreIdPayload


@runtime_checkable
class DatasetsClientProtocol(Protocol):
    """Protocol defining the interface of DatasetsClient for dependency injection."""

    async def datasets_delete_batch(
        self,
        body: DeleteDatasetBatchPayload,
        run_as: DatasetsDeleteBatchParamRunAs | None = None,
    ) -> DeleteDatasetBatchResult: ...

    async def datasets_delete_batch(
        self,
        body: DeleteDatasetBatchPayload,
        run_as: DatasetsDeleteBatchParamRunAs | None = None,
    ) -> DeleteDatasetBatchResult: ...

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
    ) -> list[AnonymousArrayItem85]: ...

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
    ) -> list[AnonymousArrayItem85]: ...

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
    ) -> dict[str, Any]: ...

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
    ) -> dict[str, Any]: ...

    async def datasets_content_get_structured_content(
        self,
        dataset_id: str,
        content_type: DatasetContentType,
        run_as: DatasetsContentGetStructuredContentParamRunAs | None = None,
    ) -> dict[str, Any]: ...

    async def datasets_content_get_structured_content(
        self,
        dataset_id: str,
        content_type: DatasetContentType,
        run_as: DatasetsContentGetStructuredContentParamRunAs | None = None,
    ) -> dict[str, Any]: ...

    async def datasets_converted_converted(
        self,
        dataset_id: str,
        run_as: DatasetsConvertedConvertedParamRunAs | None = None,
    ) -> ConvertedDatasetsMap: ...

    async def datasets_converted_converted(
        self,
        dataset_id: str,
        run_as: DatasetsConvertedConvertedParamRunAs | None = None,
    ) -> ConvertedDatasetsMap: ...

    async def datasets_converted_converted_ext(
        self,
        dataset_id: str,
        ext: str,
        view: DatasetsConvertedConvertedExtParamView | None = None,
        keys: DatasetsConvertedConvertedExtParamKeys | None = None,
        run_as: DatasetsConvertedConvertedExtParamRunAs | None = None,
    ) -> DatasetsConvertedConvertedExt200Response: ...

    async def datasets_converted_converted_ext(
        self,
        dataset_id: str,
        ext: str,
        view: DatasetsConvertedConvertedExtParamView | None = None,
        keys: DatasetsConvertedConvertedExtParamKeys | None = None,
        run_as: DatasetsConvertedConvertedExtParamRunAs | None = None,
    ) -> DatasetsConvertedConvertedExt200Response: ...

    async def datasets_extra_files_extra_files(
        self,
        dataset_id: str,
        run_as: DatasetsExtraFilesExtraFilesParamRunAs | None = None,
    ) -> DatasetExtraFiles: ...

    async def datasets_extra_files_extra_files(
        self,
        dataset_id: str,
        run_as: DatasetsExtraFilesExtraFilesParamRunAs | None = None,
    ) -> DatasetExtraFiles: ...

    async def datasets_extra_files_raw_extra_file_raw(
        self,
        dataset_id: str,
        filename: str,
        run_as: DatasetsExtraFilesRawExtraFileRawParamRunAs | None = None,
    ) -> dict[str, Any]: ...

    async def datasets_extra_files_raw_extra_file_raw(
        self,
        dataset_id: str,
        filename: str,
        run_as: DatasetsExtraFilesRawExtraFileRawParamRunAs | None = None,
    ) -> dict[str, Any]: ...

    async def datasets_get_content_as_text_get_content_as_text(
        self,
        dataset_id: str,
        filename: DatasetsGetContentAsTextGetContentAsTextParamFilename | None = None,
        run_as: DatasetsGetContentAsTextGetContentAsTextParamRunAs | None = None,
    ) -> DatasetTextContentDetails: ...

    async def datasets_get_content_as_text_get_content_as_text(
        self,
        dataset_id: str,
        filename: DatasetsGetContentAsTextGetContentAsTextParamFilename | None = None,
        run_as: DatasetsGetContentAsTextGetContentAsTextParamRunAs | None = None,
    ) -> DatasetTextContentDetails: ...

    async def datasets_hash_compute_hash(
        self,
        dataset_id: str,
        body: ComputeDatasetHashPayload,
        hda_ldda: DatasetSourceType | None = None,
        run_as: DatasetsHashComputeHashParamRunAs | None = None,
    ) -> AsyncTaskResultSummary: ...

    async def datasets_hash_compute_hash(
        self,
        dataset_id: str,
        body: ComputeDatasetHashPayload,
        hda_ldda: DatasetSourceType | None = None,
        run_as: DatasetsHashComputeHashParamRunAs | None = None,
    ) -> AsyncTaskResultSummary: ...

    async def datasets_inheritance_chain_show_inheritance_chain(
        self,
        dataset_id: str,
        hda_ldda: DatasetSourceType | None = None,
        run_as: DatasetsInheritanceChainShowInheritanceChainParamRunAs | None = None,
    ) -> DatasetInheritanceChain: ...

    async def datasets_inheritance_chain_show_inheritance_chain(
        self,
        dataset_id: str,
        hda_ldda: DatasetSourceType | None = None,
        run_as: DatasetsInheritanceChainShowInheritanceChainParamRunAs | None = None,
    ) -> DatasetInheritanceChain: ...

    async def datasets_update_object_store_id(
        self,
        dataset_id: str,
        body: UpdateObjectStoreIdPayload,
        run_as: DatasetsUpdateObjectStoreIdParamRunAs | None = None,
    ) -> dict[str, Any]: ...

    async def datasets_update_object_store_id(
        self,
        dataset_id: str,
        body: UpdateObjectStoreIdPayload,
        run_as: DatasetsUpdateObjectStoreIdParamRunAs | None = None,
    ) -> dict[str, Any]: ...

    async def datasets_permissions_update_permissions(
        self,
        dataset_id: str,
        body: DatasetsPermissionsUpdatePermissionsRequestBody,
        run_as: DatasetsPermissionsUpdatePermissionsParamRunAs | None = None,
    ) -> DatasetAssociationRoles: ...

    async def datasets_permissions_update_permissions(
        self,
        dataset_id: str,
        body: DatasetsPermissionsUpdatePermissionsRequestBody,
        run_as: DatasetsPermissionsUpdatePermissionsParamRunAs | None = None,
    ) -> DatasetAssociationRoles: ...

    async def datasets_report_report(
        self,
        dataset_id: str,
        run_as: DatasetsReportReportParamRunAs | None = None,
    ) -> ToolReportForDataset: ...

    async def datasets_report_report(
        self,
        dataset_id: str,
        run_as: DatasetsReportReportParamRunAs | None = None,
    ) -> ToolReportForDataset: ...

    async def datasets_storage_show_storage(
        self,
        dataset_id: str,
        hda_ldda: DatasetSourceType | None = None,
        run_as: DatasetsStorageShowStorageParamRunAs | None = None,
    ) -> DatasetStorageDetails: ...

    async def datasets_storage_show_storage(
        self,
        dataset_id: str,
        hda_ldda: DatasetSourceType | None = None,
        run_as: DatasetsStorageShowStorageParamRunAs | None = None,
    ) -> DatasetStorageDetails: ...

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
    ) -> None: ...

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
    ) -> None: ...

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
    ) -> dict[str, Any]: ...

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
    ) -> dict[str, Any]: ...

    async def datasets_get_metadata_file(
        self,
        history_content_id: str,
        metadata_file: str,
        run_as: DatasetsGetMetadataFileParamRunAs | None = None,
    ) -> None: ...

    async def datasets_get_metadata_file(
        self,
        history_content_id: str,
        metadata_file: str,
        run_as: DatasetsGetMetadataFileParamRunAs | None = None,
    ) -> None: ...

    async def datasets_metadata_file_get_metadata_file_datasets(
        self,
        history_content_id: str,
        metadata_file: str,
        run_as: DatasetsMetadataFileGetMetadataFileDatasetsParamRunAs | None = None,
    ) -> dict[str, Any]: ...

    async def datasets_metadata_file_get_metadata_file_datasets(
        self,
        history_content_id: str,
        metadata_file: str,
        run_as: DatasetsMetadataFileGetMetadataFileDatasetsParamRunAs | None = None,
    ) -> dict[str, Any]: ...

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
    ) -> None: ...

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
    ) -> None: ...

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
    ) -> dict[str, Any]: ...

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
    ) -> dict[str, Any]: ...

    async def datasets_contents_extra_files_extra_files_history(
        self,
        history_id: str,
        history_content_id: str,
        run_as: DatasetsContentsExtraFilesExtraFilesHistoryParamRunAs | None = None,
    ) -> DatasetExtraFiles: ...

    async def datasets_contents_extra_files_extra_files_history(
        self,
        history_id: str,
        history_content_id: str,
        run_as: DatasetsContentsExtraFilesExtraFilesHistoryParamRunAs | None = None,
    ) -> DatasetExtraFiles: ...

    async def history_contents_get_metadata_file(
        self,
        history_id: str,
        history_content_id: str,
        metadata_file: str,
        run_as: HistoryContentsGetMetadataFileParamRunAs | None = None,
    ) -> None: ...

    async def history_contents_get_metadata_file(
        self,
        history_id: str,
        history_content_id: str,
        metadata_file: str,
        run_as: HistoryContentsGetMetadataFileParamRunAs | None = None,
    ) -> None: ...


class DatasetsClient(DatasetsClientProtocol):
    """Client for datasets endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def datasets_delete_batch(
        self,
        body: DeleteDatasetBatchPayload,
        run_as: DatasetsDeleteBatchParamRunAs | None = None,
    ) -> DeleteDatasetBatchResult:
        """
        Deletes or purges a batch of datasets.

        Deletes or purges a batch of datasets. **Warning**: only the ownership of the datasets
        (and upload state for HDAs) is checked, no other checks or restrictions are made.

        Args:
            run-as (DatasetsDeleteBatchParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (DeleteDatasetBatchPayload)
                                     : Request body. (json)

        Returns:
            DeleteDatasetBatchResult: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: DeleteDatasetBatchPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("DELETE", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DeleteDatasetBatchResult)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datasets_delete_batch(
        self,
        body: DeleteDatasetBatchPayload,
        run_as: DatasetsDeleteBatchParamRunAs | None = None,
    ) -> DeleteDatasetBatchResult:
        """
        Deletes or purges a batch of datasets.

        Deletes or purges a batch of datasets. **Warning**: only the ownership of the datasets
        (and upload state for HDAs) is checked, no other checks or restrictions are made.

        Args:
            run-as (DatasetsDeleteBatchParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (DeleteDatasetBatchPayload)
                                     : Request body. (json)

        Returns:
            DeleteDatasetBatchResult: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: DeleteDatasetBatchPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("DELETE", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DeleteDatasetBatchResult)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

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
        Search datasets or collections using a query system.

        Args:
            history_id (DatasetsIndexParamHistoryId | None)
                                     : Optional identifier of a History. Use it to restrict the
                                       search within a particular History.
            view (DatasetsIndexParamView | None)
                                     : View to be passed to the serializer
            keys (DatasetsIndexParamKeys | None)
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            q (DatasetsIndexParamQ | None)
                                     : Generally a property name to filter by followed by an
                                       (often optional) hyphen and operator string.
            qv (DatasetsIndexParamQv | None)
                                     : The value to filter by.
            offset (DatasetsIndexParamOffset | None)
                                     : Starts at the beginning skip the first ( offset - 1 )
                                       items and begin returning at the Nth item
            limit (DatasetsIndexParamLimit | None)
                                     : The maximum number of items to return.
            order (DatasetsIndexParamOrder | None)
                                     : String containing one of the valid ordering attributes
                                       followed (optionally) by '-asc' or '-dsc' for ascending
                                       and descending order respectively. Orders can be stacked
                                       as a comma-separated list of values.
            run-as (DatasetsIndexParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem85]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets"

        params: dict[str, Any] = {
            **({"history_id": DataclassSerializer.serialize(history_id)} if history_id is not None else {}),
            **({"view": DataclassSerializer.serialize(view)} if view is not None else {}),
            **({"keys": DataclassSerializer.serialize(keys)} if keys is not None else {}),
            **({"q": DataclassSerializer.serialize(q)} if q is not None else {}),
            **({"qv": DataclassSerializer.serialize(qv)} if qv is not None else {}),
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
                return structure_from_dict(response.json(), list[AnonymousArrayItem85])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

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
        Search datasets or collections using a query system.

        Args:
            history_id (DatasetsIndexParamHistoryId | None)
                                     : Optional identifier of a History. Use it to restrict the
                                       search within a particular History.
            view (DatasetsIndexParamView | None)
                                     : View to be passed to the serializer
            keys (DatasetsIndexParamKeys | None)
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            q (DatasetsIndexParamQ | None)
                                     : Generally a property name to filter by followed by an
                                       (often optional) hyphen and operator string.
            qv (DatasetsIndexParamQv | None)
                                     : The value to filter by.
            offset (DatasetsIndexParamOffset | None)
                                     : Starts at the beginning skip the first ( offset - 1 )
                                       items and begin returning at the Nth item
            limit (DatasetsIndexParamLimit | None)
                                     : The maximum number of items to return.
            order (DatasetsIndexParamOrder | None)
                                     : String containing one of the valid ordering attributes
                                       followed (optionally) by '-asc' or '-dsc' for ascending
                                       and descending order respectively. Orders can be stacked
                                       as a comma-separated list of values.
            run-as (DatasetsIndexParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem85]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets"

        params: dict[str, Any] = {
            **({"history_id": DataclassSerializer.serialize(history_id)} if history_id is not None else {}),
            **({"view": DataclassSerializer.serialize(view)} if view is not None else {}),
            **({"keys": DataclassSerializer.serialize(keys)} if keys is not None else {}),
            **({"q": DataclassSerializer.serialize(q)} if q is not None else {}),
            **({"qv": DataclassSerializer.serialize(qv)} if qv is not None else {}),
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
                return structure_from_dict(response.json(), list[AnonymousArrayItem85])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

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
        Displays information about and/or content of a dataset.

        **Note**: Due to the multipurpose nature of this endpoint, which can receive a wide
        variety of parameters and return different kinds of responses, the documentation here
        will be limited. To get more information please check the source code.

        Args:
            dataset_id (str)         : The ID of the History Dataset.
            hda_ldda (DatasetSourceType | None)
                                     : The type of information about the dataset to be
                                       requested.
            data_type (DatasetsShowParamDataType | None)
                                     : The type of information about the dataset to be
                                       requested. Each of these values may require additional
                                       parameters in the request and may return different
                                       responses.
            limit (DatasetsShowParamLimit | None)
                                     : Maximum number of items to return. Currently only applies
                                       to `data_type=raw_data` requests
            offset (DatasetsShowParamOffset | None)
                                     : Starts at the beginning skip the first ( offset - 1 )
                                       items and begin returning at the Nth item. Currently only
                                       applies to `data_type=raw_data` requests
            view (DatasetsShowParamView | None)
                                     : View to be passed to the serializer
            keys (DatasetsShowParamKeys | None)
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (DatasetsShowParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        dataset_id = DataclassSerializer.serialize(dataset_id)

        url = f"{self.base_url}/api/datasets/{dataset_id}"

        params: dict[str, Any] = {
            **({"hda_ldda": DataclassSerializer.serialize(hda_ldda)} if hda_ldda is not None else {}),
            **({"data_type": DataclassSerializer.serialize(data_type)} if data_type is not None else {}),
            **({"limit": DataclassSerializer.serialize(limit)} if limit is not None else {}),
            **({"offset": DataclassSerializer.serialize(offset)} if offset is not None else {}),
            **({"view": DataclassSerializer.serialize(view)} if view is not None else {}),
            **({"keys": DataclassSerializer.serialize(keys)} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

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
        Displays information about and/or content of a dataset.

        **Note**: Due to the multipurpose nature of this endpoint, which can receive a wide
        variety of parameters and return different kinds of responses, the documentation here
        will be limited. To get more information please check the source code.

        Args:
            dataset_id (str)         : The ID of the History Dataset.
            hda_ldda (DatasetSourceType | None)
                                     : The type of information about the dataset to be
                                       requested.
            data_type (DatasetsShowParamDataType | None)
                                     : The type of information about the dataset to be
                                       requested. Each of these values may require additional
                                       parameters in the request and may return different
                                       responses.
            limit (DatasetsShowParamLimit | None)
                                     : Maximum number of items to return. Currently only applies
                                       to `data_type=raw_data` requests
            offset (DatasetsShowParamOffset | None)
                                     : Starts at the beginning skip the first ( offset - 1 )
                                       items and begin returning at the Nth item. Currently only
                                       applies to `data_type=raw_data` requests
            view (DatasetsShowParamView | None)
                                     : View to be passed to the serializer
            keys (DatasetsShowParamKeys | None)
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (DatasetsShowParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        dataset_id = DataclassSerializer.serialize(dataset_id)

        url = f"{self.base_url}/api/datasets/{dataset_id}"

        params: dict[str, Any] = {
            **({"hda_ldda": DataclassSerializer.serialize(hda_ldda)} if hda_ldda is not None else {}),
            **({"data_type": DataclassSerializer.serialize(data_type)} if data_type is not None else {}),
            **({"limit": DataclassSerializer.serialize(limit)} if limit is not None else {}),
            **({"offset": DataclassSerializer.serialize(offset)} if offset is not None else {}),
            **({"view": DataclassSerializer.serialize(view)} if view is not None else {}),
            **({"keys": DataclassSerializer.serialize(keys)} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datasets_content_get_structured_content(
        self,
        dataset_id: str,
        content_type: DatasetContentType,
        run_as: DatasetsContentGetStructuredContentParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Retrieve information about the content of a dataset.

        Args:
            dataset_id (str)         : The ID of the History Dataset.
            content_type (DatasetContentType)
                                     :
            run-as (DatasetsContentGetStructuredContentParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        dataset_id = DataclassSerializer.serialize(dataset_id)
        content_type = DataclassSerializer.serialize(content_type)

        url = f"{self.base_url}/api/datasets/{dataset_id}/content/{content_type}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datasets_content_get_structured_content(
        self,
        dataset_id: str,
        content_type: DatasetContentType,
        run_as: DatasetsContentGetStructuredContentParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Retrieve information about the content of a dataset.

        Args:
            dataset_id (str)         : The ID of the History Dataset.
            content_type (DatasetContentType)
                                     :
            run-as (DatasetsContentGetStructuredContentParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        dataset_id = DataclassSerializer.serialize(dataset_id)
        content_type = DataclassSerializer.serialize(content_type)

        url = f"{self.base_url}/api/datasets/{dataset_id}/content/{content_type}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datasets_converted_converted(
        self,
        dataset_id: str,
        run_as: DatasetsConvertedConvertedParamRunAs | None = None,
    ) -> ConvertedDatasetsMap:
        """
        Return a a map with all the existing converted datasets associated with this instance.

        Return a map of `<converted extension> : <converted id>` containing all the *existing*
        converted datasets.

        Args:
            dataset_id (str)         : The ID of the History Dataset.
            run-as (DatasetsConvertedConvertedParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ConvertedDatasetsMap: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        dataset_id = DataclassSerializer.serialize(dataset_id)

        url = f"{self.base_url}/api/datasets/{dataset_id}/converted"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), ConvertedDatasetsMap)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datasets_converted_converted(
        self,
        dataset_id: str,
        run_as: DatasetsConvertedConvertedParamRunAs | None = None,
    ) -> ConvertedDatasetsMap:
        """
        Return a a map with all the existing converted datasets associated with this instance.

        Return a map of `<converted extension> : <converted id>` containing all the *existing*
        converted datasets.

        Args:
            dataset_id (str)         : The ID of the History Dataset.
            run-as (DatasetsConvertedConvertedParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ConvertedDatasetsMap: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        dataset_id = DataclassSerializer.serialize(dataset_id)

        url = f"{self.base_url}/api/datasets/{dataset_id}/converted"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), ConvertedDatasetsMap)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datasets_converted_converted_ext(
        self,
        dataset_id: str,
        ext: str,
        view: DatasetsConvertedConvertedExtParamView | None = None,
        keys: DatasetsConvertedConvertedExtParamKeys | None = None,
        run_as: DatasetsConvertedConvertedExtParamRunAs | None = None,
    ) -> DatasetsConvertedConvertedExt200Response:
        """
        Return information about datasets made by converting this dataset to a new format.

        Return information about datasets made by converting this dataset to a new format.  If
        there is no existing converted dataset for the format in `ext`, one will be created.
        **Note**: `view` and `keys` are also available to control the serialization of the
        dataset.

        Args:
            dataset_id (str)         : The ID of the History Dataset.
            ext (str)                : File extension of the new format to convert this dataset
                                       to.
            view (DatasetsConvertedConvertedExtParamView | None)
                                     : View to be passed to the serializer
            keys (DatasetsConvertedConvertedExtParamKeys | None)
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (DatasetsConvertedConvertedExtParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DatasetsConvertedConvertedExt200Response: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        dataset_id = DataclassSerializer.serialize(dataset_id)
        ext = DataclassSerializer.serialize(ext)

        url = f"{self.base_url}/api/datasets/{dataset_id}/converted/{ext}"

        params: dict[str, Any] = {
            **({"view": DataclassSerializer.serialize(view)} if view is not None else {}),
            **({"keys": DataclassSerializer.serialize(keys)} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DatasetsConvertedConvertedExt200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datasets_converted_converted_ext(
        self,
        dataset_id: str,
        ext: str,
        view: DatasetsConvertedConvertedExtParamView | None = None,
        keys: DatasetsConvertedConvertedExtParamKeys | None = None,
        run_as: DatasetsConvertedConvertedExtParamRunAs | None = None,
    ) -> DatasetsConvertedConvertedExt200Response:
        """
        Return information about datasets made by converting this dataset to a new format.

        Return information about datasets made by converting this dataset to a new format.  If
        there is no existing converted dataset for the format in `ext`, one will be created.
        **Note**: `view` and `keys` are also available to control the serialization of the
        dataset.

        Args:
            dataset_id (str)         : The ID of the History Dataset.
            ext (str)                : File extension of the new format to convert this dataset
                                       to.
            view (DatasetsConvertedConvertedExtParamView | None)
                                     : View to be passed to the serializer
            keys (DatasetsConvertedConvertedExtParamKeys | None)
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (DatasetsConvertedConvertedExtParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DatasetsConvertedConvertedExt200Response: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        dataset_id = DataclassSerializer.serialize(dataset_id)
        ext = DataclassSerializer.serialize(ext)

        url = f"{self.base_url}/api/datasets/{dataset_id}/converted/{ext}"

        params: dict[str, Any] = {
            **({"view": DataclassSerializer.serialize(view)} if view is not None else {}),
            **({"keys": DataclassSerializer.serialize(keys)} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DatasetsConvertedConvertedExt200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datasets_extra_files_extra_files(
        self,
        dataset_id: str,
        run_as: DatasetsExtraFilesExtraFilesParamRunAs | None = None,
    ) -> DatasetExtraFiles:
        """
        Get the list of extra files/directories associated with a dataset.

        Args:
            dataset_id (str)         : The encoded database identifier of the dataset.
            run-as (DatasetsExtraFilesExtraFilesParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DatasetExtraFiles: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        dataset_id = DataclassSerializer.serialize(dataset_id)

        url = f"{self.base_url}/api/datasets/{dataset_id}/extra_files"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DatasetExtraFiles)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datasets_extra_files_extra_files(
        self,
        dataset_id: str,
        run_as: DatasetsExtraFilesExtraFilesParamRunAs | None = None,
    ) -> DatasetExtraFiles:
        """
        Get the list of extra files/directories associated with a dataset.

        Args:
            dataset_id (str)         : The encoded database identifier of the dataset.
            run-as (DatasetsExtraFilesExtraFilesParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DatasetExtraFiles: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        dataset_id = DataclassSerializer.serialize(dataset_id)

        url = f"{self.base_url}/api/datasets/{dataset_id}/extra_files"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DatasetExtraFiles)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datasets_extra_files_raw_extra_file_raw(
        self,
        dataset_id: str,
        filename: str,
        run_as: DatasetsExtraFilesRawExtraFileRawParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Downloads a raw extra file associated with a dataset.

        Args:
            dataset_id (str)         : The encoded database identifier of the dataset.
            filename (str)           : The name of the extra file to retrieve.
            run-as (DatasetsExtraFilesRawExtraFileRawParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        dataset_id = DataclassSerializer.serialize(dataset_id)
        filename = DataclassSerializer.serialize(filename)

        url = f"{self.base_url}/api/datasets/{dataset_id}/extra_files/raw/{filename}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datasets_extra_files_raw_extra_file_raw(
        self,
        dataset_id: str,
        filename: str,
        run_as: DatasetsExtraFilesRawExtraFileRawParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Downloads a raw extra file associated with a dataset.

        Args:
            dataset_id (str)         : The encoded database identifier of the dataset.
            filename (str)           : The name of the extra file to retrieve.
            run-as (DatasetsExtraFilesRawExtraFileRawParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        dataset_id = DataclassSerializer.serialize(dataset_id)
        filename = DataclassSerializer.serialize(filename)

        url = f"{self.base_url}/api/datasets/{dataset_id}/extra_files/raw/{filename}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datasets_get_content_as_text_get_content_as_text(
        self,
        dataset_id: str,
        filename: DatasetsGetContentAsTextGetContentAsTextParamFilename | None = None,
        run_as: DatasetsGetContentAsTextGetContentAsTextParamRunAs | None = None,
    ) -> DatasetTextContentDetails:
        """
        Returns dataset content as Text.

        Args:
            dataset_id (str)         : The ID of the History Dataset.
            filename (DatasetsGetContentAsTextGetContentAsTextParamFilename | None)
                                     : If non-null, get the specified filename from the extra
                                       files for this dataset.
            run-as (DatasetsGetContentAsTextGetContentAsTextParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DatasetTextContentDetails: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        dataset_id = DataclassSerializer.serialize(dataset_id)

        url = f"{self.base_url}/api/datasets/{dataset_id}/get_content_as_text"

        params: dict[str, Any] = {
            **({"filename": DataclassSerializer.serialize(filename)} if filename is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DatasetTextContentDetails)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datasets_get_content_as_text_get_content_as_text(
        self,
        dataset_id: str,
        filename: DatasetsGetContentAsTextGetContentAsTextParamFilename | None = None,
        run_as: DatasetsGetContentAsTextGetContentAsTextParamRunAs | None = None,
    ) -> DatasetTextContentDetails:
        """
        Returns dataset content as Text.

        Args:
            dataset_id (str)         : The ID of the History Dataset.
            filename (DatasetsGetContentAsTextGetContentAsTextParamFilename | None)
                                     : If non-null, get the specified filename from the extra
                                       files for this dataset.
            run-as (DatasetsGetContentAsTextGetContentAsTextParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DatasetTextContentDetails: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        dataset_id = DataclassSerializer.serialize(dataset_id)

        url = f"{self.base_url}/api/datasets/{dataset_id}/get_content_as_text"

        params: dict[str, Any] = {
            **({"filename": DataclassSerializer.serialize(filename)} if filename is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DatasetTextContentDetails)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datasets_hash_compute_hash(
        self,
        dataset_id: str,
        body: ComputeDatasetHashPayload,
        hda_ldda: DatasetSourceType | None = None,
        run_as: DatasetsHashComputeHashParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Compute dataset hash for dataset and update model

        Args:
            dataset_id (str)         : The ID of the History Dataset.
            hda_ldda (DatasetSourceType | None)
                                     : Whether this dataset belongs to a history (HDA) or a
                                       library (LDDA).
            run-as (DatasetsHashComputeHashParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (ComputeDatasetHashPayload)
                                     : Request body. (json)

        Returns:
            AsyncTaskResultSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        dataset_id = DataclassSerializer.serialize(dataset_id)

        url = f"{self.base_url}/api/datasets/{dataset_id}/hash"

        params: dict[str, Any] = {
            **({"hda_ldda": DataclassSerializer.serialize(hda_ldda)} if hda_ldda is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: ComputeDatasetHashPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), AsyncTaskResultSummary)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datasets_hash_compute_hash(
        self,
        dataset_id: str,
        body: ComputeDatasetHashPayload,
        hda_ldda: DatasetSourceType | None = None,
        run_as: DatasetsHashComputeHashParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Compute dataset hash for dataset and update model

        Args:
            dataset_id (str)         : The ID of the History Dataset.
            hda_ldda (DatasetSourceType | None)
                                     : Whether this dataset belongs to a history (HDA) or a
                                       library (LDDA).
            run-as (DatasetsHashComputeHashParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (ComputeDatasetHashPayload)
                                     : Request body. (json)

        Returns:
            AsyncTaskResultSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        dataset_id = DataclassSerializer.serialize(dataset_id)

        url = f"{self.base_url}/api/datasets/{dataset_id}/hash"

        params: dict[str, Any] = {
            **({"hda_ldda": DataclassSerializer.serialize(hda_ldda)} if hda_ldda is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: ComputeDatasetHashPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), AsyncTaskResultSummary)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datasets_inheritance_chain_show_inheritance_chain(
        self,
        dataset_id: str,
        hda_ldda: DatasetSourceType | None = None,
        run_as: DatasetsInheritanceChainShowInheritanceChainParamRunAs | None = None,
    ) -> DatasetInheritanceChain:
        """
        For internal use, this endpoint may change without warning.

        Args:
            dataset_id (str)         : The ID of the History Dataset.
            hda_ldda (DatasetSourceType | None)
                                     : Whether this dataset belongs to a history (HDA) or a
                                       library (LDDA).
            run-as (DatasetsInheritanceChainShowInheritanceChainParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DatasetInheritanceChain: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        dataset_id = DataclassSerializer.serialize(dataset_id)

        url = f"{self.base_url}/api/datasets/{dataset_id}/inheritance_chain"

        params: dict[str, Any] = {
            **({"hda_ldda": DataclassSerializer.serialize(hda_ldda)} if hda_ldda is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DatasetInheritanceChain)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datasets_inheritance_chain_show_inheritance_chain(
        self,
        dataset_id: str,
        hda_ldda: DatasetSourceType | None = None,
        run_as: DatasetsInheritanceChainShowInheritanceChainParamRunAs | None = None,
    ) -> DatasetInheritanceChain:
        """
        For internal use, this endpoint may change without warning.

        Args:
            dataset_id (str)         : The ID of the History Dataset.
            hda_ldda (DatasetSourceType | None)
                                     : Whether this dataset belongs to a history (HDA) or a
                                       library (LDDA).
            run-as (DatasetsInheritanceChainShowInheritanceChainParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DatasetInheritanceChain: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        dataset_id = DataclassSerializer.serialize(dataset_id)

        url = f"{self.base_url}/api/datasets/{dataset_id}/inheritance_chain"

        params: dict[str, Any] = {
            **({"hda_ldda": DataclassSerializer.serialize(hda_ldda)} if hda_ldda is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DatasetInheritanceChain)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datasets_update_object_store_id(
        self,
        dataset_id: str,
        body: UpdateObjectStoreIdPayload,
        run_as: DatasetsUpdateObjectStoreIdParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Update an object store ID for a dataset you own.

        Args:
            dataset_id (str)         : The ID of the History Dataset.
            run-as (DatasetsUpdateObjectStoreIdParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UpdateObjectStoreIdPayload)
                                     : Request body. (json)

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        dataset_id = DataclassSerializer.serialize(dataset_id)

        url = f"{self.base_url}/api/datasets/{dataset_id}/object_store_id"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: UpdateObjectStoreIdPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datasets_update_object_store_id(
        self,
        dataset_id: str,
        body: UpdateObjectStoreIdPayload,
        run_as: DatasetsUpdateObjectStoreIdParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Update an object store ID for a dataset you own.

        Args:
            dataset_id (str)         : The ID of the History Dataset.
            run-as (DatasetsUpdateObjectStoreIdParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UpdateObjectStoreIdPayload)
                                     : Request body. (json)

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        dataset_id = DataclassSerializer.serialize(dataset_id)

        url = f"{self.base_url}/api/datasets/{dataset_id}/object_store_id"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: UpdateObjectStoreIdPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datasets_permissions_update_permissions(
        self,
        dataset_id: str,
        body: DatasetsPermissionsUpdatePermissionsRequestBody,
        run_as: DatasetsPermissionsUpdatePermissionsParamRunAs | None = None,
    ) -> DatasetAssociationRoles:
        """
        Set permissions of the given history dataset to the given role ids.

        Set permissions of the given history dataset to the given role ids.

        Args:
            dataset_id (str)         : The ID of the History Dataset.
            run-as (DatasetsPermissionsUpdatePermissionsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (DatasetsPermissionsUpdatePermissionsRequestBody)
                                     : Request body. (json)

        Returns:
            DatasetAssociationRoles: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        dataset_id = DataclassSerializer.serialize(dataset_id)

        url = f"{self.base_url}/api/datasets/{dataset_id}/permissions"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: DatasetsPermissionsUpdatePermissionsRequestBody = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DatasetAssociationRoles)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datasets_permissions_update_permissions(
        self,
        dataset_id: str,
        body: DatasetsPermissionsUpdatePermissionsRequestBody,
        run_as: DatasetsPermissionsUpdatePermissionsParamRunAs | None = None,
    ) -> DatasetAssociationRoles:
        """
        Set permissions of the given history dataset to the given role ids.

        Set permissions of the given history dataset to the given role ids.

        Args:
            dataset_id (str)         : The ID of the History Dataset.
            run-as (DatasetsPermissionsUpdatePermissionsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (DatasetsPermissionsUpdatePermissionsRequestBody)
                                     : Request body. (json)

        Returns:
            DatasetAssociationRoles: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        dataset_id = DataclassSerializer.serialize(dataset_id)

        url = f"{self.base_url}/api/datasets/{dataset_id}/permissions"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: DatasetsPermissionsUpdatePermissionsRequestBody = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DatasetAssociationRoles)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datasets_report_report(
        self,
        dataset_id: str,
        run_as: DatasetsReportReportParamRunAs | None = None,
    ) -> ToolReportForDataset:
        """
        Return JSON content Galaxy will use to render Markdown reports

        Args:
            dataset_id (str)         : The ID of the History Dataset.
            run-as (DatasetsReportReportParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ToolReportForDataset: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        dataset_id = DataclassSerializer.serialize(dataset_id)

        url = f"{self.base_url}/api/datasets/{dataset_id}/report"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), ToolReportForDataset)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datasets_report_report(
        self,
        dataset_id: str,
        run_as: DatasetsReportReportParamRunAs | None = None,
    ) -> ToolReportForDataset:
        """
        Return JSON content Galaxy will use to render Markdown reports

        Args:
            dataset_id (str)         : The ID of the History Dataset.
            run-as (DatasetsReportReportParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ToolReportForDataset: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        dataset_id = DataclassSerializer.serialize(dataset_id)

        url = f"{self.base_url}/api/datasets/{dataset_id}/report"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), ToolReportForDataset)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datasets_storage_show_storage(
        self,
        dataset_id: str,
        hda_ldda: DatasetSourceType | None = None,
        run_as: DatasetsStorageShowStorageParamRunAs | None = None,
    ) -> DatasetStorageDetails:
        """
        Display user-facing storage details related to the objectstore a dataset resides in.

        Args:
            dataset_id (str)         : The ID of the History Dataset.
            hda_ldda (DatasetSourceType | None)
                                     : Whether this dataset belongs to a history (HDA) or a
                                       library (LDDA).
            run-as (DatasetsStorageShowStorageParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DatasetStorageDetails: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        dataset_id = DataclassSerializer.serialize(dataset_id)

        url = f"{self.base_url}/api/datasets/{dataset_id}/storage"

        params: dict[str, Any] = {
            **({"hda_ldda": DataclassSerializer.serialize(hda_ldda)} if hda_ldda is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DatasetStorageDetails)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datasets_storage_show_storage(
        self,
        dataset_id: str,
        hda_ldda: DatasetSourceType | None = None,
        run_as: DatasetsStorageShowStorageParamRunAs | None = None,
    ) -> DatasetStorageDetails:
        """
        Display user-facing storage details related to the objectstore a dataset resides in.

        Args:
            dataset_id (str)         : The ID of the History Dataset.
            hda_ldda (DatasetSourceType | None)
                                     : Whether this dataset belongs to a history (HDA) or a
                                       library (LDDA).
            run-as (DatasetsStorageShowStorageParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DatasetStorageDetails: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        dataset_id = DataclassSerializer.serialize(dataset_id)

        url = f"{self.base_url}/api/datasets/{dataset_id}/storage"

        params: dict[str, Any] = {
            **({"hda_ldda": DataclassSerializer.serialize(hda_ldda)} if hda_ldda is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DatasetStorageDetails)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

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
        Displays (preview) or downloads dataset content.

        Streams the dataset for download or the contents preview to be displayed in a browser.

        Args:
            history_content_id (str) : The ID of the History Dataset.
            preview (bool | None)    : Whether to get preview contents to be directly displayed
                                       on the web. If preview is False (default) the contents
                                       will be downloaded instead.
            filename (DatasetsDisplayDisplayParamFilename | None)
                                     : If non-null, get the specified filename from the extra
                                       files for this dataset.
            to_ext (DatasetsDisplayDisplayParamToExt | None)
                                     : The file extension when downloading the display data. Use
                                       the value `data` to let the server infer it from the data
                                       type.
            raw (bool | None)        : The query parameter 'raw' should be considered
                                       experimental and may be dropped at some point in the
                                       future without warning. Generally, data should be
                                       processed by its datatype prior to display.
            offset (DatasetsDisplayDisplayParamOffset | None)
                                     : Set this for datatypes that allow chunked display through
                                       the display_data method to enable chunking. This
                                       specifies a byte offset into the target dataset's
                                       display.
            ck_size (DatasetsDisplayDisplayParamCkSize | None)
                                     : If offset is set, this recommends 'how large' the next
                                       chunk should be. This is not respected or interpreted
                                       uniformly and should be interpreted as a very loose
                                       recommendation. Different datatypes interpret 'largeness'
                                       differently - for bam datasets this is a number of lines
                                       whereas for tabular datatypes this is interpreted as a
                                       number of bytes.
            run-as (DatasetsDisplayDisplayParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        history_content_id = DataclassSerializer.serialize(history_content_id)

        url = f"{self.base_url}/api/datasets/{history_content_id}/display"

        params: dict[str, Any] = {
            **({"preview": DataclassSerializer.serialize(preview)} if preview is not None else {}),
            **({"filename": DataclassSerializer.serialize(filename)} if filename is not None else {}),
            **({"to_ext": DataclassSerializer.serialize(to_ext)} if to_ext is not None else {}),
            **({"raw": DataclassSerializer.serialize(raw)} if raw is not None else {}),
            **({"offset": DataclassSerializer.serialize(offset)} if offset is not None else {}),
            **({"ck_size": DataclassSerializer.serialize(ck_size)} if ck_size is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

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
        Displays (preview) or downloads dataset content.

        Streams the dataset for download or the contents preview to be displayed in a browser.

        Args:
            history_content_id (str) : The ID of the History Dataset.
            preview (bool | None)    : Whether to get preview contents to be directly displayed
                                       on the web. If preview is False (default) the contents
                                       will be downloaded instead.
            filename (DatasetsDisplayDisplayParamFilename | None)
                                     : If non-null, get the specified filename from the extra
                                       files for this dataset.
            to_ext (DatasetsDisplayDisplayParamToExt | None)
                                     : The file extension when downloading the display data. Use
                                       the value `data` to let the server infer it from the data
                                       type.
            raw (bool | None)        : The query parameter 'raw' should be considered
                                       experimental and may be dropped at some point in the
                                       future without warning. Generally, data should be
                                       processed by its datatype prior to display.
            offset (DatasetsDisplayDisplayParamOffset | None)
                                     : Set this for datatypes that allow chunked display through
                                       the display_data method to enable chunking. This
                                       specifies a byte offset into the target dataset's
                                       display.
            ck_size (DatasetsDisplayDisplayParamCkSize | None)
                                     : If offset is set, this recommends 'how large' the next
                                       chunk should be. This is not respected or interpreted
                                       uniformly and should be interpreted as a very loose
                                       recommendation. Different datatypes interpret 'largeness'
                                       differently - for bam datasets this is a number of lines
                                       whereas for tabular datatypes this is interpreted as a
                                       number of bytes.
            run-as (DatasetsDisplayDisplayParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        history_content_id = DataclassSerializer.serialize(history_content_id)

        url = f"{self.base_url}/api/datasets/{history_content_id}/display"

        params: dict[str, Any] = {
            **({"preview": DataclassSerializer.serialize(preview)} if preview is not None else {}),
            **({"filename": DataclassSerializer.serialize(filename)} if filename is not None else {}),
            **({"to_ext": DataclassSerializer.serialize(to_ext)} if to_ext is not None else {}),
            **({"raw": DataclassSerializer.serialize(raw)} if raw is not None else {}),
            **({"offset": DataclassSerializer.serialize(offset)} if offset is not None else {}),
            **({"ck_size": DataclassSerializer.serialize(ck_size)} if ck_size is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

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
        Check if dataset content can be previewed or downloaded.

        Streams the dataset for download or the contents preview to be displayed in a browser.

        Args:
            history_content_id (str) : The ID of the History Dataset.
            preview (bool | None)    : Whether to get preview contents to be directly displayed
                                       on the web. If preview is False (default) the contents
                                       will be downloaded instead.
            filename (DatasetsDisplayDisplayParamFilename2 | None)
                                     : If non-null, get the specified filename from the extra
                                       files for this dataset.
            to_ext (DatasetsDisplayDisplayParamToExt2 | None)
                                     : The file extension when downloading the display data. Use
                                       the value `data` to let the server infer it from the data
                                       type.
            raw (bool | None)        : The query parameter 'raw' should be considered
                                       experimental and may be dropped at some point in the
                                       future without warning. Generally, data should be
                                       processed by its datatype prior to display.
            offset (DatasetsDisplayDisplayParamOffset2 | None)
                                     : Set this for datatypes that allow chunked display through
                                       the display_data method to enable chunking. This
                                       specifies a byte offset into the target dataset's
                                       display.
            ck_size (DatasetsDisplayDisplayParamCkSize2 | None)
                                     : If offset is set, this recommends 'how large' the next
                                       chunk should be. This is not respected or interpreted
                                       uniformly and should be interpreted as a very loose
                                       recommendation. Different datatypes interpret 'largeness'
                                       differently - for bam datasets this is a number of lines
                                       whereas for tabular datatypes this is interpreted as a
                                       number of bytes.
            run-as (DatasetsDisplayDisplayParamRunAs2 | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        history_content_id = DataclassSerializer.serialize(history_content_id)

        url = f"{self.base_url}/api/datasets/{history_content_id}/display"

        params: dict[str, Any] = {
            **({"preview": DataclassSerializer.serialize(preview)} if preview is not None else {}),
            **({"filename": DataclassSerializer.serialize(filename)} if filename is not None else {}),
            **({"to_ext": DataclassSerializer.serialize(to_ext)} if to_ext is not None else {}),
            **({"raw": DataclassSerializer.serialize(raw)} if raw is not None else {}),
            **({"offset": DataclassSerializer.serialize(offset)} if offset is not None else {}),
            **({"ck_size": DataclassSerializer.serialize(ck_size)} if ck_size is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("HEAD", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

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
        Check if dataset content can be previewed or downloaded.

        Streams the dataset for download or the contents preview to be displayed in a browser.

        Args:
            history_content_id (str) : The ID of the History Dataset.
            preview (bool | None)    : Whether to get preview contents to be directly displayed
                                       on the web. If preview is False (default) the contents
                                       will be downloaded instead.
            filename (DatasetsDisplayDisplayParamFilename2 | None)
                                     : If non-null, get the specified filename from the extra
                                       files for this dataset.
            to_ext (DatasetsDisplayDisplayParamToExt2 | None)
                                     : The file extension when downloading the display data. Use
                                       the value `data` to let the server infer it from the data
                                       type.
            raw (bool | None)        : The query parameter 'raw' should be considered
                                       experimental and may be dropped at some point in the
                                       future without warning. Generally, data should be
                                       processed by its datatype prior to display.
            offset (DatasetsDisplayDisplayParamOffset2 | None)
                                     : Set this for datatypes that allow chunked display through
                                       the display_data method to enable chunking. This
                                       specifies a byte offset into the target dataset's
                                       display.
            ck_size (DatasetsDisplayDisplayParamCkSize2 | None)
                                     : If offset is set, this recommends 'how large' the next
                                       chunk should be. This is not respected or interpreted
                                       uniformly and should be interpreted as a very loose
                                       recommendation. Different datatypes interpret 'largeness'
                                       differently - for bam datasets this is a number of lines
                                       whereas for tabular datatypes this is interpreted as a
                                       number of bytes.
            run-as (DatasetsDisplayDisplayParamRunAs2 | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        history_content_id = DataclassSerializer.serialize(history_content_id)

        url = f"{self.base_url}/api/datasets/{history_content_id}/display"

        params: dict[str, Any] = {
            **({"preview": DataclassSerializer.serialize(preview)} if preview is not None else {}),
            **({"filename": DataclassSerializer.serialize(filename)} if filename is not None else {}),
            **({"to_ext": DataclassSerializer.serialize(to_ext)} if to_ext is not None else {}),
            **({"raw": DataclassSerializer.serialize(raw)} if raw is not None else {}),
            **({"offset": DataclassSerializer.serialize(offset)} if offset is not None else {}),
            **({"ck_size": DataclassSerializer.serialize(ck_size)} if ck_size is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("HEAD", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datasets_get_metadata_file(
        self,
        history_content_id: str,
        metadata_file: str,
        run_as: DatasetsGetMetadataFileParamRunAs | None = None,
    ) -> None:
        """
        Returns the metadata file associated with this history item.

        Args:
            history_content_id (str) : The ID of the History Dataset.
            metadata_file (str)      : The name of the metadata file to retrieve.
            run-as (DatasetsGetMetadataFileParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        history_content_id = DataclassSerializer.serialize(history_content_id)

        url = f"{self.base_url}/api/datasets/{history_content_id}/metadata_file"

        params: dict[str, Any] = {
            "metadata_file": DataclassSerializer.serialize(metadata_file),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datasets_get_metadata_file(
        self,
        history_content_id: str,
        metadata_file: str,
        run_as: DatasetsGetMetadataFileParamRunAs | None = None,
    ) -> None:
        """
        Returns the metadata file associated with this history item.

        Args:
            history_content_id (str) : The ID of the History Dataset.
            metadata_file (str)      : The name of the metadata file to retrieve.
            run-as (DatasetsGetMetadataFileParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        history_content_id = DataclassSerializer.serialize(history_content_id)

        url = f"{self.base_url}/api/datasets/{history_content_id}/metadata_file"

        params: dict[str, Any] = {
            "metadata_file": DataclassSerializer.serialize(metadata_file),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datasets_metadata_file_get_metadata_file_datasets(
        self,
        history_content_id: str,
        metadata_file: str,
        run_as: DatasetsMetadataFileGetMetadataFileDatasetsParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Check if metadata file can be downloaded.

        Args:
            history_content_id (str) : The ID of the History Dataset.
            metadata_file (str)      : The name of the metadata file to retrieve.
            run-as (DatasetsMetadataFileGetMetadataFileDatasetsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        history_content_id = DataclassSerializer.serialize(history_content_id)

        url = f"{self.base_url}/api/datasets/{history_content_id}/metadata_file"

        params: dict[str, Any] = {
            "metadata_file": DataclassSerializer.serialize(metadata_file),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("HEAD", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datasets_metadata_file_get_metadata_file_datasets(
        self,
        history_content_id: str,
        metadata_file: str,
        run_as: DatasetsMetadataFileGetMetadataFileDatasetsParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Check if metadata file can be downloaded.

        Args:
            history_content_id (str) : The ID of the History Dataset.
            metadata_file (str)      : The name of the metadata file to retrieve.
            run-as (DatasetsMetadataFileGetMetadataFileDatasetsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        history_content_id = DataclassSerializer.serialize(history_content_id)

        url = f"{self.base_url}/api/datasets/{history_content_id}/metadata_file"

        params: dict[str, Any] = {
            "metadata_file": DataclassSerializer.serialize(metadata_file),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("HEAD", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

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
        Displays (preview) or downloads dataset content.

        Streams the dataset for download or the contents preview to be displayed in a browser.

        Args:
            history_content_id (str) : The ID of the History Dataset.
            history_id (DatasetsContentsDisplayDisplayHistoryContentParamHistoryId | None)
                                     :
            preview (bool | None)    : Whether to get preview contents to be directly displayed
                                       on the web. If preview is False (default) the contents
                                       will be downloaded instead.
            filename (DatasetsContentsDisplayDisplayHistoryContentParamFilename | None)
                                     : If non-null, get the specified filename from the extra
                                       files for this dataset.
            to_ext (DatasetsContentsDisplayDisplayHistoryContentParamToExt | None)
                                     : The file extension when downloading the display data. Use
                                       the value `data` to let the server infer it from the data
                                       type.
            raw (bool | None)        : The query parameter 'raw' should be considered
                                       experimental and may be dropped at some point in the
                                       future without warning. Generally, data should be
                                       processed by its datatype prior to display.
            offset (DatasetsContentsDisplayDisplayHistoryContentParamOffset | None)
                                     : Set this for datatypes that allow chunked display through
                                       the display_data method to enable chunking. This
                                       specifies a byte offset into the target dataset's
                                       display.
            ck_size (DatasetsContentsDisplayDisplayHistoryContentParamCkSize | None)
                                     : If offset is set, this recommends 'how large' the next
                                       chunk should be. This is not respected or interpreted
                                       uniformly and should be interpreted as a very loose
                                       recommendation. Different datatypes interpret 'largeness'
                                       differently - for bam datasets this is a number of lines
                                       whereas for tabular datatypes this is interpreted as a
                                       number of bytes.
            run-as (DatasetsContentsDisplayDisplayHistoryContentParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        history_content_id = DataclassSerializer.serialize(history_content_id)
        history_id = DataclassSerializer.serialize(history_id)

        url = f"{self.base_url}/api/histories/{history_id}/contents/{history_content_id}/display"

        params: dict[str, Any] = {
            **({"preview": DataclassSerializer.serialize(preview)} if preview is not None else {}),
            **({"filename": DataclassSerializer.serialize(filename)} if filename is not None else {}),
            **({"to_ext": DataclassSerializer.serialize(to_ext)} if to_ext is not None else {}),
            **({"raw": DataclassSerializer.serialize(raw)} if raw is not None else {}),
            **({"offset": DataclassSerializer.serialize(offset)} if offset is not None else {}),
            **({"ck_size": DataclassSerializer.serialize(ck_size)} if ck_size is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

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
        Displays (preview) or downloads dataset content.

        Streams the dataset for download or the contents preview to be displayed in a browser.

        Args:
            history_content_id (str) : The ID of the History Dataset.
            history_id (DatasetsContentsDisplayDisplayHistoryContentParamHistoryId | None)
                                     :
            preview (bool | None)    : Whether to get preview contents to be directly displayed
                                       on the web. If preview is False (default) the contents
                                       will be downloaded instead.
            filename (DatasetsContentsDisplayDisplayHistoryContentParamFilename | None)
                                     : If non-null, get the specified filename from the extra
                                       files for this dataset.
            to_ext (DatasetsContentsDisplayDisplayHistoryContentParamToExt | None)
                                     : The file extension when downloading the display data. Use
                                       the value `data` to let the server infer it from the data
                                       type.
            raw (bool | None)        : The query parameter 'raw' should be considered
                                       experimental and may be dropped at some point in the
                                       future without warning. Generally, data should be
                                       processed by its datatype prior to display.
            offset (DatasetsContentsDisplayDisplayHistoryContentParamOffset | None)
                                     : Set this for datatypes that allow chunked display through
                                       the display_data method to enable chunking. This
                                       specifies a byte offset into the target dataset's
                                       display.
            ck_size (DatasetsContentsDisplayDisplayHistoryContentParamCkSize | None)
                                     : If offset is set, this recommends 'how large' the next
                                       chunk should be. This is not respected or interpreted
                                       uniformly and should be interpreted as a very loose
                                       recommendation. Different datatypes interpret 'largeness'
                                       differently - for bam datasets this is a number of lines
                                       whereas for tabular datatypes this is interpreted as a
                                       number of bytes.
            run-as (DatasetsContentsDisplayDisplayHistoryContentParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        history_content_id = DataclassSerializer.serialize(history_content_id)
        history_id = DataclassSerializer.serialize(history_id)

        url = f"{self.base_url}/api/histories/{history_id}/contents/{history_content_id}/display"

        params: dict[str, Any] = {
            **({"preview": DataclassSerializer.serialize(preview)} if preview is not None else {}),
            **({"filename": DataclassSerializer.serialize(filename)} if filename is not None else {}),
            **({"to_ext": DataclassSerializer.serialize(to_ext)} if to_ext is not None else {}),
            **({"raw": DataclassSerializer.serialize(raw)} if raw is not None else {}),
            **({"offset": DataclassSerializer.serialize(offset)} if offset is not None else {}),
            **({"ck_size": DataclassSerializer.serialize(ck_size)} if ck_size is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

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
        Check if dataset content can be previewed or downloaded.

        Streams the dataset for download or the contents preview to be displayed in a browser.

        Args:
            history_content_id (str) : The ID of the History Dataset.
            history_id (DatasetsContentsDisplayDisplayHistoryContentParamHistoryId2 | None)
                                     :
            preview (bool | None)    : Whether to get preview contents to be directly displayed
                                       on the web. If preview is False (default) the contents
                                       will be downloaded instead.
            filename (DatasetsContentsDisplayDisplayHistoryContentParamFilename2 | None)
                                     : If non-null, get the specified filename from the extra
                                       files for this dataset.
            to_ext (DatasetsContentsDisplayDisplayHistoryContentParamToExt2 | None)
                                     : The file extension when downloading the display data. Use
                                       the value `data` to let the server infer it from the data
                                       type.
            raw (bool | None)        : The query parameter 'raw' should be considered
                                       experimental and may be dropped at some point in the
                                       future without warning. Generally, data should be
                                       processed by its datatype prior to display.
            offset (DatasetsContentsDisplayDisplayHistoryContentParamOffset2 | None)
                                     : Set this for datatypes that allow chunked display through
                                       the display_data method to enable chunking. This
                                       specifies a byte offset into the target dataset's
                                       display.
            ck_size (DatasetsContentsDisplayDisplayHistoryContentParamCkSize2 | None)
                                     : If offset is set, this recommends 'how large' the next
                                       chunk should be. This is not respected or interpreted
                                       uniformly and should be interpreted as a very loose
                                       recommendation. Different datatypes interpret 'largeness'
                                       differently - for bam datasets this is a number of lines
                                       whereas for tabular datatypes this is interpreted as a
                                       number of bytes.
            run-as (DatasetsContentsDisplayDisplayHistoryContentParamRunAs2 | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        history_content_id = DataclassSerializer.serialize(history_content_id)
        history_id = DataclassSerializer.serialize(history_id)

        url = f"{self.base_url}/api/histories/{history_id}/contents/{history_content_id}/display"

        params: dict[str, Any] = {
            **({"preview": DataclassSerializer.serialize(preview)} if preview is not None else {}),
            **({"filename": DataclassSerializer.serialize(filename)} if filename is not None else {}),
            **({"to_ext": DataclassSerializer.serialize(to_ext)} if to_ext is not None else {}),
            **({"raw": DataclassSerializer.serialize(raw)} if raw is not None else {}),
            **({"offset": DataclassSerializer.serialize(offset)} if offset is not None else {}),
            **({"ck_size": DataclassSerializer.serialize(ck_size)} if ck_size is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("HEAD", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

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
        Check if dataset content can be previewed or downloaded.

        Streams the dataset for download or the contents preview to be displayed in a browser.

        Args:
            history_content_id (str) : The ID of the History Dataset.
            history_id (DatasetsContentsDisplayDisplayHistoryContentParamHistoryId2 | None)
                                     :
            preview (bool | None)    : Whether to get preview contents to be directly displayed
                                       on the web. If preview is False (default) the contents
                                       will be downloaded instead.
            filename (DatasetsContentsDisplayDisplayHistoryContentParamFilename2 | None)
                                     : If non-null, get the specified filename from the extra
                                       files for this dataset.
            to_ext (DatasetsContentsDisplayDisplayHistoryContentParamToExt2 | None)
                                     : The file extension when downloading the display data. Use
                                       the value `data` to let the server infer it from the data
                                       type.
            raw (bool | None)        : The query parameter 'raw' should be considered
                                       experimental and may be dropped at some point in the
                                       future without warning. Generally, data should be
                                       processed by its datatype prior to display.
            offset (DatasetsContentsDisplayDisplayHistoryContentParamOffset2 | None)
                                     : Set this for datatypes that allow chunked display through
                                       the display_data method to enable chunking. This
                                       specifies a byte offset into the target dataset's
                                       display.
            ck_size (DatasetsContentsDisplayDisplayHistoryContentParamCkSize2 | None)
                                     : If offset is set, this recommends 'how large' the next
                                       chunk should be. This is not respected or interpreted
                                       uniformly and should be interpreted as a very loose
                                       recommendation. Different datatypes interpret 'largeness'
                                       differently - for bam datasets this is a number of lines
                                       whereas for tabular datatypes this is interpreted as a
                                       number of bytes.
            run-as (DatasetsContentsDisplayDisplayHistoryContentParamRunAs2 | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            dict[str, Any]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        history_content_id = DataclassSerializer.serialize(history_content_id)
        history_id = DataclassSerializer.serialize(history_id)

        url = f"{self.base_url}/api/histories/{history_id}/contents/{history_content_id}/display"

        params: dict[str, Any] = {
            **({"preview": DataclassSerializer.serialize(preview)} if preview is not None else {}),
            **({"filename": DataclassSerializer.serialize(filename)} if filename is not None else {}),
            **({"to_ext": DataclassSerializer.serialize(to_ext)} if to_ext is not None else {}),
            **({"raw": DataclassSerializer.serialize(raw)} if raw is not None else {}),
            **({"offset": DataclassSerializer.serialize(offset)} if offset is not None else {}),
            **({"ck_size": DataclassSerializer.serialize(ck_size)} if ck_size is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("HEAD", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(dict[str, Any], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datasets_contents_extra_files_extra_files_history(
        self,
        history_id: str,
        history_content_id: str,
        run_as: DatasetsContentsExtraFilesExtraFilesHistoryParamRunAs | None = None,
    ) -> DatasetExtraFiles:
        """
        Get the list of extra files/directories associated with a dataset.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            history_content_id (str) : The ID of the History Dataset.
            run-as (DatasetsContentsExtraFilesExtraFilesHistoryParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DatasetExtraFiles: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        history_id = DataclassSerializer.serialize(history_id)
        history_content_id = DataclassSerializer.serialize(history_content_id)

        url = f"{self.base_url}/api/histories/{history_id}/contents/{history_content_id}/extra_files"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DatasetExtraFiles)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def datasets_contents_extra_files_extra_files_history(
        self,
        history_id: str,
        history_content_id: str,
        run_as: DatasetsContentsExtraFilesExtraFilesHistoryParamRunAs | None = None,
    ) -> DatasetExtraFiles:
        """
        Get the list of extra files/directories associated with a dataset.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            history_content_id (str) : The ID of the History Dataset.
            run-as (DatasetsContentsExtraFilesExtraFilesHistoryParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DatasetExtraFiles: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        history_id = DataclassSerializer.serialize(history_id)
        history_content_id = DataclassSerializer.serialize(history_content_id)

        url = f"{self.base_url}/api/histories/{history_id}/contents/{history_content_id}/extra_files"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), DatasetExtraFiles)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def history_contents_get_metadata_file(
        self,
        history_id: str,
        history_content_id: str,
        metadata_file: str,
        run_as: HistoryContentsGetMetadataFileParamRunAs | None = None,
    ) -> None:
        """
        Returns the metadata file associated with this history item.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            history_content_id (str) : The ID of the History Dataset.
            metadata_file (str)      : The name of the metadata file to retrieve.
            run-as (HistoryContentsGetMetadataFileParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        history_id = DataclassSerializer.serialize(history_id)
        history_content_id = DataclassSerializer.serialize(history_content_id)

        url = f"{self.base_url}/api/histories/{history_id}/contents/{history_content_id}/metadata_file"

        params: dict[str, Any] = {
            "metadata_file": DataclassSerializer.serialize(metadata_file),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def history_contents_get_metadata_file(
        self,
        history_id: str,
        history_content_id: str,
        metadata_file: str,
        run_as: HistoryContentsGetMetadataFileParamRunAs | None = None,
    ) -> None:
        """
        Returns the metadata file associated with this history item.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            history_content_id (str) : The ID of the History Dataset.
            metadata_file (str)      : The name of the metadata file to retrieve.
            run-as (HistoryContentsGetMetadataFileParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        history_id = DataclassSerializer.serialize(history_id)
        history_content_id = DataclassSerializer.serialize(history_content_id)

        url = f"{self.base_url}/api/histories/{history_id}/contents/{history_content_id}/metadata_file"

        params: dict[str, Any] = {
            "metadata_file": DataclassSerializer.serialize(metadata_file),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover
