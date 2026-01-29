from typing import Any, cast

from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.anonymous_array_item_125 import AnonymousArrayItem125
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
from ..models.datasets_contents_display_display_history_content_param_filename import (
    DatasetsContentsDisplayDisplayHistoryContentParamFilename,
)
from ..models.datasets_contents_display_display_history_content_param_history_id import (
    DatasetsContentsDisplayDisplayHistoryContentParamHistoryId,
)
from ..models.datasets_contents_display_display_history_content_param_offset import (
    DatasetsContentsDisplayDisplayHistoryContentParamOffset,
)
from ..models.datasets_contents_display_display_history_content_param_run_as import (
    DatasetsContentsDisplayDisplayHistoryContentParamRunAs,
)
from ..models.datasets_contents_display_display_history_content_param_to_ext import (
    DatasetsContentsDisplayDisplayHistoryContentParamToExt,
)
from ..models.datasets_contents_extra_files_extra_files_history_param_run_as import (
    DatasetsContentsExtraFilesExtraFilesHistoryParamRunAs,
)
from ..models.datasets_converted_converted_ext_200_response_2 import DatasetsConvertedConvertedExt200Response2
from ..models.datasets_converted_converted_ext_param_keys import DatasetsConvertedConvertedExtParamKeys
from ..models.datasets_converted_converted_ext_param_run_as import DatasetsConvertedConvertedExtParamRunAs
from ..models.datasets_converted_converted_ext_param_view import DatasetsConvertedConvertedExtParamView
from ..models.datasets_converted_converted_param_run_as import DatasetsConvertedConvertedParamRunAs
from ..models.datasets_delete_batch_param_run_as import DatasetsDeleteBatchParamRunAs
from ..models.datasets_display_display_param_ck_size import DatasetsDisplayDisplayParamCkSize
from ..models.datasets_display_display_param_filename import DatasetsDisplayDisplayParamFilename
from ..models.datasets_display_display_param_offset import DatasetsDisplayDisplayParamOffset
from ..models.datasets_display_display_param_run_as import DatasetsDisplayDisplayParamRunAs
from ..models.datasets_display_display_param_to_ext import DatasetsDisplayDisplayParamToExt
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
from ..models.datasets_permissions_update_permissions_request_body_2 import (
    DatasetsPermissionsUpdatePermissionsRequestBody2,
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


class DatasetsClient:
    """Client for datasets endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def datasets_delete_batch_2_2(
        self,
        body: DeleteDatasetBatchPayload,
        run_as: DatasetsDeleteBatchParamRunAs | None = None,
    ) -> DeleteDatasetBatchResult:
        """
        Deletes or purges a batch of datasets.

        Deletes or purges a batch of datasets. **Warning**: only the ownership of the datasets
        (and upload state for HDAs) is checked, no other checks or restrictions are made.

        Args:
            run-as (Optional[DatasetsDeleteBatchParamRunAs])
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
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: DeleteDatasetBatchPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("DELETE", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DeleteDatasetBatchResult, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_delete_batch_2_2(
        self,
        body: DeleteDatasetBatchPayload,
        run_as: DatasetsDeleteBatchParamRunAs | None = None,
    ) -> DeleteDatasetBatchResult:
        """
        Deletes or purges a batch of datasets.

        Deletes or purges a batch of datasets. **Warning**: only the ownership of the datasets
        (and upload state for HDAs) is checked, no other checks or restrictions are made.

        Args:
            run-as (Optional[DatasetsDeleteBatchParamRunAs])
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
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: DeleteDatasetBatchPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("DELETE", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DeleteDatasetBatchResult, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_index_2_2(
        self,
        history_id: DatasetsIndexParamHistoryId | None = None,
        view: DatasetsIndexParamView | None = None,
        keys: DatasetsIndexParamKeys | None = None,
        q: DatasetsIndexParamQ | None = None,
        qv: DatasetsIndexParamQv | None = None,
        offset: DatasetsIndexParamOffset | None = 0,
        limit: DatasetsIndexParamLimit | None = None,
        order: DatasetsIndexParamOrder | None = None,
        run_as: DatasetsIndexParamRunAs | None = None,
    ) -> list[AnonymousArrayItem125]:
        """
        Search datasets or collections using a query system.

        Args:
            history_id (Optional[DatasetsIndexParamHistoryId])
                                     : Optional identifier of a History. Use it to restrict the
                                       search within a particular History.
            view (Optional[DatasetsIndexParamView])
                                     : View to be passed to the serializer
            keys (Optional[DatasetsIndexParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            q (Optional[DatasetsIndexParamQ])
                                     : Generally a property name to filter by followed by an
                                       (often optional) hyphen and operator string.
            qv (Optional[DatasetsIndexParamQv])
                                     : The value to filter by.
            offset (Optional[DatasetsIndexParamOffset])
                                     : Starts at the beginning skip the first ( offset - 1 )
                                       items and begin returning at the Nth item
            limit (Optional[DatasetsIndexParamLimit])
                                     : The maximum number of items to return.
            order (Optional[DatasetsIndexParamOrder])
                                     : String containing one of the valid ordering attributes
                                       followed (optionally) by '-asc' or '-dsc' for ascending
                                       and descending order respectively. Orders can be stacked
                                       as a comma-separated list of values.
            run-as (Optional[DatasetsIndexParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem125]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets"

        params: dict[str, Any] = {
            **({"history_id": history_id} if history_id is not None else {}),
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
            **({"q": q} if q is not None else {}),
            **({"qv": qv} if qv is not None else {}),
            **({"offset": offset} if offset is not None else {}),
            **({"limit": limit} if limit is not None else {}),
            **({"order": order} if order is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem125], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_index_2_2(
        self,
        history_id: DatasetsIndexParamHistoryId | None = None,
        view: DatasetsIndexParamView | None = None,
        keys: DatasetsIndexParamKeys | None = None,
        q: DatasetsIndexParamQ | None = None,
        qv: DatasetsIndexParamQv | None = None,
        offset: DatasetsIndexParamOffset | None = 0,
        limit: DatasetsIndexParamLimit | None = None,
        order: DatasetsIndexParamOrder | None = None,
        run_as: DatasetsIndexParamRunAs | None = None,
    ) -> list[AnonymousArrayItem125]:
        """
        Search datasets or collections using a query system.

        Args:
            history_id (Optional[DatasetsIndexParamHistoryId])
                                     : Optional identifier of a History. Use it to restrict the
                                       search within a particular History.
            view (Optional[DatasetsIndexParamView])
                                     : View to be passed to the serializer
            keys (Optional[DatasetsIndexParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            q (Optional[DatasetsIndexParamQ])
                                     : Generally a property name to filter by followed by an
                                       (often optional) hyphen and operator string.
            qv (Optional[DatasetsIndexParamQv])
                                     : The value to filter by.
            offset (Optional[DatasetsIndexParamOffset])
                                     : Starts at the beginning skip the first ( offset - 1 )
                                       items and begin returning at the Nth item
            limit (Optional[DatasetsIndexParamLimit])
                                     : The maximum number of items to return.
            order (Optional[DatasetsIndexParamOrder])
                                     : String containing one of the valid ordering attributes
                                       followed (optionally) by '-asc' or '-dsc' for ascending
                                       and descending order respectively. Orders can be stacked
                                       as a comma-separated list of values.
            run-as (Optional[DatasetsIndexParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem125]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets"

        params: dict[str, Any] = {
            **({"history_id": history_id} if history_id is not None else {}),
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
            **({"q": q} if q is not None else {}),
            **({"qv": qv} if qv is not None else {}),
            **({"offset": offset} if offset is not None else {}),
            **({"limit": limit} if limit is not None else {}),
            **({"order": order} if order is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem125], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_show_2_2(
        self,
        dataset_id: str,
        hda_ldda: DatasetSourceType | None = None,
        data_type: DatasetsShowParamDataType | None = None,
        limit: DatasetsShowParamLimit | None = 10000,
        offset: DatasetsShowParamOffset | None = 0,
        view: DatasetsShowParamView | None = None,
        keys: DatasetsShowParamKeys | None = None,
        run_as: DatasetsShowParamRunAs | None = None,
    ) -> Any:
        """
        Displays information about and/or content of a dataset.

        **Note**: Due to the multipurpose nature of this endpoint, which can receive a wide
        variety of parameters and return different kinds of responses, the documentation here
        will be limited. To get more information please check the source code.

        Args:
            dataset_id (str)         : The ID of the History Dataset.
            hda_ldda (Optional[DatasetSourceType])
                                     : The type of information about the dataset to be
                                       requested.
            data_type (Optional[DatasetsShowParamDataType])
                                     : The type of information about the dataset to be
                                       requested. Each of these values may require additional
                                       parameters in the request and may return different
                                       responses.
            limit (Optional[DatasetsShowParamLimit])
                                     : Maximum number of items to return. Currently only applies
                                       to `data_type=raw_data` requests
            offset (Optional[DatasetsShowParamOffset])
                                     : Starts at the beginning skip the first ( offset - 1 )
                                       items and begin returning at the Nth item. Currently only
                                       applies to `data_type=raw_data` requests
            view (Optional[DatasetsShowParamView])
                                     : View to be passed to the serializer
            keys (Optional[DatasetsShowParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[DatasetsShowParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets/{dataset_id}"

        params: dict[str, Any] = {
            **({"hda_ldda": hda_ldda} if hda_ldda is not None else {}),
            **({"data_type": data_type} if data_type is not None else {}),
            **({"limit": limit} if limit is not None else {}),
            **({"offset": offset} if offset is not None else {}),
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_show_2_2(
        self,
        dataset_id: str,
        hda_ldda: DatasetSourceType | None = None,
        data_type: DatasetsShowParamDataType | None = None,
        limit: DatasetsShowParamLimit | None = 10000,
        offset: DatasetsShowParamOffset | None = 0,
        view: DatasetsShowParamView | None = None,
        keys: DatasetsShowParamKeys | None = None,
        run_as: DatasetsShowParamRunAs | None = None,
    ) -> Any:
        """
        Displays information about and/or content of a dataset.

        **Note**: Due to the multipurpose nature of this endpoint, which can receive a wide
        variety of parameters and return different kinds of responses, the documentation here
        will be limited. To get more information please check the source code.

        Args:
            dataset_id (str)         : The ID of the History Dataset.
            hda_ldda (Optional[DatasetSourceType])
                                     : The type of information about the dataset to be
                                       requested.
            data_type (Optional[DatasetsShowParamDataType])
                                     : The type of information about the dataset to be
                                       requested. Each of these values may require additional
                                       parameters in the request and may return different
                                       responses.
            limit (Optional[DatasetsShowParamLimit])
                                     : Maximum number of items to return. Currently only applies
                                       to `data_type=raw_data` requests
            offset (Optional[DatasetsShowParamOffset])
                                     : Starts at the beginning skip the first ( offset - 1 )
                                       items and begin returning at the Nth item. Currently only
                                       applies to `data_type=raw_data` requests
            view (Optional[DatasetsShowParamView])
                                     : View to be passed to the serializer
            keys (Optional[DatasetsShowParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[DatasetsShowParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets/{dataset_id}"

        params: dict[str, Any] = {
            **({"hda_ldda": hda_ldda} if hda_ldda is not None else {}),
            **({"data_type": data_type} if data_type is not None else {}),
            **({"limit": limit} if limit is not None else {}),
            **({"offset": offset} if offset is not None else {}),
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_content_get_structured_content_2_2(
        self,
        dataset_id: str,
        content_type: DatasetContentType,
        run_as: DatasetsContentGetStructuredContentParamRunAs | None = None,
    ) -> Any:
        """
        Retrieve information about the content of a dataset.

        Args:
            dataset_id (str)         : The ID of the History Dataset.
            content_type (DatasetContentType)
                                     :
            run-as (Optional[DatasetsContentGetStructuredContentParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets/{dataset_id}/content/{content_type}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_content_get_structured_content_2_2(
        self,
        dataset_id: str,
        content_type: DatasetContentType,
        run_as: DatasetsContentGetStructuredContentParamRunAs | None = None,
    ) -> Any:
        """
        Retrieve information about the content of a dataset.

        Args:
            dataset_id (str)         : The ID of the History Dataset.
            content_type (DatasetContentType)
                                     :
            run-as (Optional[DatasetsContentGetStructuredContentParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets/{dataset_id}/content/{content_type}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_converted_converted_2_2(
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
            run-as (Optional[DatasetsConvertedConvertedParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ConvertedDatasetsMap: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets/{dataset_id}/converted"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ConvertedDatasetsMap, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_converted_converted_2_2(
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
            run-as (Optional[DatasetsConvertedConvertedParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ConvertedDatasetsMap: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets/{dataset_id}/converted"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ConvertedDatasetsMap, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_converted_converted_ext_2_2(
        self,
        dataset_id: str,
        ext: str,
        view: DatasetsConvertedConvertedExtParamView | None = None,
        keys: DatasetsConvertedConvertedExtParamKeys | None = None,
        run_as: DatasetsConvertedConvertedExtParamRunAs | None = None,
    ) -> DatasetsConvertedConvertedExt200Response2:
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
            view (Optional[DatasetsConvertedConvertedExtParamView])
                                     : View to be passed to the serializer
            keys (Optional[DatasetsConvertedConvertedExtParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[DatasetsConvertedConvertedExtParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DatasetsConvertedConvertedExt200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets/{dataset_id}/converted/{ext}"

        params: dict[str, Any] = {
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DatasetsConvertedConvertedExt200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_converted_converted_ext_2_2(
        self,
        dataset_id: str,
        ext: str,
        view: DatasetsConvertedConvertedExtParamView | None = None,
        keys: DatasetsConvertedConvertedExtParamKeys | None = None,
        run_as: DatasetsConvertedConvertedExtParamRunAs | None = None,
    ) -> DatasetsConvertedConvertedExt200Response2:
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
            view (Optional[DatasetsConvertedConvertedExtParamView])
                                     : View to be passed to the serializer
            keys (Optional[DatasetsConvertedConvertedExtParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[DatasetsConvertedConvertedExtParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DatasetsConvertedConvertedExt200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets/{dataset_id}/converted/{ext}"

        params: dict[str, Any] = {
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DatasetsConvertedConvertedExt200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_extra_files_extra_files_2_2(
        self,
        dataset_id: str,
        run_as: DatasetsExtraFilesExtraFilesParamRunAs | None = None,
    ) -> DatasetExtraFiles:
        """
        Get the list of extra files/directories associated with a dataset.

        Args:
            dataset_id (str)         : The encoded database identifier of the dataset.
            run-as (Optional[DatasetsExtraFilesExtraFilesParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DatasetExtraFiles: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets/{dataset_id}/extra_files"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DatasetExtraFiles, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_extra_files_extra_files_2_2(
        self,
        dataset_id: str,
        run_as: DatasetsExtraFilesExtraFilesParamRunAs | None = None,
    ) -> DatasetExtraFiles:
        """
        Get the list of extra files/directories associated with a dataset.

        Args:
            dataset_id (str)         : The encoded database identifier of the dataset.
            run-as (Optional[DatasetsExtraFilesExtraFilesParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DatasetExtraFiles: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets/{dataset_id}/extra_files"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DatasetExtraFiles, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_extra_files_raw_extra_file_raw_2_2(
        self,
        dataset_id: str,
        filename: str,
        run_as: DatasetsExtraFilesRawExtraFileRawParamRunAs | None = None,
    ) -> Any:
        """
        Downloads a raw extra file associated with a dataset.

        Args:
            dataset_id (str)         : The encoded database identifier of the dataset.
            filename (str)           : The name of the extra file to retrieve.
            run-as (Optional[DatasetsExtraFilesRawExtraFileRawParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets/{dataset_id}/extra_files/raw/{filename}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_extra_files_raw_extra_file_raw_2_2(
        self,
        dataset_id: str,
        filename: str,
        run_as: DatasetsExtraFilesRawExtraFileRawParamRunAs | None = None,
    ) -> Any:
        """
        Downloads a raw extra file associated with a dataset.

        Args:
            dataset_id (str)         : The encoded database identifier of the dataset.
            filename (str)           : The name of the extra file to retrieve.
            run-as (Optional[DatasetsExtraFilesRawExtraFileRawParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets/{dataset_id}/extra_files/raw/{filename}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_get_content_as_text_get_content_as_text_2_2(
        self,
        dataset_id: str,
        filename: DatasetsGetContentAsTextGetContentAsTextParamFilename | None = None,
        run_as: DatasetsGetContentAsTextGetContentAsTextParamRunAs | None = None,
    ) -> DatasetTextContentDetails:
        """
        Returns dataset content as Text.

        Args:
            dataset_id (str)         : The ID of the History Dataset.
            filename (Optional[DatasetsGetContentAsTextGetContentAsTextParamFilename])
                                     : If non-null, get the specified filename from the extra
                                       files for this dataset.
            run-as (Optional[DatasetsGetContentAsTextGetContentAsTextParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DatasetTextContentDetails: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets/{dataset_id}/get_content_as_text"

        params: dict[str, Any] = {
            **({"filename": filename} if filename is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DatasetTextContentDetails, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_get_content_as_text_get_content_as_text_2_2(
        self,
        dataset_id: str,
        filename: DatasetsGetContentAsTextGetContentAsTextParamFilename | None = None,
        run_as: DatasetsGetContentAsTextGetContentAsTextParamRunAs | None = None,
    ) -> DatasetTextContentDetails:
        """
        Returns dataset content as Text.

        Args:
            dataset_id (str)         : The ID of the History Dataset.
            filename (Optional[DatasetsGetContentAsTextGetContentAsTextParamFilename])
                                     : If non-null, get the specified filename from the extra
                                       files for this dataset.
            run-as (Optional[DatasetsGetContentAsTextGetContentAsTextParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DatasetTextContentDetails: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets/{dataset_id}/get_content_as_text"

        params: dict[str, Any] = {
            **({"filename": filename} if filename is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DatasetTextContentDetails, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_hash_compute_hash_2_2(
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
            hda_ldda (Optional[DatasetSourceType])
                                     : Whether this dataset belongs to a history (HDA) or a
                                       library (LDDA).
            run-as (Optional[DatasetsHashComputeHashParamRunAs])
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
        url = f"{self.base_url}/api/datasets/{dataset_id}/hash"

        params: dict[str, Any] = {
            **({"hda_ldda": hda_ldda} if hda_ldda is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: ComputeDatasetHashPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(AsyncTaskResultSummary, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_hash_compute_hash_2_2(
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
            hda_ldda (Optional[DatasetSourceType])
                                     : Whether this dataset belongs to a history (HDA) or a
                                       library (LDDA).
            run-as (Optional[DatasetsHashComputeHashParamRunAs])
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
        url = f"{self.base_url}/api/datasets/{dataset_id}/hash"

        params: dict[str, Any] = {
            **({"hda_ldda": hda_ldda} if hda_ldda is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: ComputeDatasetHashPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(AsyncTaskResultSummary, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_inheritance_chain_show_inheritance_chain_2_2(
        self,
        dataset_id: str,
        hda_ldda: DatasetSourceType | None = None,
        run_as: DatasetsInheritanceChainShowInheritanceChainParamRunAs | None = None,
    ) -> DatasetInheritanceChain:
        """
        For internal use, this endpoint may change without warning.

        Args:
            dataset_id (str)         : The ID of the History Dataset.
            hda_ldda (Optional[DatasetSourceType])
                                     : Whether this dataset belongs to a history (HDA) or a
                                       library (LDDA).
            run-as (Optional[DatasetsInheritanceChainShowInheritanceChainParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DatasetInheritanceChain: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets/{dataset_id}/inheritance_chain"

        params: dict[str, Any] = {
            **({"hda_ldda": hda_ldda} if hda_ldda is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DatasetInheritanceChain, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_inheritance_chain_show_inheritance_chain_2_2(
        self,
        dataset_id: str,
        hda_ldda: DatasetSourceType | None = None,
        run_as: DatasetsInheritanceChainShowInheritanceChainParamRunAs | None = None,
    ) -> DatasetInheritanceChain:
        """
        For internal use, this endpoint may change without warning.

        Args:
            dataset_id (str)         : The ID of the History Dataset.
            hda_ldda (Optional[DatasetSourceType])
                                     : Whether this dataset belongs to a history (HDA) or a
                                       library (LDDA).
            run-as (Optional[DatasetsInheritanceChainShowInheritanceChainParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DatasetInheritanceChain: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets/{dataset_id}/inheritance_chain"

        params: dict[str, Any] = {
            **({"hda_ldda": hda_ldda} if hda_ldda is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DatasetInheritanceChain, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_update_object_store_id_2_2(
        self,
        dataset_id: str,
        body: UpdateObjectStoreIdPayload,
        run_as: DatasetsUpdateObjectStoreIdParamRunAs | None = None,
    ) -> Any:
        """
        Update an object store ID for a dataset you own.

        Args:
            dataset_id (str)         : The ID of the History Dataset.
            run-as (Optional[DatasetsUpdateObjectStoreIdParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UpdateObjectStoreIdPayload)
                                     : Request body. (json)

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets/{dataset_id}/object_store_id"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: UpdateObjectStoreIdPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_update_object_store_id_2_2(
        self,
        dataset_id: str,
        body: UpdateObjectStoreIdPayload,
        run_as: DatasetsUpdateObjectStoreIdParamRunAs | None = None,
    ) -> Any:
        """
        Update an object store ID for a dataset you own.

        Args:
            dataset_id (str)         : The ID of the History Dataset.
            run-as (Optional[DatasetsUpdateObjectStoreIdParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UpdateObjectStoreIdPayload)
                                     : Request body. (json)

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets/{dataset_id}/object_store_id"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: UpdateObjectStoreIdPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_permissions_update_permissions_2_2(
        self,
        dataset_id: str,
        body: DatasetsPermissionsUpdatePermissionsRequestBody2,
        run_as: DatasetsPermissionsUpdatePermissionsParamRunAs | None = None,
    ) -> DatasetAssociationRoles:
        """
        Set permissions of the given history dataset to the given role ids.

        Set permissions of the given history dataset to the given role ids.

        Args:
            dataset_id (str)         : The ID of the History Dataset.
            run-as (Optional[DatasetsPermissionsUpdatePermissionsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (DatasetsPermissionsUpdatePermissionsRequestBody2)
                                     : Request body. (json)

        Returns:
            DatasetAssociationRoles: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets/{dataset_id}/permissions"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: DatasetsPermissionsUpdatePermissionsRequestBody2 = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DatasetAssociationRoles, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_permissions_update_permissions_2_2(
        self,
        dataset_id: str,
        body: DatasetsPermissionsUpdatePermissionsRequestBody2,
        run_as: DatasetsPermissionsUpdatePermissionsParamRunAs | None = None,
    ) -> DatasetAssociationRoles:
        """
        Set permissions of the given history dataset to the given role ids.

        Set permissions of the given history dataset to the given role ids.

        Args:
            dataset_id (str)         : The ID of the History Dataset.
            run-as (Optional[DatasetsPermissionsUpdatePermissionsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (DatasetsPermissionsUpdatePermissionsRequestBody2)
                                     : Request body. (json)

        Returns:
            DatasetAssociationRoles: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets/{dataset_id}/permissions"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: DatasetsPermissionsUpdatePermissionsRequestBody2 = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DatasetAssociationRoles, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_report_report_2_2(
        self,
        dataset_id: str,
        run_as: DatasetsReportReportParamRunAs | None = None,
    ) -> ToolReportForDataset:
        """
        Return JSON content Galaxy will use to render Markdown reports

        Args:
            dataset_id (str)         : The ID of the History Dataset.
            run-as (Optional[DatasetsReportReportParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ToolReportForDataset: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets/{dataset_id}/report"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ToolReportForDataset, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_report_report_2_2(
        self,
        dataset_id: str,
        run_as: DatasetsReportReportParamRunAs | None = None,
    ) -> ToolReportForDataset:
        """
        Return JSON content Galaxy will use to render Markdown reports

        Args:
            dataset_id (str)         : The ID of the History Dataset.
            run-as (Optional[DatasetsReportReportParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ToolReportForDataset: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets/{dataset_id}/report"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ToolReportForDataset, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_storage_show_storage_2_2(
        self,
        dataset_id: str,
        hda_ldda: DatasetSourceType | None = None,
        run_as: DatasetsStorageShowStorageParamRunAs | None = None,
    ) -> DatasetStorageDetails:
        """
        Display user-facing storage details related to the objectstore a dataset resides in.

        Args:
            dataset_id (str)         : The ID of the History Dataset.
            hda_ldda (Optional[DatasetSourceType])
                                     : Whether this dataset belongs to a history (HDA) or a
                                       library (LDDA).
            run-as (Optional[DatasetsStorageShowStorageParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DatasetStorageDetails: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets/{dataset_id}/storage"

        params: dict[str, Any] = {
            **({"hda_ldda": hda_ldda} if hda_ldda is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DatasetStorageDetails, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_storage_show_storage_2_2(
        self,
        dataset_id: str,
        hda_ldda: DatasetSourceType | None = None,
        run_as: DatasetsStorageShowStorageParamRunAs | None = None,
    ) -> DatasetStorageDetails:
        """
        Display user-facing storage details related to the objectstore a dataset resides in.

        Args:
            dataset_id (str)         : The ID of the History Dataset.
            hda_ldda (Optional[DatasetSourceType])
                                     : Whether this dataset belongs to a history (HDA) or a
                                       library (LDDA).
            run-as (Optional[DatasetsStorageShowStorageParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DatasetStorageDetails: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets/{dataset_id}/storage"

        params: dict[str, Any] = {
            **({"hda_ldda": hda_ldda} if hda_ldda is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DatasetStorageDetails, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_display_display_2_2(
        self,
        history_content_id: str,
        preview: bool | None = False,
        filename: DatasetsDisplayDisplayParamFilename | None = None,
        to_ext: DatasetsDisplayDisplayParamToExt | None = None,
        raw: bool | None = False,
        offset: DatasetsDisplayDisplayParamOffset | None = None,
        ck_size: DatasetsDisplayDisplayParamCkSize | None = None,
        run_as: DatasetsDisplayDisplayParamRunAs | None = None,
    ) -> None:
        """
        Displays (preview) or downloads dataset content.

        Streams the dataset for download or the contents preview to be displayed in a browser.

        Args:
            history_content_id (str) : The ID of the History Dataset.
            preview (Optional[bool]) : Whether to get preview contents to be directly displayed
                                       on the web. If preview is False (default) the contents
                                       will be downloaded instead.
            filename (Optional[DatasetsDisplayDisplayParamFilename])
                                     : If non-null, get the specified filename from the extra
                                       files for this dataset.
            to_ext (Optional[DatasetsDisplayDisplayParamToExt])
                                     : The file extension when downloading the display data. Use
                                       the value `data` to let the server infer it from the data
                                       type.
            raw (Optional[bool])     : The query parameter 'raw' should be considered
                                       experimental and may be dropped at some point in the
                                       future without warning. Generally, data should be
                                       processed by its datatype prior to display.
            offset (Optional[DatasetsDisplayDisplayParamOffset])
                                     : Set this for datatypes that allow chunked display through
                                       the display_data method to enable chunking. This
                                       specifies a byte offset into the target dataset's
                                       display.
            ck_size (Optional[DatasetsDisplayDisplayParamCkSize])
                                     : If offset is set, this recommends 'how large' the next
                                       chunk should be. This is not respected or interpreted
                                       uniformly and should be interpreted as a very loose
                                       recommendation. Different datatypes interpret 'largeness'
                                       differently - for bam datasets this is a number of lines
                                       whereas for tabular datatypes this is interpreted as a
                                       number of bytes.
            run-as (Optional[DatasetsDisplayDisplayParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets/{history_content_id}/display"

        params: dict[str, Any] = {
            **({"preview": preview} if preview is not None else {}),
            **({"filename": filename} if filename is not None else {}),
            **({"to_ext": to_ext} if to_ext is not None else {}),
            **({"raw": raw} if raw is not None else {}),
            **({"offset": offset} if offset is not None else {}),
            **({"ck_size": ck_size} if ck_size is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_display_display_2_2(
        self,
        history_content_id: str,
        preview: bool | None = False,
        filename: DatasetsDisplayDisplayParamFilename | None = None,
        to_ext: DatasetsDisplayDisplayParamToExt | None = None,
        raw: bool | None = False,
        offset: DatasetsDisplayDisplayParamOffset | None = None,
        ck_size: DatasetsDisplayDisplayParamCkSize | None = None,
        run_as: DatasetsDisplayDisplayParamRunAs | None = None,
    ) -> None:
        """
        Displays (preview) or downloads dataset content.

        Streams the dataset for download or the contents preview to be displayed in a browser.

        Args:
            history_content_id (str) : The ID of the History Dataset.
            preview (Optional[bool]) : Whether to get preview contents to be directly displayed
                                       on the web. If preview is False (default) the contents
                                       will be downloaded instead.
            filename (Optional[DatasetsDisplayDisplayParamFilename])
                                     : If non-null, get the specified filename from the extra
                                       files for this dataset.
            to_ext (Optional[DatasetsDisplayDisplayParamToExt])
                                     : The file extension when downloading the display data. Use
                                       the value `data` to let the server infer it from the data
                                       type.
            raw (Optional[bool])     : The query parameter 'raw' should be considered
                                       experimental and may be dropped at some point in the
                                       future without warning. Generally, data should be
                                       processed by its datatype prior to display.
            offset (Optional[DatasetsDisplayDisplayParamOffset])
                                     : Set this for datatypes that allow chunked display through
                                       the display_data method to enable chunking. This
                                       specifies a byte offset into the target dataset's
                                       display.
            ck_size (Optional[DatasetsDisplayDisplayParamCkSize])
                                     : If offset is set, this recommends 'how large' the next
                                       chunk should be. This is not respected or interpreted
                                       uniformly and should be interpreted as a very loose
                                       recommendation. Different datatypes interpret 'largeness'
                                       differently - for bam datasets this is a number of lines
                                       whereas for tabular datatypes this is interpreted as a
                                       number of bytes.
            run-as (Optional[DatasetsDisplayDisplayParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets/{history_content_id}/display"

        params: dict[str, Any] = {
            **({"preview": preview} if preview is not None else {}),
            **({"filename": filename} if filename is not None else {}),
            **({"to_ext": to_ext} if to_ext is not None else {}),
            **({"raw": raw} if raw is not None else {}),
            **({"offset": offset} if offset is not None else {}),
            **({"ck_size": ck_size} if ck_size is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_display_display_3_2(
        self,
        history_content_id: str,
        preview: bool | None = False,
        filename: DatasetsDisplayDisplayParamFilename | None = None,
        to_ext: DatasetsDisplayDisplayParamToExt | None = None,
        raw: bool | None = False,
        offset: DatasetsDisplayDisplayParamOffset | None = None,
        ck_size: DatasetsDisplayDisplayParamCkSize | None = None,
        run_as: DatasetsDisplayDisplayParamRunAs | None = None,
    ) -> Any:
        """
        Check if dataset content can be previewed or downloaded.

        Streams the dataset for download or the contents preview to be displayed in a browser.

        Args:
            history_content_id (str) : The ID of the History Dataset.
            preview (Optional[bool]) : Whether to get preview contents to be directly displayed
                                       on the web. If preview is False (default) the contents
                                       will be downloaded instead.
            filename (Optional[DatasetsDisplayDisplayParamFilename])
                                     : If non-null, get the specified filename from the extra
                                       files for this dataset.
            to_ext (Optional[DatasetsDisplayDisplayParamToExt])
                                     : The file extension when downloading the display data. Use
                                       the value `data` to let the server infer it from the data
                                       type.
            raw (Optional[bool])     : The query parameter 'raw' should be considered
                                       experimental and may be dropped at some point in the
                                       future without warning. Generally, data should be
                                       processed by its datatype prior to display.
            offset (Optional[DatasetsDisplayDisplayParamOffset])
                                     : Set this for datatypes that allow chunked display through
                                       the display_data method to enable chunking. This
                                       specifies a byte offset into the target dataset's
                                       display.
            ck_size (Optional[DatasetsDisplayDisplayParamCkSize])
                                     : If offset is set, this recommends 'how large' the next
                                       chunk should be. This is not respected or interpreted
                                       uniformly and should be interpreted as a very loose
                                       recommendation. Different datatypes interpret 'largeness'
                                       differently - for bam datasets this is a number of lines
                                       whereas for tabular datatypes this is interpreted as a
                                       number of bytes.
            run-as (Optional[DatasetsDisplayDisplayParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets/{history_content_id}/display"

        params: dict[str, Any] = {
            **({"preview": preview} if preview is not None else {}),
            **({"filename": filename} if filename is not None else {}),
            **({"to_ext": to_ext} if to_ext is not None else {}),
            **({"raw": raw} if raw is not None else {}),
            **({"offset": offset} if offset is not None else {}),
            **({"ck_size": ck_size} if ck_size is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("HEAD", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_display_display_3_2(
        self,
        history_content_id: str,
        preview: bool | None = False,
        filename: DatasetsDisplayDisplayParamFilename | None = None,
        to_ext: DatasetsDisplayDisplayParamToExt | None = None,
        raw: bool | None = False,
        offset: DatasetsDisplayDisplayParamOffset | None = None,
        ck_size: DatasetsDisplayDisplayParamCkSize | None = None,
        run_as: DatasetsDisplayDisplayParamRunAs | None = None,
    ) -> Any:
        """
        Check if dataset content can be previewed or downloaded.

        Streams the dataset for download or the contents preview to be displayed in a browser.

        Args:
            history_content_id (str) : The ID of the History Dataset.
            preview (Optional[bool]) : Whether to get preview contents to be directly displayed
                                       on the web. If preview is False (default) the contents
                                       will be downloaded instead.
            filename (Optional[DatasetsDisplayDisplayParamFilename])
                                     : If non-null, get the specified filename from the extra
                                       files for this dataset.
            to_ext (Optional[DatasetsDisplayDisplayParamToExt])
                                     : The file extension when downloading the display data. Use
                                       the value `data` to let the server infer it from the data
                                       type.
            raw (Optional[bool])     : The query parameter 'raw' should be considered
                                       experimental and may be dropped at some point in the
                                       future without warning. Generally, data should be
                                       processed by its datatype prior to display.
            offset (Optional[DatasetsDisplayDisplayParamOffset])
                                     : Set this for datatypes that allow chunked display through
                                       the display_data method to enable chunking. This
                                       specifies a byte offset into the target dataset's
                                       display.
            ck_size (Optional[DatasetsDisplayDisplayParamCkSize])
                                     : If offset is set, this recommends 'how large' the next
                                       chunk should be. This is not respected or interpreted
                                       uniformly and should be interpreted as a very loose
                                       recommendation. Different datatypes interpret 'largeness'
                                       differently - for bam datasets this is a number of lines
                                       whereas for tabular datatypes this is interpreted as a
                                       number of bytes.
            run-as (Optional[DatasetsDisplayDisplayParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets/{history_content_id}/display"

        params: dict[str, Any] = {
            **({"preview": preview} if preview is not None else {}),
            **({"filename": filename} if filename is not None else {}),
            **({"to_ext": to_ext} if to_ext is not None else {}),
            **({"raw": raw} if raw is not None else {}),
            **({"offset": offset} if offset is not None else {}),
            **({"ck_size": ck_size} if ck_size is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("HEAD", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_get_metadata_file_2_2(
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
            run-as (Optional[DatasetsGetMetadataFileParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets/{history_content_id}/metadata_file"

        params: dict[str, Any] = {
            "metadata_file": metadata_file,
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_get_metadata_file_2_2(
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
            run-as (Optional[DatasetsGetMetadataFileParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets/{history_content_id}/metadata_file"

        params: dict[str, Any] = {
            "metadata_file": metadata_file,
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_metadata_file_get_metadata_file_datasets_2_2(
        self,
        history_content_id: str,
        metadata_file: str,
        run_as: DatasetsMetadataFileGetMetadataFileDatasetsParamRunAs | None = None,
    ) -> Any:
        """
        Check if metadata file can be downloaded.

        Args:
            history_content_id (str) : The ID of the History Dataset.
            metadata_file (str)      : The name of the metadata file to retrieve.
            run-as (Optional[DatasetsMetadataFileGetMetadataFileDatasetsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets/{history_content_id}/metadata_file"

        params: dict[str, Any] = {
            "metadata_file": metadata_file,
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("HEAD", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_metadata_file_get_metadata_file_datasets_2_2(
        self,
        history_content_id: str,
        metadata_file: str,
        run_as: DatasetsMetadataFileGetMetadataFileDatasetsParamRunAs | None = None,
    ) -> Any:
        """
        Check if metadata file can be downloaded.

        Args:
            history_content_id (str) : The ID of the History Dataset.
            metadata_file (str)      : The name of the metadata file to retrieve.
            run-as (Optional[DatasetsMetadataFileGetMetadataFileDatasetsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets/{history_content_id}/metadata_file"

        params: dict[str, Any] = {
            "metadata_file": metadata_file,
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("HEAD", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_contents_display_display_history_content_2_2(
        self,
        history_content_id: str,
        history_id: DatasetsContentsDisplayDisplayHistoryContentParamHistoryId | None,
        preview: bool | None = False,
        filename: DatasetsContentsDisplayDisplayHistoryContentParamFilename | None = None,
        to_ext: DatasetsContentsDisplayDisplayHistoryContentParamToExt | None = None,
        raw: bool | None = False,
        offset: DatasetsContentsDisplayDisplayHistoryContentParamOffset | None = None,
        ck_size: DatasetsContentsDisplayDisplayHistoryContentParamCkSize | None = None,
        run_as: DatasetsContentsDisplayDisplayHistoryContentParamRunAs | None = None,
    ) -> None:
        """
        Displays (preview) or downloads dataset content.

        Streams the dataset for download or the contents preview to be displayed in a browser.

        Args:
            history_content_id (str) : The ID of the History Dataset.
            history_id (Optional[DatasetsContentsDisplayDisplayHistoryContentParamHistoryId])
                                     :
            preview (Optional[bool]) : Whether to get preview contents to be directly displayed
                                       on the web. If preview is False (default) the contents
                                       will be downloaded instead.
            filename (Optional[DatasetsContentsDisplayDisplayHistoryContentParamFilename])
                                     : If non-null, get the specified filename from the extra
                                       files for this dataset.
            to_ext (Optional[DatasetsContentsDisplayDisplayHistoryContentParamToExt])
                                     : The file extension when downloading the display data. Use
                                       the value `data` to let the server infer it from the data
                                       type.
            raw (Optional[bool])     : The query parameter 'raw' should be considered
                                       experimental and may be dropped at some point in the
                                       future without warning. Generally, data should be
                                       processed by its datatype prior to display.
            offset (Optional[DatasetsContentsDisplayDisplayHistoryContentParamOffset])
                                     : Set this for datatypes that allow chunked display through
                                       the display_data method to enable chunking. This
                                       specifies a byte offset into the target dataset's
                                       display.
            ck_size (Optional[DatasetsContentsDisplayDisplayHistoryContentParamCkSize])
                                     : If offset is set, this recommends 'how large' the next
                                       chunk should be. This is not respected or interpreted
                                       uniformly and should be interpreted as a very loose
                                       recommendation. Different datatypes interpret 'largeness'
                                       differently - for bam datasets this is a number of lines
                                       whereas for tabular datatypes this is interpreted as a
                                       number of bytes.
            run-as (Optional[DatasetsContentsDisplayDisplayHistoryContentParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/{history_content_id}/display"

        params: dict[str, Any] = {
            **({"preview": preview} if preview is not None else {}),
            **({"filename": filename} if filename is not None else {}),
            **({"to_ext": to_ext} if to_ext is not None else {}),
            **({"raw": raw} if raw is not None else {}),
            **({"offset": offset} if offset is not None else {}),
            **({"ck_size": ck_size} if ck_size is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_contents_display_display_history_content_2_2(
        self,
        history_content_id: str,
        history_id: DatasetsContentsDisplayDisplayHistoryContentParamHistoryId | None,
        preview: bool | None = False,
        filename: DatasetsContentsDisplayDisplayHistoryContentParamFilename | None = None,
        to_ext: DatasetsContentsDisplayDisplayHistoryContentParamToExt | None = None,
        raw: bool | None = False,
        offset: DatasetsContentsDisplayDisplayHistoryContentParamOffset | None = None,
        ck_size: DatasetsContentsDisplayDisplayHistoryContentParamCkSize | None = None,
        run_as: DatasetsContentsDisplayDisplayHistoryContentParamRunAs | None = None,
    ) -> None:
        """
        Displays (preview) or downloads dataset content.

        Streams the dataset for download or the contents preview to be displayed in a browser.

        Args:
            history_content_id (str) : The ID of the History Dataset.
            history_id (Optional[DatasetsContentsDisplayDisplayHistoryContentParamHistoryId])
                                     :
            preview (Optional[bool]) : Whether to get preview contents to be directly displayed
                                       on the web. If preview is False (default) the contents
                                       will be downloaded instead.
            filename (Optional[DatasetsContentsDisplayDisplayHistoryContentParamFilename])
                                     : If non-null, get the specified filename from the extra
                                       files for this dataset.
            to_ext (Optional[DatasetsContentsDisplayDisplayHistoryContentParamToExt])
                                     : The file extension when downloading the display data. Use
                                       the value `data` to let the server infer it from the data
                                       type.
            raw (Optional[bool])     : The query parameter 'raw' should be considered
                                       experimental and may be dropped at some point in the
                                       future without warning. Generally, data should be
                                       processed by its datatype prior to display.
            offset (Optional[DatasetsContentsDisplayDisplayHistoryContentParamOffset])
                                     : Set this for datatypes that allow chunked display through
                                       the display_data method to enable chunking. This
                                       specifies a byte offset into the target dataset's
                                       display.
            ck_size (Optional[DatasetsContentsDisplayDisplayHistoryContentParamCkSize])
                                     : If offset is set, this recommends 'how large' the next
                                       chunk should be. This is not respected or interpreted
                                       uniformly and should be interpreted as a very loose
                                       recommendation. Different datatypes interpret 'largeness'
                                       differently - for bam datasets this is a number of lines
                                       whereas for tabular datatypes this is interpreted as a
                                       number of bytes.
            run-as (Optional[DatasetsContentsDisplayDisplayHistoryContentParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/{history_content_id}/display"

        params: dict[str, Any] = {
            **({"preview": preview} if preview is not None else {}),
            **({"filename": filename} if filename is not None else {}),
            **({"to_ext": to_ext} if to_ext is not None else {}),
            **({"raw": raw} if raw is not None else {}),
            **({"offset": offset} if offset is not None else {}),
            **({"ck_size": ck_size} if ck_size is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_contents_display_display_history_content_2_2_2(
        self,
        history_content_id: str,
        history_id: DatasetsContentsDisplayDisplayHistoryContentParamHistoryId | None,
        preview: bool | None = False,
        filename: DatasetsContentsDisplayDisplayHistoryContentParamFilename | None = None,
        to_ext: DatasetsContentsDisplayDisplayHistoryContentParamToExt | None = None,
        raw: bool | None = False,
        offset: DatasetsContentsDisplayDisplayHistoryContentParamOffset | None = None,
        ck_size: DatasetsContentsDisplayDisplayHistoryContentParamCkSize | None = None,
        run_as: DatasetsContentsDisplayDisplayHistoryContentParamRunAs | None = None,
    ) -> Any:
        """
        Check if dataset content can be previewed or downloaded.

        Streams the dataset for download or the contents preview to be displayed in a browser.

        Args:
            history_content_id (str) : The ID of the History Dataset.
            history_id (Optional[DatasetsContentsDisplayDisplayHistoryContentParamHistoryId])
                                     :
            preview (Optional[bool]) : Whether to get preview contents to be directly displayed
                                       on the web. If preview is False (default) the contents
                                       will be downloaded instead.
            filename (Optional[DatasetsContentsDisplayDisplayHistoryContentParamFilename])
                                     : If non-null, get the specified filename from the extra
                                       files for this dataset.
            to_ext (Optional[DatasetsContentsDisplayDisplayHistoryContentParamToExt])
                                     : The file extension when downloading the display data. Use
                                       the value `data` to let the server infer it from the data
                                       type.
            raw (Optional[bool])     : The query parameter 'raw' should be considered
                                       experimental and may be dropped at some point in the
                                       future without warning. Generally, data should be
                                       processed by its datatype prior to display.
            offset (Optional[DatasetsContentsDisplayDisplayHistoryContentParamOffset])
                                     : Set this for datatypes that allow chunked display through
                                       the display_data method to enable chunking. This
                                       specifies a byte offset into the target dataset's
                                       display.
            ck_size (Optional[DatasetsContentsDisplayDisplayHistoryContentParamCkSize])
                                     : If offset is set, this recommends 'how large' the next
                                       chunk should be. This is not respected or interpreted
                                       uniformly and should be interpreted as a very loose
                                       recommendation. Different datatypes interpret 'largeness'
                                       differently - for bam datasets this is a number of lines
                                       whereas for tabular datatypes this is interpreted as a
                                       number of bytes.
            run-as (Optional[DatasetsContentsDisplayDisplayHistoryContentParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/{history_content_id}/display"

        params: dict[str, Any] = {
            **({"preview": preview} if preview is not None else {}),
            **({"filename": filename} if filename is not None else {}),
            **({"to_ext": to_ext} if to_ext is not None else {}),
            **({"raw": raw} if raw is not None else {}),
            **({"offset": offset} if offset is not None else {}),
            **({"ck_size": ck_size} if ck_size is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("HEAD", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_contents_display_display_history_content_2_2_2(
        self,
        history_content_id: str,
        history_id: DatasetsContentsDisplayDisplayHistoryContentParamHistoryId | None,
        preview: bool | None = False,
        filename: DatasetsContentsDisplayDisplayHistoryContentParamFilename | None = None,
        to_ext: DatasetsContentsDisplayDisplayHistoryContentParamToExt | None = None,
        raw: bool | None = False,
        offset: DatasetsContentsDisplayDisplayHistoryContentParamOffset | None = None,
        ck_size: DatasetsContentsDisplayDisplayHistoryContentParamCkSize | None = None,
        run_as: DatasetsContentsDisplayDisplayHistoryContentParamRunAs | None = None,
    ) -> Any:
        """
        Check if dataset content can be previewed or downloaded.

        Streams the dataset for download or the contents preview to be displayed in a browser.

        Args:
            history_content_id (str) : The ID of the History Dataset.
            history_id (Optional[DatasetsContentsDisplayDisplayHistoryContentParamHistoryId])
                                     :
            preview (Optional[bool]) : Whether to get preview contents to be directly displayed
                                       on the web. If preview is False (default) the contents
                                       will be downloaded instead.
            filename (Optional[DatasetsContentsDisplayDisplayHistoryContentParamFilename])
                                     : If non-null, get the specified filename from the extra
                                       files for this dataset.
            to_ext (Optional[DatasetsContentsDisplayDisplayHistoryContentParamToExt])
                                     : The file extension when downloading the display data. Use
                                       the value `data` to let the server infer it from the data
                                       type.
            raw (Optional[bool])     : The query parameter 'raw' should be considered
                                       experimental and may be dropped at some point in the
                                       future without warning. Generally, data should be
                                       processed by its datatype prior to display.
            offset (Optional[DatasetsContentsDisplayDisplayHistoryContentParamOffset])
                                     : Set this for datatypes that allow chunked display through
                                       the display_data method to enable chunking. This
                                       specifies a byte offset into the target dataset's
                                       display.
            ck_size (Optional[DatasetsContentsDisplayDisplayHistoryContentParamCkSize])
                                     : If offset is set, this recommends 'how large' the next
                                       chunk should be. This is not respected or interpreted
                                       uniformly and should be interpreted as a very loose
                                       recommendation. Different datatypes interpret 'largeness'
                                       differently - for bam datasets this is a number of lines
                                       whereas for tabular datatypes this is interpreted as a
                                       number of bytes.
            run-as (Optional[DatasetsContentsDisplayDisplayHistoryContentParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/{history_content_id}/display"

        params: dict[str, Any] = {
            **({"preview": preview} if preview is not None else {}),
            **({"filename": filename} if filename is not None else {}),
            **({"to_ext": to_ext} if to_ext is not None else {}),
            **({"raw": raw} if raw is not None else {}),
            **({"offset": offset} if offset is not None else {}),
            **({"ck_size": ck_size} if ck_size is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("HEAD", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_contents_extra_files_extra_files_history_2_2(
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
            run-as (Optional[DatasetsContentsExtraFilesExtraFilesHistoryParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DatasetExtraFiles: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/{history_content_id}/extra_files"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DatasetExtraFiles, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_contents_extra_files_extra_files_history_2_2(
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
            run-as (Optional[DatasetsContentsExtraFilesExtraFilesHistoryParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            DatasetExtraFiles: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/{history_content_id}/extra_files"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DatasetExtraFiles, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def history_contents_get_metadata_file_2_2(
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
            run-as (Optional[HistoryContentsGetMetadataFileParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/{history_content_id}/metadata_file"

        params: dict[str, Any] = {
            "metadata_file": metadata_file,
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def history_contents_get_metadata_file_2_2(
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
            run-as (Optional[HistoryContentsGetMetadataFileParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/{history_content_id}/metadata_file"

        params: dict[str, Any] = {
            "metadata_file": metadata_file,
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover
