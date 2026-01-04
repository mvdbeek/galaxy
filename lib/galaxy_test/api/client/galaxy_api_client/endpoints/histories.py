from typing import Any, cast

from galaxy_api_client.core import Error501
from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.anonymous_array_item_139 import AnonymousArrayItem139
from ..models.anonymous_array_item_145 import AnonymousArrayItem145
from ..models.anonymous_array_item_147 import AnonymousArrayItem147
from ..models.anonymous_array_item_149 import AnonymousArrayItem149
from ..models.anonymous_array_item_155 import AnonymousArrayItem155
from ..models.anonymous_array_item_161 import AnonymousArrayItem161
from ..models.anonymous_array_item_167 import AnonymousArrayItem167
from ..models.anonymous_array_item_168 import AnonymousArrayItem168
from ..models.anonymous_array_item_198 import AnonymousArrayItem198
from ..models.anonymous_array_item_200 import AnonymousArrayItem200
from ..models.async_file import AsyncFile
from ..models.async_task_result_summary import AsyncTaskResultSummary
from ..models.copy_datasets_payload import CopyDatasetsPayload
from ..models.copy_datasets_response import CopyDatasetsResponse
from ..models.create_history_content_from_store import CreateHistoryContentFromStore
from ..models.create_history_content_payload import CreateHistoryContentPayload
from ..models.create_history_from_store import CreateHistoryFromStore
from ..models.custom_builds_metadata_response import CustomBuildsMetadataResponse
from ..models.dataset_association_roles import DatasetAssociationRoles
from ..models.dataset_collections_download_param_run_as import DatasetCollectionsDownloadParamRunAs
from ..models.dataset_collections_update_collection_200_response_2 import DatasetCollectionsUpdateCollection200Response2
from ..models.dataset_collections_update_collection_param_keys import DatasetCollectionsUpdateCollectionParamKeys
from ..models.dataset_collections_update_collection_param_run_as import DatasetCollectionsUpdateCollectionParamRunAs
from ..models.dataset_collections_update_collection_param_view import DatasetCollectionsUpdateCollectionParamView
from ..models.dataset_extra_files import DatasetExtraFiles
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
from ..models.datasets_delete_param_purge import DatasetsDeleteParamPurge
from ..models.datasets_delete_param_recursive import DatasetsDeleteParamRecursive
from ..models.datasets_delete_param_run_as import DatasetsDeleteParamRunAs
from ..models.datasets_delete_param_stop_job import DatasetsDeleteParamStopJob
from ..models.datasets_update_dataset_200_response_2 import DatasetsUpdateDataset200Response2
from ..models.datasets_update_dataset_param_keys import DatasetsUpdateDatasetParamKeys
from ..models.datasets_update_dataset_param_run_as import DatasetsUpdateDatasetParamRunAs
from ..models.datasets_update_dataset_param_view import DatasetsUpdateDatasetParamView
from ..models.delete_histories_payload import DeleteHistoriesPayload
from ..models.delete_history_content_payload import DeleteHistoryContentPayload
from ..models.histories_archive_archive_history_200_response_2 import HistoriesArchiveArchiveHistory200Response2
from ..models.histories_archive_archive_history_param_run_as import HistoriesArchiveArchiveHistoryParamRunAs
from ..models.histories_archive_archive_history_request_body_2 import HistoriesArchiveArchiveHistoryRequestBody2
from ..models.histories_archive_restore_restore_archived_history_200_response_2 import (
    HistoriesArchiveRestoreRestoreArchivedHistory200Response2,
)
from ..models.histories_archive_restore_restore_archived_history_param_force import (
    HistoriesArchiveRestoreRestoreArchivedHistoryParamForce,
)
from ..models.histories_archive_restore_restore_archived_history_param_run_as import (
    HistoriesArchiveRestoreRestoreArchivedHistoryParamRunAs,
)
from ..models.histories_archived_get_archived_histories_param_keys import HistoriesArchivedGetArchivedHistoriesParamKeys
from ..models.histories_archived_get_archived_histories_param_limit import (
    HistoriesArchivedGetArchivedHistoriesParamLimit,
)
from ..models.histories_archived_get_archived_histories_param_offset import (
    HistoriesArchivedGetArchivedHistoriesParamOffset,
)
from ..models.histories_archived_get_archived_histories_param_order import (
    HistoriesArchivedGetArchivedHistoriesParamOrder,
)
from ..models.histories_archived_get_archived_histories_param_q import HistoriesArchivedGetArchivedHistoriesParamQ
from ..models.histories_archived_get_archived_histories_param_qv import HistoriesArchivedGetArchivedHistoriesParamQv
from ..models.histories_archived_get_archived_histories_param_run_as import (
    HistoriesArchivedGetArchivedHistoriesParamRunAs,
)
from ..models.histories_archived_get_archived_histories_param_view import HistoriesArchivedGetArchivedHistoriesParamView
from ..models.histories_batch_delete_batch_delete_param_keys import HistoriesBatchDeleteBatchDeleteParamKeys
from ..models.histories_batch_delete_batch_delete_param_run_as import HistoriesBatchDeleteBatchDeleteParamRunAs
from ..models.histories_batch_delete_batch_delete_param_view import HistoriesBatchDeleteBatchDeleteParamView
from ..models.histories_batch_undelete_batch_undelete_param_keys import HistoriesBatchUndeleteBatchUndeleteParamKeys
from ..models.histories_batch_undelete_batch_undelete_param_run_as import HistoriesBatchUndeleteBatchUndeleteParamRunAs
from ..models.histories_batch_undelete_batch_undelete_param_view import HistoriesBatchUndeleteBatchUndeleteParamView
from ..models.histories_citations_citations_param_run_as import HistoriesCitationsCitationsParamRunAs
from ..models.histories_contents_bulk_bulk_operation_param_q import HistoriesContentsBulkBulkOperationParamQ
from ..models.histories_contents_bulk_bulk_operation_param_qv import HistoriesContentsBulkBulkOperationParamQv
from ..models.histories_contents_bulk_bulk_operation_param_run_as import HistoriesContentsBulkBulkOperationParamRunAs
from ..models.histories_contents_datasets_materialize_materialize_dataset_param_run_as import (
    HistoriesContentsDatasetsMaterializeMaterializeDatasetParamRunAs,
)
from ..models.histories_contents_from_store_create_from_store_param_keys import (
    HistoriesContentsFromStoreCreateFromStoreParamKeys,
)
from ..models.histories_contents_from_store_create_from_store_param_run_as import (
    HistoriesContentsFromStoreCreateFromStoreParamRunAs,
)
from ..models.histories_contents_from_store_create_from_store_param_view import (
    HistoriesContentsFromStoreCreateFromStoreParamView,
)
from ..models.histories_contents_jobs_summary_show_jobs_summary_200_response_2 import (
    HistoriesContentsJobsSummaryShowJobsSummary200Response2,
)
from ..models.histories_contents_jobs_summary_show_jobs_summary_param_run_as import (
    HistoriesContentsJobsSummaryShowJobsSummaryParamRunAs,
)
from ..models.histories_contents_permissions_update_permissions_param_run_as import (
    HistoriesContentsPermissionsUpdatePermissionsParamRunAs,
)
from ..models.histories_contents_permissions_update_permissions_request_body_2 import (
    HistoriesContentsPermissionsUpdatePermissionsRequestBody2,
)
from ..models.histories_contents_prepare_store_download_prepare_store_download_param_run_as import (
    HistoriesContentsPrepareStoreDownloadPrepareStoreDownloadParamRunAs,
)
from ..models.histories_contents_tags_create_param_run_as import HistoriesContentsTagsCreateParamRunAs
from ..models.histories_contents_tags_delete_param_run_as import HistoriesContentsTagsDeleteParamRunAs
from ..models.histories_contents_tags_index_param_run_as import HistoriesContentsTagsIndexParamRunAs
from ..models.histories_contents_tags_show_param_run_as import HistoriesContentsTagsShowParamRunAs
from ..models.histories_contents_tags_update_param_run_as import HistoriesContentsTagsUpdateParamRunAs
from ..models.histories_contents_update_batch_param_keys import HistoriesContentsUpdateBatchParamKeys
from ..models.histories_contents_update_batch_param_run_as import HistoriesContentsUpdateBatchParamRunAs
from ..models.histories_contents_update_batch_param_view import HistoriesContentsUpdateBatchParamView
from ..models.histories_contents_validate_validate_200_response_2 import HistoriesContentsValidateValidate200Response2
from ..models.histories_contents_validate_validate_param_run_as import HistoriesContentsValidateValidateParamRunAs
from ..models.histories_contents_write_store_write_store_param_run_as import (
    HistoriesContentsWriteStoreWriteStoreParamRunAs,
)
from ..models.histories_count_count_param_run_as import HistoriesCountCountParamRunAs
from ..models.histories_create_200_response_2 import HistoriesCreate200Response2
from ..models.histories_create_param_keys import HistoriesCreateParamKeys
from ..models.histories_create_param_run_as import HistoriesCreateParamRunAs
from ..models.histories_create_param_view import HistoriesCreateParamView
from ..models.histories_custom_builds_metadata_get_custom_builds_metadata_param_run_as import (
    HistoriesCustomBuildsMetadataGetCustomBuildsMetadataParamRunAs,
)
from ..models.histories_delete_200_response_2 import HistoriesDelete200Response2
from ..models.histories_delete_param_keys import HistoriesDeleteParamKeys
from ..models.histories_delete_param_run_as import HistoriesDeleteParamRunAs
from ..models.histories_delete_param_view import HistoriesDeleteParamView
from ..models.histories_delete_request_body_2 import HistoriesDeleteRequestBody2
from ..models.histories_deleted_index_deleted_param_all import HistoriesDeletedIndexDeletedParamAll
from ..models.histories_deleted_index_deleted_param_keys import HistoriesDeletedIndexDeletedParamKeys
from ..models.histories_deleted_index_deleted_param_limit import HistoriesDeletedIndexDeletedParamLimit
from ..models.histories_deleted_index_deleted_param_offset import HistoriesDeletedIndexDeletedParamOffset
from ..models.histories_deleted_index_deleted_param_order import HistoriesDeletedIndexDeletedParamOrder
from ..models.histories_deleted_index_deleted_param_q import HistoriesDeletedIndexDeletedParamQ
from ..models.histories_deleted_index_deleted_param_qv import HistoriesDeletedIndexDeletedParamQv
from ..models.histories_deleted_index_deleted_param_run_as import HistoriesDeletedIndexDeletedParamRunAs
from ..models.histories_deleted_index_deleted_param_view import HistoriesDeletedIndexDeletedParamView
from ..models.histories_deleted_undelete_undelete_200_response_2 import HistoriesDeletedUndeleteUndelete200Response2
from ..models.histories_deleted_undelete_undelete_param_keys import HistoriesDeletedUndeleteUndeleteParamKeys
from ..models.histories_deleted_undelete_undelete_param_run_as import HistoriesDeletedUndeleteUndeleteParamRunAs
from ..models.histories_deleted_undelete_undelete_param_view import HistoriesDeletedUndeleteUndeleteParamView
from ..models.histories_disable_link_access_disable_link_access_param_run_as import (
    HistoriesDisableLinkAccessDisableLinkAccessParamRunAs,
)
from ..models.histories_enable_link_access_enable_link_access_param_run_as import (
    HistoriesEnableLinkAccessEnableLinkAccessParamRunAs,
)
from ..models.histories_exports_archive_download_param_jeha_id import HistoriesExportsArchiveDownloadParamJehaId
from ..models.histories_exports_archive_download_param_run_as import HistoriesExportsArchiveDownloadParamRunAs
from ..models.histories_exports_archive_export_200_response_2 import HistoriesExportsArchiveExport200Response2
from ..models.histories_exports_archive_export_param_run_as import HistoriesExportsArchiveExportParamRunAs
from ..models.histories_exports_archive_export_request_body_2 import HistoriesExportsArchiveExportRequestBody2
from ..models.histories_exports_index_exports_param_limit import HistoriesExportsIndexExportsParamLimit
from ..models.histories_exports_index_exports_param_offset import HistoriesExportsIndexExportsParamOffset
from ..models.histories_exports_index_exports_param_run_as import HistoriesExportsIndexExportsParamRunAs
from ..models.histories_from_store_async_create_from_store_async_param_run_as import (
    HistoriesFromStoreAsyncCreateFromStoreAsyncParamRunAs,
)
from ..models.histories_from_store_create_from_store_200_response_2 import HistoriesFromStoreCreateFromStore200Response2
from ..models.histories_from_store_create_from_store_param_keys import HistoriesFromStoreCreateFromStoreParamKeys
from ..models.histories_from_store_create_from_store_param_run_as import HistoriesFromStoreCreateFromStoreParamRunAs
from ..models.histories_from_store_create_from_store_param_view import HistoriesFromStoreCreateFromStoreParamView
from ..models.histories_index_param_all import HistoriesIndexParamAll
from ..models.histories_index_param_deleted import HistoriesIndexParamDeleted
from ..models.histories_index_param_keys import HistoriesIndexParamKeys
from ..models.histories_index_param_limit import HistoriesIndexParamLimit
from ..models.histories_index_param_offset import HistoriesIndexParamOffset
from ..models.histories_index_param_order import HistoriesIndexParamOrder
from ..models.histories_index_param_q import HistoriesIndexParamQ
from ..models.histories_index_param_qv import HistoriesIndexParamQv
from ..models.histories_index_param_run_as import HistoriesIndexParamRunAs
from ..models.histories_index_param_search import HistoriesIndexParamSearch
from ..models.histories_index_param_show_archived import HistoriesIndexParamShowArchived
from ..models.histories_index_param_view import HistoriesIndexParamView
from ..models.histories_jobs_summary_index_jobs_summary_param_ids import HistoriesJobsSummaryIndexJobsSummaryParamIds
from ..models.histories_jobs_summary_index_jobs_summary_param_run_as import (
    HistoriesJobsSummaryIndexJobsSummaryParamRunAs,
)
from ..models.histories_jobs_summary_index_jobs_summary_param_types import (
    HistoriesJobsSummaryIndexJobsSummaryParamTypes,
)
from ..models.histories_materialize_materialize_to_history_param_run_as import (
    HistoriesMaterializeMaterializeToHistoryParamRunAs,
)
from ..models.histories_most_recently_used_show_recent_200_response_2 import (
    HistoriesMostRecentlyUsedShowRecent200Response2,
)
from ..models.histories_most_recently_used_show_recent_param_keys import HistoriesMostRecentlyUsedShowRecentParamKeys
from ..models.histories_most_recently_used_show_recent_param_run_as import HistoriesMostRecentlyUsedShowRecentParamRunAs
from ..models.histories_most_recently_used_show_recent_param_view import HistoriesMostRecentlyUsedShowRecentParamView
from ..models.histories_prepare_download_prepare_collection_download_param_run_as import (
    HistoriesPrepareDownloadPrepareCollectionDownloadParamRunAs,
)
from ..models.histories_prepare_store_download_prepare_store_download_param_run_as import (
    HistoriesPrepareStoreDownloadPrepareStoreDownloadParamRunAs,
)
from ..models.histories_publish_publish_param_run_as import HistoriesPublishPublishParamRunAs
from ..models.histories_published_published_param_keys import HistoriesPublishedPublishedParamKeys
from ..models.histories_published_published_param_limit import HistoriesPublishedPublishedParamLimit
from ..models.histories_published_published_param_offset import HistoriesPublishedPublishedParamOffset
from ..models.histories_published_published_param_order import HistoriesPublishedPublishedParamOrder
from ..models.histories_published_published_param_q import HistoriesPublishedPublishedParamQ
from ..models.histories_published_published_param_qv import HistoriesPublishedPublishedParamQv
from ..models.histories_published_published_param_run_as import HistoriesPublishedPublishedParamRunAs
from ..models.histories_published_published_param_view import HistoriesPublishedPublishedParamView
from ..models.histories_share_with_users_share_with_users_param_run_as import (
    HistoriesShareWithUsersShareWithUsersParamRunAs,
)
from ..models.histories_shared_with_me_shared_with_me_param_keys import HistoriesSharedWithMeSharedWithMeParamKeys
from ..models.histories_shared_with_me_shared_with_me_param_limit import HistoriesSharedWithMeSharedWithMeParamLimit
from ..models.histories_shared_with_me_shared_with_me_param_offset import HistoriesSharedWithMeSharedWithMeParamOffset
from ..models.histories_shared_with_me_shared_with_me_param_order import HistoriesSharedWithMeSharedWithMeParamOrder
from ..models.histories_shared_with_me_shared_with_me_param_q import HistoriesSharedWithMeSharedWithMeParamQ
from ..models.histories_shared_with_me_shared_with_me_param_qv import HistoriesSharedWithMeSharedWithMeParamQv
from ..models.histories_shared_with_me_shared_with_me_param_run_as import HistoriesSharedWithMeSharedWithMeParamRunAs
from ..models.histories_shared_with_me_shared_with_me_param_view import HistoriesSharedWithMeSharedWithMeParamView
from ..models.histories_sharing_sharing_param_run_as import HistoriesSharingSharingParamRunAs
from ..models.histories_show_200_response_2 import HistoriesShow200Response2
from ..models.histories_show_param_keys import HistoriesShowParamKeys
from ..models.histories_show_param_run_as import HistoriesShowParamRunAs
from ..models.histories_show_param_view import HistoriesShowParamView
from ..models.histories_slug_set_slug_param_run_as import HistoriesSlugSetSlugParamRunAs
from ..models.histories_tags_create_param_run_as import HistoriesTagsCreateParamRunAs
from ..models.histories_tags_delete_param_run_as import HistoriesTagsDeleteParamRunAs
from ..models.histories_tags_index_param_run_as import HistoriesTagsIndexParamRunAs
from ..models.histories_tags_show_param_run_as import HistoriesTagsShowParamRunAs
from ..models.histories_tags_update_param_run_as import HistoriesTagsUpdateParamRunAs
from ..models.histories_tool_requests_tool_requests_param_run_as import HistoriesToolRequestsToolRequestsParamRunAs
from ..models.histories_unpublish_unpublish_param_run_as import HistoriesUnpublishUnpublishParamRunAs
from ..models.histories_update_200_response_2 import HistoriesUpdate200Response2
from ..models.histories_update_param_keys import HistoriesUpdateParamKeys
from ..models.histories_update_param_run_as import HistoriesUpdateParamRunAs
from ..models.histories_update_param_view import HistoriesUpdateParamView
from ..models.histories_write_store_write_store_param_run_as import HistoriesWriteStoreWriteStoreParamRunAs
from ..models.history_content_bulk_operation_payload import HistoryContentBulkOperationPayload
from ..models.history_content_bulk_operation_result import HistoryContentBulkOperationResult
from ..models.history_content_type import HistoryContentType
from ..models.history_contents_archive_named_param_dry_run import HistoryContentsArchiveNamedParamDryRun
from ..models.history_contents_archive_named_param_limit import HistoryContentsArchiveNamedParamLimit
from ..models.history_contents_archive_named_param_offset import HistoryContentsArchiveNamedParamOffset
from ..models.history_contents_archive_named_param_order import HistoryContentsArchiveNamedParamOrder
from ..models.history_contents_archive_named_param_q import HistoryContentsArchiveNamedParamQ
from ..models.history_contents_archive_named_param_qv import HistoryContentsArchiveNamedParamQv
from ..models.history_contents_archive_named_param_run_as import HistoryContentsArchiveNamedParamRunAs
from ..models.history_contents_archive_param_dry_run import HistoryContentsArchiveParamDryRun
from ..models.history_contents_archive_param_filename import HistoryContentsArchiveParamFilename
from ..models.history_contents_archive_param_limit import HistoryContentsArchiveParamLimit
from ..models.history_contents_archive_param_offset import HistoryContentsArchiveParamOffset
from ..models.history_contents_archive_param_order import HistoryContentsArchiveParamOrder
from ..models.history_contents_archive_param_q import HistoryContentsArchiveParamQ
from ..models.history_contents_archive_param_qv import HistoryContentsArchiveParamQv
from ..models.history_contents_archive_param_run_as import HistoryContentsArchiveParamRunAs
from ..models.history_contents_copy_contents_param_run_as import HistoryContentsCopyContentsParamRunAs
from ..models.history_contents_create_200_response_2 import HistoryContentsCreate200Response2
from ..models.history_contents_create_param_keys import HistoryContentsCreateParamKeys
from ..models.history_contents_create_param_run_as import HistoryContentsCreateParamRunAs
from ..models.history_contents_create_param_type import HistoryContentsCreateParamType
from ..models.history_contents_create_param_view import HistoryContentsCreateParamView
from ..models.history_contents_create_typed_200_response_2 import HistoryContentsCreateTyped200Response2
from ..models.history_contents_create_typed_param_keys import HistoryContentsCreateTypedParamKeys
from ..models.history_contents_create_typed_param_run_as import HistoryContentsCreateTypedParamRunAs
from ..models.history_contents_create_typed_param_view import HistoryContentsCreateTypedParamView
from ..models.history_contents_delete_legacy_param_purge import HistoryContentsDeleteLegacyParamPurge
from ..models.history_contents_delete_legacy_param_recursive import HistoryContentsDeleteLegacyParamRecursive
from ..models.history_contents_delete_legacy_param_run_as import HistoryContentsDeleteLegacyParamRunAs
from ..models.history_contents_delete_legacy_param_stop_job import HistoryContentsDeleteLegacyParamStopJob
from ..models.history_contents_delete_typed_param_purge import HistoryContentsDeleteTypedParamPurge
from ..models.history_contents_delete_typed_param_recursive import HistoryContentsDeleteTypedParamRecursive
from ..models.history_contents_delete_typed_param_run_as import HistoryContentsDeleteTypedParamRunAs
from ..models.history_contents_delete_typed_param_stop_job import HistoryContentsDeleteTypedParamStopJob
from ..models.history_contents_download_collection_param_history_id import (
    HistoryContentsDownloadCollectionParamHistoryId,
)
from ..models.history_contents_download_collection_param_run_as import HistoryContentsDownloadCollectionParamRunAs
from ..models.history_contents_get_metadata_file_param_run_as import HistoryContentsGetMetadataFileParamRunAs
from ..models.history_contents_index_param_deleted import HistoryContentsIndexParamDeleted
from ..models.history_contents_index_param_details import HistoryContentsIndexParamDetails
from ..models.history_contents_index_param_ids import HistoryContentsIndexParamIds
from ..models.history_contents_index_param_keys import HistoryContentsIndexParamKeys
from ..models.history_contents_index_param_limit import HistoryContentsIndexParamLimit
from ..models.history_contents_index_param_offset import HistoryContentsIndexParamOffset
from ..models.history_contents_index_param_order import HistoryContentsIndexParamOrder
from ..models.history_contents_index_param_q import HistoryContentsIndexParamQ
from ..models.history_contents_index_param_qv import HistoryContentsIndexParamQv
from ..models.history_contents_index_param_run_as import HistoryContentsIndexParamRunAs
from ..models.history_contents_index_param_shareable import HistoryContentsIndexParamShareable
from ..models.history_contents_index_param_types import HistoryContentsIndexParamTypes
from ..models.history_contents_index_param_v import HistoryContentsIndexParamV
from ..models.history_contents_index_param_view import HistoryContentsIndexParamView
from ..models.history_contents_index_param_visible import HistoryContentsIndexParamVisible
from ..models.history_contents_index_typed_param_deleted import HistoryContentsIndexTypedParamDeleted
from ..models.history_contents_index_typed_param_details import HistoryContentsIndexTypedParamDetails
from ..models.history_contents_index_typed_param_ids import HistoryContentsIndexTypedParamIds
from ..models.history_contents_index_typed_param_keys import HistoryContentsIndexTypedParamKeys
from ..models.history_contents_index_typed_param_limit import HistoryContentsIndexTypedParamLimit
from ..models.history_contents_index_typed_param_offset import HistoryContentsIndexTypedParamOffset
from ..models.history_contents_index_typed_param_order import HistoryContentsIndexTypedParamOrder
from ..models.history_contents_index_typed_param_q import HistoryContentsIndexTypedParamQ
from ..models.history_contents_index_typed_param_qv import HistoryContentsIndexTypedParamQv
from ..models.history_contents_index_typed_param_run_as import HistoryContentsIndexTypedParamRunAs
from ..models.history_contents_index_typed_param_shareable import HistoryContentsIndexTypedParamShareable
from ..models.history_contents_index_typed_param_types import HistoryContentsIndexTypedParamTypes
from ..models.history_contents_index_typed_param_v import HistoryContentsIndexTypedParamV
from ..models.history_contents_index_typed_param_view import HistoryContentsIndexTypedParamView
from ..models.history_contents_index_typed_param_visible import HistoryContentsIndexTypedParamVisible
from ..models.history_contents_result import HistoryContentsResult
from ..models.history_contents_show_200_response_2 import HistoryContentsShow200Response2
from ..models.history_contents_show_legacy_200_response_2 import HistoryContentsShowLegacy200Response2
from ..models.history_contents_show_legacy_param_fuzzy_count import HistoryContentsShowLegacyParamFuzzyCount
from ..models.history_contents_show_legacy_param_keys import HistoryContentsShowLegacyParamKeys
from ..models.history_contents_show_legacy_param_run_as import HistoryContentsShowLegacyParamRunAs
from ..models.history_contents_show_legacy_param_view import HistoryContentsShowLegacyParamView
from ..models.history_contents_show_param_fuzzy_count import HistoryContentsShowParamFuzzyCount
from ..models.history_contents_show_param_keys import HistoryContentsShowParamKeys
from ..models.history_contents_show_param_run_as import HistoryContentsShowParamRunAs
from ..models.history_contents_show_param_view import HistoryContentsShowParamView
from ..models.history_contents_update_legacy_200_response_2 import HistoryContentsUpdateLegacy200Response2
from ..models.history_contents_update_legacy_param_keys import HistoryContentsUpdateLegacyParamKeys
from ..models.history_contents_update_legacy_param_run_as import HistoryContentsUpdateLegacyParamRunAs
from ..models.history_contents_update_legacy_param_view import HistoryContentsUpdateLegacyParamView
from ..models.history_contents_update_typed_200_response_2 import HistoryContentsUpdateTyped200Response2
from ..models.history_contents_update_typed_param_keys import HistoryContentsUpdateTypedParamKeys
from ..models.history_contents_update_typed_param_run_as import HistoryContentsUpdateTypedParamRunAs
from ..models.history_contents_update_typed_param_view import HistoryContentsUpdateTypedParamView
from ..models.item_tags_create_payload import ItemTagsCreatePayload
from ..models.item_tags_list_response import ItemTagsListResponse
from ..models.item_tags_response import ItemTagsResponse
from ..models.job_export_history_archive_list_response import JobExportHistoryArchiveListResponse
from ..models.materialize_dataset_instance_api_request_2 import MaterializeDatasetInstanceApiRequest2
from ..models.set_slug_payload import SetSlugPayload
from ..models.share_history_with_status import ShareHistoryWithStatus
from ..models.share_with_payload import ShareWithPayload
from ..models.sharing_status import SharingStatus
from ..models.store_export_payload import StoreExportPayload
from ..models.tool_request_model import ToolRequestModel
from ..models.undelete_histories_payload import UndeleteHistoriesPayload
from ..models.update_history_contents_batch_payload import UpdateHistoryContentsBatchPayload
from ..models.update_history_contents_payload import UpdateHistoryContentsPayload
from ..models.update_history_payload import UpdateHistoryPayload
from ..models.write_store_to_payload import WriteStoreToPayload


class HistoriesClient:
    """Client for histories endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def dataset_collections_update_collection_2_2(
        self,
        hdca_id: str,
        body: UpdateHistoryContentsPayload,
        view: DatasetCollectionsUpdateCollectionParamView | None = None,
        keys: DatasetCollectionsUpdateCollectionParamKeys | None = None,
        run_as: DatasetCollectionsUpdateCollectionParamRunAs | None = None,
    ) -> DatasetCollectionsUpdateCollection200Response2:
        """
        Updates the values for the history dataset (HDA) item with the given ``ID``.

        Updates the values for the history content item with the given ``ID``.

        Args:
            hdca_id (str)            : The ID of the item (`HDA`/`HDCA`)
            view (Optional[DatasetCollectionsUpdateCollectionParamView])
                                     : View to be passed to the serializer
            keys (Optional[DatasetCollectionsUpdateCollectionParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[DatasetCollectionsUpdateCollectionParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UpdateHistoryContentsPayload)
                                     : Request body. (json)

        Returns:
            DatasetCollectionsUpdateCollection200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/dataset_collections/{hdca_id}"

        params: dict[str, Any] = {
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: UpdateHistoryContentsPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DatasetCollectionsUpdateCollection200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dataset_collections_update_collection_2_2(
        self,
        hdca_id: str,
        body: UpdateHistoryContentsPayload,
        view: DatasetCollectionsUpdateCollectionParamView | None = None,
        keys: DatasetCollectionsUpdateCollectionParamKeys | None = None,
        run_as: DatasetCollectionsUpdateCollectionParamRunAs | None = None,
    ) -> DatasetCollectionsUpdateCollection200Response2:
        """
        Updates the values for the history dataset (HDA) item with the given ``ID``.

        Updates the values for the history content item with the given ``ID``.

        Args:
            hdca_id (str)            : The ID of the item (`HDA`/`HDCA`)
            view (Optional[DatasetCollectionsUpdateCollectionParamView])
                                     : View to be passed to the serializer
            keys (Optional[DatasetCollectionsUpdateCollectionParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[DatasetCollectionsUpdateCollectionParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UpdateHistoryContentsPayload)
                                     : Request body. (json)

        Returns:
            DatasetCollectionsUpdateCollection200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/dataset_collections/{hdca_id}"

        params: dict[str, Any] = {
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: UpdateHistoryContentsPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DatasetCollectionsUpdateCollection200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def dataset_collections_download_2_2(
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

    async def dataset_collections_download_2_2(
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

    async def histories_prepare_download_prepare_collection_download_2_2(
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

    async def histories_prepare_download_prepare_collection_download_2_2(
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

    async def datasets_delete_2_2(
        self,
        dataset_id: str,
        purge: DatasetsDeleteParamPurge | None = False,
        recursive: DatasetsDeleteParamRecursive | None = False,
        stop_job: DatasetsDeleteParamStopJob | None = False,
        run_as: DatasetsDeleteParamRunAs | None = None,
        body: DeleteHistoryContentPayload | None = None,
    ) -> Any:
        """
        Delete the history dataset content with the given ``ID``.

        Delete the history content with the given ``ID`` and path specified type.  **Note**:
        Currently does not stop any active jobs for which this dataset is an output.

        Args:
            dataset_id (str)         : The ID of the item (`HDA`/`HDCA`)
            purge (Optional[DatasetsDeleteParamPurge])
                                     : Whether to remove from disk the target HDA or child HDAs
                                       of the target HDCA.
            recursive (Optional[DatasetsDeleteParamRecursive])
                                     : When deleting a dataset collection, whether to also
                                       delete containing datasets.
            stop_job (Optional[DatasetsDeleteParamStopJob])
                                     : Whether to stop the creating job if all outputs of the
                                       job have been deleted.
            run-as (Optional[DatasetsDeleteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (Optional[DeleteHistoryContentPayload])
                                     : Request body. (json)

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets/{dataset_id}"

        params: dict[str, Any] = {
            **({"purge": purge} if purge is not None else {}),
            **({"recursive": recursive} if recursive is not None else {}),
            **({"stop_job": stop_job} if stop_job is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: DeleteHistoryContentPayload | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("DELETE", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case 202:
                return None
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_delete_2_2(
        self,
        dataset_id: str,
        purge: DatasetsDeleteParamPurge | None = False,
        recursive: DatasetsDeleteParamRecursive | None = False,
        stop_job: DatasetsDeleteParamStopJob | None = False,
        run_as: DatasetsDeleteParamRunAs | None = None,
        body: DeleteHistoryContentPayload | None = None,
    ) -> Any:
        """
        Delete the history dataset content with the given ``ID``.

        Delete the history content with the given ``ID`` and path specified type.  **Note**:
        Currently does not stop any active jobs for which this dataset is an output.

        Args:
            dataset_id (str)         : The ID of the item (`HDA`/`HDCA`)
            purge (Optional[DatasetsDeleteParamPurge])
                                     : Whether to remove from disk the target HDA or child HDAs
                                       of the target HDCA.
            recursive (Optional[DatasetsDeleteParamRecursive])
                                     : When deleting a dataset collection, whether to also
                                       delete containing datasets.
            stop_job (Optional[DatasetsDeleteParamStopJob])
                                     : Whether to stop the creating job if all outputs of the
                                       job have been deleted.
            run-as (Optional[DatasetsDeleteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (Optional[DeleteHistoryContentPayload])
                                     : Request body. (json)

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets/{dataset_id}"

        params: dict[str, Any] = {
            **({"purge": purge} if purge is not None else {}),
            **({"recursive": recursive} if recursive is not None else {}),
            **({"stop_job": stop_job} if stop_job is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: DeleteHistoryContentPayload | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("DELETE", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case 202:
                return None
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_update_dataset_2_2(
        self,
        dataset_id: str,
        body: UpdateHistoryContentsPayload,
        view: DatasetsUpdateDatasetParamView | None = None,
        keys: DatasetsUpdateDatasetParamKeys | None = None,
        run_as: DatasetsUpdateDatasetParamRunAs | None = None,
    ) -> DatasetsUpdateDataset200Response2:
        """
        Updates the values for the history dataset (HDA) item with the given ``ID``.

        Updates the values for the history content item with the given ``ID``.

        Args:
            dataset_id (str)         : The ID of the item (`HDA`/`HDCA`)
            view (Optional[DatasetsUpdateDatasetParamView])
                                     : View to be passed to the serializer
            keys (Optional[DatasetsUpdateDatasetParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[DatasetsUpdateDatasetParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UpdateHistoryContentsPayload)
                                     : Request body. (json)

        Returns:
            DatasetsUpdateDataset200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets/{dataset_id}"

        params: dict[str, Any] = {
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: UpdateHistoryContentsPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DatasetsUpdateDataset200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_update_dataset_2_2(
        self,
        dataset_id: str,
        body: UpdateHistoryContentsPayload,
        view: DatasetsUpdateDatasetParamView | None = None,
        keys: DatasetsUpdateDatasetParamKeys | None = None,
        run_as: DatasetsUpdateDatasetParamRunAs | None = None,
    ) -> DatasetsUpdateDataset200Response2:
        """
        Updates the values for the history dataset (HDA) item with the given ``ID``.

        Updates the values for the history content item with the given ``ID``.

        Args:
            dataset_id (str)         : The ID of the item (`HDA`/`HDCA`)
            view (Optional[DatasetsUpdateDatasetParamView])
                                     : View to be passed to the serializer
            keys (Optional[DatasetsUpdateDatasetParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[DatasetsUpdateDatasetParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UpdateHistoryContentsPayload)
                                     : Request body. (json)

        Returns:
            DatasetsUpdateDataset200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets/{dataset_id}"

        params: dict[str, Any] = {
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: UpdateHistoryContentsPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DatasetsUpdateDataset200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_index_2_2(
        self,
        limit: HistoriesIndexParamLimit | None = None,
        offset: HistoriesIndexParamOffset | None = 0,
        show_own: bool | None = True,
        show_published: bool | None = True,
        show_shared: bool | None = False,
        show_archived: HistoriesIndexParamShowArchived | None = None,
        sort_by: str | None = "update_time",
        sort_desc: bool | None = True,
        search: HistoriesIndexParamSearch | None = None,
        all_: HistoriesIndexParamAll | None = False,
        deleted: HistoriesIndexParamDeleted | None = False,
        q: HistoriesIndexParamQ | None = None,
        qv: HistoriesIndexParamQv | None = None,
        order: HistoriesIndexParamOrder | None = None,
        view: HistoriesIndexParamView | None = None,
        keys: HistoriesIndexParamKeys | None = None,
        run_as: HistoriesIndexParamRunAs | None = None,
    ) -> list[AnonymousArrayItem139]:
        """
        Returns histories available to the current user.

        Args:
            limit (Optional[HistoriesIndexParamLimit])
                                     : The maximum number of items to return.
            offset (Optional[HistoriesIndexParamOffset])
                                     : Starts at the beginning skip the first ( offset - 1 )
                                       items and begin returning at the Nth item
            show_own (Optional[bool]):
            show_published (Optional[bool])
                                     :
            show_shared (Optional[bool])
                                     :
            show_archived (Optional[HistoriesIndexParamShowArchived])
                                     : Whether to include archived histories.
            sort_by (Optional[str])  : Sort index by this specified attribute
            sort_desc (Optional[bool]): Sort in descending order?
            search (Optional[HistoriesIndexParamSearch])
                                     : A mix of free text and GitHub-style tags used to filter
                                       the index operation.  ## Query Structure  GitHub-style
                                       filter tags (not be confused with Galaxy tags) are tags
                                       of the form `<tag_name>:<text_no_spaces>` or
                                       `<tag_name>:'<text with potential spaces>'`. The tag name
                                       *generally* (but not exclusively) corresponds to the name
                                       of an attribute on the model being indexed (i.e. a column
                                       in the database).  If the tag is quoted, the attribute
                                       will be filtered exactly. If the tag is unquoted,
                                       generally a partial match will be used to filter the
                                       query (i.e. in terms of the implementation this means the
                                       database operation `ILIKE` will typically be used).  Once
                                       the tagged filters are extracted from the search query,
                                       the remaining text is just used to search various
                                       documented attributes of the object.  ## GitHub-style
                                       Tags Available  `name` : The history's name.
                                       `annotation` : The history's annotation. (The tag `a` can
                                       be used a short hand alias for this tag to filter on this
                                       attribute.)  `tag` : The history's tags. (The tag `t` can
                                       be used a short hand alias for this tag to filter on this
                                       attribute.)  ## Free Text  Free text search terms will be
                                       searched against the following attributes of the
                                       Historys: `title`, `description`, `slug`, `tag`.
            all (Optional[HistoriesIndexParamAll])
                                     : Whether all histories from other users in this Galaxy
                                       should be included. Only admins are allowed to query all
                                       histories.
            deleted (Optional[HistoriesIndexParamDeleted])
                                     : Whether to return only deleted items.
            q (Optional[HistoriesIndexParamQ])
                                     : Generally a property name to filter by followed by an
                                       (often optional) hyphen and operator string.
            qv (Optional[HistoriesIndexParamQv])
                                     : The value to filter by.
            order (Optional[HistoriesIndexParamOrder])
                                     : String containing one of the valid ordering attributes
                                       followed (optionally) by '-asc' or '-dsc' for ascending
                                       and descending order respectively. Orders can be stacked
                                       as a comma-separated list of values.
            view (Optional[HistoriesIndexParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoriesIndexParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoriesIndexParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem139]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories"

        params: dict[str, Any] = {
            **({"limit": limit} if limit is not None else {}),
            **({"offset": offset} if offset is not None else {}),
            **({"show_own": show_own} if show_own is not None else {}),
            **({"show_published": show_published} if show_published is not None else {}),
            **({"show_shared": show_shared} if show_shared is not None else {}),
            **({"show_archived": show_archived} if show_archived is not None else {}),
            **({"sort_by": sort_by} if sort_by is not None else {}),
            **({"sort_desc": sort_desc} if sort_desc is not None else {}),
            **({"search": search} if search is not None else {}),
            **({"all": all_} if all_ is not None else {}),
            **({"deleted": deleted} if deleted is not None else {}),
            **({"q": q} if q is not None else {}),
            **({"qv": qv} if qv is not None else {}),
            **({"order": order} if order is not None else {}),
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
                return cast(list[AnonymousArrayItem139], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_index_2_2(
        self,
        limit: HistoriesIndexParamLimit | None = None,
        offset: HistoriesIndexParamOffset | None = 0,
        show_own: bool | None = True,
        show_published: bool | None = True,
        show_shared: bool | None = False,
        show_archived: HistoriesIndexParamShowArchived | None = None,
        sort_by: str | None = "update_time",
        sort_desc: bool | None = True,
        search: HistoriesIndexParamSearch | None = None,
        all_: HistoriesIndexParamAll | None = False,
        deleted: HistoriesIndexParamDeleted | None = False,
        q: HistoriesIndexParamQ | None = None,
        qv: HistoriesIndexParamQv | None = None,
        order: HistoriesIndexParamOrder | None = None,
        view: HistoriesIndexParamView | None = None,
        keys: HistoriesIndexParamKeys | None = None,
        run_as: HistoriesIndexParamRunAs | None = None,
    ) -> list[AnonymousArrayItem139]:
        """
        Returns histories available to the current user.

        Args:
            limit (Optional[HistoriesIndexParamLimit])
                                     : The maximum number of items to return.
            offset (Optional[HistoriesIndexParamOffset])
                                     : Starts at the beginning skip the first ( offset - 1 )
                                       items and begin returning at the Nth item
            show_own (Optional[bool]):
            show_published (Optional[bool])
                                     :
            show_shared (Optional[bool])
                                     :
            show_archived (Optional[HistoriesIndexParamShowArchived])
                                     : Whether to include archived histories.
            sort_by (Optional[str])  : Sort index by this specified attribute
            sort_desc (Optional[bool]): Sort in descending order?
            search (Optional[HistoriesIndexParamSearch])
                                     : A mix of free text and GitHub-style tags used to filter
                                       the index operation.  ## Query Structure  GitHub-style
                                       filter tags (not be confused with Galaxy tags) are tags
                                       of the form `<tag_name>:<text_no_spaces>` or
                                       `<tag_name>:'<text with potential spaces>'`. The tag name
                                       *generally* (but not exclusively) corresponds to the name
                                       of an attribute on the model being indexed (i.e. a column
                                       in the database).  If the tag is quoted, the attribute
                                       will be filtered exactly. If the tag is unquoted,
                                       generally a partial match will be used to filter the
                                       query (i.e. in terms of the implementation this means the
                                       database operation `ILIKE` will typically be used).  Once
                                       the tagged filters are extracted from the search query,
                                       the remaining text is just used to search various
                                       documented attributes of the object.  ## GitHub-style
                                       Tags Available  `name` : The history's name.
                                       `annotation` : The history's annotation. (The tag `a` can
                                       be used a short hand alias for this tag to filter on this
                                       attribute.)  `tag` : The history's tags. (The tag `t` can
                                       be used a short hand alias for this tag to filter on this
                                       attribute.)  ## Free Text  Free text search terms will be
                                       searched against the following attributes of the
                                       Historys: `title`, `description`, `slug`, `tag`.
            all (Optional[HistoriesIndexParamAll])
                                     : Whether all histories from other users in this Galaxy
                                       should be included. Only admins are allowed to query all
                                       histories.
            deleted (Optional[HistoriesIndexParamDeleted])
                                     : Whether to return only deleted items.
            q (Optional[HistoriesIndexParamQ])
                                     : Generally a property name to filter by followed by an
                                       (often optional) hyphen and operator string.
            qv (Optional[HistoriesIndexParamQv])
                                     : The value to filter by.
            order (Optional[HistoriesIndexParamOrder])
                                     : String containing one of the valid ordering attributes
                                       followed (optionally) by '-asc' or '-dsc' for ascending
                                       and descending order respectively. Orders can be stacked
                                       as a comma-separated list of values.
            view (Optional[HistoriesIndexParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoriesIndexParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoriesIndexParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem139]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories"

        params: dict[str, Any] = {
            **({"limit": limit} if limit is not None else {}),
            **({"offset": offset} if offset is not None else {}),
            **({"show_own": show_own} if show_own is not None else {}),
            **({"show_published": show_published} if show_published is not None else {}),
            **({"show_shared": show_shared} if show_shared is not None else {}),
            **({"show_archived": show_archived} if show_archived is not None else {}),
            **({"sort_by": sort_by} if sort_by is not None else {}),
            **({"sort_desc": sort_desc} if sort_desc is not None else {}),
            **({"search": search} if search is not None else {}),
            **({"all": all_} if all_ is not None else {}),
            **({"deleted": deleted} if deleted is not None else {}),
            **({"q": q} if q is not None else {}),
            **({"qv": qv} if qv is not None else {}),
            **({"order": order} if order is not None else {}),
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
                return cast(list[AnonymousArrayItem139], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_create_2_2(
        self,
        view: HistoriesCreateParamView | None = None,
        keys: HistoriesCreateParamKeys | None = None,
        run_as: HistoriesCreateParamRunAs | None = None,
        form_data: dict[str, Any] = None,
    ) -> HistoriesCreate200Response2:
        """
        Creates a new history.

        The new history can also be copied form a existing history or imported from an archive
        or URL.

        Args:
            view (Optional[HistoriesCreateParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoriesCreateParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoriesCreateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            form_data (Dict[str, Any]): Request body. (x-www-form-urlencoded)

        Returns:
            HistoriesCreate200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories"

        params: dict[str, Any] = {
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        form_data_body: dict[str, Any] = DataclassSerializer.serialize(form_data)

        response = await self._transport.request("POST", url, params=params, data=form_data_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(HistoriesCreate200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_create_2_2(
        self,
        view: HistoriesCreateParamView | None = None,
        keys: HistoriesCreateParamKeys | None = None,
        run_as: HistoriesCreateParamRunAs | None = None,
        form_data: dict[str, Any] = None,
    ) -> HistoriesCreate200Response2:
        """
        Creates a new history.

        The new history can also be copied form a existing history or imported from an archive
        or URL.

        Args:
            view (Optional[HistoriesCreateParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoriesCreateParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoriesCreateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            form_data (Dict[str, Any]): Request body. (x-www-form-urlencoded)

        Returns:
            HistoriesCreate200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories"

        params: dict[str, Any] = {
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        form_data_body: dict[str, Any] = DataclassSerializer.serialize(form_data)

        response = await self._transport.request("POST", url, params=params, data=form_data_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(HistoriesCreate200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_archived_get_archived_histories_2_2(
        self,
        view: HistoriesArchivedGetArchivedHistoriesParamView | None = None,
        keys: HistoriesArchivedGetArchivedHistoriesParamKeys | None = None,
        q: HistoriesArchivedGetArchivedHistoriesParamQ | None = None,
        qv: HistoriesArchivedGetArchivedHistoriesParamQv | None = None,
        offset: HistoriesArchivedGetArchivedHistoriesParamOffset | None = 0,
        limit: HistoriesArchivedGetArchivedHistoriesParamLimit | None = None,
        order: HistoriesArchivedGetArchivedHistoriesParamOrder | None = None,
        run_as: HistoriesArchivedGetArchivedHistoriesParamRunAs | None = None,
    ) -> list[AnonymousArrayItem145]:
        """
        Get a list of all archived histories for the current user.

        Get a list of all archived histories for the current user.  Archived histories are
        histories are not part of the active histories of the user but they can be accessed
        using this endpoint.

        Args:
            view (Optional[HistoriesArchivedGetArchivedHistoriesParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoriesArchivedGetArchivedHistoriesParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            q (Optional[HistoriesArchivedGetArchivedHistoriesParamQ])
                                     : Generally a property name to filter by followed by an
                                       (often optional) hyphen and operator string.
            qv (Optional[HistoriesArchivedGetArchivedHistoriesParamQv])
                                     : The value to filter by.
            offset (Optional[HistoriesArchivedGetArchivedHistoriesParamOffset])
                                     : Starts at the beginning skip the first ( offset - 1 )
                                       items and begin returning at the Nth item
            limit (Optional[HistoriesArchivedGetArchivedHistoriesParamLimit])
                                     : The maximum number of items to return.
            order (Optional[HistoriesArchivedGetArchivedHistoriesParamOrder])
                                     : String containing one of the valid ordering attributes
                                       followed (optionally) by '-asc' or '-dsc' for ascending
                                       and descending order respectively. Orders can be stacked
                                       as a comma-separated list of values.
            run-as (Optional[HistoriesArchivedGetArchivedHistoriesParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem145]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/archived"

        params: dict[str, Any] = {
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
                return cast(list[AnonymousArrayItem145], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_archived_get_archived_histories_2_2(
        self,
        view: HistoriesArchivedGetArchivedHistoriesParamView | None = None,
        keys: HistoriesArchivedGetArchivedHistoriesParamKeys | None = None,
        q: HistoriesArchivedGetArchivedHistoriesParamQ | None = None,
        qv: HistoriesArchivedGetArchivedHistoriesParamQv | None = None,
        offset: HistoriesArchivedGetArchivedHistoriesParamOffset | None = 0,
        limit: HistoriesArchivedGetArchivedHistoriesParamLimit | None = None,
        order: HistoriesArchivedGetArchivedHistoriesParamOrder | None = None,
        run_as: HistoriesArchivedGetArchivedHistoriesParamRunAs | None = None,
    ) -> list[AnonymousArrayItem145]:
        """
        Get a list of all archived histories for the current user.

        Get a list of all archived histories for the current user.  Archived histories are
        histories are not part of the active histories of the user but they can be accessed
        using this endpoint.

        Args:
            view (Optional[HistoriesArchivedGetArchivedHistoriesParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoriesArchivedGetArchivedHistoriesParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            q (Optional[HistoriesArchivedGetArchivedHistoriesParamQ])
                                     : Generally a property name to filter by followed by an
                                       (often optional) hyphen and operator string.
            qv (Optional[HistoriesArchivedGetArchivedHistoriesParamQv])
                                     : The value to filter by.
            offset (Optional[HistoriesArchivedGetArchivedHistoriesParamOffset])
                                     : Starts at the beginning skip the first ( offset - 1 )
                                       items and begin returning at the Nth item
            limit (Optional[HistoriesArchivedGetArchivedHistoriesParamLimit])
                                     : The maximum number of items to return.
            order (Optional[HistoriesArchivedGetArchivedHistoriesParamOrder])
                                     : String containing one of the valid ordering attributes
                                       followed (optionally) by '-asc' or '-dsc' for ascending
                                       and descending order respectively. Orders can be stacked
                                       as a comma-separated list of values.
            run-as (Optional[HistoriesArchivedGetArchivedHistoriesParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem145]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/archived"

        params: dict[str, Any] = {
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
                return cast(list[AnonymousArrayItem145], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_batch_delete_batch_delete_2_2(
        self,
        body: DeleteHistoriesPayload,
        purge: bool | None = False,
        view: HistoriesBatchDeleteBatchDeleteParamView | None = None,
        keys: HistoriesBatchDeleteBatchDeleteParamKeys | None = None,
        run_as: HistoriesBatchDeleteBatchDeleteParamRunAs | None = None,
    ) -> list[AnonymousArrayItem147]:
        """
        Marks several histories with the given IDs as deleted.

        Args:
            purge (Optional[bool])   :
            view (Optional[HistoriesBatchDeleteBatchDeleteParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoriesBatchDeleteBatchDeleteParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoriesBatchDeleteBatchDeleteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (DeleteHistoriesPayload)
                                     : Request body. (json)

        Returns:
            List[AnonymousArrayItem147]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/batch/delete"

        params: dict[str, Any] = {
            **({"purge": purge} if purge is not None else {}),
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: DeleteHistoriesPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem147], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_batch_delete_batch_delete_2_2(
        self,
        body: DeleteHistoriesPayload,
        purge: bool | None = False,
        view: HistoriesBatchDeleteBatchDeleteParamView | None = None,
        keys: HistoriesBatchDeleteBatchDeleteParamKeys | None = None,
        run_as: HistoriesBatchDeleteBatchDeleteParamRunAs | None = None,
    ) -> list[AnonymousArrayItem147]:
        """
        Marks several histories with the given IDs as deleted.

        Args:
            purge (Optional[bool])   :
            view (Optional[HistoriesBatchDeleteBatchDeleteParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoriesBatchDeleteBatchDeleteParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoriesBatchDeleteBatchDeleteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (DeleteHistoriesPayload)
                                     : Request body. (json)

        Returns:
            List[AnonymousArrayItem147]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/batch/delete"

        params: dict[str, Any] = {
            **({"purge": purge} if purge is not None else {}),
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: DeleteHistoriesPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem147], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_batch_undelete_batch_undelete_2_2(
        self,
        body: UndeleteHistoriesPayload,
        view: HistoriesBatchUndeleteBatchUndeleteParamView | None = None,
        keys: HistoriesBatchUndeleteBatchUndeleteParamKeys | None = None,
        run_as: HistoriesBatchUndeleteBatchUndeleteParamRunAs | None = None,
    ) -> list[AnonymousArrayItem149]:
        """
        Marks several histories with the given IDs as undeleted.

        Args:
            view (Optional[HistoriesBatchUndeleteBatchUndeleteParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoriesBatchUndeleteBatchUndeleteParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoriesBatchUndeleteBatchUndeleteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UndeleteHistoriesPayload)
                                     : Request body. (json)

        Returns:
            List[AnonymousArrayItem149]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/batch/undelete"

        params: dict[str, Any] = {
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: UndeleteHistoriesPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem149], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_batch_undelete_batch_undelete_2_2(
        self,
        body: UndeleteHistoriesPayload,
        view: HistoriesBatchUndeleteBatchUndeleteParamView | None = None,
        keys: HistoriesBatchUndeleteBatchUndeleteParamKeys | None = None,
        run_as: HistoriesBatchUndeleteBatchUndeleteParamRunAs | None = None,
    ) -> list[AnonymousArrayItem149]:
        """
        Marks several histories with the given IDs as undeleted.

        Args:
            view (Optional[HistoriesBatchUndeleteBatchUndeleteParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoriesBatchUndeleteBatchUndeleteParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoriesBatchUndeleteBatchUndeleteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UndeleteHistoriesPayload)
                                     : Request body. (json)

        Returns:
            List[AnonymousArrayItem149]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/batch/undelete"

        params: dict[str, Any] = {
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: UndeleteHistoriesPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem149], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_count_count_2_2(
        self,
        run_as: HistoriesCountCountParamRunAs | None = None,
    ) -> int:
        """
        Returns number of histories for the current user.

        Args:
            run-as (Optional[HistoriesCountCountParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            int: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/count"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(int, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_count_count_2_2(
        self,
        run_as: HistoriesCountCountParamRunAs | None = None,
    ) -> int:
        """
        Returns number of histories for the current user.

        Args:
            run-as (Optional[HistoriesCountCountParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            int: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/count"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(int, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_deleted_index_deleted_2_2(
        self,
        all_: HistoriesDeletedIndexDeletedParamAll | None = False,
        q: HistoriesDeletedIndexDeletedParamQ | None = None,
        qv: HistoriesDeletedIndexDeletedParamQv | None = None,
        offset: HistoriesDeletedIndexDeletedParamOffset | None = 0,
        limit: HistoriesDeletedIndexDeletedParamLimit | None = None,
        order: HistoriesDeletedIndexDeletedParamOrder | None = None,
        view: HistoriesDeletedIndexDeletedParamView | None = None,
        keys: HistoriesDeletedIndexDeletedParamKeys | None = None,
        run_as: HistoriesDeletedIndexDeletedParamRunAs | None = None,
    ) -> list[AnonymousArrayItem155]:
        """
        Returns deleted histories for the current user.

        Args:
            all (Optional[HistoriesDeletedIndexDeletedParamAll])
                                     : Whether all histories from other users in this Galaxy
                                       should be included. Only admins are allowed to query all
                                       histories.
            q (Optional[HistoriesDeletedIndexDeletedParamQ])
                                     : Generally a property name to filter by followed by an
                                       (often optional) hyphen and operator string.
            qv (Optional[HistoriesDeletedIndexDeletedParamQv])
                                     : The value to filter by.
            offset (Optional[HistoriesDeletedIndexDeletedParamOffset])
                                     : Starts at the beginning skip the first ( offset - 1 )
                                       items and begin returning at the Nth item
            limit (Optional[HistoriesDeletedIndexDeletedParamLimit])
                                     : The maximum number of items to return.
            order (Optional[HistoriesDeletedIndexDeletedParamOrder])
                                     : String containing one of the valid ordering attributes
                                       followed (optionally) by '-asc' or '-dsc' for ascending
                                       and descending order respectively. Orders can be stacked
                                       as a comma-separated list of values.
            view (Optional[HistoriesDeletedIndexDeletedParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoriesDeletedIndexDeletedParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoriesDeletedIndexDeletedParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem155]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/deleted"

        params: dict[str, Any] = {
            **({"all": all_} if all_ is not None else {}),
            **({"q": q} if q is not None else {}),
            **({"qv": qv} if qv is not None else {}),
            **({"offset": offset} if offset is not None else {}),
            **({"limit": limit} if limit is not None else {}),
            **({"order": order} if order is not None else {}),
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
                return cast(list[AnonymousArrayItem155], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_deleted_index_deleted_2_2(
        self,
        all_: HistoriesDeletedIndexDeletedParamAll | None = False,
        q: HistoriesDeletedIndexDeletedParamQ | None = None,
        qv: HistoriesDeletedIndexDeletedParamQv | None = None,
        offset: HistoriesDeletedIndexDeletedParamOffset | None = 0,
        limit: HistoriesDeletedIndexDeletedParamLimit | None = None,
        order: HistoriesDeletedIndexDeletedParamOrder | None = None,
        view: HistoriesDeletedIndexDeletedParamView | None = None,
        keys: HistoriesDeletedIndexDeletedParamKeys | None = None,
        run_as: HistoriesDeletedIndexDeletedParamRunAs | None = None,
    ) -> list[AnonymousArrayItem155]:
        """
        Returns deleted histories for the current user.

        Args:
            all (Optional[HistoriesDeletedIndexDeletedParamAll])
                                     : Whether all histories from other users in this Galaxy
                                       should be included. Only admins are allowed to query all
                                       histories.
            q (Optional[HistoriesDeletedIndexDeletedParamQ])
                                     : Generally a property name to filter by followed by an
                                       (often optional) hyphen and operator string.
            qv (Optional[HistoriesDeletedIndexDeletedParamQv])
                                     : The value to filter by.
            offset (Optional[HistoriesDeletedIndexDeletedParamOffset])
                                     : Starts at the beginning skip the first ( offset - 1 )
                                       items and begin returning at the Nth item
            limit (Optional[HistoriesDeletedIndexDeletedParamLimit])
                                     : The maximum number of items to return.
            order (Optional[HistoriesDeletedIndexDeletedParamOrder])
                                     : String containing one of the valid ordering attributes
                                       followed (optionally) by '-asc' or '-dsc' for ascending
                                       and descending order respectively. Orders can be stacked
                                       as a comma-separated list of values.
            view (Optional[HistoriesDeletedIndexDeletedParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoriesDeletedIndexDeletedParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoriesDeletedIndexDeletedParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem155]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/deleted"

        params: dict[str, Any] = {
            **({"all": all_} if all_ is not None else {}),
            **({"q": q} if q is not None else {}),
            **({"qv": qv} if qv is not None else {}),
            **({"offset": offset} if offset is not None else {}),
            **({"limit": limit} if limit is not None else {}),
            **({"order": order} if order is not None else {}),
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
                return cast(list[AnonymousArrayItem155], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_deleted_undelete_undelete_2_2(
        self,
        history_id: str,
        view: HistoriesDeletedUndeleteUndeleteParamView | None = None,
        keys: HistoriesDeletedUndeleteUndeleteParamKeys | None = None,
        run_as: HistoriesDeletedUndeleteUndeleteParamRunAs | None = None,
    ) -> HistoriesDeletedUndeleteUndelete200Response2:
        """
        Restores a deleted history with the given ID (that hasn't been purged).

        Args:
            history_id (str)         : The encoded database identifier of the History.
            view (Optional[HistoriesDeletedUndeleteUndeleteParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoriesDeletedUndeleteUndeleteParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoriesDeletedUndeleteUndeleteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            HistoriesDeletedUndeleteUndelete200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/deleted/{history_id}/undelete"

        params: dict[str, Any] = {
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(HistoriesDeletedUndeleteUndelete200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_deleted_undelete_undelete_2_2(
        self,
        history_id: str,
        view: HistoriesDeletedUndeleteUndeleteParamView | None = None,
        keys: HistoriesDeletedUndeleteUndeleteParamKeys | None = None,
        run_as: HistoriesDeletedUndeleteUndeleteParamRunAs | None = None,
    ) -> HistoriesDeletedUndeleteUndelete200Response2:
        """
        Restores a deleted history with the given ID (that hasn't been purged).

        Args:
            history_id (str)         : The encoded database identifier of the History.
            view (Optional[HistoriesDeletedUndeleteUndeleteParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoriesDeletedUndeleteUndeleteParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoriesDeletedUndeleteUndeleteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            HistoriesDeletedUndeleteUndelete200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/deleted/{history_id}/undelete"

        params: dict[str, Any] = {
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(HistoriesDeletedUndeleteUndelete200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_from_store_create_from_store_2_2(
        self,
        body: CreateHistoryFromStore,
        view: HistoriesFromStoreCreateFromStoreParamView | None = None,
        keys: HistoriesFromStoreCreateFromStoreParamKeys | None = None,
        run_as: HistoriesFromStoreCreateFromStoreParamRunAs | None = None,
    ) -> HistoriesFromStoreCreateFromStore200Response2:
        """
        Create histories from a model store.

        Args:
            view (Optional[HistoriesFromStoreCreateFromStoreParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoriesFromStoreCreateFromStoreParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoriesFromStoreCreateFromStoreParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateHistoryFromStore)
                                     : Request body. (json)

        Returns:
            HistoriesFromStoreCreateFromStore200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/from_store"

        params: dict[str, Any] = {
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateHistoryFromStore = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(HistoriesFromStoreCreateFromStore200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_from_store_create_from_store_2_2(
        self,
        body: CreateHistoryFromStore,
        view: HistoriesFromStoreCreateFromStoreParamView | None = None,
        keys: HistoriesFromStoreCreateFromStoreParamKeys | None = None,
        run_as: HistoriesFromStoreCreateFromStoreParamRunAs | None = None,
    ) -> HistoriesFromStoreCreateFromStore200Response2:
        """
        Create histories from a model store.

        Args:
            view (Optional[HistoriesFromStoreCreateFromStoreParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoriesFromStoreCreateFromStoreParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoriesFromStoreCreateFromStoreParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateHistoryFromStore)
                                     : Request body. (json)

        Returns:
            HistoriesFromStoreCreateFromStore200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/from_store"

        params: dict[str, Any] = {
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateHistoryFromStore = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(HistoriesFromStoreCreateFromStore200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_from_store_async_create_from_store_async_2_2(
        self,
        body: CreateHistoryFromStore,
        run_as: HistoriesFromStoreAsyncCreateFromStoreAsyncParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Launch a task to create histories from a model store.

        Args:
            run-as (Optional[HistoriesFromStoreAsyncCreateFromStoreAsyncParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateHistoryFromStore)
                                     : Request body. (json)

        Returns:
            AsyncTaskResultSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/from_store_async"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateHistoryFromStore = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(AsyncTaskResultSummary, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_from_store_async_create_from_store_async_2_2(
        self,
        body: CreateHistoryFromStore,
        run_as: HistoriesFromStoreAsyncCreateFromStoreAsyncParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Launch a task to create histories from a model store.

        Args:
            run-as (Optional[HistoriesFromStoreAsyncCreateFromStoreAsyncParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateHistoryFromStore)
                                     : Request body. (json)

        Returns:
            AsyncTaskResultSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/from_store_async"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateHistoryFromStore = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(AsyncTaskResultSummary, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_most_recently_used_show_recent_2_2(
        self,
        view: HistoriesMostRecentlyUsedShowRecentParamView | None = None,
        keys: HistoriesMostRecentlyUsedShowRecentParamKeys | None = None,
        run_as: HistoriesMostRecentlyUsedShowRecentParamRunAs | None = None,
    ) -> HistoriesMostRecentlyUsedShowRecent200Response2:
        """
        Returns the most recently used history of the user.

        Args:
            view (Optional[HistoriesMostRecentlyUsedShowRecentParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoriesMostRecentlyUsedShowRecentParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoriesMostRecentlyUsedShowRecentParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            HistoriesMostRecentlyUsedShowRecent200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/most_recently_used"

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
                return cast(HistoriesMostRecentlyUsedShowRecent200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_most_recently_used_show_recent_2_2(
        self,
        view: HistoriesMostRecentlyUsedShowRecentParamView | None = None,
        keys: HistoriesMostRecentlyUsedShowRecentParamKeys | None = None,
        run_as: HistoriesMostRecentlyUsedShowRecentParamRunAs | None = None,
    ) -> HistoriesMostRecentlyUsedShowRecent200Response2:
        """
        Returns the most recently used history of the user.

        Args:
            view (Optional[HistoriesMostRecentlyUsedShowRecentParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoriesMostRecentlyUsedShowRecentParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoriesMostRecentlyUsedShowRecentParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            HistoriesMostRecentlyUsedShowRecent200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/most_recently_used"

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
                return cast(HistoriesMostRecentlyUsedShowRecent200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_published_published_2_2(
        self,
        q: HistoriesPublishedPublishedParamQ | None = None,
        qv: HistoriesPublishedPublishedParamQv | None = None,
        offset: HistoriesPublishedPublishedParamOffset | None = 0,
        limit: HistoriesPublishedPublishedParamLimit | None = None,
        order: HistoriesPublishedPublishedParamOrder | None = None,
        view: HistoriesPublishedPublishedParamView | None = None,
        keys: HistoriesPublishedPublishedParamKeys | None = None,
        run_as: HistoriesPublishedPublishedParamRunAs | None = None,
    ) -> list[AnonymousArrayItem161]:
        """
        Return all histories that are published.

        Args:
            q (Optional[HistoriesPublishedPublishedParamQ])
                                     : Generally a property name to filter by followed by an
                                       (often optional) hyphen and operator string.
            qv (Optional[HistoriesPublishedPublishedParamQv])
                                     : The value to filter by.
            offset (Optional[HistoriesPublishedPublishedParamOffset])
                                     : Starts at the beginning skip the first ( offset - 1 )
                                       items and begin returning at the Nth item
            limit (Optional[HistoriesPublishedPublishedParamLimit])
                                     : The maximum number of items to return.
            order (Optional[HistoriesPublishedPublishedParamOrder])
                                     : String containing one of the valid ordering attributes
                                       followed (optionally) by '-asc' or '-dsc' for ascending
                                       and descending order respectively. Orders can be stacked
                                       as a comma-separated list of values.
            view (Optional[HistoriesPublishedPublishedParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoriesPublishedPublishedParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoriesPublishedPublishedParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem161]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/published"

        params: dict[str, Any] = {
            **({"q": q} if q is not None else {}),
            **({"qv": qv} if qv is not None else {}),
            **({"offset": offset} if offset is not None else {}),
            **({"limit": limit} if limit is not None else {}),
            **({"order": order} if order is not None else {}),
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
                return cast(list[AnonymousArrayItem161], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_published_published_2_2(
        self,
        q: HistoriesPublishedPublishedParamQ | None = None,
        qv: HistoriesPublishedPublishedParamQv | None = None,
        offset: HistoriesPublishedPublishedParamOffset | None = 0,
        limit: HistoriesPublishedPublishedParamLimit | None = None,
        order: HistoriesPublishedPublishedParamOrder | None = None,
        view: HistoriesPublishedPublishedParamView | None = None,
        keys: HistoriesPublishedPublishedParamKeys | None = None,
        run_as: HistoriesPublishedPublishedParamRunAs | None = None,
    ) -> list[AnonymousArrayItem161]:
        """
        Return all histories that are published.

        Args:
            q (Optional[HistoriesPublishedPublishedParamQ])
                                     : Generally a property name to filter by followed by an
                                       (often optional) hyphen and operator string.
            qv (Optional[HistoriesPublishedPublishedParamQv])
                                     : The value to filter by.
            offset (Optional[HistoriesPublishedPublishedParamOffset])
                                     : Starts at the beginning skip the first ( offset - 1 )
                                       items and begin returning at the Nth item
            limit (Optional[HistoriesPublishedPublishedParamLimit])
                                     : The maximum number of items to return.
            order (Optional[HistoriesPublishedPublishedParamOrder])
                                     : String containing one of the valid ordering attributes
                                       followed (optionally) by '-asc' or '-dsc' for ascending
                                       and descending order respectively. Orders can be stacked
                                       as a comma-separated list of values.
            view (Optional[HistoriesPublishedPublishedParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoriesPublishedPublishedParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoriesPublishedPublishedParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem161]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/published"

        params: dict[str, Any] = {
            **({"q": q} if q is not None else {}),
            **({"qv": qv} if qv is not None else {}),
            **({"offset": offset} if offset is not None else {}),
            **({"limit": limit} if limit is not None else {}),
            **({"order": order} if order is not None else {}),
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
                return cast(list[AnonymousArrayItem161], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_shared_with_me_shared_with_me_2_2(
        self,
        q: HistoriesSharedWithMeSharedWithMeParamQ | None = None,
        qv: HistoriesSharedWithMeSharedWithMeParamQv | None = None,
        offset: HistoriesSharedWithMeSharedWithMeParamOffset | None = 0,
        limit: HistoriesSharedWithMeSharedWithMeParamLimit | None = None,
        order: HistoriesSharedWithMeSharedWithMeParamOrder | None = None,
        view: HistoriesSharedWithMeSharedWithMeParamView | None = None,
        keys: HistoriesSharedWithMeSharedWithMeParamKeys | None = None,
        run_as: HistoriesSharedWithMeSharedWithMeParamRunAs | None = None,
    ) -> list[AnonymousArrayItem167]:
        """
        Return all histories that are shared with the current user.

        Args:
            q (Optional[HistoriesSharedWithMeSharedWithMeParamQ])
                                     : Generally a property name to filter by followed by an
                                       (often optional) hyphen and operator string.
            qv (Optional[HistoriesSharedWithMeSharedWithMeParamQv])
                                     : The value to filter by.
            offset (Optional[HistoriesSharedWithMeSharedWithMeParamOffset])
                                     : Starts at the beginning skip the first ( offset - 1 )
                                       items and begin returning at the Nth item
            limit (Optional[HistoriesSharedWithMeSharedWithMeParamLimit])
                                     : The maximum number of items to return.
            order (Optional[HistoriesSharedWithMeSharedWithMeParamOrder])
                                     : String containing one of the valid ordering attributes
                                       followed (optionally) by '-asc' or '-dsc' for ascending
                                       and descending order respectively. Orders can be stacked
                                       as a comma-separated list of values.
            view (Optional[HistoriesSharedWithMeSharedWithMeParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoriesSharedWithMeSharedWithMeParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoriesSharedWithMeSharedWithMeParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem167]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/shared_with_me"

        params: dict[str, Any] = {
            **({"q": q} if q is not None else {}),
            **({"qv": qv} if qv is not None else {}),
            **({"offset": offset} if offset is not None else {}),
            **({"limit": limit} if limit is not None else {}),
            **({"order": order} if order is not None else {}),
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
                return cast(list[AnonymousArrayItem167], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_shared_with_me_shared_with_me_2_2(
        self,
        q: HistoriesSharedWithMeSharedWithMeParamQ | None = None,
        qv: HistoriesSharedWithMeSharedWithMeParamQv | None = None,
        offset: HistoriesSharedWithMeSharedWithMeParamOffset | None = 0,
        limit: HistoriesSharedWithMeSharedWithMeParamLimit | None = None,
        order: HistoriesSharedWithMeSharedWithMeParamOrder | None = None,
        view: HistoriesSharedWithMeSharedWithMeParamView | None = None,
        keys: HistoriesSharedWithMeSharedWithMeParamKeys | None = None,
        run_as: HistoriesSharedWithMeSharedWithMeParamRunAs | None = None,
    ) -> list[AnonymousArrayItem167]:
        """
        Return all histories that are shared with the current user.

        Args:
            q (Optional[HistoriesSharedWithMeSharedWithMeParamQ])
                                     : Generally a property name to filter by followed by an
                                       (often optional) hyphen and operator string.
            qv (Optional[HistoriesSharedWithMeSharedWithMeParamQv])
                                     : The value to filter by.
            offset (Optional[HistoriesSharedWithMeSharedWithMeParamOffset])
                                     : Starts at the beginning skip the first ( offset - 1 )
                                       items and begin returning at the Nth item
            limit (Optional[HistoriesSharedWithMeSharedWithMeParamLimit])
                                     : The maximum number of items to return.
            order (Optional[HistoriesSharedWithMeSharedWithMeParamOrder])
                                     : String containing one of the valid ordering attributes
                                       followed (optionally) by '-asc' or '-dsc' for ascending
                                       and descending order respectively. Orders can be stacked
                                       as a comma-separated list of values.
            view (Optional[HistoriesSharedWithMeSharedWithMeParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoriesSharedWithMeSharedWithMeParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoriesSharedWithMeSharedWithMeParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem167]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/shared_with_me"

        params: dict[str, Any] = {
            **({"q": q} if q is not None else {}),
            **({"qv": qv} if qv is not None else {}),
            **({"offset": offset} if offset is not None else {}),
            **({"limit": limit} if limit is not None else {}),
            **({"order": order} if order is not None else {}),
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
                return cast(list[AnonymousArrayItem167], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_delete_2_2(
        self,
        history_id: str,
        purge: bool | None = False,
        view: HistoriesDeleteParamView | None = None,
        keys: HistoriesDeleteParamKeys | None = None,
        run_as: HistoriesDeleteParamRunAs | None = None,
        body: HistoriesDeleteRequestBody2 | None = None,
    ) -> HistoriesDelete200Response2:
        """
        Marks the history with the given ID as deleted.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            purge (Optional[bool])   :
            view (Optional[HistoriesDeleteParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoriesDeleteParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoriesDeleteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (Optional[HistoriesDeleteRequestBody2])
                                     : Request body. (json)

        Returns:
            HistoriesDelete200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}"

        params: dict[str, Any] = {
            **({"purge": purge} if purge is not None else {}),
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: HistoriesDeleteRequestBody2 | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("DELETE", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(HistoriesDelete200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_delete_2_2(
        self,
        history_id: str,
        purge: bool | None = False,
        view: HistoriesDeleteParamView | None = None,
        keys: HistoriesDeleteParamKeys | None = None,
        run_as: HistoriesDeleteParamRunAs | None = None,
        body: HistoriesDeleteRequestBody2 | None = None,
    ) -> HistoriesDelete200Response2:
        """
        Marks the history with the given ID as deleted.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            purge (Optional[bool])   :
            view (Optional[HistoriesDeleteParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoriesDeleteParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoriesDeleteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (Optional[HistoriesDeleteRequestBody2])
                                     : Request body. (json)

        Returns:
            HistoriesDelete200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}"

        params: dict[str, Any] = {
            **({"purge": purge} if purge is not None else {}),
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: HistoriesDeleteRequestBody2 | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("DELETE", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(HistoriesDelete200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_show_2_2(
        self,
        history_id: str,
        view: HistoriesShowParamView | None = None,
        keys: HistoriesShowParamKeys | None = None,
        run_as: HistoriesShowParamRunAs | None = None,
    ) -> HistoriesShow200Response2:
        """
        Returns the history with the given ID.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            view (Optional[HistoriesShowParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoriesShowParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoriesShowParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            HistoriesShow200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}"

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
                return cast(HistoriesShow200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_show_2_2(
        self,
        history_id: str,
        view: HistoriesShowParamView | None = None,
        keys: HistoriesShowParamKeys | None = None,
        run_as: HistoriesShowParamRunAs | None = None,
    ) -> HistoriesShow200Response2:
        """
        Returns the history with the given ID.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            view (Optional[HistoriesShowParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoriesShowParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoriesShowParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            HistoriesShow200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}"

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
                return cast(HistoriesShow200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_update_2_2(
        self,
        history_id: str,
        body: UpdateHistoryPayload,
        view: HistoriesUpdateParamView | None = None,
        keys: HistoriesUpdateParamKeys | None = None,
        run_as: HistoriesUpdateParamRunAs | None = None,
    ) -> HistoriesUpdate200Response2:
        """
        Updates the values for the history with the given ID.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            view (Optional[HistoriesUpdateParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoriesUpdateParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoriesUpdateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UpdateHistoryPayload)
                                     : Request body. (json)

        Returns:
            HistoriesUpdate200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}"

        params: dict[str, Any] = {
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: UpdateHistoryPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(HistoriesUpdate200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_update_2_2(
        self,
        history_id: str,
        body: UpdateHistoryPayload,
        view: HistoriesUpdateParamView | None = None,
        keys: HistoriesUpdateParamKeys | None = None,
        run_as: HistoriesUpdateParamRunAs | None = None,
    ) -> HistoriesUpdate200Response2:
        """
        Updates the values for the history with the given ID.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            view (Optional[HistoriesUpdateParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoriesUpdateParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoriesUpdateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UpdateHistoryPayload)
                                     : Request body. (json)

        Returns:
            HistoriesUpdate200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}"

        params: dict[str, Any] = {
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: UpdateHistoryPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(HistoriesUpdate200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_archive_archive_history_2_2(
        self,
        history_id: str,
        run_as: HistoriesArchiveArchiveHistoryParamRunAs | None = None,
        body: HistoriesArchiveArchiveHistoryRequestBody2 | None = None,
    ) -> HistoriesArchiveArchiveHistory200Response2:
        """
        Archive a history.

        Marks the given history as 'archived' and returns the history.  Archiving a history will
        remove it from the list of active histories of the user but it will still be accessible
        via the `/api/histories/{id}` or the `/api/histories/archived` endpoints.  Associating
        an export record:  - Optionally, an export record (containing information about a recent
        snapshot of the history) can be associated with the archived history by providing an
        `archive_export_id` in the payload. The export record must belong to the history and
        must be in the ready state. - When associating an export record, the history can be
        purged after it has been archived using the `purge_history` flag.  If the history is
        already archived, this endpoint will return a 409 Conflict error, indicating that the
        history is already archived. If the history was not purged after it was archived, you
        can restore it using the `/api/histories/{id}/archive/restore` endpoint.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            run-as (Optional[HistoriesArchiveArchiveHistoryParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (Optional[HistoriesArchiveArchiveHistoryRequestBody2])
                                     : Request body. (json)

        Returns:
            HistoriesArchiveArchiveHistory200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/archive"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: HistoriesArchiveArchiveHistoryRequestBody2 | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(HistoriesArchiveArchiveHistory200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_archive_archive_history_2_2(
        self,
        history_id: str,
        run_as: HistoriesArchiveArchiveHistoryParamRunAs | None = None,
        body: HistoriesArchiveArchiveHistoryRequestBody2 | None = None,
    ) -> HistoriesArchiveArchiveHistory200Response2:
        """
        Archive a history.

        Marks the given history as 'archived' and returns the history.  Archiving a history will
        remove it from the list of active histories of the user but it will still be accessible
        via the `/api/histories/{id}` or the `/api/histories/archived` endpoints.  Associating
        an export record:  - Optionally, an export record (containing information about a recent
        snapshot of the history) can be associated with the archived history by providing an
        `archive_export_id` in the payload. The export record must belong to the history and
        must be in the ready state. - When associating an export record, the history can be
        purged after it has been archived using the `purge_history` flag.  If the history is
        already archived, this endpoint will return a 409 Conflict error, indicating that the
        history is already archived. If the history was not purged after it was archived, you
        can restore it using the `/api/histories/{id}/archive/restore` endpoint.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            run-as (Optional[HistoriesArchiveArchiveHistoryParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (Optional[HistoriesArchiveArchiveHistoryRequestBody2])
                                     : Request body. (json)

        Returns:
            HistoriesArchiveArchiveHistory200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/archive"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: HistoriesArchiveArchiveHistoryRequestBody2 | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(HistoriesArchiveArchiveHistory200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_archive_restore_restore_archived_history_2_2(
        self,
        history_id: str,
        force: HistoriesArchiveRestoreRestoreArchivedHistoryParamForce | None = None,
        run_as: HistoriesArchiveRestoreRestoreArchivedHistoryParamRunAs | None = None,
    ) -> HistoriesArchiveRestoreRestoreArchivedHistory200Response2:
        """
        Restore an archived history.

        Restores an archived history and returns it.  Restoring an archived history will add it
        back to the list of active histories of the user (unless it was purged).  **Warning**:
        Please note that histories that are associated with an archive export might be purged
        after export, so un-archiving them will not restore the datasets that were in the
        history before it was archived. You will need to import back the archive export record
        to restore the history and its datasets as a new copy. See
        `/api/histories/from_store_async` for more information.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            force (Optional[HistoriesArchiveRestoreRestoreArchivedHistoryParamForce])
                                     : If true, the history will be un-archived even if it has
                                       an associated archive export record and was purged.
            run-as (Optional[HistoriesArchiveRestoreRestoreArchivedHistoryParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            HistoriesArchiveRestoreRestoreArchivedHistory200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/archive/restore"

        params: dict[str, Any] = {
            **({"force": force} if force is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(HistoriesArchiveRestoreRestoreArchivedHistory200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_archive_restore_restore_archived_history_2_2(
        self,
        history_id: str,
        force: HistoriesArchiveRestoreRestoreArchivedHistoryParamForce | None = None,
        run_as: HistoriesArchiveRestoreRestoreArchivedHistoryParamRunAs | None = None,
    ) -> HistoriesArchiveRestoreRestoreArchivedHistory200Response2:
        """
        Restore an archived history.

        Restores an archived history and returns it.  Restoring an archived history will add it
        back to the list of active histories of the user (unless it was purged).  **Warning**:
        Please note that histories that are associated with an archive export might be purged
        after export, so un-archiving them will not restore the datasets that were in the
        history before it was archived. You will need to import back the archive export record
        to restore the history and its datasets as a new copy. See
        `/api/histories/from_store_async` for more information.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            force (Optional[HistoriesArchiveRestoreRestoreArchivedHistoryParamForce])
                                     : If true, the history will be un-archived even if it has
                                       an associated archive export record and was purged.
            run-as (Optional[HistoriesArchiveRestoreRestoreArchivedHistoryParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            HistoriesArchiveRestoreRestoreArchivedHistory200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/archive/restore"

        params: dict[str, Any] = {
            **({"force": force} if force is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(HistoriesArchiveRestoreRestoreArchivedHistory200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_citations_citations_2_2(
        self,
        history_id: str,
        run_as: HistoriesCitationsCitationsParamRunAs | None = None,
    ) -> list[AnonymousArrayItem168]:
        """
        Return all the references for the tools used to produce the datasets in the history.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            run-as (Optional[HistoriesCitationsCitationsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem168]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/citations"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem168], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_citations_citations_2_2(
        self,
        history_id: str,
        run_as: HistoriesCitationsCitationsParamRunAs | None = None,
    ) -> list[AnonymousArrayItem168]:
        """
        Return all the references for the tools used to produce the datasets in the history.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            run-as (Optional[HistoriesCitationsCitationsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem168]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/citations"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem168], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def history_contents_index_2_2(
        self,
        history_id: str,
        v: HistoryContentsIndexParamV | None = None,
        details: HistoryContentsIndexParamDetails | None = None,
        ids: HistoryContentsIndexParamIds | None = None,
        types: HistoryContentsIndexParamTypes | None = None,
        deleted: HistoryContentsIndexParamDeleted | None = None,
        visible: HistoryContentsIndexParamVisible | None = None,
        shareable: HistoryContentsIndexParamShareable | None = None,
        view: HistoryContentsIndexParamView | None = None,
        keys: HistoryContentsIndexParamKeys | None = None,
        q: HistoryContentsIndexParamQ | None = None,
        qv: HistoryContentsIndexParamQv | None = None,
        offset: HistoryContentsIndexParamOffset | None = 0,
        limit: HistoryContentsIndexParamLimit | None = None,
        order: HistoryContentsIndexParamOrder | None = None,
        accept: str | None = "application/json",
        run_as: HistoryContentsIndexParamRunAs | None = None,
    ) -> HistoryContentsResult:
        """
        Returns the contents of the given history.

        Return a list of `HDA`/`HDCA` data for the history with the given ``ID``.  - The
        contents can be filtered and queried using the appropriate parameters. - The amount of
        information returned for each item can be customized.  **Note**: Anonymous users are
        allowed to get their current history contents.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            v (Optional[HistoryContentsIndexParamV])
                                     : Only `dev` value is allowed. Set it to use the latest
                                       version of this endpoint. **All parameters marked as
                                       `deprecated` will be ignored when this parameter is
                                       set.**
            details (Optional[HistoryContentsIndexParamDetails])
                                     : Legacy name for the `dataset_details` parameter.
            ids (Optional[HistoryContentsIndexParamIds])
                                     : A comma-separated list of encoded `HDA/HDCA` IDs. If this
                                       list is provided, only information about the specific
                                       datasets will be returned. Also, setting this value will
                                       return `all` details of the content item.
            types (Optional[HistoryContentsIndexParamTypes])
                                     : A list or comma-separated list of kinds of contents to
                                       return (currently just `dataset` and `dataset_collection`
                                       are available). If unset, all types will be returned.
            deleted (Optional[HistoryContentsIndexParamDeleted])
                                     : Whether to return deleted or undeleted datasets only.
                                       Leave unset for both.
            visible (Optional[HistoryContentsIndexParamVisible])
                                     : Whether to return visible or hidden datasets only. Leave
                                       unset for both.
            shareable (Optional[HistoryContentsIndexParamShareable])
                                     : Whether to return only shareable or not shareable
                                       datasets. Leave unset for both.
            view (Optional[HistoryContentsIndexParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoryContentsIndexParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            q (Optional[HistoryContentsIndexParamQ])
                                     : Generally a property name to filter by followed by an
                                       (often optional) hyphen and operator string.
            qv (Optional[HistoryContentsIndexParamQv])
                                     : The value to filter by.
            offset (Optional[HistoryContentsIndexParamOffset])
                                     : Starts at the beginning skip the first ( offset - 1 )
                                       items and begin returning at the Nth item
            limit (Optional[HistoryContentsIndexParamLimit])
                                     : The maximum number of items to return.
            order (Optional[HistoryContentsIndexParamOrder])
                                     : String containing one of the valid ordering attributes
                                       followed (optionally) by '-asc' or '-dsc' for ascending
                                       and descending order respectively. Orders can be stacked
                                       as a comma-separated list of values.
            accept (Optional[str])   : Accept header to determine the response format. Default
                                       is 'application/json'.
            run-as (Optional[HistoryContentsIndexParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            HistoryContentsResult: The contents of the history that match the query.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents"

        params: dict[str, Any] = {
            **({"v": v} if v is not None else {}),
            **({"details": details} if details is not None else {}),
            **({"ids": ids} if ids is not None else {}),
            **({"types": types} if types is not None else {}),
            **({"deleted": deleted} if deleted is not None else {}),
            **({"visible": visible} if visible is not None else {}),
            **({"shareable": shareable} if shareable is not None else {}),
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
            **({"q": q} if q is not None else {}),
            **({"qv": qv} if qv is not None else {}),
            **({"offset": offset} if offset is not None else {}),
            **({"limit": limit} if limit is not None else {}),
            **({"order": order} if order is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"accept": accept} if accept is not None else {}),
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(HistoryContentsResult, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def history_contents_index_2_2(
        self,
        history_id: str,
        v: HistoryContentsIndexParamV | None = None,
        details: HistoryContentsIndexParamDetails | None = None,
        ids: HistoryContentsIndexParamIds | None = None,
        types: HistoryContentsIndexParamTypes | None = None,
        deleted: HistoryContentsIndexParamDeleted | None = None,
        visible: HistoryContentsIndexParamVisible | None = None,
        shareable: HistoryContentsIndexParamShareable | None = None,
        view: HistoryContentsIndexParamView | None = None,
        keys: HistoryContentsIndexParamKeys | None = None,
        q: HistoryContentsIndexParamQ | None = None,
        qv: HistoryContentsIndexParamQv | None = None,
        offset: HistoryContentsIndexParamOffset | None = 0,
        limit: HistoryContentsIndexParamLimit | None = None,
        order: HistoryContentsIndexParamOrder | None = None,
        accept: str | None = "application/json",
        run_as: HistoryContentsIndexParamRunAs | None = None,
    ) -> HistoryContentsResult:
        """
        Returns the contents of the given history.

        Return a list of `HDA`/`HDCA` data for the history with the given ``ID``.  - The
        contents can be filtered and queried using the appropriate parameters. - The amount of
        information returned for each item can be customized.  **Note**: Anonymous users are
        allowed to get their current history contents.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            v (Optional[HistoryContentsIndexParamV])
                                     : Only `dev` value is allowed. Set it to use the latest
                                       version of this endpoint. **All parameters marked as
                                       `deprecated` will be ignored when this parameter is
                                       set.**
            details (Optional[HistoryContentsIndexParamDetails])
                                     : Legacy name for the `dataset_details` parameter.
            ids (Optional[HistoryContentsIndexParamIds])
                                     : A comma-separated list of encoded `HDA/HDCA` IDs. If this
                                       list is provided, only information about the specific
                                       datasets will be returned. Also, setting this value will
                                       return `all` details of the content item.
            types (Optional[HistoryContentsIndexParamTypes])
                                     : A list or comma-separated list of kinds of contents to
                                       return (currently just `dataset` and `dataset_collection`
                                       are available). If unset, all types will be returned.
            deleted (Optional[HistoryContentsIndexParamDeleted])
                                     : Whether to return deleted or undeleted datasets only.
                                       Leave unset for both.
            visible (Optional[HistoryContentsIndexParamVisible])
                                     : Whether to return visible or hidden datasets only. Leave
                                       unset for both.
            shareable (Optional[HistoryContentsIndexParamShareable])
                                     : Whether to return only shareable or not shareable
                                       datasets. Leave unset for both.
            view (Optional[HistoryContentsIndexParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoryContentsIndexParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            q (Optional[HistoryContentsIndexParamQ])
                                     : Generally a property name to filter by followed by an
                                       (often optional) hyphen and operator string.
            qv (Optional[HistoryContentsIndexParamQv])
                                     : The value to filter by.
            offset (Optional[HistoryContentsIndexParamOffset])
                                     : Starts at the beginning skip the first ( offset - 1 )
                                       items and begin returning at the Nth item
            limit (Optional[HistoryContentsIndexParamLimit])
                                     : The maximum number of items to return.
            order (Optional[HistoryContentsIndexParamOrder])
                                     : String containing one of the valid ordering attributes
                                       followed (optionally) by '-asc' or '-dsc' for ascending
                                       and descending order respectively. Orders can be stacked
                                       as a comma-separated list of values.
            accept (Optional[str])   : Accept header to determine the response format. Default
                                       is 'application/json'.
            run-as (Optional[HistoryContentsIndexParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            HistoryContentsResult: The contents of the history that match the query.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents"

        params: dict[str, Any] = {
            **({"v": v} if v is not None else {}),
            **({"details": details} if details is not None else {}),
            **({"ids": ids} if ids is not None else {}),
            **({"types": types} if types is not None else {}),
            **({"deleted": deleted} if deleted is not None else {}),
            **({"visible": visible} if visible is not None else {}),
            **({"shareable": shareable} if shareable is not None else {}),
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
            **({"q": q} if q is not None else {}),
            **({"qv": qv} if qv is not None else {}),
            **({"offset": offset} if offset is not None else {}),
            **({"limit": limit} if limit is not None else {}),
            **({"order": order} if order is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"accept": accept} if accept is not None else {}),
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(HistoryContentsResult, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def history_contents_create_2_2(
        self,
        history_id: str,
        body: CreateHistoryContentPayload,
        type_: HistoryContentsCreateParamType | None = None,
        view: HistoryContentsCreateParamView | None = None,
        keys: HistoryContentsCreateParamKeys | None = None,
        run_as: HistoryContentsCreateParamRunAs | None = None,
    ) -> HistoryContentsCreate200Response2:
        """
        Create a new `HDA` or `HDCA` in the given History.

        Create a new `HDA` or `HDCA` in the given History.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            type (Optional[HistoryContentsCreateParamType])
                                     : The type of the target history element.
            view (Optional[HistoryContentsCreateParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoryContentsCreateParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoryContentsCreateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateHistoryContentPayload)
                                     : Request body. (json)

        Returns:
            HistoryContentsCreate200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents"

        params: dict[str, Any] = {
            **({"type": type_} if type_ is not None else {}),
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateHistoryContentPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(HistoryContentsCreate200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def history_contents_create_2_2(
        self,
        history_id: str,
        body: CreateHistoryContentPayload,
        type_: HistoryContentsCreateParamType | None = None,
        view: HistoryContentsCreateParamView | None = None,
        keys: HistoryContentsCreateParamKeys | None = None,
        run_as: HistoryContentsCreateParamRunAs | None = None,
    ) -> HistoryContentsCreate200Response2:
        """
        Create a new `HDA` or `HDCA` in the given History.

        Create a new `HDA` or `HDCA` in the given History.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            type (Optional[HistoryContentsCreateParamType])
                                     : The type of the target history element.
            view (Optional[HistoryContentsCreateParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoryContentsCreateParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoryContentsCreateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateHistoryContentPayload)
                                     : Request body. (json)

        Returns:
            HistoryContentsCreate200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents"

        params: dict[str, Any] = {
            **({"type": type_} if type_ is not None else {}),
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateHistoryContentPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(HistoryContentsCreate200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_contents_update_batch_2_2(
        self,
        history_id: str,
        body: UpdateHistoryContentsBatchPayload,
        view: HistoriesContentsUpdateBatchParamView | None = None,
        keys: HistoriesContentsUpdateBatchParamKeys | None = None,
        run_as: HistoriesContentsUpdateBatchParamRunAs | None = None,
    ) -> HistoryContentsResult:
        """
        Batch update specific properties of a set items contained in the given History.

        Batch update specific properties of a set items contained in the given History.  If you
        provide an invalid/unknown property key the request will not fail, but no changes will
        be made to the items.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            view (Optional[HistoriesContentsUpdateBatchParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoriesContentsUpdateBatchParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoriesContentsUpdateBatchParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UpdateHistoryContentsBatchPayload)
                                     : Request body. (json)

        Returns:
            HistoryContentsResult: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents"

        params: dict[str, Any] = {
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: UpdateHistoryContentsBatchPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(HistoryContentsResult, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_contents_update_batch_2_2(
        self,
        history_id: str,
        body: UpdateHistoryContentsBatchPayload,
        view: HistoriesContentsUpdateBatchParamView | None = None,
        keys: HistoriesContentsUpdateBatchParamKeys | None = None,
        run_as: HistoriesContentsUpdateBatchParamRunAs | None = None,
    ) -> HistoryContentsResult:
        """
        Batch update specific properties of a set items contained in the given History.

        Batch update specific properties of a set items contained in the given History.  If you
        provide an invalid/unknown property key the request will not fail, but no changes will
        be made to the items.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            view (Optional[HistoriesContentsUpdateBatchParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoriesContentsUpdateBatchParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoriesContentsUpdateBatchParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UpdateHistoryContentsBatchPayload)
                                     : Request body. (json)

        Returns:
            HistoryContentsResult: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents"

        params: dict[str, Any] = {
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: UpdateHistoryContentsBatchPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(HistoryContentsResult, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def history_contents_archive_2_2(
        self,
        history_id: str,
        filename: HistoryContentsArchiveParamFilename | None = None,
        dry_run: HistoryContentsArchiveParamDryRun | None = True,
        q: HistoryContentsArchiveParamQ | None = None,
        qv: HistoryContentsArchiveParamQv | None = None,
        offset: HistoryContentsArchiveParamOffset | None = 0,
        limit: HistoryContentsArchiveParamLimit | None = None,
        order: HistoryContentsArchiveParamOrder | None = None,
        run_as: HistoryContentsArchiveParamRunAs | None = None,
    ) -> Any:
        """
        Build and return a compressed archive of the selected history contents.

        **Warning**: This API is unstable and may change without notice.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            filename (Optional[HistoryContentsArchiveParamFilename])
                                     : The name that the Archive will have (defaults to history
                                       name).
            dry_run (Optional[HistoryContentsArchiveParamDryRun])
                                     : Whether to return the archive and file paths only (as
                                       JSON) and not an actual archive file.
            q (Optional[HistoryContentsArchiveParamQ])
                                     : Generally a property name to filter by followed by an
                                       (often optional) hyphen and operator string.
            qv (Optional[HistoryContentsArchiveParamQv])
                                     : The value to filter by.
            offset (Optional[HistoryContentsArchiveParamOffset])
                                     : Starts at the beginning skip the first ( offset - 1 )
                                       items and begin returning at the Nth item
            limit (Optional[HistoryContentsArchiveParamLimit])
                                     : The maximum number of items to return.
            order (Optional[HistoryContentsArchiveParamOrder])
                                     : String containing one of the valid ordering attributes
                                       followed (optionally) by '-asc' or '-dsc' for ascending
                                       and descending order respectively. Orders can be stacked
                                       as a comma-separated list of values.
            run-as (Optional[HistoryContentsArchiveParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/archive"

        params: dict[str, Any] = {
            **({"filename": filename} if filename is not None else {}),
            **({"dry_run": dry_run} if dry_run is not None else {}),
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
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def history_contents_archive_2_2(
        self,
        history_id: str,
        filename: HistoryContentsArchiveParamFilename | None = None,
        dry_run: HistoryContentsArchiveParamDryRun | None = True,
        q: HistoryContentsArchiveParamQ | None = None,
        qv: HistoryContentsArchiveParamQv | None = None,
        offset: HistoryContentsArchiveParamOffset | None = 0,
        limit: HistoryContentsArchiveParamLimit | None = None,
        order: HistoryContentsArchiveParamOrder | None = None,
        run_as: HistoryContentsArchiveParamRunAs | None = None,
    ) -> Any:
        """
        Build and return a compressed archive of the selected history contents.

        **Warning**: This API is unstable and may change without notice.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            filename (Optional[HistoryContentsArchiveParamFilename])
                                     : The name that the Archive will have (defaults to history
                                       name).
            dry_run (Optional[HistoryContentsArchiveParamDryRun])
                                     : Whether to return the archive and file paths only (as
                                       JSON) and not an actual archive file.
            q (Optional[HistoryContentsArchiveParamQ])
                                     : Generally a property name to filter by followed by an
                                       (often optional) hyphen and operator string.
            qv (Optional[HistoryContentsArchiveParamQv])
                                     : The value to filter by.
            offset (Optional[HistoryContentsArchiveParamOffset])
                                     : Starts at the beginning skip the first ( offset - 1 )
                                       items and begin returning at the Nth item
            limit (Optional[HistoryContentsArchiveParamLimit])
                                     : The maximum number of items to return.
            order (Optional[HistoryContentsArchiveParamOrder])
                                     : String containing one of the valid ordering attributes
                                       followed (optionally) by '-asc' or '-dsc' for ascending
                                       and descending order respectively. Orders can be stacked
                                       as a comma-separated list of values.
            run-as (Optional[HistoryContentsArchiveParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/archive"

        params: dict[str, Any] = {
            **({"filename": filename} if filename is not None else {}),
            **({"dry_run": dry_run} if dry_run is not None else {}),
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
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def history_contents_archive_named_2_2(
        self,
        history_id: str,
        filename: str,
        format_: str,
        dry_run: HistoryContentsArchiveNamedParamDryRun | None = True,
        q: HistoryContentsArchiveNamedParamQ | None = None,
        qv: HistoryContentsArchiveNamedParamQv | None = None,
        offset: HistoryContentsArchiveNamedParamOffset | None = 0,
        limit: HistoryContentsArchiveNamedParamLimit | None = None,
        order: HistoryContentsArchiveNamedParamOrder | None = None,
        run_as: HistoryContentsArchiveNamedParamRunAs | None = None,
    ) -> Any:
        """
        Build and return a compressed archive of the selected history contents.

        **Warning**: This API is unstable and may change without notice.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            filename (str)           : The name that the Archive will have (defaults to history
                                       name).
            format (str)             : Output format of the archive.
            dry_run (Optional[HistoryContentsArchiveNamedParamDryRun])
                                     : Whether to return the archive and file paths only (as
                                       JSON) and not an actual archive file.
            q (Optional[HistoryContentsArchiveNamedParamQ])
                                     : Generally a property name to filter by followed by an
                                       (often optional) hyphen and operator string.
            qv (Optional[HistoryContentsArchiveNamedParamQv])
                                     : The value to filter by.
            offset (Optional[HistoryContentsArchiveNamedParamOffset])
                                     : Starts at the beginning skip the first ( offset - 1 )
                                       items and begin returning at the Nth item
            limit (Optional[HistoryContentsArchiveNamedParamLimit])
                                     : The maximum number of items to return.
            order (Optional[HistoryContentsArchiveNamedParamOrder])
                                     : String containing one of the valid ordering attributes
                                       followed (optionally) by '-asc' or '-dsc' for ascending
                                       and descending order respectively. Orders can be stacked
                                       as a comma-separated list of values.
            run-as (Optional[HistoryContentsArchiveNamedParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/archive/{filename}.{format_}"

        params: dict[str, Any] = {
            **({"dry_run": dry_run} if dry_run is not None else {}),
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
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def history_contents_archive_named_2_2(
        self,
        history_id: str,
        filename: str,
        format_: str,
        dry_run: HistoryContentsArchiveNamedParamDryRun | None = True,
        q: HistoryContentsArchiveNamedParamQ | None = None,
        qv: HistoryContentsArchiveNamedParamQv | None = None,
        offset: HistoryContentsArchiveNamedParamOffset | None = 0,
        limit: HistoryContentsArchiveNamedParamLimit | None = None,
        order: HistoryContentsArchiveNamedParamOrder | None = None,
        run_as: HistoryContentsArchiveNamedParamRunAs | None = None,
    ) -> Any:
        """
        Build and return a compressed archive of the selected history contents.

        **Warning**: This API is unstable and may change without notice.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            filename (str)           : The name that the Archive will have (defaults to history
                                       name).
            format (str)             : Output format of the archive.
            dry_run (Optional[HistoryContentsArchiveNamedParamDryRun])
                                     : Whether to return the archive and file paths only (as
                                       JSON) and not an actual archive file.
            q (Optional[HistoryContentsArchiveNamedParamQ])
                                     : Generally a property name to filter by followed by an
                                       (often optional) hyphen and operator string.
            qv (Optional[HistoryContentsArchiveNamedParamQv])
                                     : The value to filter by.
            offset (Optional[HistoryContentsArchiveNamedParamOffset])
                                     : Starts at the beginning skip the first ( offset - 1 )
                                       items and begin returning at the Nth item
            limit (Optional[HistoryContentsArchiveNamedParamLimit])
                                     : The maximum number of items to return.
            order (Optional[HistoryContentsArchiveNamedParamOrder])
                                     : String containing one of the valid ordering attributes
                                       followed (optionally) by '-asc' or '-dsc' for ascending
                                       and descending order respectively. Orders can be stacked
                                       as a comma-separated list of values.
            run-as (Optional[HistoryContentsArchiveNamedParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/archive/{filename}.{format_}"

        params: dict[str, Any] = {
            **({"dry_run": dry_run} if dry_run is not None else {}),
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
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_contents_bulk_bulk_operation_2_2(
        self,
        history_id: str,
        body: HistoryContentBulkOperationPayload,
        q: HistoriesContentsBulkBulkOperationParamQ | None = None,
        qv: HistoriesContentsBulkBulkOperationParamQv | None = None,
        run_as: HistoriesContentsBulkBulkOperationParamRunAs | None = None,
    ) -> HistoryContentBulkOperationResult:
        """
        Executes an operation on a set of items contained in the given History.

        Executes an operation on a set of items contained in the given History.  The items to be
        processed can be explicitly set or determined by a dynamic query.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            q (Optional[HistoriesContentsBulkBulkOperationParamQ])
                                     : Generally a property name to filter by followed by an
                                       (often optional) hyphen and operator string.
            qv (Optional[HistoriesContentsBulkBulkOperationParamQv])
                                     : The value to filter by.
            run-as (Optional[HistoriesContentsBulkBulkOperationParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (HistoryContentBulkOperationPayload)
                                     : Request body. (json)

        Returns:
            HistoryContentBulkOperationResult: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/bulk"

        params: dict[str, Any] = {
            **({"q": q} if q is not None else {}),
            **({"qv": qv} if qv is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: HistoryContentBulkOperationPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(HistoryContentBulkOperationResult, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_contents_bulk_bulk_operation_2_2(
        self,
        history_id: str,
        body: HistoryContentBulkOperationPayload,
        q: HistoriesContentsBulkBulkOperationParamQ | None = None,
        qv: HistoriesContentsBulkBulkOperationParamQv | None = None,
        run_as: HistoriesContentsBulkBulkOperationParamRunAs | None = None,
    ) -> HistoryContentBulkOperationResult:
        """
        Executes an operation on a set of items contained in the given History.

        Executes an operation on a set of items contained in the given History.  The items to be
        processed can be explicitly set or determined by a dynamic query.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            q (Optional[HistoriesContentsBulkBulkOperationParamQ])
                                     : Generally a property name to filter by followed by an
                                       (often optional) hyphen and operator string.
            qv (Optional[HistoriesContentsBulkBulkOperationParamQv])
                                     : The value to filter by.
            run-as (Optional[HistoriesContentsBulkBulkOperationParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (HistoryContentBulkOperationPayload)
                                     : Request body. (json)

        Returns:
            HistoryContentBulkOperationResult: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/bulk"

        params: dict[str, Any] = {
            **({"q": q} if q is not None else {}),
            **({"qv": qv} if qv is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: HistoryContentBulkOperationPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(HistoryContentBulkOperationResult, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def history_contents_download_collection_2_2(
        self,
        hdca_id: str,
        history_id: HistoryContentsDownloadCollectionParamHistoryId | None,
        run_as: HistoryContentsDownloadCollectionParamRunAs | None = None,
    ) -> None:
        """
        Download the content of a dataset collection as a `zip` archive.

        Download the content of a history dataset collection as a `zip` archive while
        maintaining approximate collection structure.

        Args:
            hdca_id (str)            : The ID of the `HDCA`.
            history_id (Optional[HistoryContentsDownloadCollectionParamHistoryId])
                                     : The encoded database identifier of the History.
            run-as (Optional[HistoryContentsDownloadCollectionParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/dataset_collections/{hdca_id}/download"

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

    async def history_contents_download_collection_2_2(
        self,
        hdca_id: str,
        history_id: HistoryContentsDownloadCollectionParamHistoryId | None,
        run_as: HistoryContentsDownloadCollectionParamRunAs | None = None,
    ) -> None:
        """
        Download the content of a dataset collection as a `zip` archive.

        Download the content of a history dataset collection as a `zip` archive while
        maintaining approximate collection structure.

        Args:
            hdca_id (str)            : The ID of the `HDCA`.
            history_id (Optional[HistoryContentsDownloadCollectionParamHistoryId])
                                     : The encoded database identifier of the History.
            run-as (Optional[HistoryContentsDownloadCollectionParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/dataset_collections/{hdca_id}/download"

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

    async def histories_contents_datasets_materialize_materialize_dataset_2_2(
        self,
        history_id: str,
        id_: str,
        run_as: HistoriesContentsDatasetsMaterializeMaterializeDatasetParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Materialize a deferred dataset into real, usable dataset.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            id (str)                 : The ID of the item (`HDA`/`HDCA`)
            run-as (Optional[HistoriesContentsDatasetsMaterializeMaterializeDatasetParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            AsyncTaskResultSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/datasets/{id_}/materialize"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(AsyncTaskResultSummary, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_contents_datasets_materialize_materialize_dataset_2_2(
        self,
        history_id: str,
        id_: str,
        run_as: HistoriesContentsDatasetsMaterializeMaterializeDatasetParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Materialize a deferred dataset into real, usable dataset.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            id (str)                 : The ID of the item (`HDA`/`HDCA`)
            run-as (Optional[HistoriesContentsDatasetsMaterializeMaterializeDatasetParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            AsyncTaskResultSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/datasets/{id_}/materialize"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(AsyncTaskResultSummary, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_contents_permissions_update_permissions_2_2(
        self,
        history_id: str,
        dataset_id: str,
        body: HistoriesContentsPermissionsUpdatePermissionsRequestBody2,
        run_as: HistoriesContentsPermissionsUpdatePermissionsParamRunAs | None = None,
    ) -> DatasetAssociationRoles:
        """
        Set permissions of the given history dataset to the given role ids.

        Set permissions of the given history dataset to the given role ids.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            dataset_id (str)         : The ID of the item (`HDA`/`HDCA`)
            run-as (Optional[HistoriesContentsPermissionsUpdatePermissionsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (HistoriesContentsPermissionsUpdatePermissionsRequestBody2)
                                     : Request body. (json)

        Returns:
            DatasetAssociationRoles: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/{dataset_id}/permissions"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: HistoriesContentsPermissionsUpdatePermissionsRequestBody2 = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DatasetAssociationRoles, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_contents_permissions_update_permissions_2_2(
        self,
        history_id: str,
        dataset_id: str,
        body: HistoriesContentsPermissionsUpdatePermissionsRequestBody2,
        run_as: HistoriesContentsPermissionsUpdatePermissionsParamRunAs | None = None,
    ) -> DatasetAssociationRoles:
        """
        Set permissions of the given history dataset to the given role ids.

        Set permissions of the given history dataset to the given role ids.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            dataset_id (str)         : The ID of the item (`HDA`/`HDCA`)
            run-as (Optional[HistoriesContentsPermissionsUpdatePermissionsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (HistoriesContentsPermissionsUpdatePermissionsRequestBody2)
                                     : Request body. (json)

        Returns:
            DatasetAssociationRoles: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/{dataset_id}/permissions"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: HistoriesContentsPermissionsUpdatePermissionsRequestBody2 = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(DatasetAssociationRoles, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def datasets_contents_display_display_history_content_2(
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

    async def datasets_contents_extra_files_extra_files_history_2(
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

    async def history_contents_get_metadata_file_2(
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

    async def histories_contents_tags_index(
        self,
        history_content_id: str,
        history_id: str,
        run_as: HistoriesContentsTagsIndexParamRunAs | None = None,
    ) -> ItemTagsListResponse:
        """
        Show tags based on history_content_id

        Args:
            history_content_id (str) :
            run-as (Optional[HistoriesContentsTagsIndexParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            history_id (str)         :

        Returns:
            ItemTagsListResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/{history_content_id}/tags"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ItemTagsListResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_contents_tags_delete(
        self,
        history_content_id: str,
        tag_name: str,
        history_id: str,
        run_as: HistoriesContentsTagsDeleteParamRunAs | None = None,
    ) -> bool:
        """
        Delete tag based on history_content_id

        Args:
            history_content_id (str) :
            tag_name (str)           :
            run-as (Optional[HistoriesContentsTagsDeleteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            history_id (str)         :

        Returns:
            bool: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/{history_content_id}/tags/{tag_name}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(bool, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_contents_tags_show(
        self,
        history_content_id: str,
        tag_name: str,
        history_id: str,
        run_as: HistoriesContentsTagsShowParamRunAs | None = None,
    ) -> ItemTagsResponse:
        """
        Show tag based on history_content_id

        Args:
            history_content_id (str) :
            tag_name (str)           :
            run-as (Optional[HistoriesContentsTagsShowParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            history_id (str)         :

        Returns:
            ItemTagsResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/{history_content_id}/tags/{tag_name}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ItemTagsResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_contents_tags_create(
        self,
        history_content_id: str,
        tag_name: str,
        history_id: str,
        run_as: HistoriesContentsTagsCreateParamRunAs | None = None,
        body: ItemTagsCreatePayload | None = None,
    ) -> ItemTagsResponse:
        """
        Create tag based on history_content_id

        Args:
            history_content_id (str) :
            tag_name (str)           :
            run-as (Optional[HistoriesContentsTagsCreateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            history_id (str)         :
            body (Optional[ItemTagsCreatePayload])
                                     : Request body. (json)

        Returns:
            ItemTagsResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/{history_content_id}/tags/{tag_name}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: ItemTagsCreatePayload | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ItemTagsResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_contents_tags_update(
        self,
        history_content_id: str,
        tag_name: str,
        history_id: str,
        body: ItemTagsCreatePayload,
        run_as: HistoriesContentsTagsUpdateParamRunAs | None = None,
    ) -> ItemTagsResponse:
        """
        Update tag based on history_content_id

        Args:
            history_content_id (str) :
            tag_name (str)           :
            run-as (Optional[HistoriesContentsTagsUpdateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            history_id (str)         :
            body (ItemTagsCreatePayload)
                                     : Request body. (json)

        Returns:
            ItemTagsResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/{history_content_id}/tags/{tag_name}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: ItemTagsCreatePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ItemTagsResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def history_contents_delete_legacy_2_2(
        self,
        history_id: str,
        id_: str,
        type_: HistoryContentType | None = None,
        purge: HistoryContentsDeleteLegacyParamPurge | None = False,
        recursive: HistoryContentsDeleteLegacyParamRecursive | None = False,
        stop_job: HistoryContentsDeleteLegacyParamStopJob | None = False,
        run_as: HistoryContentsDeleteLegacyParamRunAs | None = None,
        body: DeleteHistoryContentPayload | None = None,
    ) -> Any:
        """
        Delete the history dataset with the given ``ID``.

        Delete the history content with the given ``ID`` and query specified type (defaults to
        dataset).  **Note**: Currently does not stop any active jobs for which this dataset is
        an output.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            id (str)                 : The ID of the item (`HDA`/`HDCA`)
            type (Optional[HistoryContentType])
                                     : The type of the target history element.
            purge (Optional[HistoryContentsDeleteLegacyParamPurge])
                                     : Whether to remove from disk the target HDA or child HDAs
                                       of the target HDCA.
            recursive (Optional[HistoryContentsDeleteLegacyParamRecursive])
                                     : When deleting a dataset collection, whether to also
                                       delete containing datasets.
            stop_job (Optional[HistoryContentsDeleteLegacyParamStopJob])
                                     : Whether to stop the creating job if all outputs of the
                                       job have been deleted.
            run-as (Optional[HistoryContentsDeleteLegacyParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (Optional[DeleteHistoryContentPayload])
                                     : Request body. (json)

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/{id_}"

        params: dict[str, Any] = {
            **({"type": type_} if type_ is not None else {}),
            **({"purge": purge} if purge is not None else {}),
            **({"recursive": recursive} if recursive is not None else {}),
            **({"stop_job": stop_job} if stop_job is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: DeleteHistoryContentPayload | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("DELETE", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case 202:
                return None
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def history_contents_delete_legacy_2_2(
        self,
        history_id: str,
        id_: str,
        type_: HistoryContentType | None = None,
        purge: HistoryContentsDeleteLegacyParamPurge | None = False,
        recursive: HistoryContentsDeleteLegacyParamRecursive | None = False,
        stop_job: HistoryContentsDeleteLegacyParamStopJob | None = False,
        run_as: HistoryContentsDeleteLegacyParamRunAs | None = None,
        body: DeleteHistoryContentPayload | None = None,
    ) -> Any:
        """
        Delete the history dataset with the given ``ID``.

        Delete the history content with the given ``ID`` and query specified type (defaults to
        dataset).  **Note**: Currently does not stop any active jobs for which this dataset is
        an output.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            id (str)                 : The ID of the item (`HDA`/`HDCA`)
            type (Optional[HistoryContentType])
                                     : The type of the target history element.
            purge (Optional[HistoryContentsDeleteLegacyParamPurge])
                                     : Whether to remove from disk the target HDA or child HDAs
                                       of the target HDCA.
            recursive (Optional[HistoryContentsDeleteLegacyParamRecursive])
                                     : When deleting a dataset collection, whether to also
                                       delete containing datasets.
            stop_job (Optional[HistoryContentsDeleteLegacyParamStopJob])
                                     : Whether to stop the creating job if all outputs of the
                                       job have been deleted.
            run-as (Optional[HistoryContentsDeleteLegacyParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (Optional[DeleteHistoryContentPayload])
                                     : Request body. (json)

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/{id_}"

        params: dict[str, Any] = {
            **({"type": type_} if type_ is not None else {}),
            **({"purge": purge} if purge is not None else {}),
            **({"recursive": recursive} if recursive is not None else {}),
            **({"stop_job": stop_job} if stop_job is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: DeleteHistoryContentPayload | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("DELETE", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case 202:
                return None
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def history_contents_show_legacy_2_2(
        self,
        id_: str,
        history_id: str,
        type_: HistoryContentType | None = None,
        fuzzy_count: HistoryContentsShowLegacyParamFuzzyCount | None = None,
        view: HistoryContentsShowLegacyParamView | None = None,
        keys: HistoryContentsShowLegacyParamKeys | None = None,
        run_as: HistoryContentsShowLegacyParamRunAs | None = None,
    ) -> HistoryContentsShowLegacy200Response2:
        """
        Return detailed information about an HDA within a history.
        ``/api/histories/{history_id}/contents/{type}s/{id}`` should be used instead.

        Return detailed information about an `HDA` or `HDCA` within a history.  **Note**:
        Anonymous users are allowed to get their current history contents.

        Args:
            id (str)                 : The ID of the item (`HDA`/`HDCA`)
            history_id (str)         : The encoded database identifier of the History.
            type (Optional[HistoryContentType])
                                     : The type of the target history element.
            fuzzy_count (Optional[HistoryContentsShowLegacyParamFuzzyCount])
                                     : This value can be used to broadly restrict the magnitude
                                       of the number of elements returned via the API for large
                                       collections. The number of actual elements returned may
                                       be "a bit" more than this number or "a lot" less -
                                       varying on the depth of nesting, balance of nesting at
                                       each level, and size of target collection. The consumer
                                       of this API should not expect a stable number or pre-
                                       calculable number of elements to be produced given this
                                       parameter - the only promise is that this API will not
                                       respond with an order of magnitude more elements
                                       estimated with this value. The UI uses this parameter to
                                       fetch a "balanced" concept of the "start" of large
                                       collections at every depth of the collection.
            view (Optional[HistoryContentsShowLegacyParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoryContentsShowLegacyParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoryContentsShowLegacyParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            HistoryContentsShowLegacy200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/{id_}"

        params: dict[str, Any] = {
            **({"type": type_} if type_ is not None else {}),
            **({"fuzzy_count": fuzzy_count} if fuzzy_count is not None else {}),
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
                return cast(HistoryContentsShowLegacy200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def history_contents_show_legacy_2_2(
        self,
        id_: str,
        history_id: str,
        type_: HistoryContentType | None = None,
        fuzzy_count: HistoryContentsShowLegacyParamFuzzyCount | None = None,
        view: HistoryContentsShowLegacyParamView | None = None,
        keys: HistoryContentsShowLegacyParamKeys | None = None,
        run_as: HistoryContentsShowLegacyParamRunAs | None = None,
    ) -> HistoryContentsShowLegacy200Response2:
        """
        Return detailed information about an HDA within a history.
        ``/api/histories/{history_id}/contents/{type}s/{id}`` should be used instead.

        Return detailed information about an `HDA` or `HDCA` within a history.  **Note**:
        Anonymous users are allowed to get their current history contents.

        Args:
            id (str)                 : The ID of the item (`HDA`/`HDCA`)
            history_id (str)         : The encoded database identifier of the History.
            type (Optional[HistoryContentType])
                                     : The type of the target history element.
            fuzzy_count (Optional[HistoryContentsShowLegacyParamFuzzyCount])
                                     : This value can be used to broadly restrict the magnitude
                                       of the number of elements returned via the API for large
                                       collections. The number of actual elements returned may
                                       be "a bit" more than this number or "a lot" less -
                                       varying on the depth of nesting, balance of nesting at
                                       each level, and size of target collection. The consumer
                                       of this API should not expect a stable number or pre-
                                       calculable number of elements to be produced given this
                                       parameter - the only promise is that this API will not
                                       respond with an order of magnitude more elements
                                       estimated with this value. The UI uses this parameter to
                                       fetch a "balanced" concept of the "start" of large
                                       collections at every depth of the collection.
            view (Optional[HistoryContentsShowLegacyParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoryContentsShowLegacyParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoryContentsShowLegacyParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            HistoryContentsShowLegacy200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/{id_}"

        params: dict[str, Any] = {
            **({"type": type_} if type_ is not None else {}),
            **({"fuzzy_count": fuzzy_count} if fuzzy_count is not None else {}),
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
                return cast(HistoryContentsShowLegacy200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def history_contents_update_legacy_2_2(
        self,
        history_id: str,
        id_: str,
        body: UpdateHistoryContentsPayload,
        type_: HistoryContentType | None = None,
        view: HistoryContentsUpdateLegacyParamView | None = None,
        keys: HistoryContentsUpdateLegacyParamKeys | None = None,
        run_as: HistoryContentsUpdateLegacyParamRunAs | None = None,
    ) -> HistoryContentsUpdateLegacy200Response2:
        """
        Updates the values for the history content item with the given ``ID`` and query
        specified type. ``/api/histories/{history_id}/contents/{type}s/{id}`` should be used
        instead.

        Updates the values for the history content item with the given ``ID``.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            id (str)                 : The ID of the item (`HDA`/`HDCA`)
            type (Optional[HistoryContentType])
                                     : The type of the target history element.
            view (Optional[HistoryContentsUpdateLegacyParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoryContentsUpdateLegacyParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoryContentsUpdateLegacyParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UpdateHistoryContentsPayload)
                                     : Request body. (json)

        Returns:
            HistoryContentsUpdateLegacy200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/{id_}"

        params: dict[str, Any] = {
            **({"type": type_} if type_ is not None else {}),
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: UpdateHistoryContentsPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(HistoryContentsUpdateLegacy200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def history_contents_update_legacy_2_2(
        self,
        history_id: str,
        id_: str,
        body: UpdateHistoryContentsPayload,
        type_: HistoryContentType | None = None,
        view: HistoryContentsUpdateLegacyParamView | None = None,
        keys: HistoryContentsUpdateLegacyParamKeys | None = None,
        run_as: HistoryContentsUpdateLegacyParamRunAs | None = None,
    ) -> HistoryContentsUpdateLegacy200Response2:
        """
        Updates the values for the history content item with the given ``ID`` and query
        specified type. ``/api/histories/{history_id}/contents/{type}s/{id}`` should be used
        instead.

        Updates the values for the history content item with the given ``ID``.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            id (str)                 : The ID of the item (`HDA`/`HDCA`)
            type (Optional[HistoryContentType])
                                     : The type of the target history element.
            view (Optional[HistoryContentsUpdateLegacyParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoryContentsUpdateLegacyParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoryContentsUpdateLegacyParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UpdateHistoryContentsPayload)
                                     : Request body. (json)

        Returns:
            HistoryContentsUpdateLegacy200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/{id_}"

        params: dict[str, Any] = {
            **({"type": type_} if type_ is not None else {}),
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: UpdateHistoryContentsPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(HistoryContentsUpdateLegacy200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_contents_validate_validate_2_2(
        self,
        history_id: str,
        id_: str,
        run_as: HistoriesContentsValidateValidateParamRunAs | None = None,
    ) -> HistoriesContentsValidateValidate200Response2:
        """
        Validates the metadata associated with a dataset within a History.

        Validates the metadata associated with a dataset within a History.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            id (str)                 : The ID of the item (`HDA`/`HDCA`)
            run-as (Optional[HistoriesContentsValidateValidateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            HistoriesContentsValidateValidate200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/{id_}/validate"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(HistoriesContentsValidateValidate200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_contents_validate_validate_2_2(
        self,
        history_id: str,
        id_: str,
        run_as: HistoriesContentsValidateValidateParamRunAs | None = None,
    ) -> HistoriesContentsValidateValidate200Response2:
        """
        Validates the metadata associated with a dataset within a History.

        Validates the metadata associated with a dataset within a History.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            id (str)                 : The ID of the item (`HDA`/`HDCA`)
            run-as (Optional[HistoriesContentsValidateValidateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            HistoriesContentsValidateValidate200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/{id_}/validate"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(HistoriesContentsValidateValidate200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def history_contents_index_typed_2_2(
        self,
        history_id: str,
        type_: HistoryContentType,
        v: HistoryContentsIndexTypedParamV | None = None,
        details: HistoryContentsIndexTypedParamDetails | None = None,
        ids: HistoryContentsIndexTypedParamIds | None = None,
        types: HistoryContentsIndexTypedParamTypes | None = None,
        deleted: HistoryContentsIndexTypedParamDeleted | None = None,
        visible: HistoryContentsIndexTypedParamVisible | None = None,
        shareable: HistoryContentsIndexTypedParamShareable | None = None,
        view: HistoryContentsIndexTypedParamView | None = None,
        keys: HistoryContentsIndexTypedParamKeys | None = None,
        q: HistoryContentsIndexTypedParamQ | None = None,
        qv: HistoryContentsIndexTypedParamQv | None = None,
        offset: HistoryContentsIndexTypedParamOffset | None = 0,
        limit: HistoryContentsIndexTypedParamLimit | None = None,
        order: HistoryContentsIndexTypedParamOrder | None = None,
        accept: str | None = "application/json",
        run_as: HistoryContentsIndexTypedParamRunAs | None = None,
    ) -> HistoryContentsResult:
        """
        Returns the contents of the given history filtered by type.

        Return a list of either `HDA`/`HDCA` data for the history with the given ``ID``.  - The
        contents can be filtered and queried using the appropriate parameters. - The amount of
        information returned for each item can be customized.  **Note**: Anonymous users are
        allowed to get their current history contents.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            type (HistoryContentType): The type of the target history element.
            v (Optional[HistoryContentsIndexTypedParamV])
                                     : Only `dev` value is allowed. Set it to use the latest
                                       version of this endpoint. **All parameters marked as
                                       `deprecated` will be ignored when this parameter is
                                       set.**
            details (Optional[HistoryContentsIndexTypedParamDetails])
                                     : Legacy name for the `dataset_details` parameter.
            ids (Optional[HistoryContentsIndexTypedParamIds])
                                     : A comma-separated list of encoded `HDA/HDCA` IDs. If this
                                       list is provided, only information about the specific
                                       datasets will be returned. Also, setting this value will
                                       return `all` details of the content item.
            types (Optional[HistoryContentsIndexTypedParamTypes])
                                     : A list or comma-separated list of kinds of contents to
                                       return (currently just `dataset` and `dataset_collection`
                                       are available). If unset, all types will be returned.
            deleted (Optional[HistoryContentsIndexTypedParamDeleted])
                                     : Whether to return deleted or undeleted datasets only.
                                       Leave unset for both.
            visible (Optional[HistoryContentsIndexTypedParamVisible])
                                     : Whether to return visible or hidden datasets only. Leave
                                       unset for both.
            shareable (Optional[HistoryContentsIndexTypedParamShareable])
                                     : Whether to return only shareable or not shareable
                                       datasets. Leave unset for both.
            view (Optional[HistoryContentsIndexTypedParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoryContentsIndexTypedParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            q (Optional[HistoryContentsIndexTypedParamQ])
                                     : Generally a property name to filter by followed by an
                                       (often optional) hyphen and operator string.
            qv (Optional[HistoryContentsIndexTypedParamQv])
                                     : The value to filter by.
            offset (Optional[HistoryContentsIndexTypedParamOffset])
                                     : Starts at the beginning skip the first ( offset - 1 )
                                       items and begin returning at the Nth item
            limit (Optional[HistoryContentsIndexTypedParamLimit])
                                     : The maximum number of items to return.
            order (Optional[HistoryContentsIndexTypedParamOrder])
                                     : String containing one of the valid ordering attributes
                                       followed (optionally) by '-asc' or '-dsc' for ascending
                                       and descending order respectively. Orders can be stacked
                                       as a comma-separated list of values.
            accept (Optional[str])   : Accept header to determine the response format. Default
                                       is 'application/json'.
            run-as (Optional[HistoryContentsIndexTypedParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            HistoryContentsResult: The contents of the history that match the query.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/{type_}s"

        params: dict[str, Any] = {
            **({"v": v} if v is not None else {}),
            **({"details": details} if details is not None else {}),
            **({"ids": ids} if ids is not None else {}),
            **({"types": types} if types is not None else {}),
            **({"deleted": deleted} if deleted is not None else {}),
            **({"visible": visible} if visible is not None else {}),
            **({"shareable": shareable} if shareable is not None else {}),
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
            **({"q": q} if q is not None else {}),
            **({"qv": qv} if qv is not None else {}),
            **({"offset": offset} if offset is not None else {}),
            **({"limit": limit} if limit is not None else {}),
            **({"order": order} if order is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"accept": accept} if accept is not None else {}),
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(HistoryContentsResult, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def history_contents_index_typed_2_2(
        self,
        history_id: str,
        type_: HistoryContentType,
        v: HistoryContentsIndexTypedParamV | None = None,
        details: HistoryContentsIndexTypedParamDetails | None = None,
        ids: HistoryContentsIndexTypedParamIds | None = None,
        types: HistoryContentsIndexTypedParamTypes | None = None,
        deleted: HistoryContentsIndexTypedParamDeleted | None = None,
        visible: HistoryContentsIndexTypedParamVisible | None = None,
        shareable: HistoryContentsIndexTypedParamShareable | None = None,
        view: HistoryContentsIndexTypedParamView | None = None,
        keys: HistoryContentsIndexTypedParamKeys | None = None,
        q: HistoryContentsIndexTypedParamQ | None = None,
        qv: HistoryContentsIndexTypedParamQv | None = None,
        offset: HistoryContentsIndexTypedParamOffset | None = 0,
        limit: HistoryContentsIndexTypedParamLimit | None = None,
        order: HistoryContentsIndexTypedParamOrder | None = None,
        accept: str | None = "application/json",
        run_as: HistoryContentsIndexTypedParamRunAs | None = None,
    ) -> HistoryContentsResult:
        """
        Returns the contents of the given history filtered by type.

        Return a list of either `HDA`/`HDCA` data for the history with the given ``ID``.  - The
        contents can be filtered and queried using the appropriate parameters. - The amount of
        information returned for each item can be customized.  **Note**: Anonymous users are
        allowed to get their current history contents.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            type (HistoryContentType): The type of the target history element.
            v (Optional[HistoryContentsIndexTypedParamV])
                                     : Only `dev` value is allowed. Set it to use the latest
                                       version of this endpoint. **All parameters marked as
                                       `deprecated` will be ignored when this parameter is
                                       set.**
            details (Optional[HistoryContentsIndexTypedParamDetails])
                                     : Legacy name for the `dataset_details` parameter.
            ids (Optional[HistoryContentsIndexTypedParamIds])
                                     : A comma-separated list of encoded `HDA/HDCA` IDs. If this
                                       list is provided, only information about the specific
                                       datasets will be returned. Also, setting this value will
                                       return `all` details of the content item.
            types (Optional[HistoryContentsIndexTypedParamTypes])
                                     : A list or comma-separated list of kinds of contents to
                                       return (currently just `dataset` and `dataset_collection`
                                       are available). If unset, all types will be returned.
            deleted (Optional[HistoryContentsIndexTypedParamDeleted])
                                     : Whether to return deleted or undeleted datasets only.
                                       Leave unset for both.
            visible (Optional[HistoryContentsIndexTypedParamVisible])
                                     : Whether to return visible or hidden datasets only. Leave
                                       unset for both.
            shareable (Optional[HistoryContentsIndexTypedParamShareable])
                                     : Whether to return only shareable or not shareable
                                       datasets. Leave unset for both.
            view (Optional[HistoryContentsIndexTypedParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoryContentsIndexTypedParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            q (Optional[HistoryContentsIndexTypedParamQ])
                                     : Generally a property name to filter by followed by an
                                       (often optional) hyphen and operator string.
            qv (Optional[HistoryContentsIndexTypedParamQv])
                                     : The value to filter by.
            offset (Optional[HistoryContentsIndexTypedParamOffset])
                                     : Starts at the beginning skip the first ( offset - 1 )
                                       items and begin returning at the Nth item
            limit (Optional[HistoryContentsIndexTypedParamLimit])
                                     : The maximum number of items to return.
            order (Optional[HistoryContentsIndexTypedParamOrder])
                                     : String containing one of the valid ordering attributes
                                       followed (optionally) by '-asc' or '-dsc' for ascending
                                       and descending order respectively. Orders can be stacked
                                       as a comma-separated list of values.
            accept (Optional[str])   : Accept header to determine the response format. Default
                                       is 'application/json'.
            run-as (Optional[HistoryContentsIndexTypedParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            HistoryContentsResult: The contents of the history that match the query.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/{type_}s"

        params: dict[str, Any] = {
            **({"v": v} if v is not None else {}),
            **({"details": details} if details is not None else {}),
            **({"ids": ids} if ids is not None else {}),
            **({"types": types} if types is not None else {}),
            **({"deleted": deleted} if deleted is not None else {}),
            **({"visible": visible} if visible is not None else {}),
            **({"shareable": shareable} if shareable is not None else {}),
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
            **({"q": q} if q is not None else {}),
            **({"qv": qv} if qv is not None else {}),
            **({"offset": offset} if offset is not None else {}),
            **({"limit": limit} if limit is not None else {}),
            **({"order": order} if order is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"accept": accept} if accept is not None else {}),
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(HistoryContentsResult, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def history_contents_create_typed_2_2(
        self,
        history_id: str,
        type_: HistoryContentType,
        body: CreateHistoryContentPayload,
        view: HistoryContentsCreateTypedParamView | None = None,
        keys: HistoryContentsCreateTypedParamKeys | None = None,
        run_as: HistoryContentsCreateTypedParamRunAs | None = None,
    ) -> HistoryContentsCreateTyped200Response2:
        """
        Create a new `HDA` or `HDCA` in the given History.

        Create a new `HDA` or `HDCA` in the given History.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            type (HistoryContentType): The type of the target history element.
            view (Optional[HistoryContentsCreateTypedParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoryContentsCreateTypedParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoryContentsCreateTypedParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateHistoryContentPayload)
                                     : Request body. (json)

        Returns:
            HistoryContentsCreateTyped200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/{type_}s"

        params: dict[str, Any] = {
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateHistoryContentPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(HistoryContentsCreateTyped200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def history_contents_create_typed_2_2(
        self,
        history_id: str,
        type_: HistoryContentType,
        body: CreateHistoryContentPayload,
        view: HistoryContentsCreateTypedParamView | None = None,
        keys: HistoryContentsCreateTypedParamKeys | None = None,
        run_as: HistoryContentsCreateTypedParamRunAs | None = None,
    ) -> HistoryContentsCreateTyped200Response2:
        """
        Create a new `HDA` or `HDCA` in the given History.

        Create a new `HDA` or `HDCA` in the given History.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            type (HistoryContentType): The type of the target history element.
            view (Optional[HistoryContentsCreateTypedParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoryContentsCreateTypedParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoryContentsCreateTypedParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateHistoryContentPayload)
                                     : Request body. (json)

        Returns:
            HistoryContentsCreateTyped200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/{type_}s"

        params: dict[str, Any] = {
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateHistoryContentPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(HistoryContentsCreateTyped200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def history_contents_delete_typed_2_2(
        self,
        history_id: str,
        id_: str,
        type_: HistoryContentType,
        purge: HistoryContentsDeleteTypedParamPurge | None = False,
        recursive: HistoryContentsDeleteTypedParamRecursive | None = False,
        stop_job: HistoryContentsDeleteTypedParamStopJob | None = False,
        run_as: HistoryContentsDeleteTypedParamRunAs | None = None,
        body: DeleteHistoryContentPayload | None = None,
    ) -> Any:
        """
        Delete the history content with the given ``ID`` and path specified type.

        Delete the history content with the given ``ID`` and path specified type.  **Note**:
        Currently does not stop any active jobs for which this dataset is an output.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            id (str)                 : The ID of the item (`HDA`/`HDCA`)
            type (HistoryContentType): The type of the target history element.
            purge (Optional[HistoryContentsDeleteTypedParamPurge])
                                     : Whether to remove from disk the target HDA or child HDAs
                                       of the target HDCA.
            recursive (Optional[HistoryContentsDeleteTypedParamRecursive])
                                     : When deleting a dataset collection, whether to also
                                       delete containing datasets.
            stop_job (Optional[HistoryContentsDeleteTypedParamStopJob])
                                     : Whether to stop the creating job if all outputs of the
                                       job have been deleted.
            run-as (Optional[HistoryContentsDeleteTypedParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (Optional[DeleteHistoryContentPayload])
                                     : Request body. (json)

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/{type_}s/{id_}"

        params: dict[str, Any] = {
            **({"purge": purge} if purge is not None else {}),
            **({"recursive": recursive} if recursive is not None else {}),
            **({"stop_job": stop_job} if stop_job is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: DeleteHistoryContentPayload | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("DELETE", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case 202:
                return None
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def history_contents_delete_typed_2_2(
        self,
        history_id: str,
        id_: str,
        type_: HistoryContentType,
        purge: HistoryContentsDeleteTypedParamPurge | None = False,
        recursive: HistoryContentsDeleteTypedParamRecursive | None = False,
        stop_job: HistoryContentsDeleteTypedParamStopJob | None = False,
        run_as: HistoryContentsDeleteTypedParamRunAs | None = None,
        body: DeleteHistoryContentPayload | None = None,
    ) -> Any:
        """
        Delete the history content with the given ``ID`` and path specified type.

        Delete the history content with the given ``ID`` and path specified type.  **Note**:
        Currently does not stop any active jobs for which this dataset is an output.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            id (str)                 : The ID of the item (`HDA`/`HDCA`)
            type (HistoryContentType): The type of the target history element.
            purge (Optional[HistoryContentsDeleteTypedParamPurge])
                                     : Whether to remove from disk the target HDA or child HDAs
                                       of the target HDCA.
            recursive (Optional[HistoryContentsDeleteTypedParamRecursive])
                                     : When deleting a dataset collection, whether to also
                                       delete containing datasets.
            stop_job (Optional[HistoryContentsDeleteTypedParamStopJob])
                                     : Whether to stop the creating job if all outputs of the
                                       job have been deleted.
            run-as (Optional[HistoryContentsDeleteTypedParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (Optional[DeleteHistoryContentPayload])
                                     : Request body. (json)

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/{type_}s/{id_}"

        params: dict[str, Any] = {
            **({"purge": purge} if purge is not None else {}),
            **({"recursive": recursive} if recursive is not None else {}),
            **({"stop_job": stop_job} if stop_job is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: DeleteHistoryContentPayload | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("DELETE", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case 202:
                return None
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def history_contents_show_2_2(
        self,
        id_: str,
        history_id: str,
        type_: HistoryContentType,
        fuzzy_count: HistoryContentsShowParamFuzzyCount | None = None,
        view: HistoryContentsShowParamView | None = None,
        keys: HistoryContentsShowParamKeys | None = None,
        run_as: HistoryContentsShowParamRunAs | None = None,
    ) -> HistoryContentsShow200Response2:
        """
        Return detailed information about a specific HDA or HDCA with the given `ID` within a
        history.

        Return detailed information about an `HDA` or `HDCA` within a history.  **Note**:
        Anonymous users are allowed to get their current history contents.

        Args:
            id (str)                 : The ID of the item (`HDA`/`HDCA`)
            history_id (str)         : The encoded database identifier of the History.
            type (HistoryContentType): The type of the target history element.
            fuzzy_count (Optional[HistoryContentsShowParamFuzzyCount])
                                     : This value can be used to broadly restrict the magnitude
                                       of the number of elements returned via the API for large
                                       collections. The number of actual elements returned may
                                       be "a bit" more than this number or "a lot" less -
                                       varying on the depth of nesting, balance of nesting at
                                       each level, and size of target collection. The consumer
                                       of this API should not expect a stable number or pre-
                                       calculable number of elements to be produced given this
                                       parameter - the only promise is that this API will not
                                       respond with an order of magnitude more elements
                                       estimated with this value. The UI uses this parameter to
                                       fetch a "balanced" concept of the "start" of large
                                       collections at every depth of the collection.
            view (Optional[HistoryContentsShowParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoryContentsShowParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoryContentsShowParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            HistoryContentsShow200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/{type_}s/{id_}"

        params: dict[str, Any] = {
            **({"fuzzy_count": fuzzy_count} if fuzzy_count is not None else {}),
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
                return cast(HistoryContentsShow200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def history_contents_show_2_2(
        self,
        id_: str,
        history_id: str,
        type_: HistoryContentType,
        fuzzy_count: HistoryContentsShowParamFuzzyCount | None = None,
        view: HistoryContentsShowParamView | None = None,
        keys: HistoryContentsShowParamKeys | None = None,
        run_as: HistoryContentsShowParamRunAs | None = None,
    ) -> HistoryContentsShow200Response2:
        """
        Return detailed information about a specific HDA or HDCA with the given `ID` within a
        history.

        Return detailed information about an `HDA` or `HDCA` within a history.  **Note**:
        Anonymous users are allowed to get their current history contents.

        Args:
            id (str)                 : The ID of the item (`HDA`/`HDCA`)
            history_id (str)         : The encoded database identifier of the History.
            type (HistoryContentType): The type of the target history element.
            fuzzy_count (Optional[HistoryContentsShowParamFuzzyCount])
                                     : This value can be used to broadly restrict the magnitude
                                       of the number of elements returned via the API for large
                                       collections. The number of actual elements returned may
                                       be "a bit" more than this number or "a lot" less -
                                       varying on the depth of nesting, balance of nesting at
                                       each level, and size of target collection. The consumer
                                       of this API should not expect a stable number or pre-
                                       calculable number of elements to be produced given this
                                       parameter - the only promise is that this API will not
                                       respond with an order of magnitude more elements
                                       estimated with this value. The UI uses this parameter to
                                       fetch a "balanced" concept of the "start" of large
                                       collections at every depth of the collection.
            view (Optional[HistoryContentsShowParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoryContentsShowParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoryContentsShowParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            HistoryContentsShow200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/{type_}s/{id_}"

        params: dict[str, Any] = {
            **({"fuzzy_count": fuzzy_count} if fuzzy_count is not None else {}),
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
                return cast(HistoryContentsShow200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def history_contents_update_typed_2_2(
        self,
        history_id: str,
        id_: str,
        type_: HistoryContentType,
        body: UpdateHistoryContentsPayload,
        view: HistoryContentsUpdateTypedParamView | None = None,
        keys: HistoryContentsUpdateTypedParamKeys | None = None,
        run_as: HistoryContentsUpdateTypedParamRunAs | None = None,
    ) -> HistoryContentsUpdateTyped200Response2:
        """
        Updates the values for the history content item with the given ``ID`` and path specified
        type.

        Updates the values for the history content item with the given ``ID``.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            id (str)                 : The ID of the item (`HDA`/`HDCA`)
            type (HistoryContentType): The type of the target history element.
            view (Optional[HistoryContentsUpdateTypedParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoryContentsUpdateTypedParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoryContentsUpdateTypedParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UpdateHistoryContentsPayload)
                                     : Request body. (json)

        Returns:
            HistoryContentsUpdateTyped200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/{type_}s/{id_}"

        params: dict[str, Any] = {
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: UpdateHistoryContentsPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(HistoryContentsUpdateTyped200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def history_contents_update_typed_2_2(
        self,
        history_id: str,
        id_: str,
        type_: HistoryContentType,
        body: UpdateHistoryContentsPayload,
        view: HistoryContentsUpdateTypedParamView | None = None,
        keys: HistoryContentsUpdateTypedParamKeys | None = None,
        run_as: HistoryContentsUpdateTypedParamRunAs | None = None,
    ) -> HistoryContentsUpdateTyped200Response2:
        """
        Updates the values for the history content item with the given ``ID`` and path specified
        type.

        Updates the values for the history content item with the given ``ID``.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            id (str)                 : The ID of the item (`HDA`/`HDCA`)
            type (HistoryContentType): The type of the target history element.
            view (Optional[HistoryContentsUpdateTypedParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoryContentsUpdateTypedParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoryContentsUpdateTypedParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UpdateHistoryContentsPayload)
                                     : Request body. (json)

        Returns:
            HistoryContentsUpdateTyped200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/{type_}s/{id_}"

        params: dict[str, Any] = {
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: UpdateHistoryContentsPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(HistoryContentsUpdateTyped200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_contents_jobs_summary_show_jobs_summary_2_2(
        self,
        history_id: str,
        id_: str,
        type_: HistoryContentType,
        run_as: HistoriesContentsJobsSummaryShowJobsSummaryParamRunAs | None = None,
    ) -> HistoriesContentsJobsSummaryShowJobsSummary200Response2:
        """
        Return detailed information about an `HDA` or `HDCAs` jobs.

        Return detailed information about an `HDA` or `HDCAs` jobs.  **Warning**: We allow
        anyone to fetch job state information about any object they can guess an encoded ID for
        - it isn't considered protected data. This keeps polling IDs as part of state
        calculation for large histories and collections as efficient as possible.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            id (str)                 : The ID of the item (`HDA`/`HDCA`)
            type (HistoryContentType): The type of the target history element.
            run-as (Optional[HistoriesContentsJobsSummaryShowJobsSummaryParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            HistoriesContentsJobsSummaryShowJobsSummary200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/{type_}s/{id_}/jobs_summary"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(HistoriesContentsJobsSummaryShowJobsSummary200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_contents_jobs_summary_show_jobs_summary_2_2(
        self,
        history_id: str,
        id_: str,
        type_: HistoryContentType,
        run_as: HistoriesContentsJobsSummaryShowJobsSummaryParamRunAs | None = None,
    ) -> HistoriesContentsJobsSummaryShowJobsSummary200Response2:
        """
        Return detailed information about an `HDA` or `HDCAs` jobs.

        Return detailed information about an `HDA` or `HDCAs` jobs.  **Warning**: We allow
        anyone to fetch job state information about any object they can guess an encoded ID for
        - it isn't considered protected data. This keeps polling IDs as part of state
        calculation for large histories and collections as efficient as possible.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            id (str)                 : The ID of the item (`HDA`/`HDCA`)
            type (HistoryContentType): The type of the target history element.
            run-as (Optional[HistoriesContentsJobsSummaryShowJobsSummaryParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            HistoriesContentsJobsSummaryShowJobsSummary200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/{type_}s/{id_}/jobs_summary"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(HistoriesContentsJobsSummaryShowJobsSummary200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_contents_prepare_store_download_prepare_store_download_2_2(
        self,
        history_id: str,
        id_: str,
        type_: HistoryContentType,
        body: StoreExportPayload,
        run_as: HistoriesContentsPrepareStoreDownloadPrepareStoreDownloadParamRunAs | None = None,
    ) -> AsyncFile:
        """
        Prepare a dataset or dataset collection for export-style download.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            id (str)                 : The ID of the item (`HDA`/`HDCA`)
            type (HistoryContentType): The type of the target history element.
            run-as (Optional[HistoriesContentsPrepareStoreDownloadPrepareStoreDownloadParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (StoreExportPayload): Request body. (json)

        Returns:
            AsyncFile: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/{type_}s/{id_}/prepare_store_download"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: StoreExportPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(AsyncFile, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_contents_prepare_store_download_prepare_store_download_2_2(
        self,
        history_id: str,
        id_: str,
        type_: HistoryContentType,
        body: StoreExportPayload,
        run_as: HistoriesContentsPrepareStoreDownloadPrepareStoreDownloadParamRunAs | None = None,
    ) -> AsyncFile:
        """
        Prepare a dataset or dataset collection for export-style download.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            id (str)                 : The ID of the item (`HDA`/`HDCA`)
            type (HistoryContentType): The type of the target history element.
            run-as (Optional[HistoriesContentsPrepareStoreDownloadPrepareStoreDownloadParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (StoreExportPayload): Request body. (json)

        Returns:
            AsyncFile: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/{type_}s/{id_}/prepare_store_download"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: StoreExportPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(AsyncFile, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_contents_write_store_write_store_2_2(
        self,
        history_id: str,
        id_: str,
        type_: HistoryContentType,
        body: WriteStoreToPayload,
        run_as: HistoriesContentsWriteStoreWriteStoreParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Prepare a dataset or dataset collection for export-style download and write to supplied
        URI.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            id (str)                 : The ID of the item (`HDA`/`HDCA`)
            type (HistoryContentType): The type of the target history element.
            run-as (Optional[HistoriesContentsWriteStoreWriteStoreParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (WriteStoreToPayload): Request body. (json)

        Returns:
            AsyncTaskResultSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/{type_}s/{id_}/write_store"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: WriteStoreToPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(AsyncTaskResultSummary, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_contents_write_store_write_store_2_2(
        self,
        history_id: str,
        id_: str,
        type_: HistoryContentType,
        body: WriteStoreToPayload,
        run_as: HistoriesContentsWriteStoreWriteStoreParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Prepare a dataset or dataset collection for export-style download and write to supplied
        URI.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            id (str)                 : The ID of the item (`HDA`/`HDCA`)
            type (HistoryContentType): The type of the target history element.
            run-as (Optional[HistoriesContentsWriteStoreWriteStoreParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (WriteStoreToPayload): Request body. (json)

        Returns:
            AsyncTaskResultSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents/{type_}s/{id_}/write_store"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: WriteStoreToPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(AsyncTaskResultSummary, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_contents_from_store_create_from_store_2_2(
        self,
        history_id: str,
        body: CreateHistoryContentFromStore,
        view: HistoriesContentsFromStoreCreateFromStoreParamView | None = None,
        keys: HistoriesContentsFromStoreCreateFromStoreParamKeys | None = None,
        run_as: HistoriesContentsFromStoreCreateFromStoreParamRunAs | None = None,
    ) -> list[AnonymousArrayItem198]:
        """
        Create contents from store.

        Create history contents from model store. Input can be a tarfile created with
        build_objects script distributed with galaxy-data, from an exported history with files
        stripped out, or hand-crafted JSON dictionary.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            view (Optional[HistoriesContentsFromStoreCreateFromStoreParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoriesContentsFromStoreCreateFromStoreParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoriesContentsFromStoreCreateFromStoreParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateHistoryContentFromStore)
                                     : Request body. (json)

        Returns:
            List[AnonymousArrayItem198]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents_from_store"

        params: dict[str, Any] = {
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateHistoryContentFromStore = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem198], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_contents_from_store_create_from_store_2_2(
        self,
        history_id: str,
        body: CreateHistoryContentFromStore,
        view: HistoriesContentsFromStoreCreateFromStoreParamView | None = None,
        keys: HistoriesContentsFromStoreCreateFromStoreParamKeys | None = None,
        run_as: HistoriesContentsFromStoreCreateFromStoreParamRunAs | None = None,
    ) -> list[AnonymousArrayItem198]:
        """
        Create contents from store.

        Create history contents from model store. Input can be a tarfile created with
        build_objects script distributed with galaxy-data, from an exported history with files
        stripped out, or hand-crafted JSON dictionary.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            view (Optional[HistoriesContentsFromStoreCreateFromStoreParamView])
                                     : View to be passed to the serializer
            keys (Optional[HistoriesContentsFromStoreCreateFromStoreParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[HistoriesContentsFromStoreCreateFromStoreParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateHistoryContentFromStore)
                                     : Request body. (json)

        Returns:
            List[AnonymousArrayItem198]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/contents_from_store"

        params: dict[str, Any] = {
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateHistoryContentFromStore = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem198], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def history_contents_copy_contents_2_2(
        self,
        history_id: str,
        body: CopyDatasetsPayload,
        run_as: HistoryContentsCopyContentsParamRunAs | None = None,
    ) -> CopyDatasetsResponse:
        """
        Copy datasets or dataset collections to other histories.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            run-as (Optional[HistoryContentsCopyContentsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CopyDatasetsPayload): Request body. (json)

        Returns:
            CopyDatasetsResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/copy_contents"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CopyDatasetsPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(CopyDatasetsResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def history_contents_copy_contents_2_2(
        self,
        history_id: str,
        body: CopyDatasetsPayload,
        run_as: HistoryContentsCopyContentsParamRunAs | None = None,
    ) -> CopyDatasetsResponse:
        """
        Copy datasets or dataset collections to other histories.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            run-as (Optional[HistoryContentsCopyContentsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CopyDatasetsPayload): Request body. (json)

        Returns:
            CopyDatasetsResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/copy_contents"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CopyDatasetsPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(CopyDatasetsResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_custom_builds_metadata_get_custom_builds_metadata_2_2(
        self,
        history_id: str,
        run_as: HistoriesCustomBuildsMetadataGetCustomBuildsMetadataParamRunAs | None = None,
    ) -> CustomBuildsMetadataResponse:
        """
        Returns meta data for custom builds.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            run-as (Optional[HistoriesCustomBuildsMetadataGetCustomBuildsMetadataParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            CustomBuildsMetadataResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/custom_builds_metadata"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(CustomBuildsMetadataResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_custom_builds_metadata_get_custom_builds_metadata_2_2(
        self,
        history_id: str,
        run_as: HistoriesCustomBuildsMetadataGetCustomBuildsMetadataParamRunAs | None = None,
    ) -> CustomBuildsMetadataResponse:
        """
        Returns meta data for custom builds.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            run-as (Optional[HistoriesCustomBuildsMetadataGetCustomBuildsMetadataParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            CustomBuildsMetadataResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/custom_builds_metadata"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(CustomBuildsMetadataResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_disable_link_access_disable_link_access_2_2(
        self,
        history_id: str,
        run_as: HistoriesDisableLinkAccessDisableLinkAccessParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Makes this item inaccessible by a URL link.

        Makes this item inaccessible by a URL link and return the current sharing status.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            run-as (Optional[HistoriesDisableLinkAccessDisableLinkAccessParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            SharingStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/disable_link_access"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(SharingStatus, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_disable_link_access_disable_link_access_2_2(
        self,
        history_id: str,
        run_as: HistoriesDisableLinkAccessDisableLinkAccessParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Makes this item inaccessible by a URL link.

        Makes this item inaccessible by a URL link and return the current sharing status.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            run-as (Optional[HistoriesDisableLinkAccessDisableLinkAccessParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            SharingStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/disable_link_access"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(SharingStatus, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_enable_link_access_enable_link_access_2_2(
        self,
        history_id: str,
        run_as: HistoriesEnableLinkAccessEnableLinkAccessParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Makes this item accessible by a URL link.

        Makes this item accessible by a URL link and return the current sharing status.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            run-as (Optional[HistoriesEnableLinkAccessEnableLinkAccessParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            SharingStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/enable_link_access"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(SharingStatus, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_enable_link_access_enable_link_access_2_2(
        self,
        history_id: str,
        run_as: HistoriesEnableLinkAccessEnableLinkAccessParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Makes this item accessible by a URL link.

        Makes this item accessible by a URL link and return the current sharing status.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            run-as (Optional[HistoriesEnableLinkAccessEnableLinkAccessParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            SharingStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/enable_link_access"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(SharingStatus, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_exports_index_exports_2_2(
        self,
        history_id: str,
        limit: HistoriesExportsIndexExportsParamLimit | None = None,
        offset: HistoriesExportsIndexExportsParamOffset | None = 0,
        accept: str | None = "application/json",
        run_as: HistoriesExportsIndexExportsParamRunAs | None = None,
    ) -> JobExportHistoryArchiveListResponse:
        """
        Get previous history exports.

        By default the legacy job-based history exports (jeha) are returned.  Change the
        `accept` content type header to return the new task-based history exports.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            limit (Optional[HistoriesExportsIndexExportsParamLimit])
                                     : The maximum number of items to return.
            offset (Optional[HistoriesExportsIndexExportsParamOffset])
                                     : Starts at the beginning skip the first ( offset - 1 )
                                       items and begin returning at the Nth item
            accept (Optional[str])   : Accept header to determine the response format. Default
                                       is 'application/json'.
            run-as (Optional[HistoriesExportsIndexExportsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            JobExportHistoryArchiveListResponse: A list of history exports

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/exports"

        params: dict[str, Any] = {
            **({"limit": limit} if limit is not None else {}),
            **({"offset": offset} if offset is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"accept": accept} if accept is not None else {}),
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(JobExportHistoryArchiveListResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_exports_index_exports_2_2(
        self,
        history_id: str,
        limit: HistoriesExportsIndexExportsParamLimit | None = None,
        offset: HistoriesExportsIndexExportsParamOffset | None = 0,
        accept: str | None = "application/json",
        run_as: HistoriesExportsIndexExportsParamRunAs | None = None,
    ) -> JobExportHistoryArchiveListResponse:
        """
        Get previous history exports.

        By default the legacy job-based history exports (jeha) are returned.  Change the
        `accept` content type header to return the new task-based history exports.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            limit (Optional[HistoriesExportsIndexExportsParamLimit])
                                     : The maximum number of items to return.
            offset (Optional[HistoriesExportsIndexExportsParamOffset])
                                     : Starts at the beginning skip the first ( offset - 1 )
                                       items and begin returning at the Nth item
            accept (Optional[str])   : Accept header to determine the response format. Default
                                       is 'application/json'.
            run-as (Optional[HistoriesExportsIndexExportsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            JobExportHistoryArchiveListResponse: A list of history exports

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/exports"

        params: dict[str, Any] = {
            **({"limit": limit} if limit is not None else {}),
            **({"offset": offset} if offset is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"accept": accept} if accept is not None else {}),
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(JobExportHistoryArchiveListResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_exports_archive_export_2_2(
        self,
        history_id: str,
        run_as: HistoriesExportsArchiveExportParamRunAs | None = None,
        body: HistoriesExportsArchiveExportRequestBody2 | None = None,
    ) -> HistoriesExportsArchiveExport200Response2:
        """
        Start job (if needed) to create history export for corresponding history.

        This will start a job to create a history export archive.  Calling this endpoint
        multiple times will return the 202 status code until the archive has been completely
        generated and is ready to download. When ready, it will return the 200 status code along
        with the download link information.  If the history will be exported to a
        `directory_uri`, instead of returning the download link information, the Job ID will be
        returned so it can be queried to determine when the file has been written.
        **Deprecation notice**: Please use `/api/histories/{id}/prepare_store_download` or
        `/api/histories/{id}/write_store` instead.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            run-as (Optional[HistoriesExportsArchiveExportParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (Optional[HistoriesExportsArchiveExportRequestBody2])
                                     : Request body. (json)

        Returns:
            HistoriesExportsArchiveExport200Response2: Object containing url to fetch export
                                                       from.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/exports"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: HistoriesExportsArchiveExportRequestBody2 | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(HistoriesExportsArchiveExport200Response2, response.json())
            case 202:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_exports_archive_export_2_2(
        self,
        history_id: str,
        run_as: HistoriesExportsArchiveExportParamRunAs | None = None,
        body: HistoriesExportsArchiveExportRequestBody2 | None = None,
    ) -> HistoriesExportsArchiveExport200Response2:
        """
        Start job (if needed) to create history export for corresponding history.

        This will start a job to create a history export archive.  Calling this endpoint
        multiple times will return the 202 status code until the archive has been completely
        generated and is ready to download. When ready, it will return the 200 status code along
        with the download link information.  If the history will be exported to a
        `directory_uri`, instead of returning the download link information, the Job ID will be
        returned so it can be queried to determine when the file has been written.
        **Deprecation notice**: Please use `/api/histories/{id}/prepare_store_download` or
        `/api/histories/{id}/write_store` instead.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            run-as (Optional[HistoriesExportsArchiveExportParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (Optional[HistoriesExportsArchiveExportRequestBody2])
                                     : Request body. (json)

        Returns:
            HistoriesExportsArchiveExport200Response2: Object containing url to fetch export
                                                       from.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/exports"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: HistoriesExportsArchiveExportRequestBody2 | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(HistoriesExportsArchiveExport200Response2, response.json())
            case 202:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_exports_archive_download_2_2(
        self,
        history_id: str,
        jeha_id: HistoriesExportsArchiveDownloadParamJehaId,
        run_as: HistoriesExportsArchiveDownloadParamRunAs | None = None,
    ) -> None:
        """
        If ready and available, return raw contents of exported history as a downloadable
        archive.

        See ``PUT /api/histories/{id}/exports`` to initiate the creation of the history export -
        when ready, that route will return 200 status code (instead of 202) and this route can
        be used to download the archive.  **Deprecation notice**: Please use
        `/api/histories/{id}/prepare_store_download` or `/api/histories/{id}/write_store`
        instead.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            jeha_id (HistoriesExportsArchiveDownloadParamJehaId)
                                     : The ID of the specific Job Export History Association or
                                       `latest` (default) to download the last generated
                                       archive.
            run-as (Optional[HistoriesExportsArchiveDownloadParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/exports/{jeha_id}"

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

    async def histories_exports_archive_download_2_2(
        self,
        history_id: str,
        jeha_id: HistoriesExportsArchiveDownloadParamJehaId,
        run_as: HistoriesExportsArchiveDownloadParamRunAs | None = None,
    ) -> None:
        """
        If ready and available, return raw contents of exported history as a downloadable
        archive.

        See ``PUT /api/histories/{id}/exports`` to initiate the creation of the history export -
        when ready, that route will return 200 status code (instead of 202) and this route can
        be used to download the archive.  **Deprecation notice**: Please use
        `/api/histories/{id}/prepare_store_download` or `/api/histories/{id}/write_store`
        instead.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            jeha_id (HistoriesExportsArchiveDownloadParamJehaId)
                                     : The ID of the specific Job Export History Association or
                                       `latest` (default) to download the last generated
                                       archive.
            run-as (Optional[HistoriesExportsArchiveDownloadParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/exports/{jeha_id}"

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

    async def histories_jobs_summary_index_jobs_summary_2_2(
        self,
        history_id: str,
        ids: HistoriesJobsSummaryIndexJobsSummaryParamIds | None = None,
        types: HistoriesJobsSummaryIndexJobsSummaryParamTypes | None = None,
        run_as: HistoriesJobsSummaryIndexJobsSummaryParamRunAs | None = None,
    ) -> list[AnonymousArrayItem200]:
        """
        Return job state summary info for jobs, implicit groups jobs for collections or workflow
        invocations.

        Return job state summary info for jobs, implicit groups jobs for collections or workflow
        invocations.  **Warning**: We allow anyone to fetch job state information about any
        object they can guess an encoded ID for - it isn't considered protected data. This keeps
        polling IDs as part of state calculation for large histories and collections as
        efficient as possible.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            ids (Optional[HistoriesJobsSummaryIndexJobsSummaryParamIds])
                                     : A comma-separated list of encoded ids of job summary
                                       objects to return - if `ids` is specified types must also
                                       be specified and have same length.
            types (Optional[HistoriesJobsSummaryIndexJobsSummaryParamTypes])
                                     : A comma-separated list of type of object represented by
                                       elements in the `ids` array - any of `Job`,
                                       `ImplicitCollectionJob`, or `WorkflowInvocation`.
            run-as (Optional[HistoriesJobsSummaryIndexJobsSummaryParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem200]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/jobs_summary"

        params: dict[str, Any] = {
            **({"ids": ids} if ids is not None else {}),
            **({"types": types} if types is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem200], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_jobs_summary_index_jobs_summary_2_2(
        self,
        history_id: str,
        ids: HistoriesJobsSummaryIndexJobsSummaryParamIds | None = None,
        types: HistoriesJobsSummaryIndexJobsSummaryParamTypes | None = None,
        run_as: HistoriesJobsSummaryIndexJobsSummaryParamRunAs | None = None,
    ) -> list[AnonymousArrayItem200]:
        """
        Return job state summary info for jobs, implicit groups jobs for collections or workflow
        invocations.

        Return job state summary info for jobs, implicit groups jobs for collections or workflow
        invocations.  **Warning**: We allow anyone to fetch job state information about any
        object they can guess an encoded ID for - it isn't considered protected data. This keeps
        polling IDs as part of state calculation for large histories and collections as
        efficient as possible.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            ids (Optional[HistoriesJobsSummaryIndexJobsSummaryParamIds])
                                     : A comma-separated list of encoded ids of job summary
                                       objects to return - if `ids` is specified types must also
                                       be specified and have same length.
            types (Optional[HistoriesJobsSummaryIndexJobsSummaryParamTypes])
                                     : A comma-separated list of type of object represented by
                                       elements in the `ids` array - any of `Job`,
                                       `ImplicitCollectionJob`, or `WorkflowInvocation`.
            run-as (Optional[HistoriesJobsSummaryIndexJobsSummaryParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem200]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/jobs_summary"

        params: dict[str, Any] = {
            **({"ids": ids} if ids is not None else {}),
            **({"types": types} if types is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem200], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_materialize_materialize_to_history_2_2(
        self,
        history_id: str,
        body: MaterializeDatasetInstanceApiRequest2,
        run_as: HistoriesMaterializeMaterializeToHistoryParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Materialize a deferred library or HDA dataset into real, usable dataset in specified
        history.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            run-as (Optional[HistoriesMaterializeMaterializeToHistoryParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (MaterializeDatasetInstanceApiRequest2)
                                     : Request body. (json)

        Returns:
            AsyncTaskResultSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/materialize"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: MaterializeDatasetInstanceApiRequest2 = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(AsyncTaskResultSummary, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_materialize_materialize_to_history_2_2(
        self,
        history_id: str,
        body: MaterializeDatasetInstanceApiRequest2,
        run_as: HistoriesMaterializeMaterializeToHistoryParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Materialize a deferred library or HDA dataset into real, usable dataset in specified
        history.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            run-as (Optional[HistoriesMaterializeMaterializeToHistoryParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (MaterializeDatasetInstanceApiRequest2)
                                     : Request body. (json)

        Returns:
            AsyncTaskResultSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/materialize"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: MaterializeDatasetInstanceApiRequest2 = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(AsyncTaskResultSummary, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_prepare_store_download_prepare_store_download_2_2(
        self,
        history_id: str,
        body: StoreExportPayload,
        run_as: HistoriesPrepareStoreDownloadPrepareStoreDownloadParamRunAs | None = None,
    ) -> AsyncFile:
        """
        Return a short term storage token to monitor download of the history.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            run-as (Optional[HistoriesPrepareStoreDownloadPrepareStoreDownloadParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (StoreExportPayload): Request body. (json)

        Returns:
            AsyncFile: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/prepare_store_download"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: StoreExportPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(AsyncFile, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_prepare_store_download_prepare_store_download_2_2(
        self,
        history_id: str,
        body: StoreExportPayload,
        run_as: HistoriesPrepareStoreDownloadPrepareStoreDownloadParamRunAs | None = None,
    ) -> AsyncFile:
        """
        Return a short term storage token to monitor download of the history.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            run-as (Optional[HistoriesPrepareStoreDownloadPrepareStoreDownloadParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (StoreExportPayload): Request body. (json)

        Returns:
            AsyncFile: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/prepare_store_download"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: StoreExportPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(AsyncFile, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_publish_publish_2_2(
        self,
        history_id: str,
        run_as: HistoriesPublishPublishParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Makes this item public and accessible by a URL link.

        Makes this item publicly available by a URL link and return the current sharing status.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            run-as (Optional[HistoriesPublishPublishParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            SharingStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/publish"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(SharingStatus, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_publish_publish_2_2(
        self,
        history_id: str,
        run_as: HistoriesPublishPublishParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Makes this item public and accessible by a URL link.

        Makes this item publicly available by a URL link and return the current sharing status.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            run-as (Optional[HistoriesPublishPublishParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            SharingStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/publish"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(SharingStatus, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_share_with_users_share_with_users_2_2(
        self,
        history_id: str,
        body: ShareWithPayload,
        run_as: HistoriesShareWithUsersShareWithUsersParamRunAs | None = None,
    ) -> ShareHistoryWithStatus:
        """
        Share this item with specific users.

        Shares this item with specific users and return the current sharing status.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            run-as (Optional[HistoriesShareWithUsersShareWithUsersParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (ShareWithPayload)  : Request body. (json)

        Returns:
            ShareHistoryWithStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/share_with_users"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: ShareWithPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ShareHistoryWithStatus, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_share_with_users_share_with_users_2_2(
        self,
        history_id: str,
        body: ShareWithPayload,
        run_as: HistoriesShareWithUsersShareWithUsersParamRunAs | None = None,
    ) -> ShareHistoryWithStatus:
        """
        Share this item with specific users.

        Shares this item with specific users and return the current sharing status.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            run-as (Optional[HistoriesShareWithUsersShareWithUsersParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (ShareWithPayload)  : Request body. (json)

        Returns:
            ShareHistoryWithStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/share_with_users"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: ShareWithPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ShareHistoryWithStatus, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_sharing_sharing_2_2(
        self,
        history_id: str,
        run_as: HistoriesSharingSharingParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Get the current sharing status of the given item.

        Return the sharing status of the item.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            run-as (Optional[HistoriesSharingSharingParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            SharingStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/sharing"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(SharingStatus, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_sharing_sharing_2_2(
        self,
        history_id: str,
        run_as: HistoriesSharingSharingParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Get the current sharing status of the given item.

        Return the sharing status of the item.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            run-as (Optional[HistoriesSharingSharingParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            SharingStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/sharing"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(SharingStatus, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_slug_set_slug_2_2(
        self,
        history_id: str,
        body: SetSlugPayload,
        run_as: HistoriesSlugSetSlugParamRunAs | None = None,
    ) -> None:
        """
        Set a new slug for this shared item.

        Sets a new slug to access this item by URL. The new slug must be unique.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            run-as (Optional[HistoriesSlugSetSlugParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (SetSlugPayload)    : Request body. (json)

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/slug"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: SetSlugPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_slug_set_slug_2_2(
        self,
        history_id: str,
        body: SetSlugPayload,
        run_as: HistoriesSlugSetSlugParamRunAs | None = None,
    ) -> None:
        """
        Set a new slug for this shared item.

        Sets a new slug to access this item by URL. The new slug must be unique.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            run-as (Optional[HistoriesSlugSetSlugParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (SetSlugPayload)    : Request body. (json)

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/slug"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: SetSlugPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_tags_index(
        self,
        history_id: str,
        run_as: HistoriesTagsIndexParamRunAs | None = None,
    ) -> ItemTagsListResponse:
        """
        Show tags based on history_id

        Args:
            history_id (str)         :
            run-as (Optional[HistoriesTagsIndexParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ItemTagsListResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/tags"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ItemTagsListResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_tags_delete(
        self,
        history_id: str,
        tag_name: str,
        run_as: HistoriesTagsDeleteParamRunAs | None = None,
    ) -> bool:
        """
        Delete tag based on history_id

        Args:
            history_id (str)         :
            tag_name (str)           :
            run-as (Optional[HistoriesTagsDeleteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            bool: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/tags/{tag_name}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(bool, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_tags_show(
        self,
        history_id: str,
        tag_name: str,
        run_as: HistoriesTagsShowParamRunAs | None = None,
    ) -> ItemTagsResponse:
        """
        Show tag based on history_id

        Args:
            history_id (str)         :
            tag_name (str)           :
            run-as (Optional[HistoriesTagsShowParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ItemTagsResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/tags/{tag_name}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ItemTagsResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_tags_create(
        self,
        history_id: str,
        tag_name: str,
        run_as: HistoriesTagsCreateParamRunAs | None = None,
        body: ItemTagsCreatePayload | None = None,
    ) -> ItemTagsResponse:
        """
        Create tag based on history_id

        Args:
            history_id (str)         :
            tag_name (str)           :
            run-as (Optional[HistoriesTagsCreateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (Optional[ItemTagsCreatePayload])
                                     : Request body. (json)

        Returns:
            ItemTagsResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/tags/{tag_name}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: ItemTagsCreatePayload | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ItemTagsResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_tags_update(
        self,
        history_id: str,
        tag_name: str,
        body: ItemTagsCreatePayload,
        run_as: HistoriesTagsUpdateParamRunAs | None = None,
    ) -> ItemTagsResponse:
        """
        Update tag based on history_id

        Args:
            history_id (str)         :
            tag_name (str)           :
            run-as (Optional[HistoriesTagsUpdateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (ItemTagsCreatePayload)
                                     : Request body. (json)

        Returns:
            ItemTagsResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/tags/{tag_name}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: ItemTagsCreatePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ItemTagsResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_tool_requests_tool_requests_2_2(
        self,
        history_id: str,
        run_as: HistoriesToolRequestsToolRequestsParamRunAs | None = None,
    ) -> list[ToolRequestModel]:
        """
        Return all the tool requests for the tools submitted to this history.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            run-as (Optional[HistoriesToolRequestsToolRequestsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[ToolRequestModel]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/tool_requests"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[ToolRequestModel], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_tool_requests_tool_requests_2_2(
        self,
        history_id: str,
        run_as: HistoriesToolRequestsToolRequestsParamRunAs | None = None,
    ) -> list[ToolRequestModel]:
        """
        Return all the tool requests for the tools submitted to this history.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            run-as (Optional[HistoriesToolRequestsToolRequestsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[ToolRequestModel]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/tool_requests"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[ToolRequestModel], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_unpublish_unpublish_2_2(
        self,
        history_id: str,
        run_as: HistoriesUnpublishUnpublishParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Removes this item from the published list.

        Removes this item from the published list and return the current sharing status.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            run-as (Optional[HistoriesUnpublishUnpublishParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            SharingStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/unpublish"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(SharingStatus, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_unpublish_unpublish_2_2(
        self,
        history_id: str,
        run_as: HistoriesUnpublishUnpublishParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Removes this item from the published list.

        Removes this item from the published list and return the current sharing status.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            run-as (Optional[HistoriesUnpublishUnpublishParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            SharingStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/unpublish"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(SharingStatus, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_write_store_write_store_2_2(
        self,
        history_id: str,
        body: WriteStoreToPayload,
        run_as: HistoriesWriteStoreWriteStoreParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Prepare history for export-style download and write to supplied URI.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            run-as (Optional[HistoriesWriteStoreWriteStoreParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (WriteStoreToPayload): Request body. (json)

        Returns:
            AsyncTaskResultSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/write_store"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: WriteStoreToPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(AsyncTaskResultSummary, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def histories_write_store_write_store_2_2(
        self,
        history_id: str,
        body: WriteStoreToPayload,
        run_as: HistoriesWriteStoreWriteStoreParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Prepare history for export-style download and write to supplied URI.

        Args:
            history_id (str)         : The encoded database identifier of the History.
            run-as (Optional[HistoriesWriteStoreWriteStoreParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (WriteStoreToPayload): Request body. (json)

        Returns:
            AsyncTaskResultSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/histories/{history_id}/write_store"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: WriteStoreToPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(AsyncTaskResultSummary, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover
