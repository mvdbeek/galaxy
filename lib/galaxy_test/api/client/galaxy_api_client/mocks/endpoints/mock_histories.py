from typing import TYPE_CHECKING, Any

from ...models.anonymous_array_item_91 import AnonymousArrayItem91
from ...models.anonymous_array_item_93 import AnonymousArrayItem93
from ...models.anonymous_array_item_95 import AnonymousArrayItem95
from ...models.anonymous_array_item_97 import AnonymousArrayItem97
from ...models.anonymous_array_item_99 import AnonymousArrayItem99
from ...models.anonymous_array_item_101 import AnonymousArrayItem101
from ...models.anonymous_array_item_103 import AnonymousArrayItem103
from ...models.anonymous_array_item_109 import AnonymousArrayItem109
from ...models.anonymous_array_item_111 import AnonymousArrayItem111
from ...models.async_file import AsyncFile
from ...models.async_task_result_summary import AsyncTaskResultSummary
from ...models.copy_datasets_payload import CopyDatasetsPayload
from ...models.copy_datasets_response import CopyDatasetsResponse
from ...models.create_history_content_from_store import CreateHistoryContentFromStore
from ...models.create_history_content_payload import CreateHistoryContentPayload
from ...models.create_history_from_store import CreateHistoryFromStore
from ...models.custom_builds_metadata_response import CustomBuildsMetadataResponse
from ...models.dataset_association_roles import DatasetAssociationRoles
from ...models.dataset_collections_download_param_run_as import DatasetCollectionsDownloadParamRunAs
from ...models.dataset_collections_update_collection_200_response import DatasetCollectionsUpdateCollection200Response
from ...models.dataset_collections_update_collection_param_keys import DatasetCollectionsUpdateCollectionParamKeys
from ...models.dataset_collections_update_collection_param_run_as import DatasetCollectionsUpdateCollectionParamRunAs
from ...models.dataset_collections_update_collection_param_view import DatasetCollectionsUpdateCollectionParamView
from ...models.datasets_delete_param_purge import DatasetsDeleteParamPurge
from ...models.datasets_delete_param_recursive import DatasetsDeleteParamRecursive
from ...models.datasets_delete_param_run_as import DatasetsDeleteParamRunAs
from ...models.datasets_delete_param_stop_job import DatasetsDeleteParamStopJob
from ...models.datasets_update_dataset_200_response import DatasetsUpdateDataset200Response
from ...models.datasets_update_dataset_param_keys import DatasetsUpdateDatasetParamKeys
from ...models.datasets_update_dataset_param_run_as import DatasetsUpdateDatasetParamRunAs
from ...models.datasets_update_dataset_param_view import DatasetsUpdateDatasetParamView
from ...models.delete_histories_payload import DeleteHistoriesPayload
from ...models.delete_history_content_payload import DeleteHistoryContentPayload
from ...models.export_task_list_response import ExportTaskListResponse
from ...models.histories_archive_archive_history_200_response import HistoriesArchiveArchiveHistory200Response
from ...models.histories_archive_archive_history_param_run_as import HistoriesArchiveArchiveHistoryParamRunAs
from ...models.histories_archive_archive_history_request_body import HistoriesArchiveArchiveHistoryRequestBody
from ...models.histories_archive_restore_restore_archived_history_200_response import (
    HistoriesArchiveRestoreRestoreArchivedHistory200Response,
)
from ...models.histories_archive_restore_restore_archived_history_param_force import (
    HistoriesArchiveRestoreRestoreArchivedHistoryParamForce,
)
from ...models.histories_archive_restore_restore_archived_history_param_run_as import (
    HistoriesArchiveRestoreRestoreArchivedHistoryParamRunAs,
)
from ...models.histories_archived_get_archived_histories_param_keys import (
    HistoriesArchivedGetArchivedHistoriesParamKeys,
)
from ...models.histories_archived_get_archived_histories_param_limit import (
    HistoriesArchivedGetArchivedHistoriesParamLimit,
)
from ...models.histories_archived_get_archived_histories_param_offset import (
    HistoriesArchivedGetArchivedHistoriesParamOffset,
)
from ...models.histories_archived_get_archived_histories_param_order import (
    HistoriesArchivedGetArchivedHistoriesParamOrder,
)
from ...models.histories_archived_get_archived_histories_param_q import HistoriesArchivedGetArchivedHistoriesParamQ
from ...models.histories_archived_get_archived_histories_param_qv import HistoriesArchivedGetArchivedHistoriesParamQv
from ...models.histories_archived_get_archived_histories_param_run_as import (
    HistoriesArchivedGetArchivedHistoriesParamRunAs,
)
from ...models.histories_archived_get_archived_histories_param_view import (
    HistoriesArchivedGetArchivedHistoriesParamView,
)
from ...models.histories_batch_delete_batch_delete_param_keys import HistoriesBatchDeleteBatchDeleteParamKeys
from ...models.histories_batch_delete_batch_delete_param_run_as import HistoriesBatchDeleteBatchDeleteParamRunAs
from ...models.histories_batch_delete_batch_delete_param_view import HistoriesBatchDeleteBatchDeleteParamView
from ...models.histories_batch_undelete_batch_undelete_param_keys import HistoriesBatchUndeleteBatchUndeleteParamKeys
from ...models.histories_batch_undelete_batch_undelete_param_run_as import HistoriesBatchUndeleteBatchUndeleteParamRunAs
from ...models.histories_batch_undelete_batch_undelete_param_view import HistoriesBatchUndeleteBatchUndeleteParamView
from ...models.histories_citations_citations_param_run_as import HistoriesCitationsCitationsParamRunAs
from ...models.histories_contents_bulk_bulk_operation_param_q import HistoriesContentsBulkBulkOperationParamQ
from ...models.histories_contents_bulk_bulk_operation_param_qv import HistoriesContentsBulkBulkOperationParamQv
from ...models.histories_contents_bulk_bulk_operation_param_run_as import HistoriesContentsBulkBulkOperationParamRunAs
from ...models.histories_contents_datasets_materialize_materialize_dataset_param_run_as import (
    HistoriesContentsDatasetsMaterializeMaterializeDatasetParamRunAs,
)
from ...models.histories_contents_from_store_create_from_store_param_keys import (
    HistoriesContentsFromStoreCreateFromStoreParamKeys,
)
from ...models.histories_contents_from_store_create_from_store_param_run_as import (
    HistoriesContentsFromStoreCreateFromStoreParamRunAs,
)
from ...models.histories_contents_from_store_create_from_store_param_view import (
    HistoriesContentsFromStoreCreateFromStoreParamView,
)
from ...models.histories_contents_jobs_summary_show_jobs_summary_200_response import (
    HistoriesContentsJobsSummaryShowJobsSummary200Response,
)
from ...models.histories_contents_jobs_summary_show_jobs_summary_param_run_as import (
    HistoriesContentsJobsSummaryShowJobsSummaryParamRunAs,
)
from ...models.histories_contents_permissions_update_permissions_param_run_as import (
    HistoriesContentsPermissionsUpdatePermissionsParamRunAs,
)
from ...models.histories_contents_permissions_update_permissions_request_body import (
    HistoriesContentsPermissionsUpdatePermissionsRequestBody,
)
from ...models.histories_contents_prepare_store_download_prepare_store_download_param_run_as import (
    HistoriesContentsPrepareStoreDownloadPrepareStoreDownloadParamRunAs,
)
from ...models.histories_contents_tags_create_param_run_as import HistoriesContentsTagsCreateParamRunAs
from ...models.histories_contents_tags_delete_param_run_as import HistoriesContentsTagsDeleteParamRunAs
from ...models.histories_contents_tags_index_param_run_as import HistoriesContentsTagsIndexParamRunAs
from ...models.histories_contents_tags_show_param_run_as import HistoriesContentsTagsShowParamRunAs
from ...models.histories_contents_tags_update_param_run_as import HistoriesContentsTagsUpdateParamRunAs
from ...models.histories_contents_update_batch_param_keys import HistoriesContentsUpdateBatchParamKeys
from ...models.histories_contents_update_batch_param_run_as import HistoriesContentsUpdateBatchParamRunAs
from ...models.histories_contents_update_batch_param_view import HistoriesContentsUpdateBatchParamView
from ...models.histories_contents_validate_validate_200_response import HistoriesContentsValidateValidate200Response
from ...models.histories_contents_validate_validate_param_run_as import HistoriesContentsValidateValidateParamRunAs
from ...models.histories_contents_write_store_write_store_param_run_as import (
    HistoriesContentsWriteStoreWriteStoreParamRunAs,
)
from ...models.histories_count_count_param_run_as import HistoriesCountCountParamRunAs
from ...models.histories_create_200_response import HistoriesCreate200Response
from ...models.histories_create_param_keys import HistoriesCreateParamKeys
from ...models.histories_create_param_run_as import HistoriesCreateParamRunAs
from ...models.histories_create_param_view import HistoriesCreateParamView
from ...models.histories_custom_builds_metadata_get_custom_builds_metadata_param_run_as import (
    HistoriesCustomBuildsMetadataGetCustomBuildsMetadataParamRunAs,
)
from ...models.histories_delete_200_response import HistoriesDelete200Response
from ...models.histories_delete_param_keys import HistoriesDeleteParamKeys
from ...models.histories_delete_param_run_as import HistoriesDeleteParamRunAs
from ...models.histories_delete_param_view import HistoriesDeleteParamView
from ...models.histories_delete_request_body import HistoriesDeleteRequestBody
from ...models.histories_deleted_index_deleted_param_all import HistoriesDeletedIndexDeletedParamAll
from ...models.histories_deleted_index_deleted_param_keys import HistoriesDeletedIndexDeletedParamKeys
from ...models.histories_deleted_index_deleted_param_limit import HistoriesDeletedIndexDeletedParamLimit
from ...models.histories_deleted_index_deleted_param_offset import HistoriesDeletedIndexDeletedParamOffset
from ...models.histories_deleted_index_deleted_param_order import HistoriesDeletedIndexDeletedParamOrder
from ...models.histories_deleted_index_deleted_param_q import HistoriesDeletedIndexDeletedParamQ
from ...models.histories_deleted_index_deleted_param_qv import HistoriesDeletedIndexDeletedParamQv
from ...models.histories_deleted_index_deleted_param_run_as import HistoriesDeletedIndexDeletedParamRunAs
from ...models.histories_deleted_index_deleted_param_view import HistoriesDeletedIndexDeletedParamView
from ...models.histories_deleted_undelete_undelete_200_response import HistoriesDeletedUndeleteUndelete200Response
from ...models.histories_deleted_undelete_undelete_param_keys import HistoriesDeletedUndeleteUndeleteParamKeys
from ...models.histories_deleted_undelete_undelete_param_run_as import HistoriesDeletedUndeleteUndeleteParamRunAs
from ...models.histories_deleted_undelete_undelete_param_view import HistoriesDeletedUndeleteUndeleteParamView
from ...models.histories_disable_link_access_disable_link_access_param_run_as import (
    HistoriesDisableLinkAccessDisableLinkAccessParamRunAs,
)
from ...models.histories_enable_link_access_enable_link_access_param_run_as import (
    HistoriesEnableLinkAccessEnableLinkAccessParamRunAs,
)
from ...models.histories_exports_archive_download_param_jeha_id import HistoriesExportsArchiveDownloadParamJehaId
from ...models.histories_exports_archive_download_param_run_as import HistoriesExportsArchiveDownloadParamRunAs
from ...models.histories_exports_archive_export_200_response import HistoriesExportsArchiveExport200Response
from ...models.histories_exports_archive_export_param_run_as import HistoriesExportsArchiveExportParamRunAs
from ...models.histories_exports_archive_export_request_body import HistoriesExportsArchiveExportRequestBody
from ...models.histories_exports_index_exports_param_limit import HistoriesExportsIndexExportsParamLimit
from ...models.histories_exports_index_exports_param_offset import HistoriesExportsIndexExportsParamOffset
from ...models.histories_exports_index_exports_param_run_as import HistoriesExportsIndexExportsParamRunAs
from ...models.histories_from_store_async_create_from_store_async_param_run_as import (
    HistoriesFromStoreAsyncCreateFromStoreAsyncParamRunAs,
)
from ...models.histories_from_store_create_from_store_200_response import HistoriesFromStoreCreateFromStore200Response
from ...models.histories_from_store_create_from_store_param_keys import HistoriesFromStoreCreateFromStoreParamKeys
from ...models.histories_from_store_create_from_store_param_run_as import HistoriesFromStoreCreateFromStoreParamRunAs
from ...models.histories_from_store_create_from_store_param_view import HistoriesFromStoreCreateFromStoreParamView
from ...models.histories_index_param_all import HistoriesIndexParamAll
from ...models.histories_index_param_deleted import HistoriesIndexParamDeleted
from ...models.histories_index_param_keys import HistoriesIndexParamKeys
from ...models.histories_index_param_limit import HistoriesIndexParamLimit
from ...models.histories_index_param_offset import HistoriesIndexParamOffset
from ...models.histories_index_param_order import HistoriesIndexParamOrder
from ...models.histories_index_param_q import HistoriesIndexParamQ
from ...models.histories_index_param_qv import HistoriesIndexParamQv
from ...models.histories_index_param_run_as import HistoriesIndexParamRunAs
from ...models.histories_index_param_search import HistoriesIndexParamSearch
from ...models.histories_index_param_show_archived import HistoriesIndexParamShowArchived
from ...models.histories_index_param_view import HistoriesIndexParamView
from ...models.histories_jobs_summary_index_jobs_summary_param_ids import HistoriesJobsSummaryIndexJobsSummaryParamIds
from ...models.histories_jobs_summary_index_jobs_summary_param_run_as import (
    HistoriesJobsSummaryIndexJobsSummaryParamRunAs,
)
from ...models.histories_jobs_summary_index_jobs_summary_param_types import (
    HistoriesJobsSummaryIndexJobsSummaryParamTypes,
)
from ...models.histories_materialize_materialize_to_history_param_run_as import (
    HistoriesMaterializeMaterializeToHistoryParamRunAs,
)
from ...models.histories_most_recently_used_show_recent_200_response import (
    HistoriesMostRecentlyUsedShowRecent200Response,
)
from ...models.histories_most_recently_used_show_recent_param_keys import HistoriesMostRecentlyUsedShowRecentParamKeys
from ...models.histories_most_recently_used_show_recent_param_run_as import (
    HistoriesMostRecentlyUsedShowRecentParamRunAs,
)
from ...models.histories_most_recently_used_show_recent_param_view import HistoriesMostRecentlyUsedShowRecentParamView
from ...models.histories_prepare_download_prepare_collection_download_param_run_as import (
    HistoriesPrepareDownloadPrepareCollectionDownloadParamRunAs,
)
from ...models.histories_prepare_store_download_prepare_store_download_param_run_as import (
    HistoriesPrepareStoreDownloadPrepareStoreDownloadParamRunAs,
)
from ...models.histories_publish_publish_param_run_as import HistoriesPublishPublishParamRunAs
from ...models.histories_published_published_param_keys import HistoriesPublishedPublishedParamKeys
from ...models.histories_published_published_param_limit import HistoriesPublishedPublishedParamLimit
from ...models.histories_published_published_param_offset import HistoriesPublishedPublishedParamOffset
from ...models.histories_published_published_param_order import HistoriesPublishedPublishedParamOrder
from ...models.histories_published_published_param_q import HistoriesPublishedPublishedParamQ
from ...models.histories_published_published_param_qv import HistoriesPublishedPublishedParamQv
from ...models.histories_published_published_param_run_as import HistoriesPublishedPublishedParamRunAs
from ...models.histories_published_published_param_view import HistoriesPublishedPublishedParamView
from ...models.histories_share_with_users_share_with_users_param_run_as import (
    HistoriesShareWithUsersShareWithUsersParamRunAs,
)
from ...models.histories_shared_with_me_shared_with_me_param_keys import HistoriesSharedWithMeSharedWithMeParamKeys
from ...models.histories_shared_with_me_shared_with_me_param_limit import HistoriesSharedWithMeSharedWithMeParamLimit
from ...models.histories_shared_with_me_shared_with_me_param_offset import HistoriesSharedWithMeSharedWithMeParamOffset
from ...models.histories_shared_with_me_shared_with_me_param_order import HistoriesSharedWithMeSharedWithMeParamOrder
from ...models.histories_shared_with_me_shared_with_me_param_q import HistoriesSharedWithMeSharedWithMeParamQ
from ...models.histories_shared_with_me_shared_with_me_param_qv import HistoriesSharedWithMeSharedWithMeParamQv
from ...models.histories_shared_with_me_shared_with_me_param_run_as import HistoriesSharedWithMeSharedWithMeParamRunAs
from ...models.histories_shared_with_me_shared_with_me_param_view import HistoriesSharedWithMeSharedWithMeParamView
from ...models.histories_sharing_sharing_param_run_as import HistoriesSharingSharingParamRunAs
from ...models.histories_show_200_response import HistoriesShow200Response
from ...models.histories_show_param_keys import HistoriesShowParamKeys
from ...models.histories_show_param_run_as import HistoriesShowParamRunAs
from ...models.histories_show_param_view import HistoriesShowParamView
from ...models.histories_slug_set_slug_param_run_as import HistoriesSlugSetSlugParamRunAs
from ...models.histories_tags_create_param_run_as import HistoriesTagsCreateParamRunAs
from ...models.histories_tags_delete_param_run_as import HistoriesTagsDeleteParamRunAs
from ...models.histories_tags_index_param_run_as import HistoriesTagsIndexParamRunAs
from ...models.histories_tags_show_param_run_as import HistoriesTagsShowParamRunAs
from ...models.histories_tags_update_param_run_as import HistoriesTagsUpdateParamRunAs
from ...models.histories_tool_requests_tool_requests_param_run_as import HistoriesToolRequestsToolRequestsParamRunAs
from ...models.histories_unpublish_unpublish_param_run_as import HistoriesUnpublishUnpublishParamRunAs
from ...models.histories_update_200_response import HistoriesUpdate200Response
from ...models.histories_update_param_keys import HistoriesUpdateParamKeys
from ...models.histories_update_param_run_as import HistoriesUpdateParamRunAs
from ...models.histories_update_param_view import HistoriesUpdateParamView
from ...models.histories_write_store_write_store_param_run_as import HistoriesWriteStoreWriteStoreParamRunAs
from ...models.history_content_bulk_operation_payload import HistoryContentBulkOperationPayload
from ...models.history_content_bulk_operation_result import HistoryContentBulkOperationResult
from ...models.history_content_type import HistoryContentType
from ...models.history_contents_archive_named_param_dry_run import HistoryContentsArchiveNamedParamDryRun
from ...models.history_contents_archive_named_param_limit import HistoryContentsArchiveNamedParamLimit
from ...models.history_contents_archive_named_param_offset import HistoryContentsArchiveNamedParamOffset
from ...models.history_contents_archive_named_param_order import HistoryContentsArchiveNamedParamOrder
from ...models.history_contents_archive_named_param_q import HistoryContentsArchiveNamedParamQ
from ...models.history_contents_archive_named_param_qv import HistoryContentsArchiveNamedParamQv
from ...models.history_contents_archive_named_param_run_as import HistoryContentsArchiveNamedParamRunAs
from ...models.history_contents_archive_param_dry_run import HistoryContentsArchiveParamDryRun
from ...models.history_contents_archive_param_filename import HistoryContentsArchiveParamFilename
from ...models.history_contents_archive_param_limit import HistoryContentsArchiveParamLimit
from ...models.history_contents_archive_param_offset import HistoryContentsArchiveParamOffset
from ...models.history_contents_archive_param_order import HistoryContentsArchiveParamOrder
from ...models.history_contents_archive_param_q import HistoryContentsArchiveParamQ
from ...models.history_contents_archive_param_qv import HistoryContentsArchiveParamQv
from ...models.history_contents_archive_param_run_as import HistoryContentsArchiveParamRunAs
from ...models.history_contents_copy_contents_param_run_as import HistoryContentsCopyContentsParamRunAs
from ...models.history_contents_create_200_response import HistoryContentsCreate200Response
from ...models.history_contents_create_param_keys import HistoryContentsCreateParamKeys
from ...models.history_contents_create_param_run_as import HistoryContentsCreateParamRunAs
from ...models.history_contents_create_param_type import HistoryContentsCreateParamType
from ...models.history_contents_create_param_view import HistoryContentsCreateParamView
from ...models.history_contents_create_typed_200_response import HistoryContentsCreateTyped200Response
from ...models.history_contents_create_typed_param_keys import HistoryContentsCreateTypedParamKeys
from ...models.history_contents_create_typed_param_run_as import HistoryContentsCreateTypedParamRunAs
from ...models.history_contents_create_typed_param_view import HistoryContentsCreateTypedParamView
from ...models.history_contents_delete_legacy_param_purge import HistoryContentsDeleteLegacyParamPurge
from ...models.history_contents_delete_legacy_param_recursive import HistoryContentsDeleteLegacyParamRecursive
from ...models.history_contents_delete_legacy_param_run_as import HistoryContentsDeleteLegacyParamRunAs
from ...models.history_contents_delete_legacy_param_stop_job import HistoryContentsDeleteLegacyParamStopJob
from ...models.history_contents_delete_typed_param_purge import HistoryContentsDeleteTypedParamPurge
from ...models.history_contents_delete_typed_param_recursive import HistoryContentsDeleteTypedParamRecursive
from ...models.history_contents_delete_typed_param_run_as import HistoryContentsDeleteTypedParamRunAs
from ...models.history_contents_delete_typed_param_stop_job import HistoryContentsDeleteTypedParamStopJob
from ...models.history_contents_download_collection_param_history_id import (
    HistoryContentsDownloadCollectionParamHistoryId,
)
from ...models.history_contents_download_collection_param_run_as import HistoryContentsDownloadCollectionParamRunAs
from ...models.history_contents_index_param_deleted import HistoryContentsIndexParamDeleted
from ...models.history_contents_index_param_details import HistoryContentsIndexParamDetails
from ...models.history_contents_index_param_ids import HistoryContentsIndexParamIds
from ...models.history_contents_index_param_keys import HistoryContentsIndexParamKeys
from ...models.history_contents_index_param_limit import HistoryContentsIndexParamLimit
from ...models.history_contents_index_param_offset import HistoryContentsIndexParamOffset
from ...models.history_contents_index_param_order import HistoryContentsIndexParamOrder
from ...models.history_contents_index_param_q import HistoryContentsIndexParamQ
from ...models.history_contents_index_param_qv import HistoryContentsIndexParamQv
from ...models.history_contents_index_param_run_as import HistoryContentsIndexParamRunAs
from ...models.history_contents_index_param_shareable import HistoryContentsIndexParamShareable
from ...models.history_contents_index_param_types import HistoryContentsIndexParamTypes
from ...models.history_contents_index_param_v import HistoryContentsIndexParamV
from ...models.history_contents_index_param_view import HistoryContentsIndexParamView
from ...models.history_contents_index_param_visible import HistoryContentsIndexParamVisible
from ...models.history_contents_index_typed_param_deleted import HistoryContentsIndexTypedParamDeleted
from ...models.history_contents_index_typed_param_details import HistoryContentsIndexTypedParamDetails
from ...models.history_contents_index_typed_param_ids import HistoryContentsIndexTypedParamIds
from ...models.history_contents_index_typed_param_keys import HistoryContentsIndexTypedParamKeys
from ...models.history_contents_index_typed_param_limit import HistoryContentsIndexTypedParamLimit
from ...models.history_contents_index_typed_param_offset import HistoryContentsIndexTypedParamOffset
from ...models.history_contents_index_typed_param_order import HistoryContentsIndexTypedParamOrder
from ...models.history_contents_index_typed_param_q import HistoryContentsIndexTypedParamQ
from ...models.history_contents_index_typed_param_qv import HistoryContentsIndexTypedParamQv
from ...models.history_contents_index_typed_param_run_as import HistoryContentsIndexTypedParamRunAs
from ...models.history_contents_index_typed_param_shareable import HistoryContentsIndexTypedParamShareable
from ...models.history_contents_index_typed_param_types import HistoryContentsIndexTypedParamTypes
from ...models.history_contents_index_typed_param_v import HistoryContentsIndexTypedParamV
from ...models.history_contents_index_typed_param_view import HistoryContentsIndexTypedParamView
from ...models.history_contents_index_typed_param_visible import HistoryContentsIndexTypedParamVisible
from ...models.history_contents_result import HistoryContentsResult
from ...models.history_contents_show_200_response import HistoryContentsShow200Response
from ...models.history_contents_show_legacy_200_response import HistoryContentsShowLegacy200Response
from ...models.history_contents_show_legacy_param_fuzzy_count import HistoryContentsShowLegacyParamFuzzyCount
from ...models.history_contents_show_legacy_param_keys import HistoryContentsShowLegacyParamKeys
from ...models.history_contents_show_legacy_param_run_as import HistoryContentsShowLegacyParamRunAs
from ...models.history_contents_show_legacy_param_view import HistoryContentsShowLegacyParamView
from ...models.history_contents_show_param_fuzzy_count import HistoryContentsShowParamFuzzyCount
from ...models.history_contents_show_param_keys import HistoryContentsShowParamKeys
from ...models.history_contents_show_param_run_as import HistoryContentsShowParamRunAs
from ...models.history_contents_show_param_view import HistoryContentsShowParamView
from ...models.history_contents_update_legacy_200_response import HistoryContentsUpdateLegacy200Response
from ...models.history_contents_update_legacy_param_keys import HistoryContentsUpdateLegacyParamKeys
from ...models.history_contents_update_legacy_param_run_as import HistoryContentsUpdateLegacyParamRunAs
from ...models.history_contents_update_legacy_param_view import HistoryContentsUpdateLegacyParamView
from ...models.history_contents_update_typed_200_response import HistoryContentsUpdateTyped200Response
from ...models.history_contents_update_typed_param_keys import HistoryContentsUpdateTypedParamKeys
from ...models.history_contents_update_typed_param_run_as import HistoryContentsUpdateTypedParamRunAs
from ...models.history_contents_update_typed_param_view import HistoryContentsUpdateTypedParamView
from ...models.history_contents_with_stats_result import HistoryContentsWithStatsResult
from ...models.item_tags_create_payload import ItemTagsCreatePayload
from ...models.item_tags_list_response import ItemTagsListResponse
from ...models.item_tags_response import ItemTagsResponse
from ...models.job_export_history_archive_list_response import JobExportHistoryArchiveListResponse
from ...models.materialize_dataset_instance_api_request_2 import MaterializeDatasetInstanceApiRequest2
from ...models.set_slug_payload import SetSlugPayload
from ...models.share_history_with_status import ShareHistoryWithStatus
from ...models.share_with_payload import ShareWithPayload
from ...models.sharing_status import SharingStatus
from ...models.store_export_payload import StoreExportPayload
from ...models.tool_request_model import ToolRequestModel
from ...models.undelete_histories_payload import UndeleteHistoriesPayload
from ...models.update_history_contents_batch_payload import UpdateHistoryContentsBatchPayload
from ...models.update_history_contents_payload import UpdateHistoryContentsPayload
from ...models.update_history_payload import UpdateHistoryPayload
from ...models.write_store_to_payload import WriteStoreToPayload

if TYPE_CHECKING:
    pass


class MockHistoriesClient:
    """
    Mock implementation of HistoriesClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestHistoriesClient(MockHistoriesClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def dataset_collections_update_collection(
        self,
        hdca_id: str,
        body: UpdateHistoryContentsPayload,
        view: DatasetCollectionsUpdateCollectionParamView | None = None,
        keys: DatasetCollectionsUpdateCollectionParamKeys | None = None,
        run_as: DatasetCollectionsUpdateCollectionParamRunAs | None = None,
    ) -> DatasetCollectionsUpdateCollection200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.dataset_collections_update_collection() not implemented. Override this method in your test subclass."
        )

    async def dataset_collections_download(
        self,
        hdca_id: str,
        run_as: DatasetCollectionsDownloadParamRunAs | None = None,
    ) -> None:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.dataset_collections_download() not implemented. Override this method in your test subclass."
        )

    async def histories_prepare_download_prepare_collection_download(
        self,
        hdca_id: str,
        run_as: HistoriesPrepareDownloadPrepareCollectionDownloadParamRunAs | None = None,
    ) -> AsyncFile:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_prepare_download_prepare_collection_download() not implemented. Override this method in your test subclass."
        )

    async def datasets_delete(
        self,
        dataset_id: str,
        purge: DatasetsDeleteParamPurge | None = None,
        recursive: DatasetsDeleteParamRecursive | None = None,
        stop_job: DatasetsDeleteParamStopJob | None = None,
        run_as: DatasetsDeleteParamRunAs | None = None,
        body: DeleteHistoryContentPayload | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.datasets_delete() not implemented. Override this method in your test subclass."
        )

    async def datasets_update_dataset(
        self,
        dataset_id: str,
        body: UpdateHistoryContentsPayload,
        view: DatasetsUpdateDatasetParamView | None = None,
        keys: DatasetsUpdateDatasetParamKeys | None = None,
        run_as: DatasetsUpdateDatasetParamRunAs | None = None,
    ) -> DatasetsUpdateDataset200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.datasets_update_dataset() not implemented. Override this method in your test subclass."
        )

    async def histories_index(
        self,
        limit: HistoriesIndexParamLimit | None = None,
        offset: HistoriesIndexParamOffset | None = None,
        show_own: bool | None = None,
        show_published: bool | None = None,
        show_shared: bool | None = None,
        show_archived: HistoriesIndexParamShowArchived | None = None,
        sort_by: str | None = None,
        sort_desc: bool | None = None,
        search: HistoriesIndexParamSearch | None = None,
        all_: HistoriesIndexParamAll | None = None,
        deleted: HistoriesIndexParamDeleted | None = None,
        q: HistoriesIndexParamQ | None = None,
        qv: HistoriesIndexParamQv | None = None,
        order: HistoriesIndexParamOrder | None = None,
        view: HistoriesIndexParamView | None = None,
        keys: HistoriesIndexParamKeys | None = None,
        run_as: HistoriesIndexParamRunAs | None = None,
    ) -> list[AnonymousArrayItem91]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_index() not implemented. Override this method in your test subclass."
        )

    async def histories_create(
        self,
        view: HistoriesCreateParamView | None = None,
        keys: HistoriesCreateParamKeys | None = None,
        run_as: HistoriesCreateParamRunAs | None = None,
        form_data: dict[str, Any] = None,
    ) -> HistoriesCreate200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_create() not implemented. Override this method in your test subclass."
        )

    async def histories_archived_get_archived_histories(
        self,
        view: HistoriesArchivedGetArchivedHistoriesParamView | None = None,
        keys: HistoriesArchivedGetArchivedHistoriesParamKeys | None = None,
        q: HistoriesArchivedGetArchivedHistoriesParamQ | None = None,
        qv: HistoriesArchivedGetArchivedHistoriesParamQv | None = None,
        offset: HistoriesArchivedGetArchivedHistoriesParamOffset | None = None,
        limit: HistoriesArchivedGetArchivedHistoriesParamLimit | None = None,
        order: HistoriesArchivedGetArchivedHistoriesParamOrder | None = None,
        run_as: HistoriesArchivedGetArchivedHistoriesParamRunAs | None = None,
    ) -> list[AnonymousArrayItem93]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_archived_get_archived_histories() not implemented. Override this method in your test subclass."
        )

    async def histories_batch_delete_batch_delete(
        self,
        body: DeleteHistoriesPayload,
        purge: bool | None = None,
        view: HistoriesBatchDeleteBatchDeleteParamView | None = None,
        keys: HistoriesBatchDeleteBatchDeleteParamKeys | None = None,
        run_as: HistoriesBatchDeleteBatchDeleteParamRunAs | None = None,
    ) -> list[AnonymousArrayItem95]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_batch_delete_batch_delete() not implemented. Override this method in your test subclass."
        )

    async def histories_batch_undelete_batch_undelete(
        self,
        body: UndeleteHistoriesPayload,
        view: HistoriesBatchUndeleteBatchUndeleteParamView | None = None,
        keys: HistoriesBatchUndeleteBatchUndeleteParamKeys | None = None,
        run_as: HistoriesBatchUndeleteBatchUndeleteParamRunAs | None = None,
    ) -> list[AnonymousArrayItem97]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_batch_undelete_batch_undelete() not implemented. Override this method in your test subclass."
        )

    async def histories_count_count(
        self,
        run_as: HistoriesCountCountParamRunAs | None = None,
    ) -> int:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_count_count() not implemented. Override this method in your test subclass."
        )

    async def histories_deleted_index_deleted(
        self,
        all_: HistoriesDeletedIndexDeletedParamAll | None = None,
        q: HistoriesDeletedIndexDeletedParamQ | None = None,
        qv: HistoriesDeletedIndexDeletedParamQv | None = None,
        offset: HistoriesDeletedIndexDeletedParamOffset | None = None,
        limit: HistoriesDeletedIndexDeletedParamLimit | None = None,
        order: HistoriesDeletedIndexDeletedParamOrder | None = None,
        view: HistoriesDeletedIndexDeletedParamView | None = None,
        keys: HistoriesDeletedIndexDeletedParamKeys | None = None,
        run_as: HistoriesDeletedIndexDeletedParamRunAs | None = None,
    ) -> list[AnonymousArrayItem99]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_deleted_index_deleted() not implemented. Override this method in your test subclass."
        )

    async def histories_deleted_undelete_undelete(
        self,
        history_id: str,
        view: HistoriesDeletedUndeleteUndeleteParamView | None = None,
        keys: HistoriesDeletedUndeleteUndeleteParamKeys | None = None,
        run_as: HistoriesDeletedUndeleteUndeleteParamRunAs | None = None,
    ) -> HistoriesDeletedUndeleteUndelete200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_deleted_undelete_undelete() not implemented. Override this method in your test subclass."
        )

    async def histories_from_store_create_from_store(
        self,
        body: CreateHistoryFromStore,
        view: HistoriesFromStoreCreateFromStoreParamView | None = None,
        keys: HistoriesFromStoreCreateFromStoreParamKeys | None = None,
        run_as: HistoriesFromStoreCreateFromStoreParamRunAs | None = None,
    ) -> HistoriesFromStoreCreateFromStore200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_from_store_create_from_store() not implemented. Override this method in your test subclass."
        )

    async def histories_from_store_async_create_from_store_async(
        self,
        body: CreateHistoryFromStore,
        run_as: HistoriesFromStoreAsyncCreateFromStoreAsyncParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_from_store_async_create_from_store_async() not implemented. Override this method in your test subclass."
        )

    async def histories_most_recently_used_show_recent(
        self,
        view: HistoriesMostRecentlyUsedShowRecentParamView | None = None,
        keys: HistoriesMostRecentlyUsedShowRecentParamKeys | None = None,
        run_as: HistoriesMostRecentlyUsedShowRecentParamRunAs | None = None,
    ) -> HistoriesMostRecentlyUsedShowRecent200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_most_recently_used_show_recent() not implemented. Override this method in your test subclass."
        )

    async def histories_published_published(
        self,
        q: HistoriesPublishedPublishedParamQ | None = None,
        qv: HistoriesPublishedPublishedParamQv | None = None,
        offset: HistoriesPublishedPublishedParamOffset | None = None,
        limit: HistoriesPublishedPublishedParamLimit | None = None,
        order: HistoriesPublishedPublishedParamOrder | None = None,
        view: HistoriesPublishedPublishedParamView | None = None,
        keys: HistoriesPublishedPublishedParamKeys | None = None,
        run_as: HistoriesPublishedPublishedParamRunAs | None = None,
    ) -> list[AnonymousArrayItem101]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_published_published() not implemented. Override this method in your test subclass."
        )

    async def histories_shared_with_me_shared_with_me(
        self,
        q: HistoriesSharedWithMeSharedWithMeParamQ | None = None,
        qv: HistoriesSharedWithMeSharedWithMeParamQv | None = None,
        offset: HistoriesSharedWithMeSharedWithMeParamOffset | None = None,
        limit: HistoriesSharedWithMeSharedWithMeParamLimit | None = None,
        order: HistoriesSharedWithMeSharedWithMeParamOrder | None = None,
        view: HistoriesSharedWithMeSharedWithMeParamView | None = None,
        keys: HistoriesSharedWithMeSharedWithMeParamKeys | None = None,
        run_as: HistoriesSharedWithMeSharedWithMeParamRunAs | None = None,
    ) -> list[AnonymousArrayItem103]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_shared_with_me_shared_with_me() not implemented. Override this method in your test subclass."
        )

    async def histories_delete(
        self,
        history_id: str,
        purge: bool | None = None,
        view: HistoriesDeleteParamView | None = None,
        keys: HistoriesDeleteParamKeys | None = None,
        run_as: HistoriesDeleteParamRunAs | None = None,
        body: HistoriesDeleteRequestBody | None = None,
    ) -> HistoriesDelete200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_delete() not implemented. Override this method in your test subclass."
        )

    async def histories_show(
        self,
        history_id: str,
        view: HistoriesShowParamView | None = None,
        keys: HistoriesShowParamKeys | None = None,
        run_as: HistoriesShowParamRunAs | None = None,
    ) -> HistoriesShow200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_show() not implemented. Override this method in your test subclass."
        )

    async def histories_update(
        self,
        history_id: str,
        body: UpdateHistoryPayload,
        view: HistoriesUpdateParamView | None = None,
        keys: HistoriesUpdateParamKeys | None = None,
        run_as: HistoriesUpdateParamRunAs | None = None,
    ) -> HistoriesUpdate200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_update() not implemented. Override this method in your test subclass."
        )

    async def histories_archive_archive_history(
        self,
        history_id: str,
        run_as: HistoriesArchiveArchiveHistoryParamRunAs | None = None,
        body: HistoriesArchiveArchiveHistoryRequestBody | None = None,
    ) -> HistoriesArchiveArchiveHistory200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_archive_archive_history() not implemented. Override this method in your test subclass."
        )

    async def histories_archive_restore_restore_archived_history(
        self,
        history_id: str,
        force: HistoriesArchiveRestoreRestoreArchivedHistoryParamForce | None = None,
        run_as: HistoriesArchiveRestoreRestoreArchivedHistoryParamRunAs | None = None,
    ) -> HistoriesArchiveRestoreRestoreArchivedHistory200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_archive_restore_restore_archived_history() not implemented. Override this method in your test subclass."
        )

    async def histories_citations_citations(
        self,
        history_id: str,
        run_as: HistoriesCitationsCitationsParamRunAs | None = None,
    ) -> list[dict[str, Any]]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_citations_citations() not implemented. Override this method in your test subclass."
        )

    async def history_contents_index(
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
        offset: HistoryContentsIndexParamOffset | None = None,
        limit: HistoryContentsIndexParamLimit | None = None,
        order: HistoryContentsIndexParamOrder | None = None,
        accept: str | None = None,
        run_as: HistoryContentsIndexParamRunAs | None = None,
    ) -> HistoryContentsResult | HistoryContentsWithStatsResult:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.history_contents_index() not implemented. Override this method in your test subclass."
        )

    async def history_contents_create(
        self,
        history_id: str,
        body: CreateHistoryContentPayload,
        type_: HistoryContentsCreateParamType | None = None,
        view: HistoryContentsCreateParamView | None = None,
        keys: HistoryContentsCreateParamKeys | None = None,
        run_as: HistoryContentsCreateParamRunAs | None = None,
    ) -> HistoryContentsCreate200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.history_contents_create() not implemented. Override this method in your test subclass."
        )

    async def histories_contents_update_batch(
        self,
        history_id: str,
        body: UpdateHistoryContentsBatchPayload,
        view: HistoriesContentsUpdateBatchParamView | None = None,
        keys: HistoriesContentsUpdateBatchParamKeys | None = None,
        run_as: HistoriesContentsUpdateBatchParamRunAs | None = None,
    ) -> HistoryContentsResult:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_contents_update_batch() not implemented. Override this method in your test subclass."
        )

    async def history_contents_archive(
        self,
        history_id: str,
        filename: HistoryContentsArchiveParamFilename | None = None,
        dry_run: HistoryContentsArchiveParamDryRun | None = None,
        q: HistoryContentsArchiveParamQ | None = None,
        qv: HistoryContentsArchiveParamQv | None = None,
        offset: HistoryContentsArchiveParamOffset | None = None,
        limit: HistoryContentsArchiveParamLimit | None = None,
        order: HistoryContentsArchiveParamOrder | None = None,
        run_as: HistoryContentsArchiveParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.history_contents_archive() not implemented. Override this method in your test subclass."
        )

    async def history_contents_archive_named(
        self,
        history_id: str,
        filename: str,
        format_: str,
        dry_run: HistoryContentsArchiveNamedParamDryRun | None = None,
        q: HistoryContentsArchiveNamedParamQ | None = None,
        qv: HistoryContentsArchiveNamedParamQv | None = None,
        offset: HistoryContentsArchiveNamedParamOffset | None = None,
        limit: HistoryContentsArchiveNamedParamLimit | None = None,
        order: HistoryContentsArchiveNamedParamOrder | None = None,
        run_as: HistoryContentsArchiveNamedParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.history_contents_archive_named() not implemented. Override this method in your test subclass."
        )

    async def histories_contents_bulk_bulk_operation(
        self,
        history_id: str,
        body: HistoryContentBulkOperationPayload,
        q: HistoriesContentsBulkBulkOperationParamQ | None = None,
        qv: HistoriesContentsBulkBulkOperationParamQv | None = None,
        run_as: HistoriesContentsBulkBulkOperationParamRunAs | None = None,
    ) -> HistoryContentBulkOperationResult:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_contents_bulk_bulk_operation() not implemented. Override this method in your test subclass."
        )

    async def history_contents_download_collection(
        self,
        hdca_id: str,
        history_id: HistoryContentsDownloadCollectionParamHistoryId | None,
        run_as: HistoryContentsDownloadCollectionParamRunAs | None = None,
    ) -> None:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.history_contents_download_collection() not implemented. Override this method in your test subclass."
        )

    async def histories_contents_datasets_materialize_materialize_dataset(
        self,
        history_id: str,
        id_: str,
        run_as: HistoriesContentsDatasetsMaterializeMaterializeDatasetParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_contents_datasets_materialize_materialize_dataset() not implemented. Override this method in your test subclass."
        )

    async def histories_contents_permissions_update_permissions(
        self,
        history_id: str,
        dataset_id: str,
        body: HistoriesContentsPermissionsUpdatePermissionsRequestBody,
        run_as: HistoriesContentsPermissionsUpdatePermissionsParamRunAs | None = None,
    ) -> DatasetAssociationRoles:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_contents_permissions_update_permissions() not implemented. Override this method in your test subclass."
        )

    async def histories_contents_tags_index(
        self,
        history_content_id: str,
        history_id: str,
        run_as: HistoriesContentsTagsIndexParamRunAs | None = None,
    ) -> ItemTagsListResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_contents_tags_index() not implemented. Override this method in your test subclass."
        )

    async def histories_contents_tags_delete(
        self,
        history_content_id: str,
        tag_name: str,
        history_id: str,
        run_as: HistoriesContentsTagsDeleteParamRunAs | None = None,
    ) -> bool:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_contents_tags_delete() not implemented. Override this method in your test subclass."
        )

    async def histories_contents_tags_show(
        self,
        history_content_id: str,
        tag_name: str,
        history_id: str,
        run_as: HistoriesContentsTagsShowParamRunAs | None = None,
    ) -> ItemTagsResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_contents_tags_show() not implemented. Override this method in your test subclass."
        )

    async def histories_contents_tags_create(
        self,
        history_content_id: str,
        tag_name: str,
        history_id: str,
        run_as: HistoriesContentsTagsCreateParamRunAs | None = None,
        body: ItemTagsCreatePayload | None = None,
    ) -> ItemTagsResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_contents_tags_create() not implemented. Override this method in your test subclass."
        )

    async def histories_contents_tags_update(
        self,
        history_content_id: str,
        tag_name: str,
        history_id: str,
        body: ItemTagsCreatePayload,
        run_as: HistoriesContentsTagsUpdateParamRunAs | None = None,
    ) -> ItemTagsResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_contents_tags_update() not implemented. Override this method in your test subclass."
        )

    async def history_contents_delete_legacy(
        self,
        history_id: str,
        id_: str,
        type_: HistoryContentType | None = None,
        purge: HistoryContentsDeleteLegacyParamPurge | None = None,
        recursive: HistoryContentsDeleteLegacyParamRecursive | None = None,
        stop_job: HistoryContentsDeleteLegacyParamStopJob | None = None,
        run_as: HistoryContentsDeleteLegacyParamRunAs | None = None,
        body: DeleteHistoryContentPayload | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.history_contents_delete_legacy() not implemented. Override this method in your test subclass."
        )

    async def history_contents_show_legacy(
        self,
        id_: str,
        history_id: str,
        type_: HistoryContentType | None = None,
        fuzzy_count: HistoryContentsShowLegacyParamFuzzyCount | None = None,
        view: HistoryContentsShowLegacyParamView | None = None,
        keys: HistoryContentsShowLegacyParamKeys | None = None,
        run_as: HistoryContentsShowLegacyParamRunAs | None = None,
    ) -> HistoryContentsShowLegacy200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.history_contents_show_legacy() not implemented. Override this method in your test subclass."
        )

    async def history_contents_update_legacy(
        self,
        history_id: str,
        id_: str,
        body: UpdateHistoryContentsPayload,
        type_: HistoryContentType | None = None,
        view: HistoryContentsUpdateLegacyParamView | None = None,
        keys: HistoryContentsUpdateLegacyParamKeys | None = None,
        run_as: HistoryContentsUpdateLegacyParamRunAs | None = None,
    ) -> HistoryContentsUpdateLegacy200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.history_contents_update_legacy() not implemented. Override this method in your test subclass."
        )

    async def histories_contents_validate_validate(
        self,
        history_id: str,
        id_: str,
        run_as: HistoriesContentsValidateValidateParamRunAs | None = None,
    ) -> HistoriesContentsValidateValidate200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_contents_validate_validate() not implemented. Override this method in your test subclass."
        )

    async def history_contents_index_typed(
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
        offset: HistoryContentsIndexTypedParamOffset | None = None,
        limit: HistoryContentsIndexTypedParamLimit | None = None,
        order: HistoryContentsIndexTypedParamOrder | None = None,
        accept: str | None = None,
        run_as: HistoryContentsIndexTypedParamRunAs | None = None,
    ) -> HistoryContentsResult | HistoryContentsWithStatsResult:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.history_contents_index_typed() not implemented. Override this method in your test subclass."
        )

    async def history_contents_create_typed(
        self,
        history_id: str,
        type_: HistoryContentType,
        body: CreateHistoryContentPayload,
        view: HistoryContentsCreateTypedParamView | None = None,
        keys: HistoryContentsCreateTypedParamKeys | None = None,
        run_as: HistoryContentsCreateTypedParamRunAs | None = None,
    ) -> HistoryContentsCreateTyped200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.history_contents_create_typed() not implemented. Override this method in your test subclass."
        )

    async def history_contents_delete_typed(
        self,
        history_id: str,
        id_: str,
        type_: HistoryContentType,
        purge: HistoryContentsDeleteTypedParamPurge | None = None,
        recursive: HistoryContentsDeleteTypedParamRecursive | None = None,
        stop_job: HistoryContentsDeleteTypedParamStopJob | None = None,
        run_as: HistoryContentsDeleteTypedParamRunAs | None = None,
        body: DeleteHistoryContentPayload | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.history_contents_delete_typed() not implemented. Override this method in your test subclass."
        )

    async def history_contents_show(
        self,
        id_: str,
        history_id: str,
        type_: HistoryContentType,
        fuzzy_count: HistoryContentsShowParamFuzzyCount | None = None,
        view: HistoryContentsShowParamView | None = None,
        keys: HistoryContentsShowParamKeys | None = None,
        run_as: HistoryContentsShowParamRunAs | None = None,
    ) -> HistoryContentsShow200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.history_contents_show() not implemented. Override this method in your test subclass."
        )

    async def history_contents_update_typed(
        self,
        history_id: str,
        id_: str,
        type_: HistoryContentType,
        body: UpdateHistoryContentsPayload,
        view: HistoryContentsUpdateTypedParamView | None = None,
        keys: HistoryContentsUpdateTypedParamKeys | None = None,
        run_as: HistoryContentsUpdateTypedParamRunAs | None = None,
    ) -> HistoryContentsUpdateTyped200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.history_contents_update_typed() not implemented. Override this method in your test subclass."
        )

    async def histories_contents_jobs_summary_show_jobs_summary(
        self,
        history_id: str,
        id_: str,
        type_: HistoryContentType,
        run_as: HistoriesContentsJobsSummaryShowJobsSummaryParamRunAs | None = None,
    ) -> HistoriesContentsJobsSummaryShowJobsSummary200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_contents_jobs_summary_show_jobs_summary() not implemented. Override this method in your test subclass."
        )

    async def histories_contents_prepare_store_download_prepare_store_download(
        self,
        history_id: str,
        id_: str,
        type_: HistoryContentType,
        body: StoreExportPayload,
        run_as: HistoriesContentsPrepareStoreDownloadPrepareStoreDownloadParamRunAs | None = None,
    ) -> AsyncFile:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_contents_prepare_store_download_prepare_store_download() not implemented. Override this method in your test subclass."
        )

    async def histories_contents_write_store_write_store(
        self,
        history_id: str,
        id_: str,
        type_: HistoryContentType,
        body: WriteStoreToPayload,
        run_as: HistoriesContentsWriteStoreWriteStoreParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_contents_write_store_write_store() not implemented. Override this method in your test subclass."
        )

    async def histories_contents_from_store_create_from_store(
        self,
        history_id: str,
        body: CreateHistoryContentFromStore,
        view: HistoriesContentsFromStoreCreateFromStoreParamView | None = None,
        keys: HistoriesContentsFromStoreCreateFromStoreParamKeys | None = None,
        run_as: HistoriesContentsFromStoreCreateFromStoreParamRunAs | None = None,
    ) -> list[AnonymousArrayItem109]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_contents_from_store_create_from_store() not implemented. Override this method in your test subclass."
        )

    async def history_contents_copy_contents(
        self,
        history_id: str,
        body: CopyDatasetsPayload,
        run_as: HistoryContentsCopyContentsParamRunAs | None = None,
    ) -> CopyDatasetsResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.history_contents_copy_contents() not implemented. Override this method in your test subclass."
        )

    async def histories_custom_builds_metadata_get_custom_builds_metadata(
        self,
        history_id: str,
        run_as: HistoriesCustomBuildsMetadataGetCustomBuildsMetadataParamRunAs | None = None,
    ) -> CustomBuildsMetadataResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_custom_builds_metadata_get_custom_builds_metadata() not implemented. Override this method in your test subclass."
        )

    async def histories_disable_link_access_disable_link_access(
        self,
        history_id: str,
        run_as: HistoriesDisableLinkAccessDisableLinkAccessParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_disable_link_access_disable_link_access() not implemented. Override this method in your test subclass."
        )

    async def histories_enable_link_access_enable_link_access(
        self,
        history_id: str,
        run_as: HistoriesEnableLinkAccessEnableLinkAccessParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_enable_link_access_enable_link_access() not implemented. Override this method in your test subclass."
        )

    async def histories_exports_index_exports(
        self,
        history_id: str,
        limit: HistoriesExportsIndexExportsParamLimit | None = None,
        offset: HistoriesExportsIndexExportsParamOffset | None = None,
        accept: str | None = None,
        run_as: HistoriesExportsIndexExportsParamRunAs | None = None,
    ) -> JobExportHistoryArchiveListResponse | ExportTaskListResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_exports_index_exports() not implemented. Override this method in your test subclass."
        )

    async def histories_exports_archive_export(
        self,
        history_id: str,
        run_as: HistoriesExportsArchiveExportParamRunAs | None = None,
        body: HistoriesExportsArchiveExportRequestBody | None = None,
    ) -> HistoriesExportsArchiveExport200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_exports_archive_export() not implemented. Override this method in your test subclass."
        )

    async def histories_exports_archive_download(
        self,
        history_id: str,
        jeha_id: HistoriesExportsArchiveDownloadParamJehaId,
        run_as: HistoriesExportsArchiveDownloadParamRunAs | None = None,
    ) -> None:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_exports_archive_download() not implemented. Override this method in your test subclass."
        )

    async def histories_jobs_summary_index_jobs_summary(
        self,
        history_id: str,
        ids: HistoriesJobsSummaryIndexJobsSummaryParamIds | None = None,
        types: HistoriesJobsSummaryIndexJobsSummaryParamTypes | None = None,
        run_as: HistoriesJobsSummaryIndexJobsSummaryParamRunAs | None = None,
    ) -> list[AnonymousArrayItem111]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_jobs_summary_index_jobs_summary() not implemented. Override this method in your test subclass."
        )

    async def histories_materialize_materialize_to_history(
        self,
        history_id: str,
        body: MaterializeDatasetInstanceApiRequest2,
        run_as: HistoriesMaterializeMaterializeToHistoryParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_materialize_materialize_to_history() not implemented. Override this method in your test subclass."
        )

    async def histories_prepare_store_download_prepare_store_download(
        self,
        history_id: str,
        body: StoreExportPayload,
        run_as: HistoriesPrepareStoreDownloadPrepareStoreDownloadParamRunAs | None = None,
    ) -> AsyncFile:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_prepare_store_download_prepare_store_download() not implemented. Override this method in your test subclass."
        )

    async def histories_publish_publish(
        self,
        history_id: str,
        run_as: HistoriesPublishPublishParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_publish_publish() not implemented. Override this method in your test subclass."
        )

    async def histories_share_with_users_share_with_users(
        self,
        history_id: str,
        body: ShareWithPayload,
        run_as: HistoriesShareWithUsersShareWithUsersParamRunAs | None = None,
    ) -> ShareHistoryWithStatus:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_share_with_users_share_with_users() not implemented. Override this method in your test subclass."
        )

    async def histories_sharing_sharing(
        self,
        history_id: str,
        run_as: HistoriesSharingSharingParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_sharing_sharing() not implemented. Override this method in your test subclass."
        )

    async def histories_slug_set_slug(
        self,
        history_id: str,
        body: SetSlugPayload,
        run_as: HistoriesSlugSetSlugParamRunAs | None = None,
    ) -> None:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_slug_set_slug() not implemented. Override this method in your test subclass."
        )

    async def histories_tags_index(
        self,
        history_id: str,
        run_as: HistoriesTagsIndexParamRunAs | None = None,
    ) -> ItemTagsListResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_tags_index() not implemented. Override this method in your test subclass."
        )

    async def histories_tags_delete(
        self,
        history_id: str,
        tag_name: str,
        run_as: HistoriesTagsDeleteParamRunAs | None = None,
    ) -> bool:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_tags_delete() not implemented. Override this method in your test subclass."
        )

    async def histories_tags_show(
        self,
        history_id: str,
        tag_name: str,
        run_as: HistoriesTagsShowParamRunAs | None = None,
    ) -> ItemTagsResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_tags_show() not implemented. Override this method in your test subclass."
        )

    async def histories_tags_create(
        self,
        history_id: str,
        tag_name: str,
        run_as: HistoriesTagsCreateParamRunAs | None = None,
        body: ItemTagsCreatePayload | None = None,
    ) -> ItemTagsResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_tags_create() not implemented. Override this method in your test subclass."
        )

    async def histories_tags_update(
        self,
        history_id: str,
        tag_name: str,
        body: ItemTagsCreatePayload,
        run_as: HistoriesTagsUpdateParamRunAs | None = None,
    ) -> ItemTagsResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_tags_update() not implemented. Override this method in your test subclass."
        )

    async def histories_tool_requests_tool_requests(
        self,
        history_id: str,
        run_as: HistoriesToolRequestsToolRequestsParamRunAs | None = None,
    ) -> list[ToolRequestModel]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_tool_requests_tool_requests() not implemented. Override this method in your test subclass."
        )

    async def histories_unpublish_unpublish(
        self,
        history_id: str,
        run_as: HistoriesUnpublishUnpublishParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_unpublish_unpublish() not implemented. Override this method in your test subclass."
        )

    async def histories_write_store_write_store(
        self,
        history_id: str,
        body: WriteStoreToPayload,
        run_as: HistoriesWriteStoreWriteStoreParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockHistoriesClient.histories_write_store_write_store() not implemented. Override this method in your test subclass."
        )
