from typing import TYPE_CHECKING, Any
from uuid import UUID

from ...models.anonymous_array_item_113 import AnonymousArrayItem113
from ...models.anonymous_array_item_131 import AnonymousArrayItem131
from ...models.anonymous_array_item_133 import AnonymousArrayItem133
from ...models.async_file import AsyncFile
from ...models.async_task_result_summary import AsyncTaskResultSummary
from ...models.create_invocations_from_store_payload import CreateInvocationsFromStorePayload
from ...models.create_workflow_landing_request_payload import CreateWorkflowLandingRequestPayload
from ...models.invocation_jobs_response import InvocationJobsResponse
from ...models.invocation_report import InvocationReport
from ...models.invocation_step import InvocationStep
from ...models.invocation_update_payload import InvocationUpdatePayload
from ...models.invoke_workflow_payload import InvokeWorkflowPayload
from ...models.item_tags_create_payload import ItemTagsCreatePayload
from ...models.item_tags_list_response import ItemTagsListResponse
from ...models.item_tags_response import ItemTagsResponse
from ...models.prepare_store_download_payload import PrepareStoreDownloadPayload
from ...models.refactor_request import RefactorRequest
from ...models.refactor_response import RefactorResponse
from ...models.report_invocation_error_payload import ReportInvocationErrorPayload
from ...models.root_model_dict_str_int_2 import RootModelDictStrInt2
from ...models.set_slug_payload import SetSlugPayload
from ...models.share_with_payload import ShareWithPayload
from ...models.share_with_status import ShareWithStatus
from ...models.sharing_status import SharingStatus
from ...models.stored_workflow_detailed import StoredWorkflowDetailed
from ...models.workflow_invocation_request_model import WorkflowInvocationRequestModel
from ...models.workflow_invocation_response import WorkflowInvocationResponse
from ...models.workflow_job_metric import WorkflowJobMetric
from ...models.workflow_landing_request import WorkflowLandingRequest
from ...models.workflows_cancel_invocation_param_run_as import WorkflowsCancelInvocationParamRunAs
from ...models.workflows_claim_claim_landing_param_run_as import WorkflowsClaimClaimLandingParamRunAs
from ...models.workflows_claim_claim_landing_request_body import WorkflowsClaimClaimLandingRequestBody
from ...models.workflows_create_landing_param_run_as import WorkflowsCreateLandingParamRunAs
from ...models.workflows_delete_workflow_param_run_as import WorkflowsDeleteWorkflowParamRunAs
from ...models.workflows_disable_link_access_disable_link_access_param_run_as import (
    WorkflowsDisableLinkAccessDisableLinkAccessParamRunAs,
)
from ...models.workflows_enable_link_access_enable_link_access_param_run_as import (
    WorkflowsEnableLinkAccessEnableLinkAccessParamRunAs,
)
from ...models.workflows_error_report_error_param_run_as import WorkflowsErrorReportErrorParamRunAs
from ...models.workflows_from_store_create_invocations_from_store_param_run_as import (
    WorkflowsFromStoreCreateInvocationsFromStoreParamRunAs,
)
from ...models.workflows_get_landing_param_run_as import WorkflowsGetLandingParamRunAs
from ...models.workflows_index_invocations_param_history_id import WorkflowsIndexInvocationsParamHistoryId
from ...models.workflows_index_invocations_param_include_terminal import WorkflowsIndexInvocationsParamIncludeTerminal
from ...models.workflows_index_invocations_param_instance import WorkflowsIndexInvocationsParamInstance
from ...models.workflows_index_invocations_param_job_id import WorkflowsIndexInvocationsParamJobId
from ...models.workflows_index_invocations_param_limit import WorkflowsIndexInvocationsParamLimit
from ...models.workflows_index_invocations_param_offset import WorkflowsIndexInvocationsParamOffset
from ...models.workflows_index_invocations_param_run_as import WorkflowsIndexInvocationsParamRunAs
from ...models.workflows_index_invocations_param_sort_by import WorkflowsIndexInvocationsParamSortBy
from ...models.workflows_index_invocations_param_user_id import WorkflowsIndexInvocationsParamUserId
from ...models.workflows_index_invocations_param_view import WorkflowsIndexInvocationsParamView
from ...models.workflows_index_invocations_param_workflow_id import WorkflowsIndexInvocationsParamWorkflowId
from ...models.workflows_index_param_limit import WorkflowsIndexParamLimit
from ...models.workflows_index_param_offset import WorkflowsIndexParamOffset
from ...models.workflows_index_param_run_as import WorkflowsIndexParamRunAs
from ...models.workflows_index_param_search import WorkflowsIndexParamSearch
from ...models.workflows_index_param_show_published import WorkflowsIndexParamShowPublished
from ...models.workflows_index_param_show_shared import WorkflowsIndexParamShowShared
from ...models.workflows_index_param_sort_by import WorkflowsIndexParamSortBy
from ...models.workflows_index_param_sort_desc import WorkflowsIndexParamSortDesc
from ...models.workflows_invocation_counts_param_instance import WorkflowsInvocationCountsParamInstance
from ...models.workflows_invocation_counts_param_run_as import WorkflowsInvocationCountsParamRunAs
from ...models.workflows_invocations_cancel_workflow_invocation_param_run_as import (
    WorkflowsInvocationsCancelWorkflowInvocationParamRunAs,
)
from ...models.workflows_invocations_index_workflow_invocations_param_history_id import (
    WorkflowsInvocationsIndexWorkflowInvocationsParamHistoryId,
)
from ...models.workflows_invocations_index_workflow_invocations_param_include_terminal import (
    WorkflowsInvocationsIndexWorkflowInvocationsParamIncludeTerminal,
)
from ...models.workflows_invocations_index_workflow_invocations_param_instance import (
    WorkflowsInvocationsIndexWorkflowInvocationsParamInstance,
)
from ...models.workflows_invocations_index_workflow_invocations_param_job_id import (
    WorkflowsInvocationsIndexWorkflowInvocationsParamJobId,
)
from ...models.workflows_invocations_index_workflow_invocations_param_limit import (
    WorkflowsInvocationsIndexWorkflowInvocationsParamLimit,
)
from ...models.workflows_invocations_index_workflow_invocations_param_offset import (
    WorkflowsInvocationsIndexWorkflowInvocationsParamOffset,
)
from ...models.workflows_invocations_index_workflow_invocations_param_run_as import (
    WorkflowsInvocationsIndexWorkflowInvocationsParamRunAs,
)
from ...models.workflows_invocations_index_workflow_invocations_param_sort_by import (
    WorkflowsInvocationsIndexWorkflowInvocationsParamSortBy,
)
from ...models.workflows_invocations_index_workflow_invocations_param_user_id import (
    WorkflowsInvocationsIndexWorkflowInvocationsParamUserId,
)
from ...models.workflows_invocations_index_workflow_invocations_param_view import (
    WorkflowsInvocationsIndexWorkflowInvocationsParamView,
)
from ...models.workflows_invocations_invoke_200_response import WorkflowsInvocationsInvoke200Response
from ...models.workflows_invocations_invoke_param_run_as import WorkflowsInvocationsInvokeParamRunAs
from ...models.workflows_invocations_invoke_param_workflow_id import WorkflowsInvocationsInvokeParamWorkflowId
from ...models.workflows_invocations_jobs_summary_workflow_invocation_jobs_summary_param_run_as import (
    WorkflowsInvocationsJobsSummaryWorkflowInvocationJobsSummaryParamRunAs,
)
from ...models.workflows_invocations_report_pdf_show_workflow_invocation_report_pdf_param_run_as import (
    WorkflowsInvocationsReportPdfShowWorkflowInvocationReportPdfParamRunAs,
)
from ...models.workflows_invocations_report_show_workflow_invocation_report_param_run_as import (
    WorkflowsInvocationsReportShowWorkflowInvocationReportParamRunAs,
)
from ...models.workflows_invocations_show_workflow_invocation_param_run_as import (
    WorkflowsInvocationsShowWorkflowInvocationParamRunAs,
)
from ...models.workflows_invocations_step_jobs_summary_workflow_invocation_step_jobs_summary_param_run_as import (
    WorkflowsInvocationsStepJobsSummaryWorkflowInvocationStepJobsSummaryParamRunAs,
)
from ...models.workflows_invocations_steps_update_workflow_invocation_step_param_run_as import (
    WorkflowsInvocationsStepsUpdateWorkflowInvocationStepParamRunAs,
)
from ...models.workflows_invocations_steps_workflow_invocation_step_param_run_as import (
    WorkflowsInvocationsStepsWorkflowInvocationStepParamRunAs,
)
from ...models.workflows_jobs_summary_invocation_jobs_summary_param_run_as import (
    WorkflowsJobsSummaryInvocationJobsSummaryParamRunAs,
)
from ...models.workflows_menu_get_workflow_menu_param_missing_tools import WorkflowsMenuGetWorkflowMenuParamMissingTools
from ...models.workflows_menu_get_workflow_menu_param_run_as import WorkflowsMenuGetWorkflowMenuParamRunAs
from ...models.workflows_menu_get_workflow_menu_param_show_deleted import WorkflowsMenuGetWorkflowMenuParamShowDeleted
from ...models.workflows_menu_get_workflow_menu_param_show_hidden import WorkflowsMenuGetWorkflowMenuParamShowHidden
from ...models.workflows_menu_get_workflow_menu_param_show_published import (
    WorkflowsMenuGetWorkflowMenuParamShowPublished,
)
from ...models.workflows_menu_get_workflow_menu_param_show_shared import WorkflowsMenuGetWorkflowMenuParamShowShared
from ...models.workflows_metrics_get_invocation_metrics_param_run_as import (
    WorkflowsMetricsGetInvocationMetricsParamRunAs,
)
from ...models.workflows_prepare_store_download_prepare_store_download_param_run_as import (
    WorkflowsPrepareStoreDownloadPrepareStoreDownloadParamRunAs,
)
from ...models.workflows_publish_publish_param_run_as import WorkflowsPublishPublishParamRunAs
from ...models.workflows_refactor_refactor_param_instance import WorkflowsRefactorRefactorParamInstance
from ...models.workflows_refactor_refactor_param_run_as import WorkflowsRefactorRefactorParamRunAs
from ...models.workflows_report_pdf_show_invocation_report_pdf_param_run_as import (
    WorkflowsReportPdfShowInvocationReportPdfParamRunAs,
)
from ...models.workflows_report_show_invocation_report_param_run_as import WorkflowsReportShowInvocationReportParamRunAs
from ...models.workflows_request_invocation_as_request_param_run_as import WorkflowsRequestInvocationAsRequestParamRunAs
from ...models.workflows_share_with_users_share_with_users_param_run_as import (
    WorkflowsShareWithUsersShareWithUsersParamRunAs,
)
from ...models.workflows_sharing_sharing_param_run_as import WorkflowsSharingSharingParamRunAs
from ...models.workflows_show_invocation_param_run_as import WorkflowsShowInvocationParamRunAs
from ...models.workflows_show_workflow_param_instance import WorkflowsShowWorkflowParamInstance
from ...models.workflows_show_workflow_param_legacy import WorkflowsShowWorkflowParamLegacy
from ...models.workflows_show_workflow_param_run_as import WorkflowsShowWorkflowParamRunAs
from ...models.workflows_show_workflow_param_version import WorkflowsShowWorkflowParamVersion
from ...models.workflows_slug_set_slug_param_run_as import WorkflowsSlugSetSlugParamRunAs
from ...models.workflows_step_jobs_summary_invocation_step_jobs_summary_param_run_as import (
    WorkflowsStepJobsSummaryInvocationStepJobsSummaryParamRunAs,
)
from ...models.workflows_steps_invocation_step_param_run_as import WorkflowsStepsInvocationStepParamRunAs
from ...models.workflows_steps_step_param_run_as import WorkflowsStepsStepParamRunAs
from ...models.workflows_steps_update_invocation_step_param_run_as import WorkflowsStepsUpdateInvocationStepParamRunAs
from ...models.workflows_tags_create_param_run_as import WorkflowsTagsCreateParamRunAs
from ...models.workflows_tags_delete_param_run_as import WorkflowsTagsDeleteParamRunAs
from ...models.workflows_tags_index_param_run_as import WorkflowsTagsIndexParamRunAs
from ...models.workflows_tags_show_param_run_as import WorkflowsTagsShowParamRunAs
from ...models.workflows_tags_update_param_run_as import WorkflowsTagsUpdateParamRunAs
from ...models.workflows_undelete_undelete_workflow_param_run_as import WorkflowsUndeleteUndeleteWorkflowParamRunAs
from ...models.workflows_unpublish_unpublish_param_run_as import WorkflowsUnpublishUnpublishParamRunAs
from ...models.workflows_usage_cancel_workflow_invocation_param_run_as import (
    WorkflowsUsageCancelWorkflowInvocationParamRunAs,
)
from ...models.workflows_usage_index_workflow_invocations_param_history_id import (
    WorkflowsUsageIndexWorkflowInvocationsParamHistoryId,
)
from ...models.workflows_usage_index_workflow_invocations_param_include_terminal import (
    WorkflowsUsageIndexWorkflowInvocationsParamIncludeTerminal,
)
from ...models.workflows_usage_index_workflow_invocations_param_instance import (
    WorkflowsUsageIndexWorkflowInvocationsParamInstance,
)
from ...models.workflows_usage_index_workflow_invocations_param_job_id import (
    WorkflowsUsageIndexWorkflowInvocationsParamJobId,
)
from ...models.workflows_usage_index_workflow_invocations_param_limit import (
    WorkflowsUsageIndexWorkflowInvocationsParamLimit,
)
from ...models.workflows_usage_index_workflow_invocations_param_offset import (
    WorkflowsUsageIndexWorkflowInvocationsParamOffset,
)
from ...models.workflows_usage_index_workflow_invocations_param_run_as import (
    WorkflowsUsageIndexWorkflowInvocationsParamRunAs,
)
from ...models.workflows_usage_index_workflow_invocations_param_sort_by import (
    WorkflowsUsageIndexWorkflowInvocationsParamSortBy,
)
from ...models.workflows_usage_index_workflow_invocations_param_user_id import (
    WorkflowsUsageIndexWorkflowInvocationsParamUserId,
)
from ...models.workflows_usage_index_workflow_invocations_param_view import (
    WorkflowsUsageIndexWorkflowInvocationsParamView,
)
from ...models.workflows_usage_invoke_200_response import WorkflowsUsageInvoke200Response
from ...models.workflows_usage_invoke_param_run_as import WorkflowsUsageInvokeParamRunAs
from ...models.workflows_usage_invoke_param_workflow_id import WorkflowsUsageInvokeParamWorkflowId
from ...models.workflows_usage_jobs_summary_workflow_invocation_jobs_summary_param_run_as import (
    WorkflowsUsageJobsSummaryWorkflowInvocationJobsSummaryParamRunAs,
)
from ...models.workflows_usage_report_pdf_show_workflow_invocation_report_pdf_param_run_as import (
    WorkflowsUsageReportPdfShowWorkflowInvocationReportPdfParamRunAs,
)
from ...models.workflows_usage_report_show_workflow_invocation_report_param_run_as import (
    WorkflowsUsageReportShowWorkflowInvocationReportParamRunAs,
)
from ...models.workflows_usage_show_workflow_invocation_param_run_as import (
    WorkflowsUsageShowWorkflowInvocationParamRunAs,
)
from ...models.workflows_usage_step_jobs_summary_workflow_invocation_step_jobs_summary_param_run_as import (
    WorkflowsUsageStepJobsSummaryWorkflowInvocationStepJobsSummaryParamRunAs,
)
from ...models.workflows_usage_steps_update_workflow_invocation_step_param_run_as import (
    WorkflowsUsageStepsUpdateWorkflowInvocationStepParamRunAs,
)
from ...models.workflows_usage_steps_workflow_invocation_step_param_run_as import (
    WorkflowsUsageStepsWorkflowInvocationStepParamRunAs,
)
from ...models.workflows_versions_show_versions_param_instance import WorkflowsVersionsShowVersionsParamInstance
from ...models.workflows_versions_show_versions_param_run_as import WorkflowsVersionsShowVersionsParamRunAs
from ...models.workflows_write_store_write_store_param_run_as import WorkflowsWriteStoreWriteStoreParamRunAs
from ...models.write_invocation_store_to_payload import WriteInvocationStoreToPayload

if TYPE_CHECKING:
    pass


class MockWorkflowsClient:
    """
    Mock implementation of WorkflowsClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestWorkflowsClient(MockWorkflowsClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def workflows_index_invocations(
        self,
        workflow_id: WorkflowsIndexInvocationsParamWorkflowId | None = None,
        history_id: WorkflowsIndexInvocationsParamHistoryId | None = None,
        job_id: WorkflowsIndexInvocationsParamJobId | None = None,
        user_id: WorkflowsIndexInvocationsParamUserId | None = None,
        sort_by: WorkflowsIndexInvocationsParamSortBy | None = None,
        sort_desc: bool | None = None,
        include_terminal: WorkflowsIndexInvocationsParamIncludeTerminal | None = None,
        limit: WorkflowsIndexInvocationsParamLimit | None = None,
        offset: WorkflowsIndexInvocationsParamOffset | None = None,
        instance: WorkflowsIndexInvocationsParamInstance | None = None,
        view: WorkflowsIndexInvocationsParamView | None = None,
        step_details: bool | None = None,
        include_nested_invocations: bool | None = None,
        run_as: WorkflowsIndexInvocationsParamRunAs | None = None,
    ) -> list[WorkflowInvocationResponse]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_index_invocations() not implemented. Override this method in your test subclass."
        )

    async def workflows_from_store_create_invocations_from_store(
        self,
        body: CreateInvocationsFromStorePayload,
        run_as: WorkflowsFromStoreCreateInvocationsFromStoreParamRunAs | None = None,
    ) -> list[WorkflowInvocationResponse]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_from_store_create_invocations_from_store() not implemented. Override this method in your test subclass."
        )

    async def workflows_steps_step(
        self,
        step_id: str,
        run_as: WorkflowsStepsStepParamRunAs | None = None,
    ) -> InvocationStep:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_steps_step() not implemented. Override this method in your test subclass."
        )

    async def workflows_cancel_invocation(
        self,
        invocation_id: str,
        step_details: bool | None = None,
        legacy_job_state: bool | None = None,
        run_as: WorkflowsCancelInvocationParamRunAs | None = None,
    ) -> WorkflowInvocationResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_cancel_invocation() not implemented. Override this method in your test subclass."
        )

    async def workflows_show_invocation(
        self,
        invocation_id: str,
        step_details: bool | None = None,
        legacy_job_state: bool | None = None,
        run_as: WorkflowsShowInvocationParamRunAs | None = None,
    ) -> WorkflowInvocationResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_show_invocation() not implemented. Override this method in your test subclass."
        )

    async def workflows_error_report_error(
        self,
        invocation_id: str,
        body: ReportInvocationErrorPayload,
        run_as: WorkflowsErrorReportErrorParamRunAs | None = None,
    ) -> None:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_error_report_error() not implemented. Override this method in your test subclass."
        )

    async def workflows_jobs_summary_invocation_jobs_summary(
        self,
        invocation_id: str,
        run_as: WorkflowsJobsSummaryInvocationJobsSummaryParamRunAs | None = None,
    ) -> InvocationJobsResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_jobs_summary_invocation_jobs_summary() not implemented. Override this method in your test subclass."
        )

    async def workflows_metrics_get_invocation_metrics(
        self,
        invocation_id: str,
        run_as: WorkflowsMetricsGetInvocationMetricsParamRunAs | None = None,
    ) -> list[WorkflowJobMetric]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_metrics_get_invocation_metrics() not implemented. Override this method in your test subclass."
        )

    async def workflows_prepare_store_download_prepare_store_download(
        self,
        invocation_id: str,
        body: PrepareStoreDownloadPayload,
        run_as: WorkflowsPrepareStoreDownloadPrepareStoreDownloadParamRunAs | None = None,
    ) -> AsyncFile:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_prepare_store_download_prepare_store_download() not implemented. Override this method in your test subclass."
        )

    async def workflows_report_show_invocation_report(
        self,
        invocation_id: str,
        run_as: WorkflowsReportShowInvocationReportParamRunAs | None = None,
    ) -> InvocationReport:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_report_show_invocation_report() not implemented. Override this method in your test subclass."
        )

    async def workflows_report_pdf_show_invocation_report_pdf(
        self,
        invocation_id: str,
        run_as: WorkflowsReportPdfShowInvocationReportPdfParamRunAs | None = None,
    ) -> None:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_report_pdf_show_invocation_report_pdf() not implemented. Override this method in your test subclass."
        )

    async def workflows_request_invocation_as_request(
        self,
        invocation_id: str,
        run_as: WorkflowsRequestInvocationAsRequestParamRunAs | None = None,
    ) -> WorkflowInvocationRequestModel:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_request_invocation_as_request() not implemented. Override this method in your test subclass."
        )

    async def workflows_step_jobs_summary_invocation_step_jobs_summary(
        self,
        invocation_id: str,
        run_as: WorkflowsStepJobsSummaryInvocationStepJobsSummaryParamRunAs | None = None,
    ) -> list[AnonymousArrayItem113]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_step_jobs_summary_invocation_step_jobs_summary() not implemented. Override this method in your test subclass."
        )

    async def workflows_steps_invocation_step(
        self,
        invocation_id: str,
        step_id: str,
        run_as: WorkflowsStepsInvocationStepParamRunAs | None = None,
    ) -> InvocationStep:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_steps_invocation_step() not implemented. Override this method in your test subclass."
        )

    async def workflows_steps_update_invocation_step(
        self,
        invocation_id: str,
        step_id: str,
        body: InvocationUpdatePayload,
        run_as: WorkflowsStepsUpdateInvocationStepParamRunAs | None = None,
    ) -> InvocationStep:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_steps_update_invocation_step() not implemented. Override this method in your test subclass."
        )

    async def workflows_write_store_write_store(
        self,
        invocation_id: str,
        body: WriteInvocationStoreToPayload,
        run_as: WorkflowsWriteStoreWriteStoreParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_write_store_write_store() not implemented. Override this method in your test subclass."
        )

    async def workflows_create_landing(
        self,
        body: CreateWorkflowLandingRequestPayload,
        run_as: WorkflowsCreateLandingParamRunAs | None = None,
    ) -> WorkflowLandingRequest:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_create_landing() not implemented. Override this method in your test subclass."
        )

    async def workflows_get_landing(
        self,
        uuid_: UUID,
        run_as: WorkflowsGetLandingParamRunAs | None = None,
    ) -> WorkflowLandingRequest:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_get_landing() not implemented. Override this method in your test subclass."
        )

    async def workflows_claim_claim_landing(
        self,
        uuid_: UUID,
        body: WorkflowsClaimClaimLandingRequestBody | None,
        run_as: WorkflowsClaimClaimLandingParamRunAs | None = None,
    ) -> WorkflowLandingRequest:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_claim_claim_landing() not implemented. Override this method in your test subclass."
        )

    async def workflows_index(
        self,
        show_deleted: bool | None = None,
        show_hidden: bool | None = None,
        missing_tools: bool | None = None,
        show_published: WorkflowsIndexParamShowPublished | None = None,
        show_shared: WorkflowsIndexParamShowShared | None = None,
        sort_by: WorkflowsIndexParamSortBy | None = None,
        sort_desc: WorkflowsIndexParamSortDesc | None = None,
        limit: WorkflowsIndexParamLimit | None = None,
        offset: WorkflowsIndexParamOffset | None = None,
        search: WorkflowsIndexParamSearch | None = None,
        skip_step_counts: bool | None = None,
        run_as: WorkflowsIndexParamRunAs | None = None,
    ) -> list[Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_index() not implemented. Override this method in your test subclass."
        )

    async def workflows_menu_get_workflow_menu(
        self,
        show_deleted: WorkflowsMenuGetWorkflowMenuParamShowDeleted | None = None,
        show_hidden: WorkflowsMenuGetWorkflowMenuParamShowHidden | None = None,
        missing_tools: WorkflowsMenuGetWorkflowMenuParamMissingTools | None = None,
        show_published: WorkflowsMenuGetWorkflowMenuParamShowPublished | None = None,
        show_shared: WorkflowsMenuGetWorkflowMenuParamShowShared | None = None,
        run_as: WorkflowsMenuGetWorkflowMenuParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_menu_get_workflow_menu() not implemented. Override this method in your test subclass."
        )

    async def workflows_delete_workflow(
        self,
        workflow_id: str,
        run_as: WorkflowsDeleteWorkflowParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_delete_workflow() not implemented. Override this method in your test subclass."
        )

    async def workflows_show_workflow(
        self,
        workflow_id: str,
        instance: WorkflowsShowWorkflowParamInstance | None = None,
        legacy: WorkflowsShowWorkflowParamLegacy | None = None,
        version: WorkflowsShowWorkflowParamVersion | None = None,
        run_as: WorkflowsShowWorkflowParamRunAs | None = None,
    ) -> StoredWorkflowDetailed:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_show_workflow() not implemented. Override this method in your test subclass."
        )

    async def workflows_invocation_counts(
        self,
        workflow_id: str,
        instance: WorkflowsInvocationCountsParamInstance | None = None,
        run_as: WorkflowsInvocationCountsParamRunAs | None = None,
    ) -> RootModelDictStrInt2:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_invocation_counts() not implemented. Override this method in your test subclass."
        )

    async def workflows_disable_link_access_disable_link_access(
        self,
        workflow_id: str,
        run_as: WorkflowsDisableLinkAccessDisableLinkAccessParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_disable_link_access_disable_link_access() not implemented. Override this method in your test subclass."
        )

    async def workflows_enable_link_access_enable_link_access(
        self,
        workflow_id: str,
        run_as: WorkflowsEnableLinkAccessEnableLinkAccessParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_enable_link_access_enable_link_access() not implemented. Override this method in your test subclass."
        )

    async def workflows_invocations_index_workflow_invocations(
        self,
        workflow_id: str,
        history_id: WorkflowsInvocationsIndexWorkflowInvocationsParamHistoryId | None = None,
        job_id: WorkflowsInvocationsIndexWorkflowInvocationsParamJobId | None = None,
        user_id: WorkflowsInvocationsIndexWorkflowInvocationsParamUserId | None = None,
        sort_by: WorkflowsInvocationsIndexWorkflowInvocationsParamSortBy | None = None,
        sort_desc: bool | None = None,
        include_terminal: WorkflowsInvocationsIndexWorkflowInvocationsParamIncludeTerminal | None = None,
        limit: WorkflowsInvocationsIndexWorkflowInvocationsParamLimit | None = None,
        offset: WorkflowsInvocationsIndexWorkflowInvocationsParamOffset | None = None,
        instance: WorkflowsInvocationsIndexWorkflowInvocationsParamInstance | None = None,
        view: WorkflowsInvocationsIndexWorkflowInvocationsParamView | None = None,
        step_details: bool | None = None,
        run_as: WorkflowsInvocationsIndexWorkflowInvocationsParamRunAs | None = None,
    ) -> list[WorkflowInvocationResponse]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_invocations_index_workflow_invocations() not implemented. Override this method in your test subclass."
        )

    async def workflows_invocations_invoke(
        self,
        workflow_id: WorkflowsInvocationsInvokeParamWorkflowId,
        body: InvokeWorkflowPayload,
        run_as: WorkflowsInvocationsInvokeParamRunAs | None = None,
    ) -> WorkflowsInvocationsInvoke200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_invocations_invoke() not implemented. Override this method in your test subclass."
        )

    async def workflows_invocations_cancel_workflow_invocation(
        self,
        invocation_id: str,
        workflow_id: str,
        step_details: bool | None = None,
        legacy_job_state: bool | None = None,
        run_as: WorkflowsInvocationsCancelWorkflowInvocationParamRunAs | None = None,
    ) -> WorkflowInvocationResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_invocations_cancel_workflow_invocation() not implemented. Override this method in your test subclass."
        )

    async def workflows_invocations_show_workflow_invocation(
        self,
        workflow_id: str,
        invocation_id: str,
        step_details: bool | None = None,
        legacy_job_state: bool | None = None,
        run_as: WorkflowsInvocationsShowWorkflowInvocationParamRunAs | None = None,
    ) -> WorkflowInvocationResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_invocations_show_workflow_invocation() not implemented. Override this method in your test subclass."
        )

    async def workflows_invocations_jobs_summary_workflow_invocation_jobs_summary(
        self,
        workflow_id: str,
        invocation_id: str,
        run_as: WorkflowsInvocationsJobsSummaryWorkflowInvocationJobsSummaryParamRunAs | None = None,
    ) -> InvocationJobsResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_invocations_jobs_summary_workflow_invocation_jobs_summary() not implemented. Override this method in your test subclass."
        )

    async def workflows_invocations_report_show_workflow_invocation_report(
        self,
        invocation_id: str,
        workflow_id: str,
        run_as: WorkflowsInvocationsReportShowWorkflowInvocationReportParamRunAs | None = None,
    ) -> InvocationReport:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_invocations_report_show_workflow_invocation_report() not implemented. Override this method in your test subclass."
        )

    async def workflows_invocations_report_pdf_show_workflow_invocation_report_pdf(
        self,
        workflow_id: str,
        invocation_id: str,
        run_as: WorkflowsInvocationsReportPdfShowWorkflowInvocationReportPdfParamRunAs | None = None,
    ) -> None:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_invocations_report_pdf_show_workflow_invocation_report_pdf() not implemented. Override this method in your test subclass."
        )

    async def workflows_invocations_step_jobs_summary_workflow_invocation_step_jobs_summary(
        self,
        workflow_id: str,
        invocation_id: str,
        run_as: WorkflowsInvocationsStepJobsSummaryWorkflowInvocationStepJobsSummaryParamRunAs | None = None,
    ) -> list[AnonymousArrayItem131]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_invocations_step_jobs_summary_workflow_invocation_step_jobs_summary() not implemented. Override this method in your test subclass."
        )

    async def workflows_invocations_steps_workflow_invocation_step(
        self,
        workflow_id: str,
        invocation_id: str,
        step_id: str,
        run_as: WorkflowsInvocationsStepsWorkflowInvocationStepParamRunAs | None = None,
    ) -> InvocationStep:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_invocations_steps_workflow_invocation_step() not implemented. Override this method in your test subclass."
        )

    async def workflows_invocations_steps_update_workflow_invocation_step(
        self,
        workflow_id: str,
        invocation_id: str,
        step_id: str,
        body: InvocationUpdatePayload,
        run_as: WorkflowsInvocationsStepsUpdateWorkflowInvocationStepParamRunAs | None = None,
    ) -> InvocationStep:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_invocations_steps_update_workflow_invocation_step() not implemented. Override this method in your test subclass."
        )

    async def workflows_publish_publish(
        self,
        workflow_id: str,
        run_as: WorkflowsPublishPublishParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_publish_publish() not implemented. Override this method in your test subclass."
        )

    async def workflows_refactor_refactor(
        self,
        workflow_id: str,
        body: RefactorRequest,
        instance: WorkflowsRefactorRefactorParamInstance | None = None,
        run_as: WorkflowsRefactorRefactorParamRunAs | None = None,
    ) -> RefactorResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_refactor_refactor() not implemented. Override this method in your test subclass."
        )

    async def workflows_share_with_users_share_with_users(
        self,
        workflow_id: str,
        body: ShareWithPayload,
        run_as: WorkflowsShareWithUsersShareWithUsersParamRunAs | None = None,
    ) -> ShareWithStatus:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_share_with_users_share_with_users() not implemented. Override this method in your test subclass."
        )

    async def workflows_sharing_sharing(
        self,
        workflow_id: str,
        run_as: WorkflowsSharingSharingParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_sharing_sharing() not implemented. Override this method in your test subclass."
        )

    async def workflows_slug_set_slug(
        self,
        workflow_id: str,
        body: SetSlugPayload,
        run_as: WorkflowsSlugSetSlugParamRunAs | None = None,
    ) -> None:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_slug_set_slug() not implemented. Override this method in your test subclass."
        )

    async def workflows_tags_index(
        self,
        workflow_id: str,
        run_as: WorkflowsTagsIndexParamRunAs | None = None,
    ) -> ItemTagsListResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_tags_index() not implemented. Override this method in your test subclass."
        )

    async def workflows_tags_delete(
        self,
        workflow_id: str,
        tag_name: str,
        run_as: WorkflowsTagsDeleteParamRunAs | None = None,
    ) -> bool:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_tags_delete() not implemented. Override this method in your test subclass."
        )

    async def workflows_tags_show(
        self,
        workflow_id: str,
        tag_name: str,
        run_as: WorkflowsTagsShowParamRunAs | None = None,
    ) -> ItemTagsResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_tags_show() not implemented. Override this method in your test subclass."
        )

    async def workflows_tags_create(
        self,
        workflow_id: str,
        tag_name: str,
        run_as: WorkflowsTagsCreateParamRunAs | None = None,
        body: ItemTagsCreatePayload | None = None,
    ) -> ItemTagsResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_tags_create() not implemented. Override this method in your test subclass."
        )

    async def workflows_tags_update(
        self,
        workflow_id: str,
        tag_name: str,
        body: ItemTagsCreatePayload,
        run_as: WorkflowsTagsUpdateParamRunAs | None = None,
    ) -> ItemTagsResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_tags_update() not implemented. Override this method in your test subclass."
        )

    async def workflows_undelete_undelete_workflow(
        self,
        workflow_id: str,
        run_as: WorkflowsUndeleteUndeleteWorkflowParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_undelete_undelete_workflow() not implemented. Override this method in your test subclass."
        )

    async def workflows_unpublish_unpublish(
        self,
        workflow_id: str,
        run_as: WorkflowsUnpublishUnpublishParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_unpublish_unpublish() not implemented. Override this method in your test subclass."
        )

    async def workflows_usage_index_workflow_invocations(
        self,
        workflow_id: str,
        history_id: WorkflowsUsageIndexWorkflowInvocationsParamHistoryId | None = None,
        job_id: WorkflowsUsageIndexWorkflowInvocationsParamJobId | None = None,
        user_id: WorkflowsUsageIndexWorkflowInvocationsParamUserId | None = None,
        sort_by: WorkflowsUsageIndexWorkflowInvocationsParamSortBy | None = None,
        sort_desc: bool | None = None,
        include_terminal: WorkflowsUsageIndexWorkflowInvocationsParamIncludeTerminal | None = None,
        limit: WorkflowsUsageIndexWorkflowInvocationsParamLimit | None = None,
        offset: WorkflowsUsageIndexWorkflowInvocationsParamOffset | None = None,
        instance: WorkflowsUsageIndexWorkflowInvocationsParamInstance | None = None,
        view: WorkflowsUsageIndexWorkflowInvocationsParamView | None = None,
        step_details: bool | None = None,
        run_as: WorkflowsUsageIndexWorkflowInvocationsParamRunAs | None = None,
    ) -> list[WorkflowInvocationResponse]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_usage_index_workflow_invocations() not implemented. Override this method in your test subclass."
        )

    async def workflows_usage_invoke(
        self,
        workflow_id: WorkflowsUsageInvokeParamWorkflowId,
        body: InvokeWorkflowPayload,
        run_as: WorkflowsUsageInvokeParamRunAs | None = None,
    ) -> WorkflowsUsageInvoke200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_usage_invoke() not implemented. Override this method in your test subclass."
        )

    async def workflows_usage_cancel_workflow_invocation(
        self,
        invocation_id: str,
        workflow_id: str,
        step_details: bool | None = None,
        legacy_job_state: bool | None = None,
        run_as: WorkflowsUsageCancelWorkflowInvocationParamRunAs | None = None,
    ) -> WorkflowInvocationResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_usage_cancel_workflow_invocation() not implemented. Override this method in your test subclass."
        )

    async def workflows_usage_show_workflow_invocation(
        self,
        workflow_id: str,
        invocation_id: str,
        step_details: bool | None = None,
        legacy_job_state: bool | None = None,
        run_as: WorkflowsUsageShowWorkflowInvocationParamRunAs | None = None,
    ) -> WorkflowInvocationResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_usage_show_workflow_invocation() not implemented. Override this method in your test subclass."
        )

    async def workflows_usage_jobs_summary_workflow_invocation_jobs_summary(
        self,
        workflow_id: str,
        invocation_id: str,
        run_as: WorkflowsUsageJobsSummaryWorkflowInvocationJobsSummaryParamRunAs | None = None,
    ) -> InvocationJobsResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_usage_jobs_summary_workflow_invocation_jobs_summary() not implemented. Override this method in your test subclass."
        )

    async def workflows_usage_report_show_workflow_invocation_report(
        self,
        invocation_id: str,
        workflow_id: str,
        run_as: WorkflowsUsageReportShowWorkflowInvocationReportParamRunAs | None = None,
    ) -> InvocationReport:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_usage_report_show_workflow_invocation_report() not implemented. Override this method in your test subclass."
        )

    async def workflows_usage_report_pdf_show_workflow_invocation_report_pdf(
        self,
        workflow_id: str,
        invocation_id: str,
        run_as: WorkflowsUsageReportPdfShowWorkflowInvocationReportPdfParamRunAs | None = None,
    ) -> None:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_usage_report_pdf_show_workflow_invocation_report_pdf() not implemented. Override this method in your test subclass."
        )

    async def workflows_usage_step_jobs_summary_workflow_invocation_step_jobs_summary(
        self,
        workflow_id: str,
        invocation_id: str,
        run_as: WorkflowsUsageStepJobsSummaryWorkflowInvocationStepJobsSummaryParamRunAs | None = None,
    ) -> list[AnonymousArrayItem133]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_usage_step_jobs_summary_workflow_invocation_step_jobs_summary() not implemented. Override this method in your test subclass."
        )

    async def workflows_usage_steps_workflow_invocation_step(
        self,
        workflow_id: str,
        invocation_id: str,
        step_id: str,
        run_as: WorkflowsUsageStepsWorkflowInvocationStepParamRunAs | None = None,
    ) -> InvocationStep:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_usage_steps_workflow_invocation_step() not implemented. Override this method in your test subclass."
        )

    async def workflows_usage_steps_update_workflow_invocation_step(
        self,
        workflow_id: str,
        invocation_id: str,
        step_id: str,
        body: InvocationUpdatePayload,
        run_as: WorkflowsUsageStepsUpdateWorkflowInvocationStepParamRunAs | None = None,
    ) -> InvocationStep:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_usage_steps_update_workflow_invocation_step() not implemented. Override this method in your test subclass."
        )

    async def workflows_versions_show_versions(
        self,
        workflow_id: str,
        instance: WorkflowsVersionsShowVersionsParamInstance | None = None,
        run_as: WorkflowsVersionsShowVersionsParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockWorkflowsClient.workflows_versions_show_versions() not implemented. Override this method in your test subclass."
        )
