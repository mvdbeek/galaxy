"""
Synchronous client template that will be transformed by AST manipulation.
"""

from __future__ import annotations

from typing import Any, Literal

import httpx

from .base_client import BaseClient, Response
from .models import (
    AgentListResponse,
    AgentQueryRequest,
    AgentQueryResponse,
    AgentResponse,
    AnonUserModel,
    APIKeyModel,
    APIKeyResponse,
    ArchivedHistoryDetailed,
    ArchivedHistorySummary,
    ArchiveHistoryRequestPayload,
    AsyncFile,
    AsyncTaskResultSummary,
    BaseUrlParameterModel,
    BodyAi_agentsCustomTool_createCustomTool,
    BodyAi_agentsErrorAnalysis_analyzeError,
    BodyLibraries_contents_createForm,
    BodyTools_fetch_fetchForm,
    BooleanParameterModel,
    BroadcastNotificationCreateRequest,
    BroadcastNotificationResponse,
    ChatPayload,
    ChatResponse,
    CheckForUpdatesResponse,
    ClaimLandingPayload,
    CleanableItemsSummary,
    CleanupStorageItemsRequest,
    ColorParameterModel,
    ComputeDatasetHashPayload,
    ConcreteObjectStoreModel,
    ConditionalParameterModelOutput,
    ContextResponse,
    ConvertedDatasetsMap,
    CopyDatasetsPayload,
    CopyDatasetsResponse,
    CreateDataLandingPayload,
    CreatedEntryResponse,
    CreatedUserModel,
    CreateEntryPayload,
    CreateFileLandingPayload,
    CreateHistoryContentFromStore,
    CreateHistoryContentPayload,
    CreateHistoryFromStore,
    CreateInstancePayload,
    CreateInvocationsFromStorePayload,
    CreateLibrariesFromStore,
    CreateLibraryFilePayload,
    CreateLibraryFolderPayload,
    CreateLibraryPayload,
    CreateLinkFeedback,
    CreateLinkIncoming,
    CreateMetricsPayload,
    CreateNewCollectionPayload,
    CreatePagePayload,
    CreateQuotaParams,
    CreateQuotaResult,
    CreateSourceCredentialsPayload,
    CreateToolLandingRequestPayload,
    CreateWorkbookForCollectionApi,
    CreateWorkbookRequest,
    CreateWorkflowLandingRequestPayload,
    CustomArchivedHistoryView,
    CustomBuildCreationPayload,
    CustomBuildsMetadataResponse,
    CustomHistoryView,
    CwlBooleanParameterModel,
    CwlDirectoryParameterModel,
    CwlFileParameterModel,
    CwlFloatParameterModel,
    CwlIntegerParameterModel,
    CwlNullParameterModel,
    CwlStringParameterModel,
    CwlUnionParameterModelOutput,
    DataCollectionParameterModel,
    DataColumnParameterModel,
    DataParameterModel,
    DatasetAssociationRoles,
    DatasetCollectionAttributesResult,
    DatasetContentType,
    DatasetSourceType,
    DatasetStorageDetails,
    DatasetTextContentDetails,
    DatatypeDetails,
    DatatypesCombinedMap,
    DatatypesEDAMDetailsDict,
    DatatypesMap,
    DCESummary,
    DeleteDatasetBatchPayload,
    DeleteDatasetBatchResult,
    DeletedCustomBuild,
    DeleteHistoriesPayload,
    DeleteHistoryContentPayload,
    DeleteHistoryPayload,
    DeleteJobPayload,
    DeleteLibraryPayload,
    DeleteQuotaPayload,
    DetailedUserModel,
    DirectoryUriParameterModel,
    DisplayApplication,
    DrillDownParameterModelOutput,
    DrsObject,
    DynamicToolCreatePayload,
    DynamicUnprivilegedToolCreatePayload,
    EncodedJobDetails,
    ExportHistoryArchivePayload,
    FavoriteObject,
    FavoriteObjectsSummary,
    FavoriteObjectType,
    FloatParameterModel,
    GenerateTourResponse,
    GenomeBuildParameterModel,
    GroupCreatePayload,
    GroupResponse,
    GroupRoleResponse,
    GroupTagParameterModel,
    GroupUpdatePayload,
    GroupUserResponse,
    HDACustom,
    HDADetailed,
    HDAInaccessible,
    HDASummary,
    HDCACustom,
    HDCADetailed,
    HDCASummary,
    HelpForumSearchResponse,
    HiddenParameterModel,
    HistoryContentBulkOperationPayload,
    HistoryContentBulkOperationResult,
    HistoryContentType,
    HistoryDetailed,
    HistorySummary,
    ImplicitCollectionJobsStateSummary,
    ImportToolDataBundle,
    InstalledToolShedRepository,
    IntegerParameterModel,
    InvocationJobsResponse,
    InvocationReport,
    InvocationSortByEnum,
    InvocationStep,
    InvocationStepJobsResponseCollectionJobsModel,
    InvocationStepJobsResponseJobModel,
    InvocationStepJobsResponseStepModel,
    InvocationUpdatePayload,
    InvokeWorkflowPayload,
    ItemTagsCreatePayload,
    ItemTagsPayload,
    ItemTagsResponse,
    JobConsoleOutput,
    JobCreateResponse,
    JobDestinationParams,
    JobDisplayParametersSummary,
    JobErrorSummary,
    JobExportHistoryArchiveModel,
    JobIdResponse,
    JobImportHistoryResponse,
    JobIndexSortByEnum,
    JobIndexViewEnum,
    JobInputAssociation,
    JobInputSummary,
    JobLock,
    JobMetric,
    JobOutputAssociation,
    JobOutputCollectionAssociation,
    JobRequest,
    JobStateSummary,
    JobSummary,
    LegacyLibraryPermissionsPayload,
    LibraryAvailablePermissions,
    LibraryContentsCreateDatasetResponse,
    LibraryContentsDeletePayload,
    LibraryContentsDeleteResponse,
    LibraryContentsShowDatasetResponse,
    LibraryContentsShowFolderResponse,
    LibraryCurrentPermissions,
    LibraryFolderContentsIndexResult,
    LibraryFolderCurrentPermissions,
    LibraryFolderDetails,
    LibraryFolderPermissionAction,
    LibraryFolderPermissionsPayload,
    LibraryLegacySummary,
    LibraryPermissionAction,
    LibraryPermissionScope,
    LibraryPermissionsPayload,
    LibrarySummary,
    LicenseMetadataModel,
    LimitedUserModel,
    MaterializeDatasetInstanceAPIRequest,
    NotificationBroadcastUpdateRequest,
    NotificationCreatedResponse,
    NotificationCreateRequest,
    NotificationsBatchRequest,
    NotificationsBatchUpdateResponse,
    NotificationStatusSummary,
    OAuth2Info,
    PageDetails,
    PageSummary,
    ParsedFetchWorkbookForCollections,
    ParsedFetchWorkbookForDatasets,
    ParsedWorkbook,
    ParsedWorkbookForCollection,
    ParseFetchWorkbook,
    ParseWorkbook,
    ParseWorkbookForCollectionApi,
    PathBasedDynamicToolCreatePayload,
    PluginKind,
    PluginStatus,
    PrepareStoreDownloadPayload,
    QuotaDetails,
    RefactorRequest,
    RefactorResponse,
    ReloadFeedback,
    RemoteFilesDisableMode,
    RemoteFilesFormat,
    RemoteUserCreationPayload,
    RepeatParameterModelOutput,
    ReportInvocationErrorPayload,
    ReportJobErrorPayload,
    RequestDataType,
    RoleDefinitionModel,
    RoleModelResponse,
    RootModelDictStr_int_,
    RulesParameterModel,
    SearchJobsPayload,
    SectionParameterModelOutput,
    SelectParameterModel,
    SelectServiceCredentialPayload,
    Service,
    ServiceCredentialGroupPayload,
    ServiceCredentialGroupResponse,
    SetSlugPayload,
    ShareHistoryWithStatus,
    ShareWithPayload,
    ShareWithStatus,
    SharingStatus,
    ShowFullJobResponse,
    StorageItemsCleanupResult,
    StoredItem,
    StoredItemOrderBy,
    StoredWorkflowDetailed,
    StoreExportPayload,
    TaskResult,
    TaskState,
    TestUpdateInstancePayload,
    TestUpgradeInstancePayload,
    TextParameterModel,
    ToolDataDetails,
    ToolDataField,
    ToolDataItem,
    ToolLandingRequest,
    ToolReportForDataset,
    ToolRequestDetailedModel,
    ToolRequestModel,
    TourDetails,
    UndeleteHistoriesPayload,
    UnprivilegedToolResponse,
    UpdateCollectionAttributePayload,
    UpdateDatasetPermissionsPayload,
    UpdateDatasetPermissionsPayloadAliasB,
    UpdateDatasetPermissionsPayloadAliasC,
    UpdateHistoryContentsBatchPayload,
    UpdateHistoryContentsPayload,
    UpdateHistoryPayload,
    UpdateInstancePayload,
    UpdateInstanceSecretPayload,
    UpdateLibraryFolderPayload,
    UpdateLibraryPayload,
    UpdateObjectStoreIdPayload,
    UpdatePagePayload,
    UpdateQuotaParams,
    UpdateUserNotificationPreferencesRequest,
    UpgradeInstancePayload,
    UserBeaconSetting,
    UserConcreteObjectStoreModel,
    UserCreationPayload,
    UserDeletionPayload,
    UserFileSourceModel,
    UserModel,
    UserNotificationPreferences,
    UserNotificationResponse,
    UserNotificationsBatchUpdateRequest,
    UserNotificationUpdateRequest,
    UserObjectstoreUsage,
    UserQuotaUsage,
    UserUpdatePayload,
    VisualizationCreatePayload,
    VisualizationCreateResponse,
    VisualizationShowResponse,
    VisualizationUpdatePayload,
    VisualizationUpdateResponse,
    WorkflowInvocationRequestModel,
    WorkflowInvocationStateSummary,
    WorkflowJobMetric,
    WorkflowLandingRequest,
    WriteInvocationStoreToPayload,
    WriteStoreToPayload,
)


class APIClient(BaseClient):
    """Galaxy API client."""

    def __init__(
        self,
        base_url: str,
        *,
        api_key: str | None = None,
        bearer_token: str | None = None,
        timeout: float = 30.0,
        verify_ssl: bool = True,
        follow_redirects: bool = True,
        default_headers: dict[str, str] | None = None,
    ):
        super().__init__(
            base_url=base_url,
            api_key=api_key,
            bearer_token=bearer_token,
            timeout=timeout,
            verify_ssl=verify_ssl,
            follow_redirects=follow_redirects,
            default_headers=default_headers,
        )
        self._client: httpx.Client | None = None

    def _get_client(self) -> httpx.Client:
        """Get or create HTTP client."""
        if self._client is None:
            self._client = httpx.Client(
                base_url=self.base_url,
                timeout=self.timeout,
                verify=self.verify_ssl,
                follow_redirects=self.follow_redirects,
                headers=self._get_headers(),
            )
        return self._client

    def close(self) -> None:
        """Close HTTP client."""
        if self._client:
            self._client.close()
            self._client = None

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()

    def ai__agents__list_agents(self, *, run_as: str | None = None) -> Response[AgentListResponse]:
        """List Agents

        **Warning**: This API is unstable and may change without notice."""
        client = self._get_client()
        response = client.get("/api/ai/agents", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = AgentListResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def ai__agents_custom_tool__create_custom_tool(
        self, data: BodyAi_agentsCustomTool_createCustomTool, *, run_as: str | None = None
    ) -> Response[AgentResponse]:
        """Create Custom Tool

        **Warning**: This API is unstable and may change without notice."""
        client = self._get_client()
        response = client.post(
            "/api/ai/agents/custom-tool", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = AgentResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def ai__agents_error_analysis__analyze_error(
        self, data: BodyAi_agentsErrorAnalysis_analyzeError, *, run_as: str | None = None
    ) -> Response[AgentResponse]:
        """Analyze Error

        **Warning**: This API is unstable and may change without notice."""
        client = self._get_client()
        response = client.post(
            "/api/ai/agents/error-analysis", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = AgentResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def ai__agents_query__query_agent(
        self, data: AgentQueryRequest, *, run_as: str | None = None
    ) -> Response[AgentQueryResponse]:
        """Query Agent

        **Warning**: This API is unstable and may change without notice."""
        client = self._get_client()
        response = client.post(
            "/api/ai/agents/query", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = AgentQueryResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def authenticate__baseauth__get_api_key(self) -> Response[APIKeyResponse]:
        """Returns returns an API key for authenticated user based on BaseAuth headers."""
        client = self._get_client()
        response = client.get("/api/authenticate/baseauth")
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = APIKeyResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def chat__query(
        self,
        data: ChatPayload | None,
        *,
        job_id: str | None = None,
        query: str | None = None,
        agent_type: str | None = None,
        run_as: str | None = None,
    ) -> Response[ChatResponse]:
        """Query

        **Warning**: This API is unstable and may change without notice."""
        client = self._get_client()
        response = client.post(
            "/api/chat",
            params=self._filter_none_values({"job_id": job_id, "query": query, "agent_type": agent_type}),
            headers={"run-as": run_as},
            json=data,
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ChatResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def chat__exchange_feedback__set_exchange_feedback(
        self, exchange_id: int, data: int, *, run_as: str | None = None
    ) -> Response[dict[str, Any]]:
        """Set Exchange Feedback

        **Warning**: This API is unstable and may change without notice."""
        client = self._get_client()
        response = client.put(f"/api/chat/exchange/{exchange_id}/feedback", headers={"run-as": run_as}, json=data)
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def chat__exchange_messages__get_exchange_messages(
        self, exchange_id: int, *, run_as: str | None = None
    ) -> Response[list[dict[str, Any]]]:
        """Get Exchange Messages

        **Warning**: This API is unstable and may change without notice."""
        client = self._get_client()
        response = client.get(f"/api/chat/exchange/{exchange_id}/messages", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [dict[str, Any].model_validate(item) for item in response.json()]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def chat__history__clear_chat_history(self, *, run_as: str | None = None) -> Response[dict[str, Any]]:
        """Clear Chat History

        **Warning**: This API is unstable and may change without notice."""
        client = self._get_client()
        response = client.delete("/api/chat/history", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def chat__history__get_chat_history(
        self, *, limit: int | None = None, run_as: str | None = None
    ) -> Response[list[dict[str, Any]]]:
        """Get Chat History

        **Warning**: This API is unstable and may change without notice."""
        client = self._get_client()
        response = client.get(
            "/api/chat/history", params=self._filter_none_values({"limit": limit}), headers={"run-as": run_as}
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [dict[str, Any].model_validate(item) for item in response.json()]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def chat__feedback__feedback(
        self, job_id: str, *, feedback: int, run_as: str | None = None
    ) -> Response[int | None]:
        """Feedback

        **Warning**: This API is unstable and may change without notice."""
        client = self._get_client()
        response = client.put(
            f"/api/chat/{job_id}/feedback",
            params=self._filter_none_values({"feedback": feedback}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = int | None.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def configuration__index(
        self, *, view: str | None = None, keys: str | None = None, run_as: str | None = None
    ) -> Response[dict[str, Any]]:
        """Return an object containing exposable configuration settings

        Return an object containing exposable configuration settings.

        A more complete list is returned if the user is an admin.
        Pass in `view` and a comma-seperated list of keys to control which
        configuration settings are returned."""
        client = self._get_client()
        response = client.get(
            "/api/configuration",
            params=self._filter_none_values({"view": view, "keys": keys}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def configuration__decode__decode_id(
        self, encoded_id: str, *, run_as: str | None = None
    ) -> Response[dict[str, Any]]:
        """Decode a given id

        Decode a given id."""
        client = self._get_client()
        response = client.get(f"/api/configuration/decode/{encoded_id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def configuration__dynamic_tool_confs__dynamic_tool_confs(
        self, *, run_as: str | None = None
    ) -> Response[list[dict[str, Any]]]:
        """Return dynamic tool configuration files

        Return dynamic tool configuration files."""
        client = self._get_client()
        response = client.get("/api/configuration/dynamic_tool_confs", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [dict[str, Any].model_validate(item) for item in response.json()]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def configuration__encode__encode_id(
        self, decoded_id: int, *, run_as: str | None = None
    ) -> Response[dict[str, Any]]:
        """Encode a given id

        Decode a given id."""
        client = self._get_client()
        response = client.get(f"/api/configuration/encode/{decoded_id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def configuration__tool_lineages__tool_lineages(
        self, *, run_as: str | None = None
    ) -> Response[list[dict[str, Any]]]:
        """Return tool lineages for tools that have them

        Return tool lineages for tools that have them."""
        client = self._get_client()
        response = client.get("/api/configuration/tool_lineages", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [dict[str, Any].model_validate(item) for item in response.json()]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def configuration__toolbox__reload_toolbox(self, *, run_as: str | None = None) -> Response[Any]:
        """Reload the Galaxy toolbox (but not individual tools)

        Reload the Galaxy toolbox (but not individual tools)."""
        client = self._get_client()
        response = client.put("/api/configuration/toolbox", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def tools__create_data_landing(
        self, data: CreateDataLandingPayload, *, run_as: str | None = None
    ) -> Response[ToolLandingRequest]:
        """Create Data Landing"""
        client = self._get_client()
        response = client.post(
            "/api/data_landings", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ToolLandingRequest.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def dataset_collections__content(self, dce_id: str, *, run_as: str | None = None) -> Response[DCESummary]:
        """Content"""
        client = self._get_client()
        response = client.get(f"/api/dataset_collection_element/{dce_id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = DCESummary.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def dataset_collections__create(
        self, data: CreateNewCollectionPayload, *, run_as: str | None = None
    ) -> Response[HDCADetailed]:
        """Create a new dataset collection instance."""
        client = self._get_client()
        response = client.post(
            "/api/dataset_collections", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = HDCADetailed.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def dataset_collections__show(
        self,
        hdca_id: str,
        *,
        instance_type: Literal["history", "library"] | None = None,
        view: str | None = None,
        run_as: str | None = None,
    ) -> Response[HDCACustom | HDCADetailed | HDCASummary]:
        """Returns detailed information about the given collection."""
        client = self._get_client()
        response = client.get(
            f"/api/dataset_collections/{hdca_id}",
            params=self._filter_none_values({"instance_type": instance_type, "view": view}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = HDCACustom | HDCADetailed | HDCASummary.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def dataset_collections__update_collection(
        self,
        hdca_id: str,
        data: UpdateHistoryContentsPayload,
        *,
        view: str | None = None,
        keys: str | None = None,
        run_as: str | None = None,
    ) -> Response[HDACustom | HDADetailed | HDASummary | HDAInaccessible | HDCACustom | HDCADetailed | HDCASummary]:
        """Updates the values for the history dataset (HDA) item with the given ``ID``.

        Updates the values for the history content item with the given ``ID``."""
        client = self._get_client()
        response = client.put(
            f"/api/dataset_collections/{hdca_id}",
            params=self._filter_none_values({"view": view, "keys": keys}),
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = (
                HDACustom
                | HDADetailed
                | HDASummary
                | HDAInaccessible
                | HDCACustom
                | HDCADetailed
                | HDCASummary.model_validate(response.json())
            )
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def dataset_collections__attributes__attributes(
        self, hdca_id: str, *, instance_type: Literal["history", "library"] | None = None, run_as: str | None = None
    ) -> Response[DatasetCollectionAttributesResult]:
        """Returns `dbkey`/`extension` attributes for all the collection elements."""
        client = self._get_client()
        response = client.get(
            f"/api/dataset_collections/{hdca_id}/attributes",
            params=self._filter_none_values({"instance_type": instance_type}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = DatasetCollectionAttributesResult.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def dataset_collections__contents__contents(
        self,
        hdca_id: str,
        parent_id: str,
        *,
        instance_type: Literal["history", "library"] | None = None,
        limit: int | None = None,
        offset: int | None = None,
        run_as: str | None = None,
    ) -> Response[DatasetCollectionContentElements]:
        """Returns direct child contents of indicated dataset collection parent ID."""
        client = self._get_client()
        response = client.get(
            f"/api/dataset_collections/{hdca_id}/contents/{parent_id}",
            params=self._filter_none_values({"instance_type": instance_type, "limit": limit, "offset": offset}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = DatasetCollectionContentElements.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def dataset_collections__copy__copy(
        self, hdca_id: str, data: UpdateCollectionAttributePayload, *, run_as: str | None = None
    ) -> Response[Any]:
        """Copy the given collection datasets to a new collection using a new `dbkey` attribute."""
        client = self._get_client()
        response = client.post(
            f"/api/dataset_collections/{hdca_id}/copy",
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def dataset_collections__download(self, hdca_id: str, *, run_as: str | None = None) -> Response[Any]:
        """Download the content of a dataset collection as a `zip` archive.

        Download the content of a history dataset collection as a `zip` archive
        while maintaining approximate collection structure."""
        client = self._get_client()
        response = client.get(f"/api/dataset_collections/{hdca_id}/download", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__prepare_download__prepare_collection_download(
        self, hdca_id: str, *, run_as: str | None = None
    ) -> Response[AsyncFile]:
        """Prepare an short term storage object that the collection will be downloaded to.

        The history dataset collection will be written as a `zip` archive to the
        returned short term storage object. Progress tracking this file's creation
        can be tracked with the short_term_storage API."""
        client = self._get_client()
        response = client.post(f"/api/dataset_collections/{hdca_id}/prepare_download", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = AsyncFile.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def dataset_collections__workbook_download_for_collection(
        self,
        hdca_id: str,
        data: CreateWorkbookForCollectionApi,
        *,
        filename: str | None = None,
        run_as: str | None = None,
    ) -> Response[Any]:
        """Create an XLSX workbook for a sample sheet definition targeting an existing collection."""
        client = self._get_client()
        response = client.post(
            f"/api/dataset_collections/{hdca_id}/sample_sheet_workbook",
            params=self._filter_none_values({"filename": filename}),
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def dataset_collections__workbook_parse_for_collection(
        self, hdca_id: str, data: ParseWorkbookForCollectionApi, *, run_as: str | None = None
    ) -> Response[ParsedWorkbookForCollection]:
        """Parse an XLSX workbook for a sample sheet definition and supplied file contents."""
        client = self._get_client()
        response = client.post(
            f"/api/dataset_collections/{hdca_id}/sample_sheet_workbook/parse",
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ParsedWorkbookForCollection.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def dataset_collections__suitable_converters__suitable_converters(
        self, hdca_id: str, *, instance_type: Literal["history", "library"] | None = None, run_as: str | None = None
    ) -> Response[SuitableConverters]:
        """Returns a list of applicable converters for all datatypes in the given collection."""
        client = self._get_client()
        response = client.get(
            f"/api/dataset_collections/{hdca_id}/suitable_converters",
            params=self._filter_none_values({"instance_type": instance_type}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = SuitableConverters.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def datasets__delete_batch(
        self, data: DeleteDatasetBatchPayload, *, run_as: str | None = None
    ) -> Response[DeleteDatasetBatchResult]:
        """Deletes or purges a batch of datasets.

        Deletes or purges a batch of datasets.
        **Warning**: only the ownership of the datasets (and upload state for HDAs) is checked,
        no other checks or restrictions are made."""
        client = self._get_client()
        response = client.delete("/api/datasets", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True))
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = DeleteDatasetBatchResult.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def datasets__index(
        self,
        *,
        history_id: str | None = None,
        view: str | None = None,
        keys: str | None = None,
        q: list[str] | None = None,
        qv: list[str] | None = None,
        offset: int | None = None,
        limit: int | None = None,
        order: str | None = None,
        run_as: str | None = None,
    ) -> Response[
        list[HDACustom | HDADetailed | HDASummary | HDAInaccessible | HDCACustom | HDCADetailed | HDCASummary]
    ]:
        """Search datasets or collections using a query system."""
        client = self._get_client()
        response = client.get(
            "/api/datasets",
            params=self._filter_none_values(
                {
                    "history_id": history_id,
                    "view": view,
                    "keys": keys,
                    "q": q,
                    "qv": qv,
                    "offset": offset,
                    "limit": limit,
                    "order": order,
                }
            ),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [
                HDACustom
                | HDADetailed
                | HDASummary
                | HDAInaccessible
                | HDCACustom
                | HDCADetailed
                | HDCASummary.model_validate(item)
                for item in response.json()
            ]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def datasets__delete(
        self,
        dataset_id: str,
        data: DeleteHistoryContentPayload,
        *,
        purge: bool | None = None,
        recursive: bool | None = None,
        stop_job: bool | None = None,
        run_as: str | None = None,
    ) -> Response[Any]:
        """Delete the history dataset content with the given ``ID``.

        Delete the history content with the given ``ID`` and path specified type.

        **Note**: Currently does not stop any active jobs for which this dataset is an output."""
        client = self._get_client()
        response = client.delete(
            f"/api/datasets/{dataset_id}",
            params=self._filter_none_values({"purge": purge, "recursive": recursive, "stop_job": stop_job}),
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def datasets__show(
        self,
        dataset_id: str,
        *,
        hda_ldda: DatasetSourceType | None = None,
        data_type: RequestDataType | None = None,
        limit: int | None = None,
        offset: int | None = None,
        view: str | None = None,
        keys: str | None = None,
        run_as: str | None = None,
    ) -> Response[Any]:
        """Displays information about and/or content of a dataset.

        **Note**: Due to the multipurpose nature of this endpoint, which can receive a wide variety of parameters
        and return different kinds of responses, the documentation here will be limited.
        To get more information please check the source code."""
        client = self._get_client()
        response = client.get(
            f"/api/datasets/{dataset_id}",
            params=self._filter_none_values(
                {
                    "hda_ldda": hda_ldda,
                    "data_type": data_type,
                    "limit": limit,
                    "offset": offset,
                    "view": view,
                    "keys": keys,
                }
            ),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def datasets__update_dataset(
        self,
        dataset_id: str,
        data: UpdateHistoryContentsPayload,
        *,
        view: str | None = None,
        keys: str | None = None,
        run_as: str | None = None,
    ) -> Response[HDACustom | HDADetailed | HDASummary | HDAInaccessible | HDCACustom | HDCADetailed | HDCASummary]:
        """Updates the values for the history dataset (HDA) item with the given ``ID``.

        Updates the values for the history content item with the given ``ID``."""
        client = self._get_client()
        response = client.put(
            f"/api/datasets/{dataset_id}",
            params=self._filter_none_values({"view": view, "keys": keys}),
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = (
                HDACustom
                | HDADetailed
                | HDASummary
                | HDAInaccessible
                | HDCACustom
                | HDCADetailed
                | HDCASummary.model_validate(response.json())
            )
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def datasets__content__get_structured_content(
        self, dataset_id: str, content_type: DatasetContentType, *, run_as: str | None = None
    ) -> Response[Any]:
        """Retrieve information about the content of a dataset."""
        client = self._get_client()
        response = client.get(f"/api/datasets/{dataset_id}/content/{content_type}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def datasets__converted__converted(
        self, dataset_id: str, *, run_as: str | None = None
    ) -> Response[ConvertedDatasetsMap]:
        """Return a a map with all the existing converted datasets associated with this instance.

        Return a map of `<converted extension> : <converted id>` containing all the *existing* converted datasets."""
        client = self._get_client()
        response = client.get(f"/api/datasets/{dataset_id}/converted", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ConvertedDatasetsMap.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def datasets__converted__converted_ext(
        self, dataset_id: str, ext: str, *, view: str | None = None, keys: str | None = None, run_as: str | None = None
    ) -> Response[HDACustom | HDADetailed | HDASummary | HDAInaccessible]:
        """Return information about datasets made by converting this dataset to a new format.

        Return information about datasets made by converting this dataset to a new format.

        If there is no existing converted dataset for the format in `ext`, one will be created.

        **Note**: `view` and `keys` are also available to control the serialization of the dataset."""
        client = self._get_client()
        response = client.get(
            f"/api/datasets/{dataset_id}/converted/{ext}",
            params=self._filter_none_values({"view": view, "keys": keys}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = HDACustom | HDADetailed | HDASummary | HDAInaccessible.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def datasets__extra_files__extra_files(
        self, dataset_id: str, *, run_as: str | None = None
    ) -> Response[DatasetExtraFiles]:
        """Get the list of extra files/directories associated with a dataset."""
        client = self._get_client()
        response = client.get(f"/api/datasets/{dataset_id}/extra_files", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = DatasetExtraFiles.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def datasets__extra_files_raw__extra_file_raw(
        self, dataset_id: str, filename: str, *, run_as: str | None = None
    ) -> Response[Any]:
        """Downloads a raw extra file associated with a dataset."""
        client = self._get_client()
        response = client.get(f"/api/datasets/{dataset_id}/extra_files/raw/{filename}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def datasets__get_content_as_text__get_content_as_text(
        self, dataset_id: str, *, filename: str | None = None, run_as: str | None = None
    ) -> Response[DatasetTextContentDetails]:
        """Returns dataset content as Text."""
        client = self._get_client()
        response = client.get(
            f"/api/datasets/{dataset_id}/get_content_as_text",
            params=self._filter_none_values({"filename": filename}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = DatasetTextContentDetails.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def datasets__hash__compute_hash(
        self,
        dataset_id: str,
        data: ComputeDatasetHashPayload,
        *,
        hda_ldda: DatasetSourceType | None = None,
        run_as: str | None = None,
    ) -> Response[AsyncTaskResultSummary]:
        """Compute dataset hash for dataset and update model"""
        client = self._get_client()
        response = client.put(
            f"/api/datasets/{dataset_id}/hash",
            params=self._filter_none_values({"hda_ldda": hda_ldda}),
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = AsyncTaskResultSummary.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def datasets__inheritance_chain__show_inheritance_chain(
        self, dataset_id: str, *, hda_ldda: DatasetSourceType | None = None, run_as: str | None = None
    ) -> Response[DatasetInheritanceChain]:
        """For internal use, this endpoint may change without warning."""
        client = self._get_client()
        response = client.get(
            f"/api/datasets/{dataset_id}/inheritance_chain",
            params=self._filter_none_values({"hda_ldda": hda_ldda}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = DatasetInheritanceChain.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def jobs__metrics__metrics_by_dataset(
        self, dataset_id: str, *, hda_ldda: DatasetSourceType | None = None, run_as: str | None = None
    ) -> Response[list[JobMetric | None]]:
        """Return job metrics for specified job."""
        client = self._get_client()
        response = client.get(
            f"/api/datasets/{dataset_id}/metrics",
            params=self._filter_none_values({"hda_ldda": hda_ldda}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [JobMetric | None.model_validate(item) for item in response.json()]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def datasets__update_object_store_id(
        self, dataset_id: str, data: UpdateObjectStoreIdPayload, *, run_as: str | None = None
    ) -> Response[Any]:
        """Update an object store ID for a dataset you own."""
        client = self._get_client()
        response = client.put(
            f"/api/datasets/{dataset_id}/object_store_id",
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def jobs__parameters_display__parameters_display_by_dataset(
        self, dataset_id: str, *, hda_ldda: DatasetSourceType | None = None, run_as: str | None = None
    ) -> Response[JobDisplayParametersSummary]:
        """Resolve parameters as a list for nested display.

        **Warning**: This API is unstable and may change without notice."""
        client = self._get_client()
        response = client.get(
            f"/api/datasets/{dataset_id}/parameters_display",
            params=self._filter_none_values({"hda_ldda": hda_ldda}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = JobDisplayParametersSummary.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def datasets__permissions__update_permissions(
        self,
        dataset_id: str,
        data: UpdateDatasetPermissionsPayload
        | UpdateDatasetPermissionsPayloadAliasB
        | UpdateDatasetPermissionsPayloadAliasC,
        *,
        run_as: str | None = None,
    ) -> Response[DatasetAssociationRoles]:
        """Set permissions of the given history dataset to the given role ids."""
        client = self._get_client()
        response = client.put(f"/api/datasets/{dataset_id}/permissions", headers={"run-as": run_as}, json=data)
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = DatasetAssociationRoles.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def datasets__report__report(self, dataset_id: str, *, run_as: str | None = None) -> Response[ToolReportForDataset]:
        """Return JSON content Galaxy will use to render Markdown reports"""
        client = self._get_client()
        response = client.get(f"/api/datasets/{dataset_id}/report", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ToolReportForDataset.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def datasets__storage__show_storage(
        self, dataset_id: str, *, hda_ldda: DatasetSourceType | None = None, run_as: str | None = None
    ) -> Response[DatasetStorageDetails]:
        """Display user-facing storage details related to the objectstore a dataset resides in."""
        client = self._get_client()
        response = client.get(
            f"/api/datasets/{dataset_id}/storage",
            params=self._filter_none_values({"hda_ldda": hda_ldda}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = DatasetStorageDetails.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def datasets__display__display(
        self,
        history_content_id: str,
        *,
        preview: bool | None = None,
        filename: str | None = None,
        to_ext: str | None = None,
        raw: bool | None = None,
        offset: int | None = None,
        ck_size: int | None = None,
        run_as: str | None = None,
    ) -> Response[Any]:
        """Displays (preview) or downloads dataset content.

        Streams the dataset for download or the contents preview to be displayed in a browser."""
        client = self._get_client()
        response = client.get(
            f"/api/datasets/{history_content_id}/display",
            params=self._filter_none_values(
                {
                    "preview": preview,
                    "filename": filename,
                    "to_ext": to_ext,
                    "raw": raw,
                    "offset": offset,
                    "ck_size": ck_size,
                }
            ),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def head_api_datasets_history_content_id_display(
        self,
        history_content_id: str,
        *,
        preview: bool | None = None,
        filename: str | None = None,
        to_ext: str | None = None,
        raw: bool | None = None,
        offset: int | None = None,
        ck_size: int | None = None,
        run_as: str | None = None,
    ) -> Response[Any]:
        """Check if dataset content can be previewed or downloaded.

        Streams the dataset for download or the contents preview to be displayed in a browser."""
        client = self._get_client()
        response = client.head(
            f"/api/datasets/{history_content_id}/display",
            params=self._filter_none_values(
                {
                    "preview": preview,
                    "filename": filename,
                    "to_ext": to_ext,
                    "raw": raw,
                    "offset": offset,
                    "ck_size": ck_size,
                }
            ),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def datasets__get_metadata_file(
        self, history_content_id: str, *, metadata_file: str, run_as: str | None = None
    ) -> Response[Any]:
        """Returns the metadata file associated with this history item."""
        client = self._get_client()
        response = client.get(
            f"/api/datasets/{history_content_id}/metadata_file",
            params=self._filter_none_values({"metadata_file": metadata_file}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def datasets__metadata_file__get_metadata_file_datasets(
        self, history_content_id: str, *, metadata_file: str, run_as: str | None = None
    ) -> Response[Any]:
        """Check if metadata file can be downloaded."""
        client = self._get_client()
        response = client.head(
            f"/api/datasets/{history_content_id}/metadata_file",
            params=self._filter_none_values({"metadata_file": metadata_file}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def datatypes__index(
        self, *, extension_only: bool | None = None, upload_only: bool | None = None
    ) -> Response[list[DatatypeDetails] | list[str]]:
        """Lists all available data types

        Gets the list of all available data types."""
        client = self._get_client()
        response = client.get(
            "/api/datatypes",
            params=self._filter_none_values({"extension_only": extension_only, "upload_only": upload_only}),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            json_data = response.json()
            # Union type: list[DatatypeDetails] | list[str] - parse based on content
            if json_data and isinstance(json_data[0], dict):
                data = [DatatypeDetails.model_validate(item) for item in json_data]
            else:
                data = json_data
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def datatypes__converters__converters(self) -> Response[DatatypeConverterList]:
        """Returns the list of all installed converters

        Gets the list of all installed converters."""
        client = self._get_client()
        response = client.get("/api/datatypes/converters")
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = DatatypeConverterList.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def datatypes__edam_data__edam_data(self) -> Response[dict[str, Any]]:
        """Returns a dictionary/map of datatypes and EDAM data

        Gets a map of datatypes and their corresponding EDAM data."""
        client = self._get_client()
        response = client.get("/api/datatypes/edam_data")
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def datatypes__edam_data_detailed__edam_data_detailed(self) -> Response[DatatypesEDAMDetailsDict]:
        """Returns a dictionary of datatypes and EDAM data details

        Gets a map of datatypes and their corresponding EDAM data.
        EDAM data contains the EDAM iri, label, and definition."""
        client = self._get_client()
        response = client.get("/api/datatypes/edam_data/detailed")
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = DatatypesEDAMDetailsDict.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def datatypes__edam_formats__edam_formats(self) -> Response[dict[str, Any]]:
        """Returns a dictionary/map of datatypes and EDAM formats

        Gets a map of datatypes and their corresponding EDAM formats."""
        client = self._get_client()
        response = client.get("/api/datatypes/edam_formats")
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def datatypes__edam_formats_detailed__edam_formats_detailed(self) -> Response[DatatypesEDAMDetailsDict]:
        """Returns a dictionary of datatypes and EDAM format details

        Gets a map of datatypes and their corresponding EDAM formats.
        EDAM formats contain the EDAM iri, label, and definition."""
        client = self._get_client()
        response = client.get("/api/datatypes/edam_formats/detailed")
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = DatatypesEDAMDetailsDict.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def datatypes__mapping__mapping(self) -> Response[DatatypesMap]:
        """Returns mappings for data types and their implementing classes

        Gets mappings for data types."""
        client = self._get_client()
        response = client.get("/api/datatypes/mapping")
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = DatatypesMap.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def datatypes__sniffers__sniffers(self) -> Response[list[str]]:
        """Returns the list of all installed sniffers

        Gets the list of all installed data type sniffers."""
        client = self._get_client()
        response = client.get("/api/datatypes/sniffers")
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [str.model_validate(item) for item in response.json()]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def datatypes__types_and_mapping__types_and_mapping(
        self, *, extension_only: bool | None = None, upload_only: bool | None = None
    ) -> Response[DatatypesCombinedMap]:
        """Returns all the data types extensions and their mappings

        Combines the datatype information from (/api/datatypes) and the
        mapping information from (/api/datatypes/mapping) into a single
        response."""
        client = self._get_client()
        response = client.get(
            "/api/datatypes/types_and_mapping",
            params=self._filter_none_values({"extension_only": extension_only, "upload_only": upload_only}),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = DatatypesCombinedMap.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def datatypes__show(self, datatype: str) -> Response[Any]:
        """Get details for a specific datatype

        Gets detailed information about a specific datatype.

        Includes information about:
        - Basic properties (description, mime type, etc.)
        - Available converters
        - EDAM mappings
        - Preferred visualization"""
        client = self._get_client()
        response = client.get(f"/api/datatypes/{datatype}")
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def datatypes__visualizations__visualization_for_datatype(
        self, datatype: str
    ) -> Response[DatatypeVisualizationMappingsList]:
        """Returns the visualization mapping for a specific datatype

        Gets the visualization mapping for a specific datatype.

        Mappings are defined in the datatypes_conf.xml configuration file."""
        client = self._get_client()
        response = client.get(f"/api/datatypes/{datatype}/visualizations")
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = DatatypeVisualizationMappingsList.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def display_applications__index(self) -> Response[list[DisplayApplication]]:
        """Returns the list of display applications."""
        client = self._get_client()
        response = client.get("/api/display_applications")
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [DisplayApplication.model_validate(item) for item in response.json()]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def display_applications__create_link__create_link(
        self, data: CreateLinkIncoming, *, run_as: str | None = None
    ) -> Response[CreateLinkFeedback]:
        """Creates a link for display applications."""
        client = self._get_client()
        response = client.post(
            "/api/display_applications/create_link",
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = CreateLinkFeedback.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def display_applications__reload__reload(
        self, data: dict[str, Any] | None, *, run_as: str | None = None
    ) -> Response[ReloadFeedback]:
        """Reloads the list of display applications."""
        client = self._get_client()
        response = client.post("/api/display_applications/reload", headers={"run-as": run_as}, json=data)
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ReloadFeedback.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def drs__download(self, object_id: str, *, run_as: str | None = None) -> Response[Any]:
        """Download"""
        client = self._get_client()
        response = client.get(f"/api/drs_download/{object_id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def dynamic_tools__index(self) -> Response[Any]:
        """Index"""
        client = self._get_client()
        response = client.get("/api/dynamic_tools")
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def dynamic_tools__create(
        self, data: DynamicToolCreatePayload | PathBasedDynamicToolCreatePayload, *, run_as: str | None = None
    ) -> Response[Any]:
        """Create"""
        client = self._get_client()
        response = client.post("/api/dynamic_tools", headers={"run-as": run_as}, json=data)
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def dynamic_tools__delete(self, dynamic_tool_id: str, *, run_as: str | None = None) -> Response[dict[str, Any]]:
        """Delete

        DELETE /api/dynamic_tools/{encoded_dynamic_tool_id|tool_uuid}

        Deactivate the specified dynamic tool. Deactivated tools will not
        be loaded into the toolbox."""
        client = self._get_client()
        response = client.delete(f"/api/dynamic_tools/{dynamic_tool_id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def dynamic_tools__show(self, dynamic_tool_id: str) -> Response[Any]:
        """Show"""
        client = self._get_client()
        response = client.get(f"/api/dynamic_tools/{dynamic_tool_id}")
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def tools__create_file_landing(
        self, data: CreateFileLandingPayload, *, run_as: str | None = None
    ) -> Response[ToolLandingRequest]:
        """Create File Landing"""
        client = self._get_client()
        response = client.post(
            "/api/file_landings", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ToolLandingRequest.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def file_sources__instances_index(self, *, run_as: str | None = None) -> Response[list[UserFileSourceModel]]:
        """Get a list of persisted file source instances defined by the requesting user."""
        client = self._get_client()
        response = client.get("/api/file_source_instances", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [UserFileSourceModel.model_validate(item) for item in response.json()]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def file_sources__create_instance(
        self, data: CreateInstancePayload, *, run_as: str | None = None
    ) -> Response[UserFileSourceModel]:
        """Create a user-bound file source."""
        client = self._get_client()
        response = client.post(
            "/api/file_source_instances", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = UserFileSourceModel.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def file_sources__test_new_instance_configuration(
        self, data: CreateInstancePayload, *, run_as: str | None = None
    ) -> Response[PluginStatus]:
        """Test payload for creating user-bound file source."""
        client = self._get_client()
        response = client.post(
            "/api/file_source_instances/test", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = PluginStatus.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def file_sources__instances_purge(self, uuid: str, *, run_as: str | None = None) -> Response[Any]:
        """Purge user file source instance."""
        client = self._get_client()
        response = client.delete(f"/api/file_source_instances/{uuid}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def file_sources__instances_get(self, uuid: str, *, run_as: str | None = None) -> Response[UserFileSourceModel]:
        """Get a persisted user file source instance."""
        client = self._get_client()
        response = client.get(f"/api/file_source_instances/{uuid}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = UserFileSourceModel.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def file_sources__instances_update(
        self,
        uuid: str,
        data: UpdateInstanceSecretPayload | UpgradeInstancePayload | UpdateInstancePayload,
        *,
        run_as: str | None = None,
    ) -> Response[UserFileSourceModel]:
        """Update or upgrade user file source instance."""
        client = self._get_client()
        response = client.put(f"/api/file_source_instances/{uuid}", headers={"run-as": run_as}, json=data)
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = UserFileSourceModel.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def file_sources__instances_test_instance(self, uuid: str, *, run_as: str | None = None) -> Response[PluginStatus]:
        """Test a file source instance and return status."""
        client = self._get_client()
        response = client.get(f"/api/file_source_instances/{uuid}/test", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = PluginStatus.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def file_sources__test_instances_update(
        self, uuid: str, data: TestUpgradeInstancePayload | TestUpdateInstancePayload, *, run_as: str | None = None
    ) -> Response[PluginStatus]:
        """Test updating or upgrading user file source instance."""
        client = self._get_client()
        response = client.post(f"/api/file_source_instances/{uuid}/test", headers={"run-as": run_as}, json=data)
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = PluginStatus.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def file_sources__templates_index(self, *, run_as: str | None = None) -> Response[FileSourceTemplateSummaries]:
        """Get a list of file source templates available to build user defined file sources from"""
        client = self._get_client()
        response = client.get("/api/file_source_templates", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = FileSourceTemplateSummaries.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def file_sources__template_oauth2(
        self, template_id: str, template_version: int, *, run_as: str | None = None
    ) -> Response[OAuth2Info]:
        """Template Oauth2"""
        client = self._get_client()
        response = client.get(
            f"/api/file_source_templates/{template_id}/{template_version}/oauth2", headers={"run-as": run_as}
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = OAuth2Info.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def data_libraries_folders__contents__index(
        self,
        folder_id: str,
        *,
        limit: int | None = None,
        offset: int | None = None,
        search_text: str | None = None,
        include_deleted: bool | None = None,
        order_by: Literal["name", "description", "type", "size", "update_time"] | None = None,
        sort_desc: bool | None = None,
        run_as: str | None = None,
    ) -> Response[LibraryFolderContentsIndexResult]:
        """Returns a list of a folder's contents (files and sub-folders) with additional metadata about the folder.

        Returns a list of a folder's contents (files and sub-folders).

        Additional metadata for the folder is provided in the response as a separate object containing data
        for breadcrumb path building, permissions and other folder's details.

        *Note*: When sorting, folders always have priority (they show-up before any dataset regardless of the sorting).

        **Security note**:
        - Accessing a library folder or sub-folder requires only access to the parent library.
        - Deleted folders can only be accessed by admins or users with `MODIFY` permission.
        - Datasets may be public, private or restricted (to a group of users). Listing deleted datasets has the same requirements as folders."""
        client = self._get_client()
        response = client.get(
            f"/api/folders/{folder_id}/contents",
            params=self._filter_none_values(
                {
                    "limit": limit,
                    "offset": offset,
                    "search_text": search_text,
                    "include_deleted": include_deleted,
                    "order_by": order_by,
                    "sort_desc": sort_desc,
                }
            ),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = LibraryFolderContentsIndexResult.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def data_libraries_folders__contents__create(
        self, folder_id: str, data: CreateLibraryFilePayload, *, run_as: str | None = None
    ) -> Response[Any]:
        """Creates a new library file from an existing HDA/HDCA."""
        client = self._get_client()
        response = client.post(
            f"/api/folders/{folder_id}/contents", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def data_libraries_folders__delete(
        self, id: str, *, undelete: bool | None = None, run_as: str | None = None
    ) -> Response[LibraryFolderDetails]:
        """Marks the specified library folder as deleted (or undeleted)."""
        client = self._get_client()
        response = client.delete(
            f"/api/folders/{id}", params=self._filter_none_values({"undelete": undelete}), headers={"run-as": run_as}
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = LibraryFolderDetails.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def data_libraries_folders__show(self, id: str, *, run_as: str | None = None) -> Response[LibraryFolderDetails]:
        """Displays information about a particular library folder.

        Returns detailed information about the library folder with the given ID."""
        client = self._get_client()
        response = client.get(f"/api/folders/{id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = LibraryFolderDetails.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def data_libraries_folders__update(
        self, id: str, data: UpdateLibraryFolderPayload, *, run_as: str | None = None
    ) -> Response[LibraryFolderDetails]:
        """Update

        Updates the information of an existing library folder."""
        client = self._get_client()
        response = client.patch(
            f"/api/folders/{id}", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = LibraryFolderDetails.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def data_libraries_folders__create(
        self, id: str, data: CreateLibraryFolderPayload, *, run_as: str | None = None
    ) -> Response[LibraryFolderDetails]:
        """Create a new library folder underneath the one specified by the ID.

        Returns detailed information about the newly created library folder."""
        client = self._get_client()
        response = client.post(
            f"/api/folders/{id}", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = LibraryFolderDetails.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def put_api_folders_id(
        self, id: str, data: UpdateLibraryFolderPayload, *, run_as: str | None = None
    ) -> Response[LibraryFolderDetails]:
        """Updates the information of an existing library folder."""
        client = self._get_client()
        response = client.put(
            f"/api/folders/{id}", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = LibraryFolderDetails.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def data_libraries_folders__permissions__get_permissions(
        self,
        id: str,
        *,
        scope: LibraryPermissionScope | None = None,
        page: int | None = None,
        page_limit: int | None = None,
        q: str | None = None,
        run_as: str | None = None,
    ) -> Response[LibraryFolderCurrentPermissions | LibraryAvailablePermissions]:
        """Gets the current or available permissions of a particular library folder.

        Gets the current or available permissions of a particular library.
        The results can be paginated and additionally filtered by a query."""
        client = self._get_client()
        response = client.get(
            f"/api/folders/{id}/permissions",
            params=self._filter_none_values({"scope": scope, "page": page, "page_limit": page_limit, "q": q}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = LibraryFolderCurrentPermissions | LibraryAvailablePermissions.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def data_libraries_folders__permissions__set_permissions(
        self,
        id: str,
        data: LibraryFolderPermissionsPayload,
        *,
        action: LibraryFolderPermissionAction | None = None,
        run_as: str | None = None,
    ) -> Response[LibraryFolderCurrentPermissions]:
        """Sets the permissions to manage a library folder."""
        client = self._get_client()
        response = client.post(
            f"/api/folders/{id}/permissions",
            params=self._filter_none_values({"action": action}),
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = LibraryFolderCurrentPermissions.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def forms__delete(self, id: str, *, run_as: str | None = None) -> Response[Any]:
        """Delete"""
        client = self._get_client()
        response = client.delete(f"/api/forms/{id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def forms__undelete__undelete(self, id: str, *, run_as: str | None = None) -> Response[Any]:
        """Undelete"""
        client = self._get_client()
        response = client.post(f"/api/forms/{id}/undelete", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def remote_files__index(
        self,
        *,
        target: str | None = None,
        format: RemoteFilesFormat | None = None,
        recursive: bool | None = None,
        disable: RemoteFilesDisableMode | None = None,
        writeable: bool | None = None,
        write_intent: bool | None = None,
        limit: int | None = None,
        offset: int | None = None,
        query: str | None = None,
        sort_by: str | None = None,
        run_as: str | None = None,
    ) -> Response[ListUriResponse | ListJstreeResponse]:
        """Displays remote files available to the user. Please use /api/remote_files instead.

        Lists all remote files available to the user from different sources.

        The total count of files and directories is returned in the 'total_matches' header."""
        client = self._get_client()
        response = client.get(
            "/api/ftp_files",
            params=self._filter_none_values(
                {
                    "target": target,
                    "format": format,
                    "recursive": recursive,
                    "disable": disable,
                    "writeable": writeable,
                    "write_intent": write_intent,
                    "limit": limit,
                    "offset": offset,
                    "query": query,
                    "sort_by": sort_by,
                }
            ),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ListUriResponse | ListJstreeResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def genomes__index(self, *, chrom_info: bool | None = None, run_as: str | None = None) -> Response[list[list[str]]]:
        """Return a list of installed genomes"""
        client = self._get_client()
        response = client.get(
            "/api/genomes", params=self._filter_none_values({"chrom_info": chrom_info}), headers={"run-as": run_as}
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [list[str].model_validate(item) for item in response.json()]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def genomes__show(
        self,
        id: str,
        *,
        reference: bool | None = None,
        num: int | None = None,
        chrom: str | None = None,
        low: int | None = None,
        high: int | None = None,
        format: str | None = None,
        run_as: str | None = None,
    ) -> Response[Any]:
        """Return information about build <id>"""
        client = self._get_client()
        response = client.get(
            f"/api/genomes/{id}",
            params=self._filter_none_values(
                {"reference": reference, "num": num, "chrom": chrom, "low": low, "high": high, "format": format}
            ),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def genomes__indexes__indexes(
        self, id: str, *, type: str | None = None, format: str | None = None, run_as: str | None = None
    ) -> Response[Any]:
        """Return all available indexes for a genome id for provided type"""
        client = self._get_client()
        response = client.get(
            f"/api/genomes/{id}/indexes",
            params=self._filter_none_values({"type": type, "format": format}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def genomes__sequences__sequences(
        self,
        id: str,
        *,
        reference: bool | None = None,
        chrom: str | None = None,
        low: int | None = None,
        high: int | None = None,
        format: str | None = None,
        run_as: str | None = None,
    ) -> Response[Any]:
        """Return raw sequence data"""
        client = self._get_client()
        response = client.get(
            f"/api/genomes/{id}/sequences",
            params=self._filter_none_values(
                {"reference": reference, "chrom": chrom, "low": low, "high": high, "format": format}
            ),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def groups__index(self, *, run_as: str | None = None) -> Response[GroupListResponse]:
        """Displays a collection (list) of groups."""
        client = self._get_client()
        response = client.get("/api/groups", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = GroupListResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def groups__create(self, data: GroupCreatePayload, *, run_as: str | None = None) -> Response[GroupListResponse]:
        """Creates a new group."""
        client = self._get_client()
        response = client.post("/api/groups", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True))
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = GroupListResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def groups__delete(self, group_id: str, *, run_as: str | None = None) -> Response[Any]:
        """Delete"""
        client = self._get_client()
        response = client.delete(f"/api/groups/{group_id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def groups__show(self, group_id: str, *, run_as: str | None = None) -> Response[GroupResponse]:
        """Displays information about a group."""
        client = self._get_client()
        response = client.get(f"/api/groups/{group_id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = GroupResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def groups__update(
        self, group_id: str, data: GroupUpdatePayload, *, run_as: str | None = None
    ) -> Response[GroupResponse]:
        """Modifies a group."""
        client = self._get_client()
        response = client.put(
            f"/api/groups/{group_id}", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = GroupResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def groups__purge__purge(self, group_id: str, *, run_as: str | None = None) -> Response[Any]:
        """Purge"""
        client = self._get_client()
        response = client.post(f"/api/groups/{group_id}/purge", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def group_roles__roles__index(self, group_id: str, *, run_as: str | None = None) -> Response[GroupRoleListResponse]:
        """Displays a collection (list) of groups."""
        client = self._get_client()
        response = client.get(f"/api/groups/{group_id}/roles", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = GroupRoleListResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def group_roles__roles__delete(
        self, group_id: str, role_id: str, *, run_as: str | None = None
    ) -> Response[GroupRoleResponse]:
        """Removes a role from a group"""
        client = self._get_client()
        response = client.delete(f"/api/groups/{group_id}/roles/{role_id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = GroupRoleResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def group_roles__roles__show(
        self, group_id: str, role_id: str, *, run_as: str | None = None
    ) -> Response[GroupRoleResponse]:
        """Displays information about a group role."""
        client = self._get_client()
        response = client.get(f"/api/groups/{group_id}/roles/{role_id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = GroupRoleResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def group_roles__roles__update(
        self, group_id: str, role_id: str, *, run_as: str | None = None
    ) -> Response[GroupRoleResponse]:
        """Adds a role to a group"""
        client = self._get_client()
        response = client.put(f"/api/groups/{group_id}/roles/{role_id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = GroupRoleResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def groups__undelete__undelete(self, group_id: str, *, run_as: str | None = None) -> Response[Any]:
        """Undelete"""
        client = self._get_client()
        response = client.post(f"/api/groups/{group_id}/undelete", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def group_users__user__delete(
        self, group_id: str, user_id: str, *, run_as: str | None = None
    ) -> Response[GroupUserResponse]:
        """Removes a user from a group

        DELETE /api/groups/{encoded_group_id}/users/{encoded_user_id}
        Removes a user from a group"""
        client = self._get_client()
        response = client.delete(f"/api/groups/{group_id}/user/{user_id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = GroupUserResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def group_users__user__show(
        self, group_id: str, user_id: str, *, run_as: str | None = None
    ) -> Response[GroupUserResponse]:
        """Displays information about a group user."""
        client = self._get_client()
        response = client.get(f"/api/groups/{group_id}/user/{user_id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = GroupUserResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def group_users__user__update(
        self, group_id: str, user_id: str, *, run_as: str | None = None
    ) -> Response[GroupUserResponse]:
        """Adds a user to a group

        PUT /api/groups/{encoded_group_id}/users/{encoded_user_id}
        Adds a user to a group"""
        client = self._get_client()
        response = client.put(f"/api/groups/{group_id}/user/{user_id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = GroupUserResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def group_users__users__index(self, group_id: str, *, run_as: str | None = None) -> Response[GroupUserListResponse]:
        """Displays a collection (list) of groups.

        GET /api/groups/{encoded_group_id}/users
        Displays a collection (list) of groups."""
        client = self._get_client()
        response = client.get(f"/api/groups/{group_id}/users", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = GroupUserListResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def group_users__users__delete(
        self, group_id: str, user_id: str, *, run_as: str | None = None
    ) -> Response[GroupUserResponse]:
        """Removes a user from a group

        DELETE /api/groups/{encoded_group_id}/users/{encoded_user_id}
        Removes a user from a group"""
        client = self._get_client()
        response = client.delete(f"/api/groups/{group_id}/users/{user_id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = GroupUserResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def group_users__users__show(
        self, group_id: str, user_id: str, *, run_as: str | None = None
    ) -> Response[GroupUserResponse]:
        """Displays information about a group user."""
        client = self._get_client()
        response = client.get(f"/api/groups/{group_id}/users/{user_id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = GroupUserResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def group_users__users__update(
        self, group_id: str, user_id: str, *, run_as: str | None = None
    ) -> Response[GroupUserResponse]:
        """Adds a user to a group

        PUT /api/groups/{encoded_group_id}/users/{encoded_user_id}
        Adds a user to a group"""
        client = self._get_client()
        response = client.put(f"/api/groups/{group_id}/users/{user_id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = GroupUserResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def help__forum_search__search_forum(
        self, *, query: str, run_as: str | None = None
    ) -> Response[HelpForumSearchResponse]:
        """Search the Galaxy Help forum.

        **Warning**: This API is unstable and may change without notice."""
        client = self._get_client()
        response = client.get(
            "/api/help/forum/search", params=self._filter_none_values({"query": query}), headers={"run-as": run_as}
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = HelpForumSearchResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__index(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        show_own: bool | None = None,
        show_published: bool | None = None,
        show_shared: bool | None = None,
        show_archived: bool | None = None,
        sort_by: Literal["create_time", "name", "update_time", "username"] | None = None,
        sort_desc: bool | None = None,
        search: str | None = None,
        all: bool | None = None,
        deleted: bool | None = None,
        q: list[str] | None = None,
        qv: list[str] | None = None,
        order: str | None = None,
        view: str | None = None,
        keys: str | None = None,
        run_as: str | None = None,
    ) -> Response[list[CustomHistoryView | HistoryDetailed | HistorySummary]]:
        """Returns histories available to the current user."""
        client = self._get_client()
        response = client.get(
            "/api/histories",
            params=self._filter_none_values(
                {
                    "limit": limit,
                    "offset": offset,
                    "show_own": show_own,
                    "show_published": show_published,
                    "show_shared": show_shared,
                    "show_archived": show_archived,
                    "sort_by": sort_by,
                    "sort_desc": sort_desc,
                    "search": search,
                    "all": all,
                    "deleted": deleted,
                    "q": q,
                    "qv": qv,
                    "order": order,
                    "view": view,
                    "keys": keys,
                }
            ),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [
                CustomHistoryView | HistoryDetailed | HistorySummary.model_validate(item) for item in response.json()
            ]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__create(
        self, *, view: str | None = None, keys: str | None = None, run_as: str | None = None
    ) -> Response[JobImportHistoryResponse | CustomHistoryView | HistoryDetailed | HistorySummary]:
        """Creates a new history.

        The new history can also be copied form a existing history or imported from an archive or URL."""
        client = self._get_client()
        response = client.post(
            "/api/histories", params=self._filter_none_values({"view": view, "keys": keys}), headers={"run-as": run_as}
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = (
                JobImportHistoryResponse
                | CustomHistoryView
                | HistoryDetailed
                | HistorySummary.model_validate(response.json())
            )
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__archived__get_archived_histories(
        self,
        *,
        view: str | None = None,
        keys: str | None = None,
        q: list[str] | None = None,
        qv: list[str] | None = None,
        offset: int | None = None,
        limit: int | None = None,
        order: str | None = None,
        run_as: str | None = None,
    ) -> Response[list[CustomArchivedHistoryView | ArchivedHistoryDetailed | ArchivedHistorySummary]]:
        """Get a list of all archived histories for the current user.

        Get a list of all archived histories for the current user.

        Archived histories are histories are not part of the active histories of the user but they can be accessed using this endpoint."""
        client = self._get_client()
        response = client.get(
            "/api/histories/archived",
            params=self._filter_none_values(
                {"view": view, "keys": keys, "q": q, "qv": qv, "offset": offset, "limit": limit, "order": order}
            ),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [
                CustomArchivedHistoryView | ArchivedHistoryDetailed | ArchivedHistorySummary.model_validate(item)
                for item in response.json()
            ]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__batch_delete__batch_delete(
        self,
        data: DeleteHistoriesPayload,
        *,
        purge: bool | None = None,
        view: str | None = None,
        keys: str | None = None,
        run_as: str | None = None,
    ) -> Response[list[CustomHistoryView | HistoryDetailed | HistorySummary]]:
        """Marks several histories with the given IDs as deleted."""
        client = self._get_client()
        response = client.put(
            "/api/histories/batch/delete",
            params=self._filter_none_values({"purge": purge, "view": view, "keys": keys}),
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [
                CustomHistoryView | HistoryDetailed | HistorySummary.model_validate(item) for item in response.json()
            ]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__batch_undelete__batch_undelete(
        self,
        data: UndeleteHistoriesPayload,
        *,
        view: str | None = None,
        keys: str | None = None,
        run_as: str | None = None,
    ) -> Response[list[CustomHistoryView | HistoryDetailed | HistorySummary]]:
        """Marks several histories with the given IDs as undeleted."""
        client = self._get_client()
        response = client.put(
            "/api/histories/batch/undelete",
            params=self._filter_none_values({"view": view, "keys": keys}),
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [
                CustomHistoryView | HistoryDetailed | HistorySummary.model_validate(item) for item in response.json()
            ]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__count__count(self, *, run_as: str | None = None) -> Response[int]:
        """Returns number of histories for the current user."""
        client = self._get_client()
        response = client.get("/api/histories/count", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__deleted__index_deleted(
        self,
        *,
        all: bool | None = None,
        q: list[str] | None = None,
        qv: list[str] | None = None,
        offset: int | None = None,
        limit: int | None = None,
        order: str | None = None,
        view: str | None = None,
        keys: str | None = None,
        run_as: str | None = None,
    ) -> Response[list[CustomHistoryView | HistoryDetailed | HistorySummary]]:
        """Returns deleted histories for the current user."""
        client = self._get_client()
        response = client.get(
            "/api/histories/deleted",
            params=self._filter_none_values(
                {
                    "all": all,
                    "q": q,
                    "qv": qv,
                    "offset": offset,
                    "limit": limit,
                    "order": order,
                    "view": view,
                    "keys": keys,
                }
            ),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [
                CustomHistoryView | HistoryDetailed | HistorySummary.model_validate(item) for item in response.json()
            ]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__deleted_undelete__undelete(
        self, history_id: str, *, view: str | None = None, keys: str | None = None, run_as: str | None = None
    ) -> Response[CustomHistoryView | HistoryDetailed | HistorySummary]:
        """Restores a deleted history with the given ID (that hasn't been purged)."""
        client = self._get_client()
        response = client.post(
            f"/api/histories/deleted/{history_id}/undelete",
            params=self._filter_none_values({"view": view, "keys": keys}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = CustomHistoryView | HistoryDetailed | HistorySummary.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__from_store__create_from_store(
        self,
        data: CreateHistoryFromStore,
        *,
        view: str | None = None,
        keys: str | None = None,
        run_as: str | None = None,
    ) -> Response[CustomHistoryView | HistoryDetailed | HistorySummary]:
        """Create histories from a model store."""
        client = self._get_client()
        response = client.post(
            "/api/histories/from_store",
            params=self._filter_none_values({"view": view, "keys": keys}),
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = CustomHistoryView | HistoryDetailed | HistorySummary.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__from_store_async__create_from_store_async(
        self, data: CreateHistoryFromStore, *, run_as: str | None = None
    ) -> Response[AsyncTaskResultSummary]:
        """Launch a task to create histories from a model store."""
        client = self._get_client()
        response = client.post(
            "/api/histories/from_store_async", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = AsyncTaskResultSummary.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__most_recently_used__show_recent(
        self, *, view: str | None = None, keys: str | None = None, run_as: str | None = None
    ) -> Response[CustomHistoryView | HistoryDetailed | HistorySummary]:
        """Returns the most recently used history of the user."""
        client = self._get_client()
        response = client.get(
            "/api/histories/most_recently_used",
            params=self._filter_none_values({"view": view, "keys": keys}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = CustomHistoryView | HistoryDetailed | HistorySummary.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__published__published(
        self,
        *,
        q: list[str] | None = None,
        qv: list[str] | None = None,
        offset: int | None = None,
        limit: int | None = None,
        order: str | None = None,
        view: str | None = None,
        keys: str | None = None,
        run_as: str | None = None,
    ) -> Response[list[CustomHistoryView | HistoryDetailed | HistorySummary]]:
        """Return all histories that are published."""
        client = self._get_client()
        response = client.get(
            "/api/histories/published",
            params=self._filter_none_values(
                {"q": q, "qv": qv, "offset": offset, "limit": limit, "order": order, "view": view, "keys": keys}
            ),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [
                CustomHistoryView | HistoryDetailed | HistorySummary.model_validate(item) for item in response.json()
            ]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__shared_with_me__shared_with_me(
        self,
        *,
        q: list[str] | None = None,
        qv: list[str] | None = None,
        offset: int | None = None,
        limit: int | None = None,
        order: str | None = None,
        view: str | None = None,
        keys: str | None = None,
        run_as: str | None = None,
    ) -> Response[list[CustomHistoryView | HistoryDetailed | HistorySummary]]:
        """Return all histories that are shared with the current user."""
        client = self._get_client()
        response = client.get(
            "/api/histories/shared_with_me",
            params=self._filter_none_values(
                {"q": q, "qv": qv, "offset": offset, "limit": limit, "order": order, "view": view, "keys": keys}
            ),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [
                CustomHistoryView | HistoryDetailed | HistorySummary.model_validate(item) for item in response.json()
            ]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__delete(
        self,
        history_id: str,
        data: DeleteHistoryPayload | None,
        *,
        purge: bool | None = None,
        view: str | None = None,
        keys: str | None = None,
        run_as: str | None = None,
    ) -> Response[CustomHistoryView | HistoryDetailed | HistorySummary]:
        """Marks the history with the given ID as deleted."""
        client = self._get_client()
        response = client.delete(
            f"/api/histories/{history_id}",
            params=self._filter_none_values({"purge": purge, "view": view, "keys": keys}),
            headers={"run-as": run_as},
            json=data,
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = CustomHistoryView | HistoryDetailed | HistorySummary.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__show(
        self, history_id: str, *, view: str | None = None, keys: str | None = None, run_as: str | None = None
    ) -> Response[CustomHistoryView | HistoryDetailed | HistorySummary]:
        """Returns the history with the given ID."""
        client = self._get_client()
        response = client.get(
            f"/api/histories/{history_id}",
            params=self._filter_none_values({"view": view, "keys": keys}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = CustomHistoryView | HistoryDetailed | HistorySummary.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__update(
        self,
        history_id: str,
        data: UpdateHistoryPayload,
        *,
        view: str | None = None,
        keys: str | None = None,
        run_as: str | None = None,
    ) -> Response[CustomHistoryView | HistoryDetailed | HistorySummary]:
        """Updates the values for the history with the given ID."""
        client = self._get_client()
        response = client.put(
            f"/api/histories/{history_id}",
            params=self._filter_none_values({"view": view, "keys": keys}),
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = CustomHistoryView | HistoryDetailed | HistorySummary.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__archive__archive_history(
        self, history_id: str, data: ArchiveHistoryRequestPayload | None, *, run_as: str | None = None
    ) -> Response[CustomArchivedHistoryView | ArchivedHistoryDetailed | ArchivedHistorySummary]:
        """Archive a history.

        Marks the given history as 'archived' and returns the history.

        Archiving a history will remove it from the list of active histories of the user but it will still be
        accessible via the `/api/histories/{id}` or the `/api/histories/archived` endpoints.

        Associating an export record:

        - Optionally, an export record (containing information about a recent snapshot of the history) can be associated with the
        archived history by providing an `archive_export_id` in the payload. The export record must belong to the history and
        must be in the ready state.
        - When associating an export record, the history can be purged after it has been archived using the `purge_history` flag.

        If the history is already archived, this endpoint will return a 409 Conflict error, indicating that the history is already archived.
        If the history was not purged after it was archived, you can restore it using the `/api/histories/{id}/archive/restore` endpoint."""
        client = self._get_client()
        response = client.post(f"/api/histories/{history_id}/archive", headers={"run-as": run_as}, json=data)
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = (
                CustomArchivedHistoryView
                | ArchivedHistoryDetailed
                | ArchivedHistorySummary.model_validate(response.json())
            )
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__archive_restore__restore_archived_history(
        self, history_id: str, *, force: bool | None = None, run_as: str | None = None
    ) -> Response[CustomHistoryView | HistoryDetailed | HistorySummary]:
        """Restore an archived history.

        Restores an archived history and returns it.

        Restoring an archived history will add it back to the list of active histories of the user (unless it was purged).

        **Warning**: Please note that histories that are associated with an archive export might be purged after export, so un-archiving them
        will not restore the datasets that were in the history before it was archived. You will need to import back the archive export
        record to restore the history and its datasets as a new copy. See `/api/histories/from_store_async` for more information."""
        client = self._get_client()
        response = client.put(
            f"/api/histories/{history_id}/archive/restore",
            params=self._filter_none_values({"force": force}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = CustomHistoryView | HistoryDetailed | HistorySummary.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__citations__citations(self, history_id: str, *, run_as: str | None = None) -> Response[list[Any]]:
        """Return all the references for the tools used to produce the datasets in the history."""
        client = self._get_client()
        response = client.get(f"/api/histories/{history_id}/citations", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [Any.model_validate(item) for item in response.json()]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def history_contents__index(
        self,
        history_id: str,
        *,
        v: str | None = None,
        details: str | None = None,
        ids: str | None = None,
        types: list[str] | None = None,
        deleted: bool | None = None,
        visible: bool | None = None,
        shareable: bool | None = None,
        view: str | None = None,
        keys: str | None = None,
        q: list[str] | None = None,
        qv: list[str] | None = None,
        offset: int | None = None,
        limit: int | None = None,
        order: str | None = None,
        accept: Literal["application/json", "application/vnd.galaxy.history.contents.stats+json"] | None = None,
        run_as: str | None = None,
    ) -> Response[HistoryContentsResult]:
        """Returns the contents of the given history.

        Return a list of `HDA`/`HDCA` data for the history with the given ``ID``.

        - The contents can be filtered and queried using the appropriate parameters.
        - The amount of information returned for each item can be customized.

        **Note**: Anonymous users are allowed to get their current history contents."""
        client = self._get_client()
        response = client.get(
            f"/api/histories/{history_id}/contents",
            params=self._filter_none_values(
                {
                    "v": v,
                    "details": details,
                    "ids": ids,
                    "types": types,
                    "deleted": deleted,
                    "visible": visible,
                    "shareable": shareable,
                    "view": view,
                    "keys": keys,
                    "q": q,
                    "qv": qv,
                    "offset": offset,
                    "limit": limit,
                    "order": order,
                }
            ),
            headers={"accept": accept, "run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = HistoryContentsResult.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def history_contents__create(
        self,
        history_id: str,
        data: CreateHistoryContentPayload,
        *,
        type: HistoryContentType | None = None,
        view: str | None = None,
        keys: str | None = None,
        run_as: str | None = None,
    ) -> Response[
        HDACustom
        | HDADetailed
        | HDASummary
        | HDAInaccessible
        | HDCACustom
        | HDCADetailed
        | HDCASummary
        | list[HDACustom | HDADetailed | HDASummary | HDAInaccessible | HDCACustom | HDCADetailed | HDCASummary]
    ]:
        """Create a new `HDA` or `HDCA` in the given History."""
        client = self._get_client()
        response = client.post(
            f"/api/histories/{history_id}/contents",
            params=self._filter_none_values({"type": type, "view": view, "keys": keys}),
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = (
                HDACustom
                | HDADetailed
                | HDASummary
                | HDAInaccessible
                | HDCACustom
                | HDCADetailed
                | HDCASummary
                | list[
                    HDACustom | HDADetailed | HDASummary | HDAInaccessible | HDCACustom | HDCADetailed | HDCASummary
                ].model_validate(response.json())
            )
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__contents__update_batch(
        self,
        history_id: str,
        data: UpdateHistoryContentsBatchPayload,
        *,
        view: str | None = None,
        keys: str | None = None,
        run_as: str | None = None,
    ) -> Response[HistoryContentsResult]:
        """Batch update specific properties of a set items contained in the given History.

        Batch update specific properties of a set items contained in the given History.

        If you provide an invalid/unknown property key the request will not fail, but no changes
        will be made to the items."""
        client = self._get_client()
        response = client.put(
            f"/api/histories/{history_id}/contents",
            params=self._filter_none_values({"view": view, "keys": keys}),
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = HistoryContentsResult.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def history_contents__archive(
        self,
        history_id: str,
        *,
        filename: str | None = None,
        dry_run: bool | None = None,
        q: list[str] | None = None,
        qv: list[str] | None = None,
        offset: int | None = None,
        limit: int | None = None,
        order: str | None = None,
        run_as: str | None = None,
    ) -> Response[Any]:
        """Build and return a compressed archive of the selected history contents.

        **Warning**: This API is unstable and may change without notice."""
        client = self._get_client()
        response = client.get(
            f"/api/histories/{history_id}/contents/archive",
            params=self._filter_none_values(
                {
                    "filename": filename,
                    "dry_run": dry_run,
                    "q": q,
                    "qv": qv,
                    "offset": offset,
                    "limit": limit,
                    "order": order,
                }
            ),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def history_contents__archive_named(
        self,
        history_id: str,
        filename: str,
        format: str,
        *,
        dry_run: bool | None = None,
        q: list[str] | None = None,
        qv: list[str] | None = None,
        offset: int | None = None,
        limit: int | None = None,
        order: str | None = None,
        run_as: str | None = None,
    ) -> Response[Any]:
        """Build and return a compressed archive of the selected history contents.

        **Warning**: This API is unstable and may change without notice."""
        client = self._get_client()
        response = client.get(
            f"/api/histories/{history_id}/contents/archive/{filename}.{format}",
            params=self._filter_none_values(
                {"dry_run": dry_run, "q": q, "qv": qv, "offset": offset, "limit": limit, "order": order}
            ),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__contents_bulk__bulk_operation(
        self,
        history_id: str,
        data: HistoryContentBulkOperationPayload,
        *,
        q: list[str] | None = None,
        qv: list[str] | None = None,
        run_as: str | None = None,
    ) -> Response[HistoryContentBulkOperationResult]:
        """Executes an operation on a set of items contained in the given History.

        Executes an operation on a set of items contained in the given History.

        The items to be processed can be explicitly set or determined by a dynamic query."""
        client = self._get_client()
        response = client.put(
            f"/api/histories/{history_id}/contents/bulk",
            params=self._filter_none_values({"q": q, "qv": qv}),
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = HistoryContentBulkOperationResult.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def history_contents__download_collection(
        self, hdca_id: str, history_id: str | None, *, run_as: str | None = None
    ) -> Response[Any]:
        """Download the content of a dataset collection as a `zip` archive.

        Download the content of a history dataset collection as a `zip` archive
        while maintaining approximate collection structure."""
        client = self._get_client()
        response = client.get(
            f"/api/histories/{history_id}/contents/dataset_collections/{hdca_id}/download", headers={"run-as": run_as}
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__contents_datasets_materialize__materialize_dataset(
        self, history_id: str, id: str, *, run_as: str | None = None
    ) -> Response[AsyncTaskResultSummary]:
        """Materialize a deferred dataset into real, usable dataset."""
        client = self._get_client()
        response = client.post(
            f"/api/histories/{history_id}/contents/datasets/{id}/materialize", headers={"run-as": run_as}
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = AsyncTaskResultSummary.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__contents_permissions__update_permissions(
        self,
        history_id: str,
        dataset_id: str,
        data: UpdateDatasetPermissionsPayload
        | UpdateDatasetPermissionsPayloadAliasB
        | UpdateDatasetPermissionsPayloadAliasC,
        *,
        run_as: str | None = None,
    ) -> Response[DatasetAssociationRoles]:
        """Set permissions of the given history dataset to the given role ids."""
        client = self._get_client()
        response = client.put(
            f"/api/histories/{history_id}/contents/{dataset_id}/permissions", headers={"run-as": run_as}, json=data
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = DatasetAssociationRoles.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def datasets__contents_display__display_history_content(
        self,
        history_content_id: str,
        history_id: str | None,
        *,
        preview: bool | None = None,
        filename: str | None = None,
        to_ext: str | None = None,
        raw: bool | None = None,
        offset: int | None = None,
        ck_size: int | None = None,
        run_as: str | None = None,
    ) -> Response[Any]:
        """Displays (preview) or downloads dataset content.

        Streams the dataset for download or the contents preview to be displayed in a browser."""
        client = self._get_client()
        response = client.get(
            f"/api/histories/{history_id}/contents/{history_content_id}/display",
            params=self._filter_none_values(
                {
                    "preview": preview,
                    "filename": filename,
                    "to_ext": to_ext,
                    "raw": raw,
                    "offset": offset,
                    "ck_size": ck_size,
                }
            ),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def head_api_histories_history_id_contents_history_content_id_display(
        self,
        history_content_id: str,
        history_id: str | None,
        *,
        preview: bool | None = None,
        filename: str | None = None,
        to_ext: str | None = None,
        raw: bool | None = None,
        offset: int | None = None,
        ck_size: int | None = None,
        run_as: str | None = None,
    ) -> Response[Any]:
        """Check if dataset content can be previewed or downloaded.

        Streams the dataset for download or the contents preview to be displayed in a browser."""
        client = self._get_client()
        response = client.head(
            f"/api/histories/{history_id}/contents/{history_content_id}/display",
            params=self._filter_none_values(
                {
                    "preview": preview,
                    "filename": filename,
                    "to_ext": to_ext,
                    "raw": raw,
                    "offset": offset,
                    "ck_size": ck_size,
                }
            ),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def datasets__contents_extra_files__extra_files_history(
        self, history_id: str, history_content_id: str, *, run_as: str | None = None
    ) -> Response[DatasetExtraFiles]:
        """Get the list of extra files/directories associated with a dataset."""
        client = self._get_client()
        response = client.get(
            f"/api/histories/{history_id}/contents/{history_content_id}/extra_files", headers={"run-as": run_as}
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = DatasetExtraFiles.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def history_contents__get_metadata_file(
        self, history_id: str, history_content_id: str, *, metadata_file: str, run_as: str | None = None
    ) -> Response[Any]:
        """Returns the metadata file associated with this history item."""
        client = self._get_client()
        response = client.get(
            f"/api/histories/{history_id}/contents/{history_content_id}/metadata_file",
            params=self._filter_none_values({"metadata_file": metadata_file}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__contents_tags__index(
        self, history_content_id: str, history_id: str, *, run_as: str | None = None
    ) -> Response[ItemTagsListResponse]:
        """Show tags based on history_content_id"""
        client = self._get_client()
        response = client.get(
            f"/api/histories/{history_id}/contents/{history_content_id}/tags", headers={"run-as": run_as}
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ItemTagsListResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__contents_tags__delete(
        self, history_content_id: str, tag_name: str, history_id: str, *, run_as: str | None = None
    ) -> Response[bool]:
        """Delete tag based on history_content_id"""
        client = self._get_client()
        response = client.delete(
            f"/api/histories/{history_id}/contents/{history_content_id}/tags/{tag_name}", headers={"run-as": run_as}
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__contents_tags__show(
        self, history_content_id: str, tag_name: str, history_id: str, *, run_as: str | None = None
    ) -> Response[ItemTagsResponse]:
        """Show tag based on history_content_id"""
        client = self._get_client()
        response = client.get(
            f"/api/histories/{history_id}/contents/{history_content_id}/tags/{tag_name}", headers={"run-as": run_as}
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ItemTagsResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__contents_tags__create(
        self,
        history_content_id: str,
        tag_name: str,
        history_id: str,
        data: ItemTagsCreatePayload,
        *,
        run_as: str | None = None,
    ) -> Response[ItemTagsResponse]:
        """Create tag based on history_content_id"""
        client = self._get_client()
        response = client.post(
            f"/api/histories/{history_id}/contents/{history_content_id}/tags/{tag_name}",
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ItemTagsResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__contents_tags__update(
        self,
        history_content_id: str,
        tag_name: str,
        history_id: str,
        data: ItemTagsCreatePayload,
        *,
        run_as: str | None = None,
    ) -> Response[ItemTagsResponse]:
        """Update tag based on history_content_id"""
        client = self._get_client()
        response = client.put(
            f"/api/histories/{history_id}/contents/{history_content_id}/tags/{tag_name}",
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ItemTagsResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def history_contents__delete_legacy(
        self,
        history_id: str,
        id: str,
        data: DeleteHistoryContentPayload,
        *,
        type: HistoryContentType | None = None,
        purge: bool | None = None,
        recursive: bool | None = None,
        stop_job: bool | None = None,
        run_as: str | None = None,
    ) -> Response[Any]:
        """Delete the history dataset with the given ``ID``.

        Delete the history content with the given ``ID`` and query specified type (defaults to dataset).

        **Note**: Currently does not stop any active jobs for which this dataset is an output."""
        client = self._get_client()
        response = client.delete(
            f"/api/histories/{history_id}/contents/{id}",
            params=self._filter_none_values(
                {"type": type, "purge": purge, "recursive": recursive, "stop_job": stop_job}
            ),
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def history_contents__show_legacy(
        self,
        id: str,
        history_id: str,
        *,
        type: HistoryContentType | None = None,
        fuzzy_count: int | None = None,
        view: str | None = None,
        keys: str | None = None,
        run_as: str | None = None,
    ) -> Response[HDACustom | HDADetailed | HDASummary | HDAInaccessible | HDCACustom | HDCADetailed | HDCASummary]:
        """Return detailed information about an HDA within a history. ``/api/histories/{history_id}/contents/{type}s/{id}`` should be used instead.

        Return detailed information about an `HDA` or `HDCA` within a history.

        **Note**: Anonymous users are allowed to get their current history contents."""
        client = self._get_client()
        response = client.get(
            f"/api/histories/{history_id}/contents/{id}",
            params=self._filter_none_values({"type": type, "fuzzy_count": fuzzy_count, "view": view, "keys": keys}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = (
                HDACustom
                | HDADetailed
                | HDASummary
                | HDAInaccessible
                | HDCACustom
                | HDCADetailed
                | HDCASummary.model_validate(response.json())
            )
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def history_contents__update_legacy(
        self,
        history_id: str,
        id: str,
        data: UpdateHistoryContentsPayload,
        *,
        type: HistoryContentType | None = None,
        view: str | None = None,
        keys: str | None = None,
        run_as: str | None = None,
    ) -> Response[HDACustom | HDADetailed | HDASummary | HDAInaccessible | HDCACustom | HDCADetailed | HDCASummary]:
        """Updates the values for the history content item with the given ``ID`` and query specified type. ``/api/histories/{history_id}/contents/{type}s/{id}`` should be used instead.

        Updates the values for the history content item with the given ``ID``."""
        client = self._get_client()
        response = client.put(
            f"/api/histories/{history_id}/contents/{id}",
            params=self._filter_none_values({"type": type, "view": view, "keys": keys}),
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = (
                HDACustom
                | HDADetailed
                | HDASummary
                | HDAInaccessible
                | HDCACustom
                | HDCADetailed
                | HDCASummary.model_validate(response.json())
            )
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__contents_validate__validate(
        self, history_id: str, id: str, *, run_as: str | None = None
    ) -> Response[dict[str, Any]]:
        """Validates the metadata associated with a dataset within a History."""
        client = self._get_client()
        response = client.put(f"/api/histories/{history_id}/contents/{id}/validate", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def history_contents__index_typed(
        self,
        history_id: str,
        type: HistoryContentType,
        *,
        v: str | None = None,
        details: str | None = None,
        ids: str | None = None,
        types: list[str] | None = None,
        deleted: bool | None = None,
        visible: bool | None = None,
        shareable: bool | None = None,
        view: str | None = None,
        keys: str | None = None,
        q: list[str] | None = None,
        qv: list[str] | None = None,
        offset: int | None = None,
        limit: int | None = None,
        order: str | None = None,
        accept: Literal["application/json", "application/vnd.galaxy.history.contents.stats+json"] | None = None,
        run_as: str | None = None,
    ) -> Response[HistoryContentsResult]:
        """Returns the contents of the given history filtered by type.

        Return a list of either `HDA`/`HDCA` data for the history with the given ``ID``.

        - The contents can be filtered and queried using the appropriate parameters.
        - The amount of information returned for each item can be customized.

        **Note**: Anonymous users are allowed to get their current history contents."""
        client = self._get_client()
        response = client.get(
            f"/api/histories/{history_id}/contents/{type}s",
            params=self._filter_none_values(
                {
                    "v": v,
                    "details": details,
                    "ids": ids,
                    "types": types,
                    "deleted": deleted,
                    "visible": visible,
                    "shareable": shareable,
                    "view": view,
                    "keys": keys,
                    "q": q,
                    "qv": qv,
                    "offset": offset,
                    "limit": limit,
                    "order": order,
                }
            ),
            headers={"accept": accept, "run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = HistoryContentsResult.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def history_contents__create_typed(
        self,
        history_id: str,
        type: HistoryContentType,
        data: CreateHistoryContentPayload,
        *,
        view: str | None = None,
        keys: str | None = None,
        run_as: str | None = None,
    ) -> Response[
        HDACustom
        | HDADetailed
        | HDASummary
        | HDAInaccessible
        | HDCACustom
        | HDCADetailed
        | HDCASummary
        | list[HDACustom | HDADetailed | HDASummary | HDAInaccessible | HDCACustom | HDCADetailed | HDCASummary]
    ]:
        """Create a new `HDA` or `HDCA` in the given History."""
        client = self._get_client()
        response = client.post(
            f"/api/histories/{history_id}/contents/{type}s",
            params=self._filter_none_values({"view": view, "keys": keys}),
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = (
                HDACustom
                | HDADetailed
                | HDASummary
                | HDAInaccessible
                | HDCACustom
                | HDCADetailed
                | HDCASummary
                | list[
                    HDACustom | HDADetailed | HDASummary | HDAInaccessible | HDCACustom | HDCADetailed | HDCASummary
                ].model_validate(response.json())
            )
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def history_contents__delete_typed(
        self,
        history_id: str,
        id: str,
        type: HistoryContentType,
        data: DeleteHistoryContentPayload,
        *,
        purge: bool | None = None,
        recursive: bool | None = None,
        stop_job: bool | None = None,
        run_as: str | None = None,
    ) -> Response[Any]:
        """Delete the history content with the given ``ID`` and path specified type.

        Delete the history content with the given ``ID`` and path specified type.

        **Note**: Currently does not stop any active jobs for which this dataset is an output."""
        client = self._get_client()
        response = client.delete(
            f"/api/histories/{history_id}/contents/{type}s/{id}",
            params=self._filter_none_values({"purge": purge, "recursive": recursive, "stop_job": stop_job}),
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def history_contents__show(
        self,
        id: str,
        history_id: str,
        type: HistoryContentType,
        *,
        fuzzy_count: int | None = None,
        view: str | None = None,
        keys: str | None = None,
        run_as: str | None = None,
    ) -> Response[HDACustom | HDADetailed | HDASummary | HDAInaccessible | HDCACustom | HDCADetailed | HDCASummary]:
        """Return detailed information about a specific HDA or HDCA with the given `ID` within a history.

        Return detailed information about an `HDA` or `HDCA` within a history.

        **Note**: Anonymous users are allowed to get their current history contents."""
        client = self._get_client()
        response = client.get(
            f"/api/histories/{history_id}/contents/{type}s/{id}",
            params=self._filter_none_values({"fuzzy_count": fuzzy_count, "view": view, "keys": keys}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = (
                HDACustom
                | HDADetailed
                | HDASummary
                | HDAInaccessible
                | HDCACustom
                | HDCADetailed
                | HDCASummary.model_validate(response.json())
            )
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def history_contents__update_typed(
        self,
        history_id: str,
        id: str,
        type: HistoryContentType,
        data: UpdateHistoryContentsPayload,
        *,
        view: str | None = None,
        keys: str | None = None,
        run_as: str | None = None,
    ) -> Response[HDACustom | HDADetailed | HDASummary | HDAInaccessible | HDCACustom | HDCADetailed | HDCASummary]:
        """Updates the values for the history content item with the given ``ID`` and path specified type.

        Updates the values for the history content item with the given ``ID``."""
        client = self._get_client()
        response = client.put(
            f"/api/histories/{history_id}/contents/{type}s/{id}",
            params=self._filter_none_values({"view": view, "keys": keys}),
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = (
                HDACustom
                | HDADetailed
                | HDASummary
                | HDAInaccessible
                | HDCACustom
                | HDCADetailed
                | HDCASummary.model_validate(response.json())
            )
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__contents_jobs_summary__show_jobs_summary(
        self, history_id: str, id: str, type: HistoryContentType, *, run_as: str | None = None
    ) -> Response[JobStateSummary | ImplicitCollectionJobsStateSummary | WorkflowInvocationStateSummary]:
        """Return detailed information about an `HDA` or `HDCAs` jobs.

        Return detailed information about an `HDA` or `HDCAs` jobs.

        **Warning**: We allow anyone to fetch job state information about any object they
        can guess an encoded ID for - it isn't considered protected data. This keeps
        polling IDs as part of state calculation for large histories and collections as
        efficient as possible."""
        client = self._get_client()
        response = client.get(
            f"/api/histories/{history_id}/contents/{type}s/{id}/jobs_summary", headers={"run-as": run_as}
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = (
                JobStateSummary
                | ImplicitCollectionJobsStateSummary
                | WorkflowInvocationStateSummary.model_validate(response.json())
            )
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__contents_prepare_store_download__prepare_store_download(
        self, history_id: str, id: str, type: HistoryContentType, data: StoreExportPayload, *, run_as: str | None = None
    ) -> Response[AsyncFile]:
        """Prepare a dataset or dataset collection for export-style download."""
        client = self._get_client()
        response = client.post(
            f"/api/histories/{history_id}/contents/{type}s/{id}/prepare_store_download",
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = AsyncFile.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__contents_write_store__write_store(
        self,
        history_id: str,
        id: str,
        type: HistoryContentType,
        data: WriteStoreToPayload,
        *,
        run_as: str | None = None,
    ) -> Response[AsyncTaskResultSummary]:
        """Prepare a dataset or dataset collection for export-style download and write to supplied URI."""
        client = self._get_client()
        response = client.post(
            f"/api/histories/{history_id}/contents/{type}s/{id}/write_store",
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = AsyncTaskResultSummary.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__contents_from_store__create_from_store(
        self,
        history_id: str,
        data: CreateHistoryContentFromStore,
        *,
        view: str | None = None,
        keys: str | None = None,
        run_as: str | None = None,
    ) -> Response[
        list[HDACustom | HDADetailed | HDASummary | HDAInaccessible | HDCACustom | HDCADetailed | HDCASummary]
    ]:
        """Create contents from store.

        Create history contents from model store.
        Input can be a tarfile created with build_objects script distributed
        with galaxy-data, from an exported history with files stripped out,
        or hand-crafted JSON dictionary."""
        client = self._get_client()
        response = client.post(
            f"/api/histories/{history_id}/contents_from_store",
            params=self._filter_none_values({"view": view, "keys": keys}),
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [
                HDACustom
                | HDADetailed
                | HDASummary
                | HDAInaccessible
                | HDCACustom
                | HDCADetailed
                | HDCASummary.model_validate(item)
                for item in response.json()
            ]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def history_contents__copy_contents(
        self, history_id: str, data: CopyDatasetsPayload, *, run_as: str | None = None
    ) -> Response[CopyDatasetsResponse]:
        """Copy datasets or dataset collections to other histories."""
        client = self._get_client()
        response = client.post(
            f"/api/histories/{history_id}/copy_contents",
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = CopyDatasetsResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__custom_builds_metadata__get_custom_builds_metadata(
        self, history_id: str, *, run_as: str | None = None
    ) -> Response[CustomBuildsMetadataResponse]:
        """Returns meta data for custom builds."""
        client = self._get_client()
        response = client.get(f"/api/histories/{history_id}/custom_builds_metadata", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = CustomBuildsMetadataResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__disable_link_access__disable_link_access(
        self, history_id: str, *, run_as: str | None = None
    ) -> Response[SharingStatus]:
        """Makes this item inaccessible by a URL link.

        Makes this item inaccessible by a URL link and return the current sharing status."""
        client = self._get_client()
        response = client.put(f"/api/histories/{history_id}/disable_link_access", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = SharingStatus.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__enable_link_access__enable_link_access(
        self, history_id: str, *, run_as: str | None = None
    ) -> Response[SharingStatus]:
        """Makes this item accessible by a URL link.

        Makes this item accessible by a URL link and return the current sharing status."""
        client = self._get_client()
        response = client.put(f"/api/histories/{history_id}/enable_link_access", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = SharingStatus.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__exports__index_exports(
        self,
        history_id: str,
        *,
        limit: int | None = None,
        offset: int | None = None,
        accept: Literal["application/json", "application/vnd.galaxy.task.export+json"] | None = None,
        run_as: str | None = None,
    ) -> Response[JobExportHistoryArchiveListResponse]:
        """Get previous history exports.

        By default the legacy job-based history exports (jeha) are returned.

        Change the `accept` content type header to return the new task-based history exports."""
        client = self._get_client()
        response = client.get(
            f"/api/histories/{history_id}/exports",
            params=self._filter_none_values({"limit": limit, "offset": offset}),
            headers={"accept": accept, "run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = JobExportHistoryArchiveListResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__exports__archive_export(
        self, history_id: str, data: ExportHistoryArchivePayload | None, *, run_as: str | None = None
    ) -> Response[JobExportHistoryArchiveModel | JobIdResponse]:
        """Start job (if needed) to create history export for corresponding history.

        This will start a job to create a history export archive.

        Calling this endpoint multiple times will return the 202 status code until the archive
        has been completely generated and is ready to download. When ready, it will return
        the 200 status code along with the download link information.

        If the history will be exported to a `directory_uri`, instead of returning the download
        link information, the Job ID will be returned so it can be queried to determine when
        the file has been written.

        **Deprecation notice**: Please use `/api/histories/{id}/prepare_store_download` or
        `/api/histories/{id}/write_store` instead."""
        client = self._get_client()
        response = client.put(f"/api/histories/{history_id}/exports", headers={"run-as": run_as}, json=data)
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = JobExportHistoryArchiveModel | JobIdResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__exports__archive_download(
        self, history_id: str, jeha_id: str, *, run_as: str | None = None
    ) -> Response[Any]:
        """If ready and available, return raw contents of exported history as a downloadable archive.

        See ``PUT /api/histories/{id}/exports`` to initiate the creation
        of the history export - when ready, that route will return 200 status
        code (instead of 202) and this route can be used to download the archive.

        **Deprecation notice**: Please use `/api/histories/{id}/prepare_store_download` or
        `/api/histories/{id}/write_store` instead."""
        client = self._get_client()
        response = client.get(f"/api/histories/{history_id}/exports/{jeha_id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__jobs_summary__index_jobs_summary(
        self, history_id: str, *, ids: str | None = None, types: str | None = None, run_as: str | None = None
    ) -> Response[list[JobStateSummary | ImplicitCollectionJobsStateSummary | WorkflowInvocationStateSummary]]:
        """Return job state summary info for jobs, implicit groups jobs for collections or workflow invocations.

        Return job state summary info for jobs, implicit groups jobs for collections or workflow invocations.

        **Warning**: We allow anyone to fetch job state information about any object they
        can guess an encoded ID for - it isn't considered protected data. This keeps
        polling IDs as part of state calculation for large histories and collections as
        efficient as possible."""
        client = self._get_client()
        response = client.get(
            f"/api/histories/{history_id}/jobs_summary",
            params=self._filter_none_values({"ids": ids, "types": types}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [
                JobStateSummary
                | ImplicitCollectionJobsStateSummary
                | WorkflowInvocationStateSummary.model_validate(item)
                for item in response.json()
            ]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__materialize__materialize_to_history(
        self, history_id: str, data: MaterializeDatasetInstanceAPIRequest, *, run_as: str | None = None
    ) -> Response[AsyncTaskResultSummary]:
        """Materialize a deferred library or HDA dataset into real, usable dataset in specified history."""
        client = self._get_client()
        response = client.post(
            f"/api/histories/{history_id}/materialize",
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = AsyncTaskResultSummary.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__prepare_store_download__prepare_store_download(
        self, history_id: str, data: StoreExportPayload, *, run_as: str | None = None
    ) -> Response[AsyncFile]:
        """Return a short term storage token to monitor download of the history."""
        client = self._get_client()
        response = client.post(
            f"/api/histories/{history_id}/prepare_store_download",
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = AsyncFile.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__publish__publish(self, history_id: str, *, run_as: str | None = None) -> Response[SharingStatus]:
        """Makes this item public and accessible by a URL link.

        Makes this item publicly available by a URL link and return the current sharing status."""
        client = self._get_client()
        response = client.put(f"/api/histories/{history_id}/publish", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = SharingStatus.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__share_with_users__share_with_users(
        self, history_id: str, data: ShareWithPayload, *, run_as: str | None = None
    ) -> Response[ShareHistoryWithStatus]:
        """Share this item with specific users.

        Shares this item with specific users and return the current sharing status."""
        client = self._get_client()
        response = client.put(
            f"/api/histories/{history_id}/share_with_users",
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ShareHistoryWithStatus.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__sharing__sharing(self, history_id: str, *, run_as: str | None = None) -> Response[SharingStatus]:
        """Get the current sharing status of the given item.

        Return the sharing status of the item."""
        client = self._get_client()
        response = client.get(f"/api/histories/{history_id}/sharing", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = SharingStatus.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__slug__set_slug(
        self, history_id: str, data: SetSlugPayload, *, run_as: str | None = None
    ) -> Response[Any]:
        """Set a new slug for this shared item.

        Sets a new slug to access this item by URL. The new slug must be unique."""
        client = self._get_client()
        response = client.put(
            f"/api/histories/{history_id}/slug", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__tags__index(self, history_id: str, *, run_as: str | None = None) -> Response[ItemTagsListResponse]:
        """Show tags based on history_id"""
        client = self._get_client()
        response = client.get(f"/api/histories/{history_id}/tags", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ItemTagsListResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__tags__delete(self, history_id: str, tag_name: str, *, run_as: str | None = None) -> Response[bool]:
        """Delete tag based on history_id"""
        client = self._get_client()
        response = client.delete(f"/api/histories/{history_id}/tags/{tag_name}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__tags__show(
        self, history_id: str, tag_name: str, *, run_as: str | None = None
    ) -> Response[ItemTagsResponse]:
        """Show tag based on history_id"""
        client = self._get_client()
        response = client.get(f"/api/histories/{history_id}/tags/{tag_name}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ItemTagsResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__tags__create(
        self, history_id: str, tag_name: str, data: ItemTagsCreatePayload, *, run_as: str | None = None
    ) -> Response[ItemTagsResponse]:
        """Create tag based on history_id"""
        client = self._get_client()
        response = client.post(
            f"/api/histories/{history_id}/tags/{tag_name}",
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ItemTagsResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__tags__update(
        self, history_id: str, tag_name: str, data: ItemTagsCreatePayload, *, run_as: str | None = None
    ) -> Response[ItemTagsResponse]:
        """Update tag based on history_id"""
        client = self._get_client()
        response = client.put(
            f"/api/histories/{history_id}/tags/{tag_name}",
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ItemTagsResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__tool_requests__tool_requests(
        self, history_id: str, *, run_as: str | None = None
    ) -> Response[list[ToolRequestModel]]:
        """Return all the tool requests for the tools submitted to this history."""
        client = self._get_client()
        response = client.get(f"/api/histories/{history_id}/tool_requests", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [ToolRequestModel.model_validate(item) for item in response.json()]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__unpublish__unpublish(self, history_id: str, *, run_as: str | None = None) -> Response[SharingStatus]:
        """Removes this item from the published list.

        Removes this item from the published list and return the current sharing status."""
        client = self._get_client()
        response = client.put(f"/api/histories/{history_id}/unpublish", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = SharingStatus.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def histories__write_store__write_store(
        self, history_id: str, data: WriteStoreToPayload, *, run_as: str | None = None
    ) -> Response[AsyncTaskResultSummary]:
        """Prepare history for export-style download and write to supplied URI."""
        client = self._get_client()
        response = client.post(
            f"/api/histories/{history_id}/write_store",
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = AsyncTaskResultSummary.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__index_invocations(
        self,
        *,
        workflow_id: str | None = None,
        history_id: str | None = None,
        job_id: str | None = None,
        user_id: str | None = None,
        sort_by: InvocationSortByEnum | None = None,
        sort_desc: bool | None = None,
        include_terminal: bool | None = None,
        limit: int | None = None,
        offset: int | None = None,
        instance: bool | None = None,
        view: str | None = None,
        step_details: bool | None = None,
        include_nested_invocations: bool | None = None,
        run_as: str | None = None,
    ) -> Response[list[Any]]:
        """Get the list of a user's workflow invocations."""
        client = self._get_client()
        response = client.get(
            "/api/invocations",
            params=self._filter_none_values(
                {
                    "workflow_id": workflow_id,
                    "history_id": history_id,
                    "job_id": job_id,
                    "user_id": user_id,
                    "sort_by": sort_by,
                    "sort_desc": sort_desc,
                    "include_terminal": include_terminal,
                    "limit": limit,
                    "offset": offset,
                    "instance": instance,
                    "view": view,
                    "step_details": step_details,
                    "include_nested_invocations": include_nested_invocations,
                }
            ),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [Any.model_validate(item) for item in response.json()]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__from_store__create_invocations_from_store(
        self, data: CreateInvocationsFromStorePayload, *, run_as: str | None = None
    ) -> Response[list[Any]]:
        """Create Invocations From Store

        Create invocation(s) from a supplied model store."""
        client = self._get_client()
        response = client.post(
            "/api/invocations/from_store", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [Any.model_validate(item) for item in response.json()]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__steps__step(self, step_id: str, *, run_as: str | None = None) -> Response[InvocationStep]:
        """Show details of workflow invocation step."""
        client = self._get_client()
        response = client.get(f"/api/invocations/steps/{step_id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = InvocationStep.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__cancel_invocation(
        self,
        invocation_id: str,
        *,
        step_details: bool | None = None,
        legacy_job_state: bool | None = None,
        run_as: str | None = None,
    ) -> Response[Any]:
        """Cancel the specified workflow invocation."""
        client = self._get_client()
        response = client.delete(
            f"/api/invocations/{invocation_id}",
            params=self._filter_none_values({"step_details": step_details, "legacy_job_state": legacy_job_state}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__show_invocation(
        self,
        invocation_id: str,
        *,
        step_details: bool | None = None,
        legacy_job_state: bool | None = None,
        run_as: str | None = None,
    ) -> Response[Any]:
        """Get detailed description of a workflow invocation."""
        client = self._get_client()
        response = client.get(
            f"/api/invocations/{invocation_id}",
            params=self._filter_none_values({"step_details": step_details, "legacy_job_state": legacy_job_state}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__error__report_error(
        self, invocation_id: str, data: ReportInvocationErrorPayload, *, run_as: str | None = None
    ) -> Response[Any]:
        """Submits a bug report for a workflow run via the API."""
        client = self._get_client()
        response = client.post(
            f"/api/invocations/{invocation_id}/error",
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__jobs_summary__invocation_jobs_summary(
        self, invocation_id: str, *, run_as: str | None = None
    ) -> Response[InvocationJobsResponse]:
        """Get job state summary info aggregated across all current jobs of the workflow invocation.

        Warning: We allow anyone to fetch job state information about any object they
        can guess an encoded ID for - it isn't considered protected data. This keeps
        polling IDs as part of state calculation for large histories and collections as
        efficient as possible."""
        client = self._get_client()
        response = client.get(f"/api/invocations/{invocation_id}/jobs_summary", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = InvocationJobsResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__metrics__get_invocation_metrics(
        self, invocation_id: str, *, run_as: str | None = None
    ) -> Response[list[WorkflowJobMetric]]:
        """Get Invocation Metrics"""
        client = self._get_client()
        response = client.get(f"/api/invocations/{invocation_id}/metrics", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [WorkflowJobMetric.model_validate(item) for item in response.json()]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__prepare_store_download__prepare_store_download(
        self, invocation_id: str, data: PrepareStoreDownloadPayload, *, run_as: str | None = None
    ) -> Response[AsyncFile]:
        """Prepare a workflow invocation export-style download."""
        client = self._get_client()
        response = client.post(
            f"/api/invocations/{invocation_id}/prepare_store_download",
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = AsyncFile.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__report__show_invocation_report(
        self, invocation_id: str, *, run_as: str | None = None
    ) -> Response[InvocationReport]:
        """Get JSON summarizing invocation for reporting."""
        client = self._get_client()
        response = client.get(f"/api/invocations/{invocation_id}/report", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = InvocationReport.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__report_pdf__show_invocation_report_pdf(
        self, invocation_id: str, *, run_as: str | None = None
    ) -> Response[Any]:
        """Get PDF summarizing invocation for reporting."""
        client = self._get_client()
        response = client.get(f"/api/invocations/{invocation_id}/report.pdf", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__request__invocation_as_request(
        self, invocation_id: str, *, run_as: str | None = None
    ) -> Response[WorkflowInvocationRequestModel]:
        """Get a description modeling an API request to invoke this workflow - this is recreated and will be more specific in some ways than the initial creation request."""
        client = self._get_client()
        response = client.get(f"/api/invocations/{invocation_id}/request", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = WorkflowInvocationRequestModel.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__step_jobs_summary__invocation_step_jobs_summary(
        self, invocation_id: str, *, run_as: str | None = None
    ) -> Response[
        list[
            InvocationStepJobsResponseStepModel
            | InvocationStepJobsResponseJobModel
            | InvocationStepJobsResponseCollectionJobsModel
        ]
    ]:
        """Get job state summary info aggregated per step of the workflow invocation.

        Warning: We allow anyone to fetch job state information about any object they
        can guess an encoded ID for - it isn't considered protected data. This keeps
        polling IDs as part of state calculation for large histories and collections as
        efficient as possible."""
        client = self._get_client()
        response = client.get(f"/api/invocations/{invocation_id}/step_jobs_summary", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [
                InvocationStepJobsResponseStepModel
                | InvocationStepJobsResponseJobModel
                | InvocationStepJobsResponseCollectionJobsModel.model_validate(item)
                for item in response.json()
            ]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__steps__invocation_step(
        self, invocation_id: str, step_id: str, *, run_as: str | None = None
    ) -> Response[InvocationStep]:
        """Show details of workflow invocation step.

        An alias for `GET /api/invocations/steps/{step_id}`. `invocation_id` is ignored."""
        client = self._get_client()
        response = client.get(f"/api/invocations/{invocation_id}/steps/{step_id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = InvocationStep.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__steps__update_invocation_step(
        self, invocation_id: str, step_id: str, data: InvocationUpdatePayload, *, run_as: str | None = None
    ) -> Response[InvocationStep]:
        """Update state of running workflow step invocation - still very nebulous but this would be for stuff like confirming paused steps can proceed etc."""
        client = self._get_client()
        response = client.put(
            f"/api/invocations/{invocation_id}/steps/{step_id}",
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = InvocationStep.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__write_store__write_store(
        self, invocation_id: str, data: WriteInvocationStoreToPayload, *, run_as: str | None = None
    ) -> Response[AsyncTaskResultSummary]:
        """Prepare a workflow invocation export-style download and write to supplied URI."""
        client = self._get_client()
        response = client.post(
            f"/api/invocations/{invocation_id}/write_store",
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = AsyncTaskResultSummary.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def job_lock__job_lock_status(self, *, run_as: str | None = None) -> Response[JobLock]:
        """Job Lock Status

        Get job lock status."""
        client = self._get_client()
        response = client.get("/api/job_lock", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = JobLock.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def job_lock__update_job_lock(self, data: JobLock, *, run_as: str | None = None) -> Response[JobLock]:
        """Update Job Lock

        Set job lock status."""
        client = self._get_client()
        response = client.put("/api/job_lock", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True))
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = JobLock.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def jobs__index(
        self,
        *,
        user_details: bool | None = None,
        user_id: str | None = None,
        view: JobIndexViewEnum | None = None,
        date_range_min: str | None = None,
        date_range_max: str | None = None,
        history_id: str | None = None,
        workflow_id: str | None = None,
        invocation_id: str | None = None,
        implicit_collection_jobs_id: str | None = None,
        tool_request_id: str | None = None,
        order_by: JobIndexSortByEnum | None = None,
        search: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
        state: list[str] | None = None,
        tool_id: list[str] | None = None,
        tool_id_like: list[str] | None = None,
        run_as: str | None = None,
    ) -> Response[list[ShowFullJobResponse | EncodedJobDetails | JobSummary]]:
        """Index"""
        client = self._get_client()
        response = client.get(
            "/api/jobs",
            params=self._filter_none_values(
                {
                    "user_details": user_details,
                    "user_id": user_id,
                    "view": view,
                    "date_range_min": date_range_min,
                    "date_range_max": date_range_max,
                    "history_id": history_id,
                    "workflow_id": workflow_id,
                    "invocation_id": invocation_id,
                    "implicit_collection_jobs_id": implicit_collection_jobs_id,
                    "tool_request_id": tool_request_id,
                    "order_by": order_by,
                    "search": search,
                    "limit": limit,
                    "offset": offset,
                    "state": state,
                    "tool_id": tool_id,
                    "tool_id_like": tool_id_like,
                }
            ),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [
                ShowFullJobResponse | EncodedJobDetails | JobSummary.model_validate(item) for item in response.json()
            ]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def jobs__create(self, data: JobRequest, *, run_as: str | None = None) -> Response[JobCreateResponse]:
        """Create"""
        client = self._get_client()
        response = client.post("/api/jobs", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True))
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = JobCreateResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def jobs__search__search(
        self, data: SearchJobsPayload, *, run_as: str | None = None
    ) -> Response[list[EncodedJobDetails]]:
        """Return jobs for current user

        This method is designed to scan the list of previously run jobs and find records of jobs that had
        the exact some input parameters and datasets. This can be used to minimize the amount of repeated work, and simply
        recycle the old results."""
        client = self._get_client()
        response = client.post("/api/jobs/search", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True))
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [EncodedJobDetails.model_validate(item) for item in response.json()]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def jobs__delete(self, job_id: str, data: DeleteJobPayload | None, *, run_as: str | None = None) -> Response[bool]:
        """Cancels specified job"""
        client = self._get_client()
        response = client.delete(f"/api/jobs/{job_id}", headers={"run-as": run_as}, json=data)
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def jobs__show(
        self, job_id: str, *, full: bool | None = None, run_as: str | None = None
    ) -> Response[ShowFullJobResponse | EncodedJobDetails]:
        """Return dictionary containing description of job data."""
        client = self._get_client()
        response = client.get(
            f"/api/jobs/{job_id}", params=self._filter_none_values({"full": full}), headers={"run-as": run_as}
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ShowFullJobResponse | EncodedJobDetails.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def jobs__common_problems__common_problems(
        self, job_id: str, *, run_as: str | None = None
    ) -> Response[JobInputSummary]:
        """Check inputs and job for common potential problems to aid in error reporting"""
        client = self._get_client()
        response = client.get(f"/api/jobs/{job_id}/common_problems", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = JobInputSummary.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def jobs__console_output__console_output(
        self,
        job_id: str,
        *,
        stdout_position: int,
        stdout_length: int,
        stderr_position: int,
        stderr_length: int,
        run_as: str | None = None,
    ) -> Response[JobConsoleOutput]:
        """Returns STDOUT and STDERR from the tool running in a specific job.

        Get the stdout and/or stderr from the tool running in a specific job. The position parameters are the index
        of where to start reading stdout/stderr. The length parameters control how much
        stdout/stderr is read."""
        client = self._get_client()
        response = client.get(
            f"/api/jobs/{job_id}/console_output",
            params=self._filter_none_values(
                {
                    "stdout_position": stdout_position,
                    "stdout_length": stdout_length,
                    "stderr_position": stderr_position,
                    "stderr_length": stderr_length,
                }
            ),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = JobConsoleOutput.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def jobs__destination_params__destination_params(
        self, job_id: str, *, run_as: str | None = None
    ) -> Response[JobDestinationParams]:
        """Return destination parameters for specified job."""
        client = self._get_client()
        response = client.get(f"/api/jobs/{job_id}/destination_params", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = JobDestinationParams.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def jobs__error__error(
        self, job_id: str, data: ReportJobErrorPayload, *, run_as: str | None = None
    ) -> Response[JobErrorSummary]:
        """Submits a bug report via the API."""
        client = self._get_client()
        response = client.post(
            f"/api/jobs/{job_id}/error", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = JobErrorSummary.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def jobs__inputs__inputs(self, job_id: str, *, run_as: str | None = None) -> Response[list[JobInputAssociation]]:
        """Returns input datasets created by a job."""
        client = self._get_client()
        response = client.get(f"/api/jobs/{job_id}/inputs", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [JobInputAssociation.model_validate(item) for item in response.json()]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def jobs__metrics__metrics_by_job(
        self, job_id: str, *, hda_ldda: DatasetSourceType | None = None, run_as: str | None = None
    ) -> Response[list[JobMetric | None]]:
        """Return job metrics for specified job."""
        client = self._get_client()
        response = client.get(
            f"/api/jobs/{job_id}/metrics",
            params=self._filter_none_values({"hda_ldda": hda_ldda}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [JobMetric | None.model_validate(item) for item in response.json()]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def remote_files__oidc_tokens__get_token(
        self, job_id: str, *, job_key: str, provider: str, run_as: str | None = None
    ) -> Response[str]:
        """Get a fresh OIDC token

        Allows remote job running mechanisms to get a fresh OIDC token that can be used on remote side to authorize user. It is not meant to represent part of Galaxy's stable, user facing API"""
        client = self._get_client()
        response = client.get(
            f"/api/jobs/{job_id}/oidc-tokens",
            params=self._filter_none_values({"job_key": job_key, "provider": provider}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.text
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def jobs__outputs__outputs(
        self, job_id: str, *, run_as: str | None = None
    ) -> Response[list[JobOutputAssociation | JobOutputCollectionAssociation]]:
        """Returns output datasets created by a job."""
        client = self._get_client()
        response = client.get(f"/api/jobs/{job_id}/outputs", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [
                JobOutputAssociation | JobOutputCollectionAssociation.model_validate(item) for item in response.json()
            ]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def jobs__parameters_display__parameters_display_by_job(
        self, job_id: str, *, hda_ldda: DatasetSourceType | None = None, run_as: str | None = None
    ) -> Response[JobDisplayParametersSummary]:
        """Resolve parameters as a list for nested display.

        **Warning**: This API is unstable and may change without notice."""
        client = self._get_client()
        response = client.get(
            f"/api/jobs/{job_id}/parameters_display",
            params=self._filter_none_values({"hda_ldda": hda_ldda}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = JobDisplayParametersSummary.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def jobs__resume__resume(self, job_id: str, *, run_as: str | None = None) -> Response[list[JobOutputAssociation]]:
        """Resumes a paused job."""
        client = self._get_client()
        response = client.put(f"/api/jobs/{job_id}/resume", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [JobOutputAssociation.model_validate(item) for item in response.json()]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def libraries__index(
        self, *, deleted: bool | None = None, run_as: str | None = None
    ) -> Response[LibrarySummaryList]:
        """Returns a list of summary data for all libraries."""
        client = self._get_client()
        response = client.get(
            "/api/libraries", params=self._filter_none_values({"deleted": deleted}), headers={"run-as": run_as}
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = LibrarySummaryList.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def libraries__create(self, data: CreateLibraryPayload, *, run_as: str | None = None) -> Response[LibrarySummary]:
        """Creates a new library and returns its summary information.

        Creates a new library and returns its summary information. Currently, only admin users can create libraries."""
        client = self._get_client()
        response = client.post("/api/libraries", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True))
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = LibrarySummary.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def libraries__deleted__index_deleted(self, *, run_as: str | None = None) -> Response[LibrarySummaryList]:
        """Returns a list of summary data for all libraries marked as deleted."""
        client = self._get_client()
        response = client.get("/api/libraries/deleted", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = LibrarySummaryList.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def libraries__from_store__create_from_store(
        self, data: CreateLibrariesFromStore, *, run_as: str | None = None
    ) -> Response[list[LibrarySummary]]:
        """Create libraries from a model store."""
        client = self._get_client()
        response = client.post(
            "/api/libraries/from_store", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [LibrarySummary.model_validate(item) for item in response.json()]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def libraries__delete(
        self, id: str, data: DeleteLibraryPayload | None, *, undelete: bool | None = None, run_as: str | None = None
    ) -> Response[LibrarySummary]:
        """Marks the specified library as deleted (or undeleted).

        Marks the specified library as deleted (or undeleted).
        Currently, only admin users can delete or restore libraries."""
        client = self._get_client()
        response = client.delete(
            f"/api/libraries/{id}",
            params=self._filter_none_values({"undelete": undelete}),
            headers={"run-as": run_as},
            json=data,
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = LibrarySummary.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def libraries__show(self, id: str, *, run_as: str | None = None) -> Response[LibrarySummary]:
        """Returns summary information about a particular library."""
        client = self._get_client()
        response = client.get(f"/api/libraries/{id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = LibrarySummary.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def libraries__update(
        self, id: str, data: UpdateLibraryPayload, *, run_as: str | None = None
    ) -> Response[LibrarySummary]:
        """Updates the information of an existing library."""
        client = self._get_client()
        response = client.patch(
            f"/api/libraries/{id}", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = LibrarySummary.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def libraries__permissions__get_permissions(
        self,
        id: str,
        *,
        scope: LibraryPermissionScope | None = None,
        is_library_access: bool | None = None,
        page: int | None = None,
        page_limit: int | None = None,
        q: str | None = None,
        run_as: str | None = None,
    ) -> Response[LibraryCurrentPermissions | LibraryAvailablePermissions]:
        """Gets the current or available permissions of a particular library.

        Gets the current or available permissions of a particular library.
        The results can be paginated and additionally filtered by a query."""
        client = self._get_client()
        response = client.get(
            f"/api/libraries/{id}/permissions",
            params=self._filter_none_values(
                {"scope": scope, "is_library_access": is_library_access, "page": page, "page_limit": page_limit, "q": q}
            ),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = LibraryCurrentPermissions | LibraryAvailablePermissions.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def libraries__permissions__set_permissions(
        self,
        id: str,
        data: LibraryPermissionsPayload | LegacyLibraryPermissionsPayload,
        *,
        action: LibraryPermissionAction | None = None,
        run_as: str | None = None,
    ) -> Response[LibraryLegacySummary | LibraryCurrentPermissions]:
        """Sets the permissions to access and manipulate a library."""
        client = self._get_client()
        response = client.post(
            f"/api/libraries/{id}/permissions",
            params=self._filter_none_values({"action": action}),
            headers={"run-as": run_as},
            json=data,
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = LibraryLegacySummary | LibraryCurrentPermissions.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def libraries__contents__index(
        self, library_id: str, *, run_as: str | None = None
    ) -> Response[LibraryContentsIndexListResponse]:
        """Return a list of library files and folders.

        This endpoint is deprecated. Please use GET /api/folders/{folder_id}/contents instead."""
        client = self._get_client()
        response = client.get(f"/api/libraries/{library_id}/contents", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = LibraryContentsIndexListResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def libraries__contents__create_form(
        self, library_id: str, data: BodyLibraries_contents_createForm, *, run_as: str | None = None
    ) -> Response[
        LibraryContentsCreateFolderListResponse
        | LibraryContentsCreateFileListResponse
        | LibraryContentsCreateDatasetCollectionResponse
        | LibraryContentsCreateDatasetResponse
    ]:
        """Create a new library file or folder.

        This endpoint is deprecated. Please use POST /api/folders/{folder_id} or POST /api/folders/{folder_id}/contents instead."""
        client = self._get_client()
        response = client.post(
            f"/api/libraries/{library_id}/contents",
            headers={"run-as": run_as},
            data=dict(
                [
                    item
                    for item in [
                        ("create_type", data.create_type),
                        ("dbkey", data.dbkey) if data.dbkey is not None else None,
                        ("extended_metadata", data.extended_metadata) if data.extended_metadata is not None else None,
                        ("file_type", data.file_type) if data.file_type is not None else None,
                        ("files", data.files) if data.files is not None else None,
                        ("filesystem_paths", data.filesystem_paths) if data.filesystem_paths is not None else None,
                        ("folder_id", data.folder_id),
                        ("from_hda_id", data.from_hda_id) if data.from_hda_id is not None else None,
                        ("from_hdca_id", data.from_hdca_id) if data.from_hdca_id is not None else None,
                        ("ldda_message", data.ldda_message) if data.ldda_message is not None else None,
                        ("link_data_only", data.link_data_only) if data.link_data_only is not None else None,
                        ("roles", data.roles) if data.roles is not None else None,
                        ("server_dir", data.server_dir) if data.server_dir is not None else None,
                        ("tag_using_filenames", data.tag_using_filenames)
                        if data.tag_using_filenames is not None
                        else None,
                        ("tags", data.tags) if data.tags is not None else None,
                        ("upload_files", data.upload_files) if data.upload_files is not None else None,
                        ("upload_option", data.upload_option) if data.upload_option is not None else None,
                        ("uuid", data.uuid) if data.uuid is not None else None,
                    ]
                    if item is not None
                ]
            ),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = (
                LibraryContentsCreateFolderListResponse
                | LibraryContentsCreateFileListResponse
                | LibraryContentsCreateDatasetCollectionResponse
                | LibraryContentsCreateDatasetResponse.model_validate(response.json())
            )
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def libraries__contents__delete(
        self, library_id: str, id: str, data: LibraryContentsDeletePayload | None, *, run_as: str | None = None
    ) -> Response[LibraryContentsDeleteResponse]:
        """Delete a library file or folder.

        This endpoint is deprecated. Please use DELETE /api/libraries/datasets/{id} instead."""
        client = self._get_client()
        response = client.delete(f"/api/libraries/{library_id}/contents/{id}", headers={"run-as": run_as}, json=data)
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = LibraryContentsDeleteResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def libraries__contents__show(
        self, library_id: str, id: str, *, run_as: str | None = None
    ) -> Response[LibraryContentsShowFolderResponse | LibraryContentsShowDatasetResponse]:
        """Return a library file or folder.

        This endpoint is deprecated. Please use GET /api/libraries/datasets/{id} instead."""
        client = self._get_client()
        response = client.get(f"/api/libraries/{library_id}/contents/{id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = LibraryContentsShowFolderResponse | LibraryContentsShowDatasetResponse.model_validate(
                response.json()
            )
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def libraries__contents__update(
        self, library_id: str, id: str, *, payload: Any, run_as: str | None = None
    ) -> Response[Any]:
        """Update a library file or folder.

        This endpoint is deprecated. Please use PATCH /api/libraries/datasets/{id} instead."""
        client = self._get_client()
        response = client.put(
            f"/api/libraries/{library_id}/contents/{id}",
            params=self._filter_none_values({"payload": payload}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def licenses__index(self) -> Response[list[LicenseMetadataModel]]:
        """Lists all available SPDX licenses

        Returns an index with all the available [SPDX licenses](https://spdx.org/licenses/)."""
        client = self._get_client()
        response = client.get("/api/licenses")
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [LicenseMetadataModel.model_validate(item) for item in response.json()]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def licenses__get(self, id: Any) -> Response[LicenseMetadataModel]:
        """Gets the SPDX license metadata associated with the short identifier

        Returns the license metadata associated with the given
        [SPDX license short ID](https://spdx.github.io/spdx-spec/appendix-I-SPDX-license-list/)."""
        client = self._get_client()
        response = client.get(f"/api/licenses/{id}")
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = LicenseMetadataModel.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def metrics__create(self, data: CreateMetricsPayload, *, run_as: str | None = None) -> Response[Any]:
        """Records a collection of metrics.

        Record any metrics sent and return some status object."""
        client = self._get_client()
        response = client.post("/api/metrics", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True))
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def notifications__delete_user_notifications(
        self, data: NotificationsBatchRequest, *, run_as: str | None = None
    ) -> Response[NotificationsBatchUpdateResponse]:
        """Deletes a list of notifications received by the user in a single request."""
        client = self._get_client()
        response = client.delete(
            "/api/notifications", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = NotificationsBatchUpdateResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def notifications__get_user_notifications(
        self, *, limit: int | None = None, offset: int | None = None, run_as: str | None = None
    ) -> Response[UserNotificationListResponse]:
        """Returns the list of notifications associated with the user.

        Anonymous users cannot receive personal notifications, only broadcasted notifications.

        You can use the `limit` and `offset` parameters to paginate through the notifications."""
        client = self._get_client()
        response = client.get(
            "/api/notifications",
            params=self._filter_none_values({"limit": limit, "offset": offset}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = UserNotificationListResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def notifications__send_notification(
        self, data: NotificationCreateRequest, *, run_as: str | None = None
    ) -> Response[NotificationCreatedResponse | AsyncTaskResultSummary]:
        """Sends a notification to a list of recipients (users, groups or roles)."""
        client = self._get_client()
        response = client.post(
            "/api/notifications", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = NotificationCreatedResponse | AsyncTaskResultSummary.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def notifications__update_user_notifications(
        self, data: UserNotificationsBatchUpdateRequest, *, run_as: str | None = None
    ) -> Response[NotificationsBatchUpdateResponse]:
        """Updates a list of notifications with the requested values in a single request."""
        client = self._get_client()
        response = client.put(
            "/api/notifications", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = NotificationsBatchUpdateResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def notifications__broadcast__get_all_broadcasted(
        self, *, run_as: str | None = None
    ) -> Response[BroadcastNotificationListResponse]:
        """Returns all currently active broadcasted notifications.

        Only Admin users can access inactive notifications (scheduled or recently expired)."""
        client = self._get_client()
        response = client.get("/api/notifications/broadcast", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = BroadcastNotificationListResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def notifications__broadcast__broadcast_notification(
        self, data: BroadcastNotificationCreateRequest, *, run_as: str | None = None
    ) -> Response[NotificationCreatedResponse]:
        """Broadcasts a notification to every user in the system.

        Broadcasted notifications are a special kind of notification that are always accessible to all users, including anonymous users.
        They are typically used to display important information such as maintenance windows or new features.
        These notifications are displayed differently from regular notifications, usually in a banner at the top or bottom of the page.

        Broadcasted notifications can include action links that are displayed as buttons.
        This allows users to easily perform tasks such as filling out surveys, accepting legal agreements, or accessing new tutorials.

        Some key features of broadcasted notifications include:
        - They are not associated with a specific user, so they cannot be deleted or marked as read.
        - They can be scheduled to be displayed in the future or to expire after a certain time.
        - By default, broadcasted notifications are published immediately and expire six months after publication.
        - Only admins can create, edit, reschedule, or expire broadcasted notifications as needed."""
        client = self._get_client()
        response = client.post(
            "/api/notifications/broadcast", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = NotificationCreatedResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def notifications__broadcast__get_broadcasted(
        self, notification_id: str, *, run_as: str | None = None
    ) -> Response[BroadcastNotificationResponse]:
        """Returns the information of a specific broadcasted notification.

        Only Admin users can access inactive notifications (scheduled or recently expired)."""
        client = self._get_client()
        response = client.get(f"/api/notifications/broadcast/{notification_id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = BroadcastNotificationResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def notifications__broadcast__update_broadcasted_notification(
        self, notification_id: str, data: NotificationBroadcastUpdateRequest, *, run_as: str | None = None
    ) -> Response[Any]:
        """Updates the state of a broadcasted notification.

        Only Admins can update broadcasted notifications. This is useful to reschedule, edit or expire broadcasted notifications."""
        client = self._get_client()
        response = client.put(
            f"/api/notifications/broadcast/{notification_id}",
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def notifications__preferences__get_notification_preferences(
        self, *, run_as: str | None = None
    ) -> Response[UserNotificationPreferences]:
        """Returns the current user's preferences for notifications.

        Anonymous users cannot have notification preferences. They will receive only broadcasted notifications.

        - The settings will contain all possible channels, but the client should only show the ones that are really supported by the server.
          The supported channels are returned in the `supported-channels` header."""
        client = self._get_client()
        response = client.get("/api/notifications/preferences", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = UserNotificationPreferences.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def notifications__preferences__update_notification_preferences(
        self, data: UpdateUserNotificationPreferencesRequest, *, run_as: str | None = None
    ) -> Response[UserNotificationPreferences]:
        """Updates the user's preferences for notifications.

        Anonymous users cannot have notification preferences. They will receive only broadcasted notifications.

        - Can be used to completely enable/disable notifications for a particular type (category)
        or to enable/disable a particular channel on each category."""
        client = self._get_client()
        response = client.put(
            "/api/notifications/preferences", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = UserNotificationPreferences.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def notifications__status__get_notifications_status(
        self, *, since: str, run_as: str | None = None
    ) -> Response[NotificationStatusSummary]:
        """Returns the current status summary of the user's notifications since a particular date.

        Anonymous users cannot receive personal notifications, only broadcasted notifications."""
        client = self._get_client()
        response = client.get(
            "/api/notifications/status", params=self._filter_none_values({"since": since}), headers={"run-as": run_as}
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = NotificationStatusSummary.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def notifications__delete_user_notification(
        self, notification_id: str, *, run_as: str | None = None
    ) -> Response[Any]:
        """Deletes a notification received by the user.

        When a notification is deleted, it is not immediately removed from the database, but marked as deleted.

        - It will not be returned in the list of notifications, but admins can still access it as long as it is not expired.
        - It will be eventually removed from the database by a background task after the expiration time.
        - Deleted notifications will be permanently deleted when the expiration time is reached."""
        client = self._get_client()
        response = client.delete(f"/api/notifications/{notification_id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def notifications__show_notification(
        self, notification_id: str, *, run_as: str | None = None
    ) -> Response[UserNotificationResponse]:
        """Displays information about a notification received by the user."""
        client = self._get_client()
        response = client.get(f"/api/notifications/{notification_id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = UserNotificationResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def notifications__update_user_notification(
        self, notification_id: str, data: UserNotificationUpdateRequest, *, run_as: str | None = None
    ) -> Response[Any]:
        """Updates the state of a notification received by the user."""
        client = self._get_client()
        response = client.put(
            f"/api/notifications/{notification_id}",
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def object_stores__instances_index(
        self, *, run_as: str | None = None
    ) -> Response[list[UserConcreteObjectStoreModel]]:
        """Get a list of persisted object store instances defined by the requesting user."""
        client = self._get_client()
        response = client.get("/api/object_store_instances", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [UserConcreteObjectStoreModel.model_validate(item) for item in response.json()]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def object_stores__create_instance(
        self, data: CreateInstancePayload, *, run_as: str | None = None
    ) -> Response[UserConcreteObjectStoreModel]:
        """Create a user-bound object store."""
        client = self._get_client()
        response = client.post(
            "/api/object_store_instances", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = UserConcreteObjectStoreModel.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def object_stores__test_new_instance_configuration(
        self, data: CreateInstancePayload, *, run_as: str | None = None
    ) -> Response[PluginStatus]:
        """Test payload for creating user-bound object store."""
        client = self._get_client()
        response = client.post(
            "/api/object_store_instances/test", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = PluginStatus.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def object_stores__instances_purge(self, uuid: str, *, run_as: str | None = None) -> Response[Any]:
        """Purge user object store instance."""
        client = self._get_client()
        response = client.delete(f"/api/object_store_instances/{uuid}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def object_stores__instances_get(
        self, uuid: str, *, run_as: str | None = None
    ) -> Response[UserConcreteObjectStoreModel]:
        """Get a persisted user object store instance."""
        client = self._get_client()
        response = client.get(f"/api/object_store_instances/{uuid}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = UserConcreteObjectStoreModel.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def object_stores__instances_update(
        self,
        uuid: str,
        data: UpdateInstanceSecretPayload | UpgradeInstancePayload | UpdateInstancePayload,
        *,
        run_as: str | None = None,
    ) -> Response[UserConcreteObjectStoreModel]:
        """Update or upgrade user object store instance."""
        client = self._get_client()
        response = client.put(f"/api/object_store_instances/{uuid}", headers={"run-as": run_as}, json=data)
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = UserConcreteObjectStoreModel.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def object_stores__instances_test_instance(self, uuid: str, *, run_as: str | None = None) -> Response[PluginStatus]:
        """Get a persisted user object store instance."""
        client = self._get_client()
        response = client.get(f"/api/object_store_instances/{uuid}/test", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = PluginStatus.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def object_stores__test_instances_update(
        self, uuid: str, data: TestUpgradeInstancePayload | TestUpdateInstancePayload, *, run_as: str | None = None
    ) -> Response[PluginStatus]:
        """Test updating or upgrading user object source instance."""
        client = self._get_client()
        response = client.post(f"/api/object_store_instances/{uuid}/test", headers={"run-as": run_as}, json=data)
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = PluginStatus.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def object_stores__templates_index(self, *, run_as: str | None = None) -> Response[ObjectStoreTemplateSummaries]:
        """Get a list of object store templates available to build user defined object stores from"""
        client = self._get_client()
        response = client.get("/api/object_store_templates", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ObjectStoreTemplateSummaries.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def object_stores__index(
        self, *, selectable: bool | None = None, run_as: str | None = None
    ) -> Response[list[ConcreteObjectStoreModel | UserConcreteObjectStoreModel]]:
        """Get a list of (currently only concrete) object stores configured with this Galaxy instance."""
        client = self._get_client()
        response = client.get(
            "/api/object_stores",
            params=self._filter_none_values({"selectable": selectable}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [
                ConcreteObjectStoreModel | UserConcreteObjectStoreModel.model_validate(item) for item in response.json()
            ]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def object_stores__show_info(
        self, object_store_id: str, *, run_as: str | None = None
    ) -> Response[ConcreteObjectStoreModel]:
        """Get information about a concrete object store configured with Galaxy."""
        client = self._get_client()
        response = client.get(f"/api/object_stores/{object_store_id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ConcreteObjectStoreModel.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def pages__index(
        self,
        *,
        deleted: bool | None = None,
        limit: int | None = None,
        offset: int | None = None,
        search: str | None = None,
        show_own: bool | None = None,
        show_published: bool | None = None,
        show_shared: bool | None = None,
        sort_by: Literal["create_time", "title", "update_time", "username"] | None = None,
        sort_desc: bool | None = None,
        user_id: str | None = None,
        run_as: str | None = None,
    ) -> Response[PageSummaryList]:
        """Lists all Pages viewable by the user.

        Get a list with summary information of all Pages available to the user."""
        client = self._get_client()
        response = client.get(
            "/api/pages",
            params=self._filter_none_values(
                {
                    "deleted": deleted,
                    "limit": limit,
                    "offset": offset,
                    "search": search,
                    "show_own": show_own,
                    "show_published": show_published,
                    "show_shared": show_shared,
                    "sort_by": sort_by,
                    "sort_desc": sort_desc,
                    "user_id": user_id,
                }
            ),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = PageSummaryList.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def pages__create(self, data: CreatePagePayload, *, run_as: str | None = None) -> Response[PageSummary]:
        """Create a page and return summary information.

        Creates a new Page."""
        client = self._get_client()
        response = client.post("/api/pages", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True))
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = PageSummary.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def pages__delete(self, id: str, *, run_as: str | None = None) -> Response[Any]:
        """Marks the specific Page as deleted.

        Marks the Page with the given ID as deleted."""
        client = self._get_client()
        response = client.delete(f"/api/pages/{id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def pages__show(self, id: str, *, run_as: str | None = None) -> Response[PageDetails]:
        """Return a page summary and the content of the last revision.

        Return summary information about a specific Page and the content of the last revision."""
        client = self._get_client()
        response = client.get(f"/api/pages/{id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = PageDetails.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def pages__update(self, id: str, data: UpdatePagePayload, *, run_as: str | None = None) -> Response[PageSummary]:
        """Update a page and return summary information.

        Updates an existing Page."""
        client = self._get_client()
        response = client.put(f"/api/pages/{id}", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True))
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = PageSummary.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def pages__show_pdf(self, id: str, *, run_as: str | None = None) -> Response[bytes]:
        """Return a PDF document of the last revision of the Page.

        Return a PDF document of the last revision of the Page.

        This feature may not be available in this Galaxy."""
        client = self._get_client()
        response = client.get(f"/api/pages/{id}.pdf", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.content
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def pages__disable_link_access__disable_link_access(
        self, id: str, *, run_as: str | None = None
    ) -> Response[SharingStatus]:
        """Makes this item inaccessible by a URL link.

        Makes this item inaccessible by a URL link and return the current sharing status."""
        client = self._get_client()
        response = client.put(f"/api/pages/{id}/disable_link_access", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = SharingStatus.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def pages__enable_link_access__enable_link_access(
        self, id: str, *, run_as: str | None = None
    ) -> Response[SharingStatus]:
        """Makes this item accessible by a URL link.

        Makes this item accessible by a URL link and return the current sharing status."""
        client = self._get_client()
        response = client.put(f"/api/pages/{id}/enable_link_access", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = SharingStatus.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def pages__prepare_download__prepare_pdf(self, id: str, *, run_as: str | None = None) -> Response[AsyncFile]:
        """Return a PDF document of the last revision of the Page.

        Return a STS download link for this page to be downloaded as a PDF.

        This feature may not be available in this Galaxy."""
        client = self._get_client()
        response = client.post(f"/api/pages/{id}/prepare_download", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = AsyncFile.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def pages__publish__publish(self, id: str, *, run_as: str | None = None) -> Response[SharingStatus]:
        """Makes this item public and accessible by a URL link.

        Makes this item publicly available by a URL link and return the current sharing status."""
        client = self._get_client()
        response = client.put(f"/api/pages/{id}/publish", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = SharingStatus.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def pages__share_with_users__share_with_users(
        self, id: str, data: ShareWithPayload, *, run_as: str | None = None
    ) -> Response[ShareWithStatus]:
        """Share this item with specific users.

        Shares this item with specific users and return the current sharing status."""
        client = self._get_client()
        response = client.put(
            f"/api/pages/{id}/share_with_users", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ShareWithStatus.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def pages__sharing__sharing(self, id: str, *, run_as: str | None = None) -> Response[SharingStatus]:
        """Get the current sharing status of the given Page.

        Return the sharing status of the item."""
        client = self._get_client()
        response = client.get(f"/api/pages/{id}/sharing", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = SharingStatus.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def pages__slug__set_slug(self, id: str, data: SetSlugPayload, *, run_as: str | None = None) -> Response[Any]:
        """Set a new slug for this shared item.

        Sets a new slug to access this item by URL. The new slug must be unique."""
        client = self._get_client()
        response = client.put(
            f"/api/pages/{id}/slug", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def pages__undelete__undelete(self, id: str, *, run_as: str | None = None) -> Response[Any]:
        """Undelete the specific Page.

        Marks the Page with the given ID as undeleted."""
        client = self._get_client()
        response = client.put(f"/api/pages/{id}/undelete", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def pages__unpublish__unpublish(self, id: str, *, run_as: str | None = None) -> Response[SharingStatus]:
        """Removes this item from the published list.

        Removes this item from the published list and return the current sharing status."""
        client = self._get_client()
        response = client.put(f"/api/pages/{id}/unpublish", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = SharingStatus.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def utilities__proxy(self, *, url: str, run_as: str | None = None) -> Response[Any]:
        """Proxy

        Proxy a remote file to the client to avoid CORS issues."""
        client = self._get_client()
        response = client.get("/api/proxy", params=self._filter_none_values({"url": url}), headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def head_api_proxy(self, *, url: str, run_as: str | None = None) -> Response[Any]:
        """Proxy

        Proxy a remote file to the client to avoid CORS issues."""
        client = self._get_client()
        response = client.head("/api/proxy", params=self._filter_none_values({"url": url}), headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def quotas__index(self, *, run_as: str | None = None) -> Response[QuotaSummaryList]:
        """Displays a list with information of quotas that are currently active."""
        client = self._get_client()
        response = client.get("/api/quotas", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = QuotaSummaryList.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def quotas__create(self, data: CreateQuotaParams, *, run_as: str | None = None) -> Response[CreateQuotaResult]:
        """Creates a new quota."""
        client = self._get_client()
        response = client.post("/api/quotas", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True))
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = CreateQuotaResult.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def quotas__deleted__index_deleted(self, *, run_as: str | None = None) -> Response[QuotaSummaryList]:
        """Displays a list with information of quotas that have been deleted."""
        client = self._get_client()
        response = client.get("/api/quotas/deleted", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = QuotaSummaryList.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def quotas__deleted__show_deleted(self, id: str, *, run_as: str | None = None) -> Response[QuotaDetails]:
        """Displays details on a particular quota that has been deleted."""
        client = self._get_client()
        response = client.get(f"/api/quotas/deleted/{id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = QuotaDetails.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def quotas__deleted_undelete__undelete(self, id: str, *, run_as: str | None = None) -> Response[str]:
        """Restores a previously deleted quota."""
        client = self._get_client()
        response = client.post(f"/api/quotas/deleted/{id}/undelete", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def quotas__delete(self, id: str, data: DeleteQuotaPayload, *, run_as: str | None = None) -> Response[str]:
        """Deletes an existing quota."""
        client = self._get_client()
        response = client.delete(
            f"/api/quotas/{id}", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def quotas__show(self, id: str, *, run_as: str | None = None) -> Response[QuotaDetails]:
        """Displays details on a particular active quota."""
        client = self._get_client()
        response = client.get(f"/api/quotas/{id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = QuotaDetails.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def quotas__update(self, id: str, data: UpdateQuotaParams, *, run_as: str | None = None) -> Response[str]:
        """Updates an existing quota."""
        client = self._get_client()
        response = client.put(f"/api/quotas/{id}", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True))
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def quotas__purge__purge(self, id: str, *, run_as: str | None = None) -> Response[str]:
        """Purges a previously deleted quota."""
        client = self._get_client()
        response = client.post(f"/api/quotas/{id}/purge", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def get_api_remote_files(
        self,
        *,
        target: str | None = None,
        format: RemoteFilesFormat | None = None,
        recursive: bool | None = None,
        disable: RemoteFilesDisableMode | None = None,
        writeable: bool | None = None,
        write_intent: bool | None = None,
        limit: int | None = None,
        offset: int | None = None,
        query: str | None = None,
        sort_by: str | None = None,
        run_as: str | None = None,
    ) -> Response[ListUriResponse | ListJstreeResponse]:
        """Displays remote files available to the user.

        Lists all remote files available to the user from different sources.

        The total count of files and directories is returned in the 'total_matches' header."""
        client = self._get_client()
        response = client.get(
            "/api/remote_files",
            params=self._filter_none_values(
                {
                    "target": target,
                    "format": format,
                    "recursive": recursive,
                    "disable": disable,
                    "writeable": writeable,
                    "write_intent": write_intent,
                    "limit": limit,
                    "offset": offset,
                    "query": query,
                    "sort_by": sort_by,
                }
            ),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ListUriResponse | ListJstreeResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def remote_files__create_entry(
        self, data: CreateEntryPayload, *, run_as: str | None = None
    ) -> Response[CreatedEntryResponse]:
        """Creates a new entry (directory/record) on the remote files source.

        Creates a new entry on the remote files source."""
        client = self._get_client()
        response = client.post(
            "/api/remote_files", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = CreatedEntryResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def remote_files__plugins__plugins(
        self,
        *,
        browsable_only: bool | None = None,
        include_kind: list[PluginKind] | None = None,
        exclude_kind: list[PluginKind] | None = None,
        run_as: str | None = None,
    ) -> Response[FilesSourcePluginList]:
        """Display plugin information for each of the gxfiles:// URI targets available."""
        client = self._get_client()
        response = client.get(
            "/api/remote_files/plugins",
            params=self._filter_none_values(
                {"browsable_only": browsable_only, "include_kind": include_kind, "exclude_kind": exclude_kind}
            ),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = FilesSourcePluginList.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def roles__index(self, *, run_as: str | None = None) -> Response[RoleListResponse]:
        """Index"""
        client = self._get_client()
        response = client.get("/api/roles", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = RoleListResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def roles__create(self, data: RoleDefinitionModel, *, run_as: str | None = None) -> Response[RoleModelResponse]:
        """Create"""
        client = self._get_client()
        response = client.post("/api/roles", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True))
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = RoleModelResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def roles__delete(self, id: str, *, run_as: str | None = None) -> Response[RoleModelResponse]:
        """Delete"""
        client = self._get_client()
        response = client.delete(f"/api/roles/{id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = RoleModelResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def roles__show(self, id: str, *, run_as: str | None = None) -> Response[RoleModelResponse]:
        """Show"""
        client = self._get_client()
        response = client.get(f"/api/roles/{id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = RoleModelResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def roles__purge__purge(self, id: str, *, run_as: str | None = None) -> Response[RoleModelResponse]:
        """Purge"""
        client = self._get_client()
        response = client.post(f"/api/roles/{id}/purge", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = RoleModelResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def roles__undelete__undelete(self, id: str, *, run_as: str | None = None) -> Response[RoleModelResponse]:
        """Undelete"""
        client = self._get_client()
        response = client.post(f"/api/roles/{id}/undelete", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = RoleModelResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def dataset_collections__workbook_download(
        self, data: CreateWorkbookRequest, *, filename: str | None = None, run_as: str | None = None
    ) -> Response[Any]:
        """Create an XLSX workbook for a sample sheet definition."""
        client = self._get_client()
        response = client.post(
            "/api/sample_sheet_workbook",
            params=self._filter_none_values({"filename": filename}),
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def dataset_collections__workbook_parse(
        self, data: ParseWorkbook, *, run_as: str | None = None
    ) -> Response[ParsedWorkbook]:
        """Parse an XLSX workbook for a sample sheet definition and supplied file contents."""
        client = self._get_client()
        response = client.post(
            "/api/sample_sheet_workbook/parse", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ParsedWorkbook.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def short_term_storage__serve(self, storage_request_id: str) -> Response[Any]:
        """Serve the staged download specified by request ID."""
        client = self._get_client()
        response = client.get(f"/api/short_term_storage/{storage_request_id}")
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def short_term_storage__ready__is_ready(self, storage_request_id: str) -> Response[bool]:
        """Determine if specified storage request ID is ready for download."""
        client = self._get_client()
        response = client.get(f"/api/short_term_storage/{storage_request_id}/ready")
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def storage_management__datasets__cleanup_datasets(
        self, data: CleanupStorageItemsRequest, *, run_as: str | None = None
    ) -> Response[StorageItemsCleanupResult]:
        """Purges a set of datasets by ID from disk. The datasets must be owned by the user.

        **Warning**: This operation cannot be undone. All objects will be deleted permanently from the disk."""
        client = self._get_client()
        response = client.delete(
            "/api/storage/datasets", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = StorageItemsCleanupResult.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def storage_management__datasets_discarded__discarded_datasets(
        self,
        *,
        offset: int | None = None,
        limit: int | None = None,
        order: StoredItemOrderBy | None = None,
        run_as: str | None = None,
    ) -> Response[list[StoredItem]]:
        """Returns discarded datasets owned by the given user. The results can be paginated."""
        client = self._get_client()
        response = client.get(
            "/api/storage/datasets/discarded",
            params=self._filter_none_values({"offset": offset, "limit": limit, "order": order}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [StoredItem.model_validate(item) for item in response.json()]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def storage_management__datasets_discarded_summary__discarded_datasets_summary(
        self, *, run_as: str | None = None
    ) -> Response[CleanableItemsSummary]:
        """Returns information with the total storage space taken by discarded datasets owned by the given user."""
        client = self._get_client()
        response = client.get("/api/storage/datasets/discarded/summary", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = CleanableItemsSummary.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def storage_management__histories__cleanup_histories(
        self, data: CleanupStorageItemsRequest, *, run_as: str | None = None
    ) -> Response[StorageItemsCleanupResult]:
        """Purges a set of histories by ID. The histories must be owned by the user.

        **Warning**: This operation cannot be undone. All objects will be deleted permanently from the disk."""
        client = self._get_client()
        response = client.delete(
            "/api/storage/histories", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = StorageItemsCleanupResult.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def storage_management__histories_archived__archived_histories(
        self,
        *,
        offset: int | None = None,
        limit: int | None = None,
        order: StoredItemOrderBy | None = None,
        run_as: str | None = None,
    ) -> Response[list[StoredItem]]:
        """Returns archived histories owned by the given user that are not purged. The results can be paginated."""
        client = self._get_client()
        response = client.get(
            "/api/storage/histories/archived",
            params=self._filter_none_values({"offset": offset, "limit": limit, "order": order}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [StoredItem.model_validate(item) for item in response.json()]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def storage_management__histories_archived_summary__archived_histories_summary(
        self, *, run_as: str | None = None
    ) -> Response[CleanableItemsSummary]:
        """Returns information with the total storage space taken by non-purged archived histories associated with the given user."""
        client = self._get_client()
        response = client.get("/api/storage/histories/archived/summary", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = CleanableItemsSummary.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def storage_management__histories_discarded__discarded_histories(
        self,
        *,
        offset: int | None = None,
        limit: int | None = None,
        order: StoredItemOrderBy | None = None,
        run_as: str | None = None,
    ) -> Response[list[StoredItem]]:
        """Returns all discarded histories associated with the given user."""
        client = self._get_client()
        response = client.get(
            "/api/storage/histories/discarded",
            params=self._filter_none_values({"offset": offset, "limit": limit, "order": order}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [StoredItem.model_validate(item) for item in response.json()]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def storage_management__histories_discarded_summary__discarded_histories_summary(
        self, *, run_as: str | None = None
    ) -> Response[CleanableItemsSummary]:
        """Returns information with the total storage space taken by discarded histories associated with the given user."""
        client = self._get_client()
        response = client.get("/api/storage/histories/discarded/summary", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = CleanableItemsSummary.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def tags__update(self, data: ItemTagsPayload, *, run_as: str | None = None) -> Response[Any]:
        """Apply a new set of tags to an item.

        Replaces the tags associated with an item with the new ones specified in the payload.

        - The previous tags will be __deleted__.
        - If no tags are provided in the request body, the currently associated tags will also be __deleted__."""
        client = self._get_client()
        response = client.put("/api/tags", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True))
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def tasks__result__get_result(self, task_id: str) -> Response[TaskResult]:
        """Get result message for task ID

        If the task is still running, pending, or is waiting for retry then the result is an empty string.
        If the task failed, the result is an error message."""
        client = self._get_client()
        response = client.get(f"/api/tasks/{task_id}/result")
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = TaskResult.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def tasks__state__state(self, task_id: str) -> Response[TaskState]:
        """Determine state of task ID"""
        client = self._get_client()
        response = client.get(f"/api/tasks/{task_id}/state")
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = TaskState.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def tool_data_tables__index(self) -> Response[ToolDataEntryList]:
        """Lists all available data tables

        Get the list of all available data tables."""
        client = self._get_client()
        response = client.get("/api/tool_data")
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ToolDataEntryList.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def tool_data_tables__create(
        self, data: ImportToolDataBundle, *, tool_data_file_path: str | None = None, run_as: str | None = None
    ) -> Response[AsyncTaskResultSummary]:
        """Import a data manager bundle"""
        client = self._get_client()
        response = client.post(
            "/api/tool_data",
            params=self._filter_none_values({"tool_data_file_path": tool_data_file_path}),
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = AsyncTaskResultSummary.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def tool_data_tables__delete(
        self, table_name: str, data: ToolDataItem, *, run_as: str | None = None
    ) -> Response[ToolDataDetails]:
        """Removes an item from a data table

        Removes an item from a data table and reloads it to return its updated details."""
        client = self._get_client()
        response = client.delete(
            f"/api/tool_data/{table_name}", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ToolDataDetails.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def tool_data_tables__show(self, table_name: str, *, run_as: str | None = None) -> Response[ToolDataDetails]:
        """Get details of a data table. For non-administrators, base directories in the path column are stripped, leaving only the basename.

        Get details of a given tool data table."""
        client = self._get_client()
        response = client.get(f"/api/tool_data/{table_name}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ToolDataDetails.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def tool_data_tables__fields__show_field(
        self, table_name: str, field_name: str, *, run_as: str | None = None
    ) -> Response[ToolDataField]:
        """Get information about a particular field in a tool data table

        Displays information about a data table field."""
        client = self._get_client()
        response = client.get(f"/api/tool_data/{table_name}/fields/{field_name}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ToolDataField.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def tool_data_tables__fields_files__download_field_file(
        self, table_name: str, field_name: str, file_name: str, *, run_as: str | None = None
    ) -> Response[Any]:
        """Get files associated with a particular field in a tool data table

        Download a file associated with the data table field."""
        client = self._get_client()
        response = client.get(
            f"/api/tool_data/{table_name}/fields/{field_name}/files/{file_name}", headers={"run-as": run_as}
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def tool_data_tables__reload__reload(
        self, table_name: str, *, run_as: str | None = None
    ) -> Response[ToolDataDetails]:
        """Reloads a tool data table

        Reloads a data table and return its details."""
        client = self._get_client()
        response = client.get(f"/api/tool_data/{table_name}/reload", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ToolDataDetails.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def tools__create_landing(
        self, data: CreateToolLandingRequestPayload, *, run_as: str | None = None
    ) -> Response[ToolLandingRequest]:
        """Create Landing"""
        client = self._get_client()
        response = client.post(
            "/api/tool_landings", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ToolLandingRequest.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def tools__get_landing(self, uuid: str, *, run_as: str | None = None) -> Response[ToolLandingRequest]:
        """Get Landing"""
        client = self._get_client()
        response = client.get(f"/api/tool_landings/{uuid}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ToolLandingRequest.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def tools__claim__claim_landing(
        self, uuid: str, data: ClaimLandingPayload | None, *, run_as: str | None = None
    ) -> Response[ToolLandingRequest]:
        """Claim Landing"""
        client = self._get_client()
        response = client.post(f"/api/tool_landings/{uuid}/claim", headers={"run-as": run_as}, json=data)
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ToolLandingRequest.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def tools__get_tool_request(self, id: str, *, run_as: str | None = None) -> Response[ToolRequestDetailedModel]:
        """Get tool request state."""
        client = self._get_client()
        response = client.get(f"/api/tool_requests/{id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ToolRequestDetailedModel.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def tools__state__tool_request_state(self, id: str, *, run_as: str | None = None) -> Response[str]:
        """Get tool request state."""
        client = self._get_client()
        response = client.get(f"/api/tool_requests/{id}/state", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def tool_shed_repositories__index(
        self,
        *,
        name: str | None = None,
        owner: str | None = None,
        changeset: str | None = None,
        deleted: bool | None = None,
        uninstalled: bool | None = None,
    ) -> Response[list[InstalledToolShedRepository]]:
        """Lists installed tool shed repositories."""
        client = self._get_client()
        response = client.get(
            "/api/tool_shed_repositories",
            params=self._filter_none_values(
                {"name": name, "owner": owner, "changeset": changeset, "deleted": deleted, "uninstalled": uninstalled}
            ),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [InstalledToolShedRepository.model_validate(item) for item in response.json()]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def tool_shed_repositories__check_for_updates__check_for_updates(
        self, *, id: str | None = None, run_as: str | None = None
    ) -> Response[CheckForUpdatesResponse]:
        """Check for updates to the specified repository, or all installed repositories."""
        client = self._get_client()
        response = client.get(
            "/api/tool_shed_repositories/check_for_updates",
            params=self._filter_none_values({"id": id}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = CheckForUpdatesResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def tool_shed_repositories__show(self, id: str) -> Response[InstalledToolShedRepository]:
        """Show installed tool shed repository."""
        client = self._get_client()
        response = client.get(f"/api/tool_shed_repositories/{id}")
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = InstalledToolShedRepository.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def tools__fetch__fetch_form(self, data: BodyTools_fetch_fetchForm, *, run_as: str | None = None) -> Response[Any]:
        """Upload files to Galaxy"""
        client = self._get_client()
        response = client.post(
            "/api/tools/fetch",
            headers={"run-as": run_as},
            data=dict(
                [
                    item
                    for item in [
                        ("files", data.files) if data.files is not None else None,
                        ("history_id", data.history_id),
                        ("landing_uuid", data.landing_uuid) if data.landing_uuid is not None else None,
                        ("targets", data.targets),
                    ]
                    if item is not None
                ]
            ),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def tools__fetch_workbook_download(
        self,
        *,
        type: Literal["datasets", "collection", "collections"] | None = None,
        collection_type: Literal["list", "list:paired", "list:list", "list:list:paired", "list:paired_or_unpaired"]
        | None = None,
        filename: str | None = None,
        run_as: str | None = None,
    ) -> Response[Any]:
        """Generate a template workbook to use with the activity builder UI"""
        client = self._get_client()
        response = client.get(
            "/api/tools/fetch/workbook",
            params=self._filter_none_values({"type": type, "collection_type": collection_type, "filename": filename}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def tools__fetch_workbook_parse(
        self, data: ParseFetchWorkbook, *, run_as: str | None = None
    ) -> Response[ParsedFetchWorkbookForDatasets | ParsedFetchWorkbookForCollections]:
        """Generate a template workbook to use with the activity builder UI"""
        client = self._get_client()
        response = client.post(
            "/api/tools/fetch/workbook/parse", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ParsedFetchWorkbookForDatasets | ParsedFetchWorkbookForCollections.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def tools__icon__get_icon(self, tool_id: str, *, run_as: str | None = None) -> Response[bytes]:
        """Get the icon image associated with a tool

        Returns the icon image associated with a tool.

        The icon image is served with caching headers to allow for efficient
        client-side caching. The icon image is expected to be in PNG format."""
        client = self._get_client()
        response = client.get(f"/api/tools/{tool_id}/icon", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.content
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def tools__inputs__tool_inputs(
        self, tool_id: str, *, tool_version: str | None = None, run_as: str | None = None
    ) -> Response[
        list[
            CwlIntegerParameterModel
            | CwlFloatParameterModel
            | CwlStringParameterModel
            | CwlBooleanParameterModel
            | CwlNullParameterModel
            | CwlFileParameterModel
            | CwlDirectoryParameterModel
            | CwlUnionParameterModelOutput
            | TextParameterModel
            | IntegerParameterModel
            | FloatParameterModel
            | BooleanParameterModel
            | HiddenParameterModel
            | SelectParameterModel
            | DataParameterModel
            | DataCollectionParameterModel
            | DataColumnParameterModel
            | DirectoryUriParameterModel
            | RulesParameterModel
            | DrillDownParameterModelOutput
            | GroupTagParameterModel
            | BaseUrlParameterModel
            | GenomeBuildParameterModel
            | ColorParameterModel
            | ConditionalParameterModelOutput
            | RepeatParameterModelOutput
            | SectionParameterModelOutput
        ]
    ]:
        """Get tool inputs."""
        client = self._get_client()
        response = client.get(
            f"/api/tools/{tool_id}/inputs",
            params=self._filter_none_values({"tool_version": tool_version}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [
                CwlIntegerParameterModel
                | CwlFloatParameterModel
                | CwlStringParameterModel
                | CwlBooleanParameterModel
                | CwlNullParameterModel
                | CwlFileParameterModel
                | CwlDirectoryParameterModel
                | CwlUnionParameterModelOutput
                | TextParameterModel
                | IntegerParameterModel
                | FloatParameterModel
                | BooleanParameterModel
                | HiddenParameterModel
                | SelectParameterModel
                | DataParameterModel
                | DataCollectionParameterModel
                | DataColumnParameterModel
                | DirectoryUriParameterModel
                | RulesParameterModel
                | DrillDownParameterModelOutput
                | GroupTagParameterModel
                | BaseUrlParameterModel
                | GenomeBuildParameterModel
                | ColorParameterModel
                | ConditionalParameterModelOutput
                | RepeatParameterModelOutput
                | SectionParameterModelOutput.model_validate(item)
                for item in response.json()
            ]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def tools__parameter_landing_request_schema(
        self, tool_id: str, *, tool_version: str | None = None, run_as: str | None = None
    ) -> Response[Any]:
        """Return a JSON schema description of the tool's inputs for the tool landing request API."""
        client = self._get_client()
        response = client.get(
            f"/api/tools/{tool_id}/parameter_landing_request_schema",
            params=self._filter_none_values({"tool_version": tool_version}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def tools__parameter_request_schema(
        self, tool_id: str, *, tool_version: str | None = None, run_as: str | None = None
    ) -> Response[Any]:
        """Return a JSON schema description of the tool's inputs for the tool request API that will be added to Galaxy at some point

        The tool request schema includes validation of map/reduce concepts that can be consumed by the tool execution API and not just the request for a single execution."""
        client = self._get_client()
        response = client.get(
            f"/api/tools/{tool_id}/parameter_request_schema",
            params=self._filter_none_values({"tool_version": tool_version}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def tools__parameter_test_case_xml_schema(
        self, tool_id: str, *, tool_version: str | None = None, run_as: str | None = None
    ) -> Response[Any]:
        """Return a JSON schema description of the tool's inputs for test case construction."""
        client = self._get_client()
        response = client.get(
            f"/api/tools/{tool_id}/parameter_test_case_xml_schema",
            params=self._filter_none_values({"tool_version": tool_version}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def tours__index(self) -> Response[TourList]:
        """Index

        Return list of available tours."""
        client = self._get_client()
        response = client.get("/api/tours")
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = TourList.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def tours__generate__generate_tour(
        self, *, tool_id: str, tool_version: str, performs_upload: bool | None = None, run_as: str | None = None
    ) -> Response[GenerateTourResponse]:
        """Generate Tour

        Generate a tour designed for the given tool."""
        client = self._get_client()
        response = client.get(
            "/api/tours/generate",
            params=self._filter_none_values(
                {"tool_id": tool_id, "tool_version": tool_version, "performs_upload": performs_upload}
            ),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = GenerateTourResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def tours__show(self, tour_id: str) -> Response[TourDetails]:
        """Show

        Return a tour definition."""
        client = self._get_client()
        response = client.get(f"/api/tours/{tour_id}")
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = TourDetails.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def tours__update_tour(self, tour_id: str, *, run_as: str | None = None) -> Response[TourDetails]:
        """Update Tour

        Return a tour definition."""
        client = self._get_client()
        response = client.post(f"/api/tours/{tour_id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = TourDetails.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def get_api_unprivileged_tools(
        self, *, active: bool | None = None, run_as: str | None = None
    ) -> Response[list[UnprivilegedToolResponse]]:
        """Index"""
        client = self._get_client()
        response = client.get(
            "/api/unprivileged_tools", params=self._filter_none_values({"active": active}), headers={"run-as": run_as}
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [UnprivilegedToolResponse.model_validate(item) for item in response.json()]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def post_api_unprivileged_tools(
        self, data: DynamicUnprivilegedToolCreatePayload, *, run_as: str | None = None
    ) -> Response[UnprivilegedToolResponse]:
        """Create"""
        client = self._get_client()
        response = client.post(
            "/api/unprivileged_tools", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = UnprivilegedToolResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def dynamic_tools__build__build(
        self, data: DynamicUnprivilegedToolCreatePayload, *, history_id: str, run_as: str | None = None
    ) -> Response[Any]:
        """Build"""
        client = self._get_client()
        response = client.post(
            "/api/unprivileged_tools/build",
            params=self._filter_none_values({"history_id": history_id}),
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def dynamic_tools__runtime_model__runtime_model(
        self, data: DynamicUnprivilegedToolCreatePayload, *, run_as: str | None = None
    ) -> Response[Any]:
        """Runtime Model"""
        client = self._get_client()
        response = client.post(
            "/api/unprivileged_tools/runtime_model",
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def delete_api_unprivileged_tools_uuid(self, uuid: str, *, run_as: str | None = None) -> Response[Any]:
        """Delete

        DELETE /api/unprivileged_tools/{encoded_dynamic_tool_id|tool_uuid}

        Deactivate the specified dynamic tool. Deactivated tools will not
        be loaded into the toolbox."""
        client = self._get_client()
        response = client.delete(f"/api/unprivileged_tools/{uuid}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def get_api_unprivileged_tools_uuid(
        self, uuid: str, *, run_as: str | None = None
    ) -> Response[UnprivilegedToolResponse]:
        """Show"""
        client = self._get_client()
        response = client.get(f"/api/unprivileged_tools/{uuid}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = UnprivilegedToolResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def users__index(
        self,
        *,
        deleted: bool | None = None,
        f_email: str | None = None,
        f_name: str | None = None,
        f_any: str | None = None,
        run_as: str | None = None,
    ) -> Response[list[UserModel | LimitedUserModel]]:
        """Get Users

        Return a collection of users. Filters will only work if enabled in config or user is admin."""
        client = self._get_client()
        response = client.get(
            "/api/users",
            params=self._filter_none_values({"deleted": deleted, "f_email": f_email, "f_name": f_name, "f_any": f_any}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [UserModel | LimitedUserModel.model_validate(item) for item in response.json()]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def users__create(
        self, data: UserCreationPayload | RemoteUserCreationPayload, *, run_as: str | None = None
    ) -> Response[CreatedUserModel]:
        """Create a new Galaxy user. Only admins can create users for now."""
        client = self._get_client()
        response = client.post("/api/users", headers={"run-as": run_as}, json=data)
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = CreatedUserModel.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def users__current_recalculate_disk_usage__recalculate_disk_usage(
        self, *, run_as: str | None = None
    ) -> Response[AsyncTaskResultSummary]:
        """Triggers a recalculation of the current user disk usage.

        This route will be removed in a future version.

        Please use `/api/users/current/recalculate_disk_usage` instead."""
        client = self._get_client()
        response = client.put("/api/users/current/recalculate_disk_usage", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = AsyncTaskResultSummary.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def users__deleted__index_deleted(
        self,
        *,
        f_email: str | None = None,
        f_name: str | None = None,
        f_any: str | None = None,
        run_as: str | None = None,
    ) -> Response[list[UserModel | LimitedUserModel]]:
        """Get Deleted Users

        Return a collection of deleted users. Only admins can see deleted users."""
        client = self._get_client()
        response = client.get(
            "/api/users/deleted",
            params=self._filter_none_values({"f_email": f_email, "f_name": f_name, "f_any": f_any}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [UserModel | LimitedUserModel.model_validate(item) for item in response.json()]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def users__deleted__show_deleted(
        self, user_id: str, *, run_as: str | None = None
    ) -> Response[DetailedUserModel | AnonUserModel]:
        """Return information about a deleted user. Only admins can see deleted users."""
        client = self._get_client()
        response = client.get(f"/api/users/deleted/{user_id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = DetailedUserModel | AnonUserModel.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def users__deleted_undelete__undelete(
        self, user_id: str, *, run_as: str | None = None
    ) -> Response[DetailedUserModel]:
        """Restore a deleted user. Only admins can restore users."""
        client = self._get_client()
        response = client.post(f"/api/users/deleted/{user_id}/undelete", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = DetailedUserModel.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def users__recalculate_disk_usage__recalculate_disk_usage(
        self, *, run_as: str | None = None
    ) -> Response[AsyncTaskResultSummary]:
        """Triggers a recalculation of the current user disk usage.

        This route will be removed in a future version.

        Please use `/api/users/current/recalculate_disk_usage` instead."""
        client = self._get_client()
        response = client.put("/api/users/recalculate_disk_usage", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = AsyncTaskResultSummary.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def users__delete(
        self, user_id: str, data: UserDeletionPayload | None, *, purge: bool | None = None, run_as: str | None = None
    ) -> Response[DetailedUserModel]:
        """Delete a user. Only admins can delete others or purge users."""
        client = self._get_client()
        response = client.delete(
            f"/api/users/{user_id}",
            params=self._filter_none_values({"purge": purge}),
            headers={"run-as": run_as},
            json=data,
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = DetailedUserModel.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def users__show(
        self, user_id: str, *, deleted: bool | None = None, run_as: str | None = None
    ) -> Response[DetailedUserModel | AnonUserModel]:
        """Return information about a specified or the current user. Only admin can see deleted or other users"""
        client = self._get_client()
        response = client.get(
            f"/api/users/{user_id}", params=self._filter_none_values({"deleted": deleted}), headers={"run-as": run_as}
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = DetailedUserModel | AnonUserModel.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def users__update(
        self, user_id: str, data: UserUpdatePayload, *, deleted: bool | None = None, run_as: str | None = None
    ) -> Response[DetailedUserModel]:
        """Update the values of a user. Only admin can update others."""
        client = self._get_client()
        response = client.put(
            f"/api/users/{user_id}",
            params=self._filter_none_values({"deleted": deleted}),
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = DetailedUserModel.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def users__api_key__delete_api_key(self, user_id: str, *, run_as: str | None = None) -> Response[Any]:
        """Delete the current API key of the user"""
        client = self._get_client()
        response = client.delete(f"/api/users/{user_id}/api_key", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def users__api_key__get_or_create_api_key(self, user_id: str, *, run_as: str | None = None) -> Response[str]:
        """Return the user's API key"""
        client = self._get_client()
        response = client.get(f"/api/users/{user_id}/api_key", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def users__api_key__create_api_key(self, user_id: str, *, run_as: str | None = None) -> Response[str]:
        """Create a new API key for the user"""
        client = self._get_client()
        response = client.post(f"/api/users/{user_id}/api_key", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def users__api_key_detailed__get_api_key(self, user_id: str, *, run_as: str | None = None) -> Response[APIKeyModel]:
        """Return the user's API key with extra information."""
        client = self._get_client()
        response = client.get(f"/api/users/{user_id}/api_key/detailed", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = APIKeyModel.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def users__beacon__get_beacon(self, user_id: str, *, run_as: str | None = None) -> Response[UserBeaconSetting]:
        """Return information about beacon share settings

        **Warning**: This API is unstable and may change without notice."""
        client = self._get_client()
        response = client.get(f"/api/users/{user_id}/beacon", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = UserBeaconSetting.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def users__beacon__set_beacon(
        self, user_id: str, data: UserBeaconSetting, *, run_as: str | None = None
    ) -> Response[UserBeaconSetting]:
        """Change beacon setting

        **Warning**: This API is unstable and may change without notice."""
        client = self._get_client()
        response = client.post(
            f"/api/users/{user_id}/beacon", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = UserBeaconSetting.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def users__credentials__list_user_credentials(
        self,
        user_id: str,
        *,
        source_type: str | None = None,
        source_id: str | None = None,
        source_version: str | None = None,
        include_definition: bool | None = None,
        run_as: str | None = None,
    ) -> Response[UserServiceCredentialsListResponse | ExtendedUserCredentialsListResponse]:
        """Lists all credentials the user has provided"""
        client = self._get_client()
        response = client.get(
            f"/api/users/{user_id}/credentials",
            params=self._filter_none_values(
                {
                    "source_type": source_type,
                    "source_id": source_id,
                    "source_version": source_version,
                    "include_definition": include_definition,
                }
            ),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = UserServiceCredentialsListResponse | ExtendedUserCredentialsListResponse.model_validate(
                response.json()
            )
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def users__credentials__provide_credential(
        self, user_id: str, data: CreateSourceCredentialsPayload, *, run_as: str | None = None
    ) -> Response[ServiceCredentialGroupResponse]:
        """Allows users to provide credentials for a secret/variable"""
        client = self._get_client()
        response = client.post(
            f"/api/users/{user_id}/credentials", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ServiceCredentialGroupResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def users__credentials__update_user_credentials_group(
        self, user_id: str, data: SelectServiceCredentialPayload, *, run_as: str | None = None
    ) -> Response[Any]:
        """Updates the current credentials group"""
        client = self._get_client()
        response = client.put(
            f"/api/users/{user_id}/credentials", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def users__credentials__delete_service_credentials(
        self, user_id: str, user_credentials_id: str, *, run_as: str | None = None
    ) -> Response[Any]:
        """Deletes all credentials for a specific service"""
        client = self._get_client()
        response = client.delete(f"/api/users/{user_id}/credentials/{user_credentials_id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def users__credentials_groups__delete_credentials(
        self, user_id: str, user_credentials_id: str, group_id: str, *, run_as: str | None = None
    ) -> Response[Any]:
        """Deletes a specific credential group"""
        client = self._get_client()
        response = client.delete(
            f"/api/users/{user_id}/credentials/{user_credentials_id}/groups/{group_id}", headers={"run-as": run_as}
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def users__credentials_groups__update_user_credentials(
        self,
        user_id: str,
        user_credentials_id: str,
        group_id: str,
        data: ServiceCredentialGroupPayload,
        *,
        run_as: str | None = None,
    ) -> Response[ServiceCredentialGroupResponse]:
        """Updates user credentials"""
        client = self._get_client()
        response = client.put(
            f"/api/users/{user_id}/credentials/{user_credentials_id}/groups/{group_id}",
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ServiceCredentialGroupResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def users__custom_builds__get_custom_builds(
        self, user_id: str, *, run_as: str | None = None
    ) -> Response[CustomBuildsCollection]:
        """Returns collection of custom builds."""
        client = self._get_client()
        response = client.get(f"/api/users/{user_id}/custom_builds", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = CustomBuildsCollection.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def users__custom_builds__delete_custom_builds(
        self, user_id: str, key: str, *, run_as: str | None = None
    ) -> Response[DeletedCustomBuild]:
        """Delete a custom build"""
        client = self._get_client()
        response = client.delete(f"/api/users/{user_id}/custom_builds/{key}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = DeletedCustomBuild.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def users__custom_builds__add_custom_builds(
        self, user_id: str, key: str, data: CustomBuildCreationPayload, *, run_as: str | None = None
    ) -> Response[Any]:
        """Add new custom build."""
        client = self._get_client()
        response = client.put(
            f"/api/users/{user_id}/custom_builds/{key}",
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def users__favorites__set_favorite(
        self, user_id: str, object_type: FavoriteObjectType, data: FavoriteObject, *, run_as: str | None = None
    ) -> Response[FavoriteObjectsSummary]:
        """Add the object to user's favorites"""
        client = self._get_client()
        response = client.put(
            f"/api/users/{user_id}/favorites/{object_type}",
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = FavoriteObjectsSummary.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def users__favorites__remove_favorite(
        self, user_id: str, object_type: FavoriteObjectType, object_id: str, *, run_as: str | None = None
    ) -> Response[FavoriteObjectsSummary]:
        """Remove the object from user's favorites"""
        client = self._get_client()
        response = client.delete(
            f"/api/users/{user_id}/favorites/{object_type}/{object_id}", headers={"run-as": run_as}
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = FavoriteObjectsSummary.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def users__objectstore_usage__objectstore_usage(
        self, user_id: str, *, run_as: str | None = None
    ) -> Response[list[UserObjectstoreUsage]]:
        """Return the user's object store usage summary broken down by object store ID"""
        client = self._get_client()
        response = client.get(f"/api/users/{user_id}/objectstore_usage", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [UserObjectstoreUsage.model_validate(item) for item in response.json()]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def users__recalculate_disk_usage__recalculate_disk_usage_by_user_id(
        self, user_id: str, *, run_as: str | None = None
    ) -> Response[AsyncTaskResultSummary]:
        """Triggers a recalculation of the current user disk usage."""
        client = self._get_client()
        response = client.put(f"/api/users/{user_id}/recalculate_disk_usage", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = AsyncTaskResultSummary.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def users__roles__get_user_roles(self, user_id: str, *, run_as: str | None = None) -> Response[RoleListResponse]:
        """Get User Roles

        Return a list of roles associated with this user. Only admins can see user roles."""
        client = self._get_client()
        response = client.get(f"/api/users/{user_id}/roles", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = RoleListResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def users__send_activation_email__send_activation_email(
        self, user_id: str, *, run_as: str | None = None
    ) -> Response[Any]:
        """Sends activation email to user."""
        client = self._get_client()
        response = client.post(f"/api/users/{user_id}/send_activation_email", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def users__theme__set_theme(self, user_id: str, theme: str, *, run_as: str | None = None) -> Response[str]:
        """Set the user's theme choice"""
        client = self._get_client()
        response = client.put(f"/api/users/{user_id}/theme/{theme}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def users__usage__usage(self, user_id: str, *, run_as: str | None = None) -> Response[list[UserQuotaUsage]]:
        """Return the user's quota usage summary broken down by quota source"""
        client = self._get_client()
        response = client.get(f"/api/users/{user_id}/usage", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [UserQuotaUsage.model_validate(item) for item in response.json()]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def users__usage__usage_for(
        self, user_id: str, label: str, *, run_as: str | None = None
    ) -> Response[UserQuotaUsage | None]:
        """Return the user's quota usage summary for a given quota source label"""
        client = self._get_client()
        response = client.get(f"/api/users/{user_id}/usage/{label}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = UserQuotaUsage | None.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def configuration__version(self) -> Response[dict[str, Any]]:
        """Return Galaxy version information: major/minor version, optional extra info

        Return Galaxy version information: major/minor version, optional extra info."""
        client = self._get_client()
        response = client.get("/api/version")
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def visualizations__index(
        self,
        *,
        deleted: bool | None = None,
        limit: int | None = None,
        offset: int | None = None,
        user_id: str | None = None,
        show_own: bool | None = None,
        show_published: bool | None = None,
        show_shared: bool | None = None,
        sort_by: Literal["create_time", "title", "update_time", "username"] | None = None,
        sort_desc: bool | None = None,
        search: str | None = None,
        run_as: str | None = None,
    ) -> Response[VisualizationSummaryList]:
        """Returns visualizations for the current user."""
        client = self._get_client()
        response = client.get(
            "/api/visualizations",
            params=self._filter_none_values(
                {
                    "deleted": deleted,
                    "limit": limit,
                    "offset": offset,
                    "user_id": user_id,
                    "show_own": show_own,
                    "show_published": show_published,
                    "show_shared": show_shared,
                    "sort_by": sort_by,
                    "sort_desc": sort_desc,
                    "search": search,
                }
            ),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = VisualizationSummaryList.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def visualizations__create(
        self, data: VisualizationCreatePayload, *, import_id: str | None = None, run_as: str | None = None
    ) -> Response[VisualizationCreateResponse]:
        """Create a new visualization.

        Creates a new visualization using the given payload and does not require the import_id field.
        If import_id given, it imports a copy of an existing visualization into the user's workspace and does not require the rest of the payload."""
        client = self._get_client()
        response = client.post(
            "/api/visualizations",
            params=self._filter_none_values({"import_id": import_id}),
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = VisualizationCreateResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def visualizations__show(self, id: str, *, run_as: str | None = None) -> Response[VisualizationShowResponse]:
        """Get a visualization by ID.

        Return the visualization."""
        client = self._get_client()
        response = client.get(f"/api/visualizations/{id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = VisualizationShowResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def visualizations__update(
        self, id: str, data: VisualizationUpdatePayload, *, run_as: str | None = None
    ) -> Response[VisualizationUpdateResponse | None]:
        """Update a visualization."""
        client = self._get_client()
        response = client.put(
            f"/api/visualizations/{id}", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = VisualizationUpdateResponse | None.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def visualizations__disable_link_access__disable_link_access(
        self, id: str, *, run_as: str | None = None
    ) -> Response[SharingStatus]:
        """Makes this item inaccessible by a URL link.

        Makes this item inaccessible by a URL link and return the current sharing status."""
        client = self._get_client()
        response = client.put(f"/api/visualizations/{id}/disable_link_access", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = SharingStatus.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def visualizations__enable_link_access__enable_link_access(
        self, id: str, *, run_as: str | None = None
    ) -> Response[SharingStatus]:
        """Makes this item accessible by a URL link.

        Makes this item accessible by a URL link and return the current sharing status."""
        client = self._get_client()
        response = client.put(f"/api/visualizations/{id}/enable_link_access", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = SharingStatus.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def visualizations__publish__publish(self, id: str, *, run_as: str | None = None) -> Response[SharingStatus]:
        """Makes this item public and accessible by a URL link.

        Makes this item publicly available by a URL link and return the current sharing status."""
        client = self._get_client()
        response = client.put(f"/api/visualizations/{id}/publish", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = SharingStatus.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def visualizations__share_with_users__share_with_users(
        self, id: str, data: ShareWithPayload, *, run_as: str | None = None
    ) -> Response[ShareWithStatus]:
        """Share this item with specific users.

        Shares this item with specific users and return the current sharing status."""
        client = self._get_client()
        response = client.put(
            f"/api/visualizations/{id}/share_with_users",
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ShareWithStatus.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def visualizations__sharing__sharing(self, id: str, *, run_as: str | None = None) -> Response[SharingStatus]:
        """Get the current sharing status of the given Visualization.

        Return the sharing status of the item."""
        client = self._get_client()
        response = client.get(f"/api/visualizations/{id}/sharing", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = SharingStatus.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def visualizations__slug__set_slug(
        self, id: str, data: SetSlugPayload, *, run_as: str | None = None
    ) -> Response[Any]:
        """Set a new slug for this shared item.

        Sets a new slug to access this item by URL. The new slug must be unique."""
        client = self._get_client()
        response = client.put(
            f"/api/visualizations/{id}/slug", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def visualizations__unpublish__unpublish(self, id: str, *, run_as: str | None = None) -> Response[SharingStatus]:
        """Removes this item from the published list.

        Removes this item from the published list and return the current sharing status."""
        client = self._get_client()
        response = client.put(f"/api/visualizations/{id}/unpublish", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = SharingStatus.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def configuration__whoami(self, *, run_as: str | None = None) -> Response[UserModel | None]:
        """Return information about the current authenticated user

        Return information about the current authenticated user."""
        client = self._get_client()
        response = client.get("/api/whoami", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = UserModel | None.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__create_landing(
        self, data: CreateWorkflowLandingRequestPayload, *, run_as: str | None = None
    ) -> Response[WorkflowLandingRequest]:
        """Create Landing"""
        client = self._get_client()
        response = client.post(
            "/api/workflow_landings", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = WorkflowLandingRequest.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__get_landing(self, uuid: str, *, run_as: str | None = None) -> Response[WorkflowLandingRequest]:
        """Get Landing"""
        client = self._get_client()
        response = client.get(f"/api/workflow_landings/{uuid}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = WorkflowLandingRequest.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__claim__claim_landing(
        self, uuid: str, data: ClaimLandingPayload | None, *, run_as: str | None = None
    ) -> Response[WorkflowLandingRequest]:
        """Claim Landing"""
        client = self._get_client()
        response = client.post(f"/api/workflow_landings/{uuid}/claim", headers={"run-as": run_as}, json=data)
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = WorkflowLandingRequest.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__index(
        self,
        *,
        show_deleted: bool | None = None,
        show_hidden: bool | None = None,
        missing_tools: bool | None = None,
        show_published: bool | None = None,
        show_shared: bool | None = None,
        sort_by: Literal["create_time", "update_time", "name"] | None = None,
        sort_desc: bool | None = None,
        limit: int | None = None,
        offset: int | None = None,
        search: str | None = None,
        skip_step_counts: bool | None = None,
        run_as: str | None = None,
    ) -> Response[list[dict[str, Any]]]:
        """Lists stored workflows viewable by the user."""
        client = self._get_client()
        response = client.get(
            "/api/workflows",
            params=self._filter_none_values(
                {
                    "show_deleted": show_deleted,
                    "show_hidden": show_hidden,
                    "missing_tools": missing_tools,
                    "show_published": show_published,
                    "show_shared": show_shared,
                    "sort_by": sort_by,
                    "sort_desc": sort_desc,
                    "limit": limit,
                    "offset": offset,
                    "search": search,
                    "skip_step_counts": skip_step_counts,
                }
            ),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [dict[str, Any].model_validate(item) for item in response.json()]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__menu__get_workflow_menu(
        self,
        *,
        show_deleted: bool | None = None,
        show_hidden: bool | None = None,
        missing_tools: bool | None = None,
        show_published: bool | None = None,
        show_shared: bool | None = None,
        run_as: str | None = None,
    ) -> Response[Any]:
        """Get workflows present in the tools panel."""
        client = self._get_client()
        response = client.get(
            "/api/workflows/menu",
            params=self._filter_none_values(
                {
                    "show_deleted": show_deleted,
                    "show_hidden": show_hidden,
                    "missing_tools": missing_tools,
                    "show_published": show_published,
                    "show_shared": show_shared,
                }
            ),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__delete_workflow(self, workflow_id: str, *, run_as: str | None = None) -> Response[Any]:
        """Add the deleted flag to a workflow."""
        client = self._get_client()
        response = client.delete(f"/api/workflows/{workflow_id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__show_workflow(
        self,
        workflow_id: str,
        *,
        instance: bool | None = None,
        legacy: bool | None = None,
        version: int | None = None,
        run_as: str | None = None,
    ) -> Response[StoredWorkflowDetailed]:
        """Displays information needed to run a workflow."""
        client = self._get_client()
        response = client.get(
            f"/api/workflows/{workflow_id}",
            params=self._filter_none_values({"instance": instance, "legacy": legacy, "version": version}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = StoredWorkflowDetailed.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__invocation_counts(
        self, workflow_id: str, *, instance: bool | None = None, run_as: str | None = None
    ) -> Response[RootModelDictStr_int_]:
        """Get state counts for accessible workflow."""
        client = self._get_client()
        response = client.get(
            f"/api/workflows/{workflow_id}/counts",
            params=self._filter_none_values({"instance": instance}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = RootModelDictStr_int_.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__disable_link_access__disable_link_access(
        self, workflow_id: str, *, run_as: str | None = None
    ) -> Response[SharingStatus]:
        """Makes this item inaccessible by a URL link.

        Makes this item inaccessible by a URL link and return the current sharing status."""
        client = self._get_client()
        response = client.put(f"/api/workflows/{workflow_id}/disable_link_access", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = SharingStatus.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__enable_link_access__enable_link_access(
        self, workflow_id: str, *, run_as: str | None = None
    ) -> Response[SharingStatus]:
        """Makes this item accessible by a URL link.

        Makes this item accessible by a URL link and return the current sharing status."""
        client = self._get_client()
        response = client.put(f"/api/workflows/{workflow_id}/enable_link_access", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = SharingStatus.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__invocations__index_workflow_invocations(
        self,
        workflow_id: str,
        *,
        history_id: str | None = None,
        job_id: str | None = None,
        user_id: str | None = None,
        sort_by: InvocationSortByEnum | None = None,
        sort_desc: bool | None = None,
        include_terminal: bool | None = None,
        limit: int | None = None,
        offset: int | None = None,
        instance: bool | None = None,
        view: str | None = None,
        step_details: bool | None = None,
        run_as: str | None = None,
    ) -> Response[list[Any]]:
        """Get the list of a user's workflow invocations."""
        client = self._get_client()
        response = client.get(
            f"/api/workflows/{workflow_id}/invocations",
            params=self._filter_none_values(
                {
                    "history_id": history_id,
                    "job_id": job_id,
                    "user_id": user_id,
                    "sort_by": sort_by,
                    "sort_desc": sort_desc,
                    "include_terminal": include_terminal,
                    "limit": limit,
                    "offset": offset,
                    "instance": instance,
                    "view": view,
                    "step_details": step_details,
                }
            ),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [Any.model_validate(item) for item in response.json()]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__invocations__invoke(
        self, workflow_id: str, data: InvokeWorkflowPayload, *, run_as: str | None = None
    ) -> Response[Any | list[Any]]:
        """Schedule the workflow specified by `workflow_id` to run."""
        client = self._get_client()
        response = client.post(
            f"/api/workflows/{workflow_id}/invocations",
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = Any | list[Any].model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__invocations__cancel_workflow_invocation(
        self,
        invocation_id: str,
        workflow_id: str,
        *,
        step_details: bool | None = None,
        legacy_job_state: bool | None = None,
        run_as: str | None = None,
    ) -> Response[Any]:
        """Cancel the specified workflow invocation.

        An alias for `DELETE /api/invocations/{invocation_id}`. `workflow_id` is ignored."""
        client = self._get_client()
        response = client.delete(
            f"/api/workflows/{workflow_id}/invocations/{invocation_id}",
            params=self._filter_none_values({"step_details": step_details, "legacy_job_state": legacy_job_state}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__invocations__show_workflow_invocation(
        self,
        workflow_id: str,
        invocation_id: str,
        *,
        step_details: bool | None = None,
        legacy_job_state: bool | None = None,
        run_as: str | None = None,
    ) -> Response[Any]:
        """Get detailed description of a workflow invocation.

        An alias for `GET /api/invocations/{invocation_id}`. `workflow_id` is ignored."""
        client = self._get_client()
        response = client.get(
            f"/api/workflows/{workflow_id}/invocations/{invocation_id}",
            params=self._filter_none_values({"step_details": step_details, "legacy_job_state": legacy_job_state}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__invocations_jobs_summary__workflow_invocation_jobs_summary(
        self, workflow_id: str, invocation_id: str, *, run_as: str | None = None
    ) -> Response[InvocationJobsResponse]:
        """Get job state summary info aggregated across all current jobs of the workflow invocation.

        An alias for `GET /api/invocations/{invocation_id}/jobs_summary`. `workflow_id` is ignored."""
        client = self._get_client()
        response = client.get(
            f"/api/workflows/{workflow_id}/invocations/{invocation_id}/jobs_summary", headers={"run-as": run_as}
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = InvocationJobsResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__invocations_report__show_workflow_invocation_report(
        self, invocation_id: str, workflow_id: str, *, run_as: str | None = None
    ) -> Response[InvocationReport]:
        """Get JSON summarizing invocation for reporting.

        An alias for `GET /api/invocations/{invocation_id}/report`. `workflow_id` is ignored."""
        client = self._get_client()
        response = client.get(
            f"/api/workflows/{workflow_id}/invocations/{invocation_id}/report", headers={"run-as": run_as}
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = InvocationReport.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__invocations_report_pdf__show_workflow_invocation_report_pdf(
        self, workflow_id: str, invocation_id: str, *, run_as: str | None = None
    ) -> Response[Any]:
        """Get PDF summarizing invocation for reporting.

        An alias for `GET /api/invocations/{invocation_id}/report.pdf`. `workflow_id` is ignored."""
        client = self._get_client()
        response = client.get(
            f"/api/workflows/{workflow_id}/invocations/{invocation_id}/report.pdf", headers={"run-as": run_as}
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__invocations_step_jobs_summary__workflow_invocation_step_jobs_summary(
        self, workflow_id: str, invocation_id: str, *, run_as: str | None = None
    ) -> Response[
        list[
            InvocationStepJobsResponseStepModel
            | InvocationStepJobsResponseJobModel
            | InvocationStepJobsResponseCollectionJobsModel
        ]
    ]:
        """Get job state summary info aggregated per step of the workflow invocation.

        An alias for `GET /api/invocations/{invocation_id}/step_jobs_summary`. `workflow_id` is ignored."""
        client = self._get_client()
        response = client.get(
            f"/api/workflows/{workflow_id}/invocations/{invocation_id}/step_jobs_summary", headers={"run-as": run_as}
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [
                InvocationStepJobsResponseStepModel
                | InvocationStepJobsResponseJobModel
                | InvocationStepJobsResponseCollectionJobsModel.model_validate(item)
                for item in response.json()
            ]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__invocations_steps__workflow_invocation_step(
        self, workflow_id: str, invocation_id: str, step_id: str, *, run_as: str | None = None
    ) -> Response[InvocationStep]:
        """Show details of workflow invocation step.

        An alias for `GET /api/invocations/{invocation_id}/steps/{step_id}`. `workflow_id` and `invocation_id` are ignored."""
        client = self._get_client()
        response = client.get(
            f"/api/workflows/{workflow_id}/invocations/{invocation_id}/steps/{step_id}", headers={"run-as": run_as}
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = InvocationStep.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__invocations_steps__update_workflow_invocation_step(
        self,
        workflow_id: str,
        invocation_id: str,
        step_id: str,
        data: InvocationUpdatePayload,
        *,
        run_as: str | None = None,
    ) -> Response[InvocationStep]:
        """Update state of running workflow step invocation.

        An alias for `PUT /api/invocations/{invocation_id}/steps/{step_id}`. `workflow_id` is ignored."""
        client = self._get_client()
        response = client.put(
            f"/api/workflows/{workflow_id}/invocations/{invocation_id}/steps/{step_id}",
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = InvocationStep.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__publish__publish(self, workflow_id: str, *, run_as: str | None = None) -> Response[SharingStatus]:
        """Makes this item public and accessible by a URL link.

        Makes this item publicly available by a URL link and return the current sharing status."""
        client = self._get_client()
        response = client.put(f"/api/workflows/{workflow_id}/publish", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = SharingStatus.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__refactor__refactor(
        self, workflow_id: str, data: RefactorRequest, *, instance: bool | None = None, run_as: str | None = None
    ) -> Response[RefactorResponse]:
        """Updates the workflow stored with the given ID."""
        client = self._get_client()
        response = client.put(
            f"/api/workflows/{workflow_id}/refactor",
            params=self._filter_none_values({"instance": instance}),
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = RefactorResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__share_with_users__share_with_users(
        self, workflow_id: str, data: ShareWithPayload, *, run_as: str | None = None
    ) -> Response[ShareWithStatus]:
        """Share this item with specific users.

        Shares this item with specific users and return the current sharing status."""
        client = self._get_client()
        response = client.put(
            f"/api/workflows/{workflow_id}/share_with_users",
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ShareWithStatus.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__sharing__sharing(self, workflow_id: str, *, run_as: str | None = None) -> Response[SharingStatus]:
        """Get the current sharing status of the given item.

        Return the sharing status of the item."""
        client = self._get_client()
        response = client.get(f"/api/workflows/{workflow_id}/sharing", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = SharingStatus.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__slug__set_slug(
        self, workflow_id: str, data: SetSlugPayload, *, run_as: str | None = None
    ) -> Response[Any]:
        """Set a new slug for this shared item.

        Sets a new slug to access this item by URL. The new slug must be unique."""
        client = self._get_client()
        response = client.put(
            f"/api/workflows/{workflow_id}/slug", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__tags__index(self, workflow_id: str, *, run_as: str | None = None) -> Response[ItemTagsListResponse]:
        """Show tags based on workflow_id"""
        client = self._get_client()
        response = client.get(f"/api/workflows/{workflow_id}/tags", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ItemTagsListResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__tags__delete(self, workflow_id: str, tag_name: str, *, run_as: str | None = None) -> Response[bool]:
        """Delete tag based on workflow_id"""
        client = self._get_client()
        response = client.delete(f"/api/workflows/{workflow_id}/tags/{tag_name}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__tags__show(
        self, workflow_id: str, tag_name: str, *, run_as: str | None = None
    ) -> Response[ItemTagsResponse]:
        """Show tag based on workflow_id"""
        client = self._get_client()
        response = client.get(f"/api/workflows/{workflow_id}/tags/{tag_name}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ItemTagsResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__tags__create(
        self, workflow_id: str, tag_name: str, data: ItemTagsCreatePayload, *, run_as: str | None = None
    ) -> Response[ItemTagsResponse]:
        """Create tag based on workflow_id"""
        client = self._get_client()
        response = client.post(
            f"/api/workflows/{workflow_id}/tags/{tag_name}",
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ItemTagsResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__tags__update(
        self, workflow_id: str, tag_name: str, data: ItemTagsCreatePayload, *, run_as: str | None = None
    ) -> Response[ItemTagsResponse]:
        """Update tag based on workflow_id"""
        client = self._get_client()
        response = client.put(
            f"/api/workflows/{workflow_id}/tags/{tag_name}",
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ItemTagsResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__undelete__undelete_workflow(self, workflow_id: str, *, run_as: str | None = None) -> Response[Any]:
        """Remove the deleted flag from a workflow."""
        client = self._get_client()
        response = client.post(f"/api/workflows/{workflow_id}/undelete", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__unpublish__unpublish(
        self, workflow_id: str, *, run_as: str | None = None
    ) -> Response[SharingStatus]:
        """Removes this item from the published list.

        Removes this item from the published list and return the current sharing status."""
        client = self._get_client()
        response = client.put(f"/api/workflows/{workflow_id}/unpublish", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = SharingStatus.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__usage__index_workflow_invocations(
        self,
        workflow_id: str,
        *,
        history_id: str | None = None,
        job_id: str | None = None,
        user_id: str | None = None,
        sort_by: InvocationSortByEnum | None = None,
        sort_desc: bool | None = None,
        include_terminal: bool | None = None,
        limit: int | None = None,
        offset: int | None = None,
        instance: bool | None = None,
        view: str | None = None,
        step_details: bool | None = None,
        run_as: str | None = None,
    ) -> Response[list[Any]]:
        """Get the list of a user's workflow invocations."""
        client = self._get_client()
        response = client.get(
            f"/api/workflows/{workflow_id}/usage",
            params=self._filter_none_values(
                {
                    "history_id": history_id,
                    "job_id": job_id,
                    "user_id": user_id,
                    "sort_by": sort_by,
                    "sort_desc": sort_desc,
                    "include_terminal": include_terminal,
                    "limit": limit,
                    "offset": offset,
                    "instance": instance,
                    "view": view,
                    "step_details": step_details,
                }
            ),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [Any.model_validate(item) for item in response.json()]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__usage__invoke(
        self, workflow_id: str, data: InvokeWorkflowPayload, *, run_as: str | None = None
    ) -> Response[Any | list[Any]]:
        """Schedule the workflow specified by `workflow_id` to run."""
        client = self._get_client()
        response = client.post(
            f"/api/workflows/{workflow_id}/usage", headers={"run-as": run_as}, json=data.model_dump(exclude_unset=True)
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = Any | list[Any].model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__usage__cancel_workflow_invocation(
        self,
        invocation_id: str,
        workflow_id: str,
        *,
        step_details: bool | None = None,
        legacy_job_state: bool | None = None,
        run_as: str | None = None,
    ) -> Response[Any]:
        """Cancel the specified workflow invocation.

        An alias for `DELETE /api/invocations/{invocation_id}`. `workflow_id` is ignored."""
        client = self._get_client()
        response = client.delete(
            f"/api/workflows/{workflow_id}/usage/{invocation_id}",
            params=self._filter_none_values({"step_details": step_details, "legacy_job_state": legacy_job_state}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__usage__show_workflow_invocation(
        self,
        workflow_id: str,
        invocation_id: str,
        *,
        step_details: bool | None = None,
        legacy_job_state: bool | None = None,
        run_as: str | None = None,
    ) -> Response[Any]:
        """Get detailed description of a workflow invocation.

        An alias for `GET /api/invocations/{invocation_id}`. `workflow_id` is ignored."""
        client = self._get_client()
        response = client.get(
            f"/api/workflows/{workflow_id}/usage/{invocation_id}",
            params=self._filter_none_values({"step_details": step_details, "legacy_job_state": legacy_job_state}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__usage_jobs_summary__workflow_invocation_jobs_summary(
        self, workflow_id: str, invocation_id: str, *, run_as: str | None = None
    ) -> Response[InvocationJobsResponse]:
        """Get job state summary info aggregated across all current jobs of the workflow invocation.

        An alias for `GET /api/invocations/{invocation_id}/jobs_summary`. `workflow_id` is ignored."""
        client = self._get_client()
        response = client.get(
            f"/api/workflows/{workflow_id}/usage/{invocation_id}/jobs_summary", headers={"run-as": run_as}
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = InvocationJobsResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__usage_report__show_workflow_invocation_report(
        self, invocation_id: str, workflow_id: str, *, run_as: str | None = None
    ) -> Response[InvocationReport]:
        """Get JSON summarizing invocation for reporting.

        An alias for `GET /api/invocations/{invocation_id}/report`. `workflow_id` is ignored."""
        client = self._get_client()
        response = client.get(f"/api/workflows/{workflow_id}/usage/{invocation_id}/report", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = InvocationReport.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__usage_report_pdf__show_workflow_invocation_report_pdf(
        self, workflow_id: str, invocation_id: str, *, run_as: str | None = None
    ) -> Response[Any]:
        """Get PDF summarizing invocation for reporting.

        An alias for `GET /api/invocations/{invocation_id}/report.pdf`. `workflow_id` is ignored."""
        client = self._get_client()
        response = client.get(
            f"/api/workflows/{workflow_id}/usage/{invocation_id}/report.pdf", headers={"run-as": run_as}
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__usage_step_jobs_summary__workflow_invocation_step_jobs_summary(
        self, workflow_id: str, invocation_id: str, *, run_as: str | None = None
    ) -> Response[
        list[
            InvocationStepJobsResponseStepModel
            | InvocationStepJobsResponseJobModel
            | InvocationStepJobsResponseCollectionJobsModel
        ]
    ]:
        """Get job state summary info aggregated per step of the workflow invocation.

        An alias for `GET /api/invocations/{invocation_id}/step_jobs_summary`. `workflow_id` is ignored."""
        client = self._get_client()
        response = client.get(
            f"/api/workflows/{workflow_id}/usage/{invocation_id}/step_jobs_summary", headers={"run-as": run_as}
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = [
                InvocationStepJobsResponseStepModel
                | InvocationStepJobsResponseJobModel
                | InvocationStepJobsResponseCollectionJobsModel.model_validate(item)
                for item in response.json()
            ]
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__usage_steps__workflow_invocation_step(
        self, workflow_id: str, invocation_id: str, step_id: str, *, run_as: str | None = None
    ) -> Response[InvocationStep]:
        """Show details of workflow invocation step.

        An alias for `GET /api/invocations/{invocation_id}/steps/{step_id}`. `workflow_id` and `invocation_id` are ignored."""
        client = self._get_client()
        response = client.get(
            f"/api/workflows/{workflow_id}/usage/{invocation_id}/steps/{step_id}", headers={"run-as": run_as}
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = InvocationStep.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__usage_steps__update_workflow_invocation_step(
        self,
        workflow_id: str,
        invocation_id: str,
        step_id: str,
        data: InvocationUpdatePayload,
        *,
        run_as: str | None = None,
    ) -> Response[InvocationStep]:
        """Update state of running workflow step invocation.

        An alias for `PUT /api/invocations/{invocation_id}/steps/{step_id}`. `workflow_id` is ignored."""
        client = self._get_client()
        response = client.put(
            f"/api/workflows/{workflow_id}/usage/{invocation_id}/steps/{step_id}",
            headers={"run-as": run_as},
            json=data.model_dump(exclude_unset=True),
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = InvocationStep.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def workflows__versions__show_versions(
        self, workflow_id: str, *, instance: bool | None = None, run_as: str | None = None
    ) -> Response[Any]:
        """List all versions of a workflow."""
        client = self._get_client()
        response = client.get(
            f"/api/workflows/{workflow_id}/versions",
            params=self._filter_none_values({"instance": instance}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def context__index(self, *, run_as: str | None = None) -> Response[ContextResponse]:
        """Return bootstrapped client context"""
        client = self._get_client()
        response = client.get("/context", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = ContextResponse.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def drs__v1_objects__get_object(self, object_id: str, *, run_as: str | None = None) -> Response[DrsObject]:
        """Get Object"""
        client = self._get_client()
        response = client.get(f"/ga4gh/drs/v1/objects/{object_id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = DrsObject.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def post_ga4gh_drs_v1_objects_object_id(self, object_id: str, *, run_as: str | None = None) -> Response[DrsObject]:
        """Get Object"""
        client = self._get_client()
        response = client.post(f"/ga4gh/drs/v1/objects/{object_id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = DrsObject.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def drs__v1_objects_access__get_access_url(
        self, object_id: str, access_id: str, *, run_as: str | None = None
    ) -> Response[Any]:
        """Get Access Url"""
        client = self._get_client()
        response = client.get(f"/ga4gh/drs/v1/objects/{object_id}/access/{access_id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def post_ga4gh_drs_v1_objects_object_id_access_access_id(
        self, object_id: str, access_id: str, *, run_as: str | None = None
    ) -> Response[Any]:
        """Get Access Url"""
        client = self._get_client()
        response = client.post(f"/ga4gh/drs/v1/objects/{object_id}/access/{access_id}", headers={"run-as": run_as})
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def drs__v1_service_info__service_info(self) -> Response[Service]:
        """Service Info"""
        client = self._get_client()
        response = client.get("/ga4gh/drs/v1/service-info")
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = Service.model_validate(response.json())
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )

    def oauth2__oauth2_callback(
        self, *, state: str, code: str | None = None, error: str | None = None, run_as: str | None = None
    ) -> Response[Any]:
        """Callback entry point for remote resource responses with OAuth2 authorization codes"""
        client = self._get_client()
        response = client.get(
            "/oauth2_callback",
            params=self._filter_none_values({"state": state, "code": code, "error": error}),
            headers={"run-as": run_as},
        )
        self._handle_response(response)
        if response.status_code == 204:
            return Response(
                data=None,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
        else:
            data = response.json()
            return Response(
                data=data,
                status_code=response.status_code,
                headers=dict(response.headers),
                response_time=response.elapsed.total_seconds(),
            )
