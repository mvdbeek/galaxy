from typing import Any, cast
from uuid import UUID

from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.anonymous_array_item_202 import AnonymousArrayItem202
from ..models.anonymous_array_item_224 import AnonymousArrayItem224
from ..models.anonymous_array_item_226 import AnonymousArrayItem226
from ..models.anonymous_array_item_228 import AnonymousArrayItem228
from ..models.async_file import AsyncFile
from ..models.async_task_result_summary import AsyncTaskResultSummary
from ..models.create_invocations_from_store_payload import CreateInvocationsFromStorePayload
from ..models.create_workflow_landing_request_payload import CreateWorkflowLandingRequestPayload
from ..models.invocation_jobs_response import InvocationJobsResponse
from ..models.invocation_report import InvocationReport
from ..models.invocation_step import InvocationStep
from ..models.invocation_update_payload import InvocationUpdatePayload
from ..models.invoke_workflow_payload import InvokeWorkflowPayload
from ..models.item_tags_create_payload import ItemTagsCreatePayload
from ..models.item_tags_list_response import ItemTagsListResponse
from ..models.item_tags_response import ItemTagsResponse
from ..models.prepare_store_download_payload import PrepareStoreDownloadPayload
from ..models.refactor_request import RefactorRequest
from ..models.refactor_response import RefactorResponse
from ..models.report_invocation_error_payload import ReportInvocationErrorPayload
from ..models.root_model_dict_str_int_2 import RootModelDictStrInt2
from ..models.set_slug_payload import SetSlugPayload
from ..models.share_with_payload import ShareWithPayload
from ..models.share_with_status import ShareWithStatus
from ..models.sharing_status import SharingStatus
from ..models.stored_workflow_detailed import StoredWorkflowDetailed
from ..models.workflow_invocation_request_model import WorkflowInvocationRequestModel
from ..models.workflow_invocation_response import WorkflowInvocationResponse
from ..models.workflow_job_metric import WorkflowJobMetric
from ..models.workflow_landing_request import WorkflowLandingRequest
from ..models.workflows_cancel_invocation_param_run_as import WorkflowsCancelInvocationParamRunAs
from ..models.workflows_claim_claim_landing_param_run_as import WorkflowsClaimClaimLandingParamRunAs
from ..models.workflows_claim_claim_landing_request_body_2 import WorkflowsClaimClaimLandingRequestBody2
from ..models.workflows_create_landing_param_run_as import WorkflowsCreateLandingParamRunAs
from ..models.workflows_delete_workflow_param_run_as import WorkflowsDeleteWorkflowParamRunAs
from ..models.workflows_disable_link_access_disable_link_access_param_run_as import (
    WorkflowsDisableLinkAccessDisableLinkAccessParamRunAs,
)
from ..models.workflows_enable_link_access_enable_link_access_param_run_as import (
    WorkflowsEnableLinkAccessEnableLinkAccessParamRunAs,
)
from ..models.workflows_error_report_error_param_run_as import WorkflowsErrorReportErrorParamRunAs
from ..models.workflows_from_store_create_invocations_from_store_param_run_as import (
    WorkflowsFromStoreCreateInvocationsFromStoreParamRunAs,
)
from ..models.workflows_get_landing_param_run_as import WorkflowsGetLandingParamRunAs
from ..models.workflows_index_invocations_param_history_id import WorkflowsIndexInvocationsParamHistoryId
from ..models.workflows_index_invocations_param_include_terminal import WorkflowsIndexInvocationsParamIncludeTerminal
from ..models.workflows_index_invocations_param_instance import WorkflowsIndexInvocationsParamInstance
from ..models.workflows_index_invocations_param_job_id import WorkflowsIndexInvocationsParamJobId
from ..models.workflows_index_invocations_param_limit import WorkflowsIndexInvocationsParamLimit
from ..models.workflows_index_invocations_param_offset import WorkflowsIndexInvocationsParamOffset
from ..models.workflows_index_invocations_param_run_as import WorkflowsIndexInvocationsParamRunAs
from ..models.workflows_index_invocations_param_sort_by import WorkflowsIndexInvocationsParamSortBy
from ..models.workflows_index_invocations_param_user_id import WorkflowsIndexInvocationsParamUserId
from ..models.workflows_index_invocations_param_view import WorkflowsIndexInvocationsParamView
from ..models.workflows_index_invocations_param_workflow_id import WorkflowsIndexInvocationsParamWorkflowId
from ..models.workflows_index_param_limit import WorkflowsIndexParamLimit
from ..models.workflows_index_param_offset import WorkflowsIndexParamOffset
from ..models.workflows_index_param_run_as import WorkflowsIndexParamRunAs
from ..models.workflows_index_param_search import WorkflowsIndexParamSearch
from ..models.workflows_index_param_show_published import WorkflowsIndexParamShowPublished
from ..models.workflows_index_param_show_shared import WorkflowsIndexParamShowShared
from ..models.workflows_index_param_sort_by import WorkflowsIndexParamSortBy
from ..models.workflows_index_param_sort_desc import WorkflowsIndexParamSortDesc
from ..models.workflows_invocation_counts_param_instance import WorkflowsInvocationCountsParamInstance
from ..models.workflows_invocation_counts_param_run_as import WorkflowsInvocationCountsParamRunAs
from ..models.workflows_invocations_cancel_workflow_invocation_param_run_as import (
    WorkflowsInvocationsCancelWorkflowInvocationParamRunAs,
)
from ..models.workflows_invocations_index_workflow_invocations_param_history_id import (
    WorkflowsInvocationsIndexWorkflowInvocationsParamHistoryId,
)
from ..models.workflows_invocations_index_workflow_invocations_param_include_terminal import (
    WorkflowsInvocationsIndexWorkflowInvocationsParamIncludeTerminal,
)
from ..models.workflows_invocations_index_workflow_invocations_param_instance import (
    WorkflowsInvocationsIndexWorkflowInvocationsParamInstance,
)
from ..models.workflows_invocations_index_workflow_invocations_param_job_id import (
    WorkflowsInvocationsIndexWorkflowInvocationsParamJobId,
)
from ..models.workflows_invocations_index_workflow_invocations_param_limit import (
    WorkflowsInvocationsIndexWorkflowInvocationsParamLimit,
)
from ..models.workflows_invocations_index_workflow_invocations_param_offset import (
    WorkflowsInvocationsIndexWorkflowInvocationsParamOffset,
)
from ..models.workflows_invocations_index_workflow_invocations_param_run_as import (
    WorkflowsInvocationsIndexWorkflowInvocationsParamRunAs,
)
from ..models.workflows_invocations_index_workflow_invocations_param_sort_by import (
    WorkflowsInvocationsIndexWorkflowInvocationsParamSortBy,
)
from ..models.workflows_invocations_index_workflow_invocations_param_user_id import (
    WorkflowsInvocationsIndexWorkflowInvocationsParamUserId,
)
from ..models.workflows_invocations_index_workflow_invocations_param_view import (
    WorkflowsInvocationsIndexWorkflowInvocationsParamView,
)
from ..models.workflows_invocations_invoke_200_response_2 import WorkflowsInvocationsInvoke200Response2
from ..models.workflows_invocations_invoke_param_run_as import WorkflowsInvocationsInvokeParamRunAs
from ..models.workflows_invocations_invoke_param_workflow_id import WorkflowsInvocationsInvokeParamWorkflowId
from ..models.workflows_invocations_jobs_summary_workflow_invocation_jobs_summary_param_run_as import (
    WorkflowsInvocationsJobsSummaryWorkflowInvocationJobsSummaryParamRunAs,
)
from ..models.workflows_invocations_report_pdf_show_workflow_invocation_report_pdf_param_run_as import (
    WorkflowsInvocationsReportPdfShowWorkflowInvocationReportPdfParamRunAs,
)
from ..models.workflows_invocations_report_show_workflow_invocation_report_param_run_as import (
    WorkflowsInvocationsReportShowWorkflowInvocationReportParamRunAs,
)
from ..models.workflows_invocations_show_workflow_invocation_param_run_as import (
    WorkflowsInvocationsShowWorkflowInvocationParamRunAs,
)
from ..models.workflows_invocations_step_jobs_summary_workflow_invocation_step_jobs_summary_param_run_as import (
    WorkflowsInvocationsStepJobsSummaryWorkflowInvocationStepJobsSummaryParamRunAs,
)
from ..models.workflows_invocations_steps_update_workflow_invocation_step_param_run_as import (
    WorkflowsInvocationsStepsUpdateWorkflowInvocationStepParamRunAs,
)
from ..models.workflows_invocations_steps_workflow_invocation_step_param_run_as import (
    WorkflowsInvocationsStepsWorkflowInvocationStepParamRunAs,
)
from ..models.workflows_jobs_summary_invocation_jobs_summary_param_run_as import (
    WorkflowsJobsSummaryInvocationJobsSummaryParamRunAs,
)
from ..models.workflows_menu_get_workflow_menu_param_missing_tools import WorkflowsMenuGetWorkflowMenuParamMissingTools
from ..models.workflows_menu_get_workflow_menu_param_run_as import WorkflowsMenuGetWorkflowMenuParamRunAs
from ..models.workflows_menu_get_workflow_menu_param_show_deleted import WorkflowsMenuGetWorkflowMenuParamShowDeleted
from ..models.workflows_menu_get_workflow_menu_param_show_hidden import WorkflowsMenuGetWorkflowMenuParamShowHidden
from ..models.workflows_menu_get_workflow_menu_param_show_published import (
    WorkflowsMenuGetWorkflowMenuParamShowPublished,
)
from ..models.workflows_menu_get_workflow_menu_param_show_shared import WorkflowsMenuGetWorkflowMenuParamShowShared
from ..models.workflows_metrics_get_invocation_metrics_param_run_as import (
    WorkflowsMetricsGetInvocationMetricsParamRunAs,
)
from ..models.workflows_prepare_store_download_prepare_store_download_param_run_as import (
    WorkflowsPrepareStoreDownloadPrepareStoreDownloadParamRunAs,
)
from ..models.workflows_publish_publish_param_run_as import WorkflowsPublishPublishParamRunAs
from ..models.workflows_refactor_refactor_param_instance import WorkflowsRefactorRefactorParamInstance
from ..models.workflows_refactor_refactor_param_run_as import WorkflowsRefactorRefactorParamRunAs
from ..models.workflows_report_pdf_show_invocation_report_pdf_param_run_as import (
    WorkflowsReportPdfShowInvocationReportPdfParamRunAs,
)
from ..models.workflows_report_show_invocation_report_param_run_as import WorkflowsReportShowInvocationReportParamRunAs
from ..models.workflows_request_invocation_as_request_param_run_as import WorkflowsRequestInvocationAsRequestParamRunAs
from ..models.workflows_share_with_users_share_with_users_param_run_as import (
    WorkflowsShareWithUsersShareWithUsersParamRunAs,
)
from ..models.workflows_sharing_sharing_param_run_as import WorkflowsSharingSharingParamRunAs
from ..models.workflows_show_invocation_param_run_as import WorkflowsShowInvocationParamRunAs
from ..models.workflows_show_workflow_param_instance import WorkflowsShowWorkflowParamInstance
from ..models.workflows_show_workflow_param_legacy import WorkflowsShowWorkflowParamLegacy
from ..models.workflows_show_workflow_param_run_as import WorkflowsShowWorkflowParamRunAs
from ..models.workflows_show_workflow_param_version import WorkflowsShowWorkflowParamVersion
from ..models.workflows_slug_set_slug_param_run_as import WorkflowsSlugSetSlugParamRunAs
from ..models.workflows_step_jobs_summary_invocation_step_jobs_summary_param_run_as import (
    WorkflowsStepJobsSummaryInvocationStepJobsSummaryParamRunAs,
)
from ..models.workflows_steps_invocation_step_param_run_as import WorkflowsStepsInvocationStepParamRunAs
from ..models.workflows_steps_step_param_run_as import WorkflowsStepsStepParamRunAs
from ..models.workflows_steps_update_invocation_step_param_run_as import WorkflowsStepsUpdateInvocationStepParamRunAs
from ..models.workflows_tags_create_param_run_as import WorkflowsTagsCreateParamRunAs
from ..models.workflows_tags_delete_param_run_as import WorkflowsTagsDeleteParamRunAs
from ..models.workflows_tags_index_param_run_as import WorkflowsTagsIndexParamRunAs
from ..models.workflows_tags_show_param_run_as import WorkflowsTagsShowParamRunAs
from ..models.workflows_tags_update_param_run_as import WorkflowsTagsUpdateParamRunAs
from ..models.workflows_undelete_undelete_workflow_param_run_as import WorkflowsUndeleteUndeleteWorkflowParamRunAs
from ..models.workflows_unpublish_unpublish_param_run_as import WorkflowsUnpublishUnpublishParamRunAs
from ..models.workflows_usage_cancel_workflow_invocation_param_run_as import (
    WorkflowsUsageCancelWorkflowInvocationParamRunAs,
)
from ..models.workflows_usage_index_workflow_invocations_param_history_id import (
    WorkflowsUsageIndexWorkflowInvocationsParamHistoryId,
)
from ..models.workflows_usage_index_workflow_invocations_param_include_terminal import (
    WorkflowsUsageIndexWorkflowInvocationsParamIncludeTerminal,
)
from ..models.workflows_usage_index_workflow_invocations_param_instance import (
    WorkflowsUsageIndexWorkflowInvocationsParamInstance,
)
from ..models.workflows_usage_index_workflow_invocations_param_job_id import (
    WorkflowsUsageIndexWorkflowInvocationsParamJobId,
)
from ..models.workflows_usage_index_workflow_invocations_param_limit import (
    WorkflowsUsageIndexWorkflowInvocationsParamLimit,
)
from ..models.workflows_usage_index_workflow_invocations_param_offset import (
    WorkflowsUsageIndexWorkflowInvocationsParamOffset,
)
from ..models.workflows_usage_index_workflow_invocations_param_run_as import (
    WorkflowsUsageIndexWorkflowInvocationsParamRunAs,
)
from ..models.workflows_usage_index_workflow_invocations_param_sort_by import (
    WorkflowsUsageIndexWorkflowInvocationsParamSortBy,
)
from ..models.workflows_usage_index_workflow_invocations_param_user_id import (
    WorkflowsUsageIndexWorkflowInvocationsParamUserId,
)
from ..models.workflows_usage_index_workflow_invocations_param_view import (
    WorkflowsUsageIndexWorkflowInvocationsParamView,
)
from ..models.workflows_usage_invoke_200_response_2 import WorkflowsUsageInvoke200Response2
from ..models.workflows_usage_invoke_param_run_as import WorkflowsUsageInvokeParamRunAs
from ..models.workflows_usage_invoke_param_workflow_id import WorkflowsUsageInvokeParamWorkflowId
from ..models.workflows_usage_jobs_summary_workflow_invocation_jobs_summary_param_run_as import (
    WorkflowsUsageJobsSummaryWorkflowInvocationJobsSummaryParamRunAs,
)
from ..models.workflows_usage_report_pdf_show_workflow_invocation_report_pdf_param_run_as import (
    WorkflowsUsageReportPdfShowWorkflowInvocationReportPdfParamRunAs,
)
from ..models.workflows_usage_report_show_workflow_invocation_report_param_run_as import (
    WorkflowsUsageReportShowWorkflowInvocationReportParamRunAs,
)
from ..models.workflows_usage_show_workflow_invocation_param_run_as import (
    WorkflowsUsageShowWorkflowInvocationParamRunAs,
)
from ..models.workflows_usage_step_jobs_summary_workflow_invocation_step_jobs_summary_param_run_as import (
    WorkflowsUsageStepJobsSummaryWorkflowInvocationStepJobsSummaryParamRunAs,
)
from ..models.workflows_usage_steps_update_workflow_invocation_step_param_run_as import (
    WorkflowsUsageStepsUpdateWorkflowInvocationStepParamRunAs,
)
from ..models.workflows_usage_steps_workflow_invocation_step_param_run_as import (
    WorkflowsUsageStepsWorkflowInvocationStepParamRunAs,
)
from ..models.workflows_versions_show_versions_param_instance import WorkflowsVersionsShowVersionsParamInstance
from ..models.workflows_versions_show_versions_param_run_as import WorkflowsVersionsShowVersionsParamRunAs
from ..models.workflows_write_store_write_store_param_run_as import WorkflowsWriteStoreWriteStoreParamRunAs
from ..models.write_invocation_store_to_payload import WriteInvocationStoreToPayload


class WorkflowsClient:
    """Client for workflows endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def workflows_index_invocations_2_2(
        self,
        workflow_id: WorkflowsIndexInvocationsParamWorkflowId | None = None,
        history_id: WorkflowsIndexInvocationsParamHistoryId | None = None,
        job_id: WorkflowsIndexInvocationsParamJobId | None = None,
        user_id: WorkflowsIndexInvocationsParamUserId | None = None,
        sort_by: WorkflowsIndexInvocationsParamSortBy | None = None,
        sort_desc: bool | None = False,
        include_terminal: WorkflowsIndexInvocationsParamIncludeTerminal | None = True,
        limit: WorkflowsIndexInvocationsParamLimit | None = 20,
        offset: WorkflowsIndexInvocationsParamOffset | None = None,
        instance: WorkflowsIndexInvocationsParamInstance | None = False,
        view: WorkflowsIndexInvocationsParamView | None = None,
        step_details: bool | None = False,
        include_nested_invocations: bool | None = True,
        run_as: WorkflowsIndexInvocationsParamRunAs | None = None,
    ) -> list[WorkflowInvocationResponse]:
        """
        Get the list of a user's workflow invocations.

        Args:
            workflow_id (Optional[WorkflowsIndexInvocationsParamWorkflowId])
                                     : Return only invocations for this Workflow ID
            history_id (Optional[WorkflowsIndexInvocationsParamHistoryId])
                                     : Return only invocations for this History ID
            job_id (Optional[WorkflowsIndexInvocationsParamJobId])
                                     : Return only invocations for this Job ID
            user_id (Optional[WorkflowsIndexInvocationsParamUserId])
                                     : Return invocations for this User ID.
            sort_by (Optional[WorkflowsIndexInvocationsParamSortBy])
                                     : Sort Workflow Invocations by this attribute
            sort_desc (Optional[bool]): Sort in descending order?
            include_terminal (Optional[WorkflowsIndexInvocationsParamIncludeTerminal])
                                     : Set to false to only include terminal Invocations.
            limit (Optional[WorkflowsIndexInvocationsParamLimit])
                                     : Limit the number of invocations to return.
            offset (Optional[WorkflowsIndexInvocationsParamOffset])
                                     : Number of invocations to skip.
            instance (Optional[WorkflowsIndexInvocationsParamInstance])
                                     : Is provided workflow id for Workflow instead of
                                       StoredWorkflow?
            view (Optional[WorkflowsIndexInvocationsParamView])
                                     : View to be passed to the serializer
            step_details (Optional[bool])
                                     : Include details for individual invocation steps and
                                       populate a steps attribute in the resulting dictionary.
            include_nested_invocations (Optional[bool])
                                     :
            run-as (Optional[WorkflowsIndexInvocationsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[WorkflowInvocationResponse]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/invocations"

        params: dict[str, Any] = {
            **({"workflow_id": workflow_id} if workflow_id is not None else {}),
            **({"history_id": history_id} if history_id is not None else {}),
            **({"job_id": job_id} if job_id is not None else {}),
            **({"user_id": user_id} if user_id is not None else {}),
            **({"sort_by": sort_by} if sort_by is not None else {}),
            **({"sort_desc": sort_desc} if sort_desc is not None else {}),
            **({"include_terminal": include_terminal} if include_terminal is not None else {}),
            **({"limit": limit} if limit is not None else {}),
            **({"offset": offset} if offset is not None else {}),
            **({"instance": instance} if instance is not None else {}),
            **({"view": view} if view is not None else {}),
            **({"step_details": step_details} if step_details is not None else {}),
            **(
                {"include_nested_invocations": include_nested_invocations}
                if include_nested_invocations is not None
                else {}
            ),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[WorkflowInvocationResponse], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_index_invocations_2_2(
        self,
        workflow_id: WorkflowsIndexInvocationsParamWorkflowId | None = None,
        history_id: WorkflowsIndexInvocationsParamHistoryId | None = None,
        job_id: WorkflowsIndexInvocationsParamJobId | None = None,
        user_id: WorkflowsIndexInvocationsParamUserId | None = None,
        sort_by: WorkflowsIndexInvocationsParamSortBy | None = None,
        sort_desc: bool | None = False,
        include_terminal: WorkflowsIndexInvocationsParamIncludeTerminal | None = True,
        limit: WorkflowsIndexInvocationsParamLimit | None = 20,
        offset: WorkflowsIndexInvocationsParamOffset | None = None,
        instance: WorkflowsIndexInvocationsParamInstance | None = False,
        view: WorkflowsIndexInvocationsParamView | None = None,
        step_details: bool | None = False,
        include_nested_invocations: bool | None = True,
        run_as: WorkflowsIndexInvocationsParamRunAs | None = None,
    ) -> list[WorkflowInvocationResponse]:
        """
        Get the list of a user's workflow invocations.

        Args:
            workflow_id (Optional[WorkflowsIndexInvocationsParamWorkflowId])
                                     : Return only invocations for this Workflow ID
            history_id (Optional[WorkflowsIndexInvocationsParamHistoryId])
                                     : Return only invocations for this History ID
            job_id (Optional[WorkflowsIndexInvocationsParamJobId])
                                     : Return only invocations for this Job ID
            user_id (Optional[WorkflowsIndexInvocationsParamUserId])
                                     : Return invocations for this User ID.
            sort_by (Optional[WorkflowsIndexInvocationsParamSortBy])
                                     : Sort Workflow Invocations by this attribute
            sort_desc (Optional[bool]): Sort in descending order?
            include_terminal (Optional[WorkflowsIndexInvocationsParamIncludeTerminal])
                                     : Set to false to only include terminal Invocations.
            limit (Optional[WorkflowsIndexInvocationsParamLimit])
                                     : Limit the number of invocations to return.
            offset (Optional[WorkflowsIndexInvocationsParamOffset])
                                     : Number of invocations to skip.
            instance (Optional[WorkflowsIndexInvocationsParamInstance])
                                     : Is provided workflow id for Workflow instead of
                                       StoredWorkflow?
            view (Optional[WorkflowsIndexInvocationsParamView])
                                     : View to be passed to the serializer
            step_details (Optional[bool])
                                     : Include details for individual invocation steps and
                                       populate a steps attribute in the resulting dictionary.
            include_nested_invocations (Optional[bool])
                                     :
            run-as (Optional[WorkflowsIndexInvocationsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[WorkflowInvocationResponse]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/invocations"

        params: dict[str, Any] = {
            **({"workflow_id": workflow_id} if workflow_id is not None else {}),
            **({"history_id": history_id} if history_id is not None else {}),
            **({"job_id": job_id} if job_id is not None else {}),
            **({"user_id": user_id} if user_id is not None else {}),
            **({"sort_by": sort_by} if sort_by is not None else {}),
            **({"sort_desc": sort_desc} if sort_desc is not None else {}),
            **({"include_terminal": include_terminal} if include_terminal is not None else {}),
            **({"limit": limit} if limit is not None else {}),
            **({"offset": offset} if offset is not None else {}),
            **({"instance": instance} if instance is not None else {}),
            **({"view": view} if view is not None else {}),
            **({"step_details": step_details} if step_details is not None else {}),
            **(
                {"include_nested_invocations": include_nested_invocations}
                if include_nested_invocations is not None
                else {}
            ),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[WorkflowInvocationResponse], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_from_store_create_invocations_from_store_2_2(
        self,
        body: CreateInvocationsFromStorePayload,
        run_as: WorkflowsFromStoreCreateInvocationsFromStoreParamRunAs | None = None,
    ) -> list[WorkflowInvocationResponse]:
        """
        Create Invocations From Store

        Create invocation(s) from a supplied model store.

        Args:
            run-as (Optional[WorkflowsFromStoreCreateInvocationsFromStoreParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateInvocationsFromStorePayload)
                                     : Request body. (json)

        Returns:
            List[WorkflowInvocationResponse]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/invocations/from_store"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateInvocationsFromStorePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[WorkflowInvocationResponse], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_from_store_create_invocations_from_store_2_2(
        self,
        body: CreateInvocationsFromStorePayload,
        run_as: WorkflowsFromStoreCreateInvocationsFromStoreParamRunAs | None = None,
    ) -> list[WorkflowInvocationResponse]:
        """
        Create Invocations From Store

        Create invocation(s) from a supplied model store.

        Args:
            run-as (Optional[WorkflowsFromStoreCreateInvocationsFromStoreParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateInvocationsFromStorePayload)
                                     : Request body. (json)

        Returns:
            List[WorkflowInvocationResponse]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/invocations/from_store"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateInvocationsFromStorePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[WorkflowInvocationResponse], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_steps_step_2_2(
        self,
        step_id: str,
        run_as: WorkflowsStepsStepParamRunAs | None = None,
    ) -> InvocationStep:
        """
        Show details of workflow invocation step.

        Args:
            step_id (str)            : The encoded database identifier of the
                                       WorkflowInvocationStep.
            run-as (Optional[WorkflowsStepsStepParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            InvocationStep: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/invocations/steps/{step_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(InvocationStep, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_steps_step_2_2(
        self,
        step_id: str,
        run_as: WorkflowsStepsStepParamRunAs | None = None,
    ) -> InvocationStep:
        """
        Show details of workflow invocation step.

        Args:
            step_id (str)            : The encoded database identifier of the
                                       WorkflowInvocationStep.
            run-as (Optional[WorkflowsStepsStepParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            InvocationStep: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/invocations/steps/{step_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(InvocationStep, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_cancel_invocation_2_2(
        self,
        invocation_id: str,
        step_details: bool | None = False,
        legacy_job_state: bool | None = False,
        run_as: WorkflowsCancelInvocationParamRunAs | None = None,
    ) -> WorkflowInvocationResponse:
        """
        Cancel the specified workflow invocation.

        Args:
            invocation_id (str)      : The encoded database identifier of the Invocation.
            step_details (Optional[bool])
                                     : Include details for individual invocation steps and
                                       populate a steps attribute in the resulting dictionary.
            legacy_job_state (Optional[bool])
                                     : Populate the invocation step state with the job state
                                       instead of the invocation step state.         This will
                                       also produce one step per job in mapping jobs to mimic
                                       the older behavior with respect to collections.
                                       Partially scheduled steps may provide incomplete
                                       information and the listed steps outputs         are not
                                       the mapped over step outputs but the individual job
                                       outputs.
            run-as (Optional[WorkflowsCancelInvocationParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            WorkflowInvocationResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/invocations/{invocation_id}"

        params: dict[str, Any] = {
            **({"step_details": step_details} if step_details is not None else {}),
            **({"legacy_job_state": legacy_job_state} if legacy_job_state is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(WorkflowInvocationResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_cancel_invocation_2_2(
        self,
        invocation_id: str,
        step_details: bool | None = False,
        legacy_job_state: bool | None = False,
        run_as: WorkflowsCancelInvocationParamRunAs | None = None,
    ) -> WorkflowInvocationResponse:
        """
        Cancel the specified workflow invocation.

        Args:
            invocation_id (str)      : The encoded database identifier of the Invocation.
            step_details (Optional[bool])
                                     : Include details for individual invocation steps and
                                       populate a steps attribute in the resulting dictionary.
            legacy_job_state (Optional[bool])
                                     : Populate the invocation step state with the job state
                                       instead of the invocation step state.         This will
                                       also produce one step per job in mapping jobs to mimic
                                       the older behavior with respect to collections.
                                       Partially scheduled steps may provide incomplete
                                       information and the listed steps outputs         are not
                                       the mapped over step outputs but the individual job
                                       outputs.
            run-as (Optional[WorkflowsCancelInvocationParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            WorkflowInvocationResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/invocations/{invocation_id}"

        params: dict[str, Any] = {
            **({"step_details": step_details} if step_details is not None else {}),
            **({"legacy_job_state": legacy_job_state} if legacy_job_state is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(WorkflowInvocationResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_show_invocation_2_2(
        self,
        invocation_id: str,
        step_details: bool | None = False,
        legacy_job_state: bool | None = False,
        run_as: WorkflowsShowInvocationParamRunAs | None = None,
    ) -> WorkflowInvocationResponse:
        """
        Get detailed description of a workflow invocation.

        Args:
            invocation_id (str)      : The encoded database identifier of the Invocation.
            step_details (Optional[bool])
                                     : Include details for individual invocation steps and
                                       populate a steps attribute in the resulting dictionary.
            legacy_job_state (Optional[bool])
                                     : Populate the invocation step state with the job state
                                       instead of the invocation step state.         This will
                                       also produce one step per job in mapping jobs to mimic
                                       the older behavior with respect to collections.
                                       Partially scheduled steps may provide incomplete
                                       information and the listed steps outputs         are not
                                       the mapped over step outputs but the individual job
                                       outputs.
            run-as (Optional[WorkflowsShowInvocationParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            WorkflowInvocationResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/invocations/{invocation_id}"

        params: dict[str, Any] = {
            **({"step_details": step_details} if step_details is not None else {}),
            **({"legacy_job_state": legacy_job_state} if legacy_job_state is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(WorkflowInvocationResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_show_invocation_2_2(
        self,
        invocation_id: str,
        step_details: bool | None = False,
        legacy_job_state: bool | None = False,
        run_as: WorkflowsShowInvocationParamRunAs | None = None,
    ) -> WorkflowInvocationResponse:
        """
        Get detailed description of a workflow invocation.

        Args:
            invocation_id (str)      : The encoded database identifier of the Invocation.
            step_details (Optional[bool])
                                     : Include details for individual invocation steps and
                                       populate a steps attribute in the resulting dictionary.
            legacy_job_state (Optional[bool])
                                     : Populate the invocation step state with the job state
                                       instead of the invocation step state.         This will
                                       also produce one step per job in mapping jobs to mimic
                                       the older behavior with respect to collections.
                                       Partially scheduled steps may provide incomplete
                                       information and the listed steps outputs         are not
                                       the mapped over step outputs but the individual job
                                       outputs.
            run-as (Optional[WorkflowsShowInvocationParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            WorkflowInvocationResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/invocations/{invocation_id}"

        params: dict[str, Any] = {
            **({"step_details": step_details} if step_details is not None else {}),
            **({"legacy_job_state": legacy_job_state} if legacy_job_state is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(WorkflowInvocationResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_error_report_error_2_2(
        self,
        invocation_id: str,
        body: ReportInvocationErrorPayload,
        run_as: WorkflowsErrorReportErrorParamRunAs | None = None,
    ) -> None:
        """
        Submits a bug report for a workflow run via the API.

        Args:
            invocation_id (str)      : The encoded database identifier of the Invocation.
            run-as (Optional[WorkflowsErrorReportErrorParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (ReportInvocationErrorPayload)
                                     : Request body. (json)

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/invocations/{invocation_id}/error"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: ReportInvocationErrorPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_error_report_error_2_2(
        self,
        invocation_id: str,
        body: ReportInvocationErrorPayload,
        run_as: WorkflowsErrorReportErrorParamRunAs | None = None,
    ) -> None:
        """
        Submits a bug report for a workflow run via the API.

        Args:
            invocation_id (str)      : The encoded database identifier of the Invocation.
            run-as (Optional[WorkflowsErrorReportErrorParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (ReportInvocationErrorPayload)
                                     : Request body. (json)

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/invocations/{invocation_id}/error"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: ReportInvocationErrorPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 204:
                return None
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_jobs_summary_invocation_jobs_summary_2_2(
        self,
        invocation_id: str,
        run_as: WorkflowsJobsSummaryInvocationJobsSummaryParamRunAs | None = None,
    ) -> InvocationJobsResponse:
        """
        Get job state summary info aggregated across all current jobs of the workflow
        invocation.

        Warning: We allow anyone to fetch job state information about any object they can guess
        an encoded ID for - it isn't considered protected data. This keeps polling IDs as part
        of state calculation for large histories and collections as efficient as possible.

        Args:
            invocation_id (str)      : The encoded database identifier of the Invocation.
            run-as (Optional[WorkflowsJobsSummaryInvocationJobsSummaryParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            InvocationJobsResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/invocations/{invocation_id}/jobs_summary"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(InvocationJobsResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_jobs_summary_invocation_jobs_summary_2_2(
        self,
        invocation_id: str,
        run_as: WorkflowsJobsSummaryInvocationJobsSummaryParamRunAs | None = None,
    ) -> InvocationJobsResponse:
        """
        Get job state summary info aggregated across all current jobs of the workflow
        invocation.

        Warning: We allow anyone to fetch job state information about any object they can guess
        an encoded ID for - it isn't considered protected data. This keeps polling IDs as part
        of state calculation for large histories and collections as efficient as possible.

        Args:
            invocation_id (str)      : The encoded database identifier of the Invocation.
            run-as (Optional[WorkflowsJobsSummaryInvocationJobsSummaryParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            InvocationJobsResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/invocations/{invocation_id}/jobs_summary"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(InvocationJobsResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_metrics_get_invocation_metrics_2_2(
        self,
        invocation_id: str,
        run_as: WorkflowsMetricsGetInvocationMetricsParamRunAs | None = None,
    ) -> list[WorkflowJobMetric]:
        """
        Get Invocation Metrics

        Args:
            invocation_id (str)      : The encoded database identifier of the Invocation.
            run-as (Optional[WorkflowsMetricsGetInvocationMetricsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[WorkflowJobMetric]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/invocations/{invocation_id}/metrics"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[WorkflowJobMetric], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_metrics_get_invocation_metrics_2_2(
        self,
        invocation_id: str,
        run_as: WorkflowsMetricsGetInvocationMetricsParamRunAs | None = None,
    ) -> list[WorkflowJobMetric]:
        """
        Get Invocation Metrics

        Args:
            invocation_id (str)      : The encoded database identifier of the Invocation.
            run-as (Optional[WorkflowsMetricsGetInvocationMetricsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[WorkflowJobMetric]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/invocations/{invocation_id}/metrics"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[WorkflowJobMetric], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_prepare_store_download_prepare_store_download_2_2(
        self,
        invocation_id: str,
        body: PrepareStoreDownloadPayload,
        run_as: WorkflowsPrepareStoreDownloadPrepareStoreDownloadParamRunAs | None = None,
    ) -> AsyncFile:
        """
        Prepare a workflow invocation export-style download.

        Args:
            invocation_id (str)      : The encoded database identifier of the Invocation.
            run-as (Optional[WorkflowsPrepareStoreDownloadPrepareStoreDownloadParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (PrepareStoreDownloadPayload)
                                     : Request body. (json)

        Returns:
            AsyncFile: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/invocations/{invocation_id}/prepare_store_download"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: PrepareStoreDownloadPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(AsyncFile, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_prepare_store_download_prepare_store_download_2_2(
        self,
        invocation_id: str,
        body: PrepareStoreDownloadPayload,
        run_as: WorkflowsPrepareStoreDownloadPrepareStoreDownloadParamRunAs | None = None,
    ) -> AsyncFile:
        """
        Prepare a workflow invocation export-style download.

        Args:
            invocation_id (str)      : The encoded database identifier of the Invocation.
            run-as (Optional[WorkflowsPrepareStoreDownloadPrepareStoreDownloadParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (PrepareStoreDownloadPayload)
                                     : Request body. (json)

        Returns:
            AsyncFile: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/invocations/{invocation_id}/prepare_store_download"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: PrepareStoreDownloadPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(AsyncFile, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_report_show_invocation_report_2_2(
        self,
        invocation_id: str,
        run_as: WorkflowsReportShowInvocationReportParamRunAs | None = None,
    ) -> InvocationReport:
        """
        Get JSON summarizing invocation for reporting.

        Args:
            invocation_id (str)      : The encoded database identifier of the Invocation.
            run-as (Optional[WorkflowsReportShowInvocationReportParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            InvocationReport: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/invocations/{invocation_id}/report"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(InvocationReport, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_report_show_invocation_report_2_2(
        self,
        invocation_id: str,
        run_as: WorkflowsReportShowInvocationReportParamRunAs | None = None,
    ) -> InvocationReport:
        """
        Get JSON summarizing invocation for reporting.

        Args:
            invocation_id (str)      : The encoded database identifier of the Invocation.
            run-as (Optional[WorkflowsReportShowInvocationReportParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            InvocationReport: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/invocations/{invocation_id}/report"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(InvocationReport, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_report_pdf_show_invocation_report_pdf_2_2(
        self,
        invocation_id: str,
        run_as: WorkflowsReportPdfShowInvocationReportPdfParamRunAs | None = None,
    ) -> None:
        """
        Get PDF summarizing invocation for reporting.

        Args:
            invocation_id (str)      : The encoded database identifier of the Invocation.
            run-as (Optional[WorkflowsReportPdfShowInvocationReportPdfParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/invocations/{invocation_id}/report.pdf"

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

    async def workflows_report_pdf_show_invocation_report_pdf_2_2(
        self,
        invocation_id: str,
        run_as: WorkflowsReportPdfShowInvocationReportPdfParamRunAs | None = None,
    ) -> None:
        """
        Get PDF summarizing invocation for reporting.

        Args:
            invocation_id (str)      : The encoded database identifier of the Invocation.
            run-as (Optional[WorkflowsReportPdfShowInvocationReportPdfParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/invocations/{invocation_id}/report.pdf"

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

    async def workflows_request_invocation_as_request_2_2(
        self,
        invocation_id: str,
        run_as: WorkflowsRequestInvocationAsRequestParamRunAs | None = None,
    ) -> WorkflowInvocationRequestModel:
        """
        Get a description modeling an API request to invoke this workflow - this is recreated
        and will be more specific in some ways than the initial creation request.

        Args:
            invocation_id (str)      : The encoded database identifier of the Invocation.
            run-as (Optional[WorkflowsRequestInvocationAsRequestParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            WorkflowInvocationRequestModel: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/invocations/{invocation_id}/request"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(WorkflowInvocationRequestModel, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_request_invocation_as_request_2_2(
        self,
        invocation_id: str,
        run_as: WorkflowsRequestInvocationAsRequestParamRunAs | None = None,
    ) -> WorkflowInvocationRequestModel:
        """
        Get a description modeling an API request to invoke this workflow - this is recreated
        and will be more specific in some ways than the initial creation request.

        Args:
            invocation_id (str)      : The encoded database identifier of the Invocation.
            run-as (Optional[WorkflowsRequestInvocationAsRequestParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            WorkflowInvocationRequestModel: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/invocations/{invocation_id}/request"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(WorkflowInvocationRequestModel, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_step_jobs_summary_invocation_step_jobs_summary_2_2(
        self,
        invocation_id: str,
        run_as: WorkflowsStepJobsSummaryInvocationStepJobsSummaryParamRunAs | None = None,
    ) -> list[AnonymousArrayItem202]:
        """
        Get job state summary info aggregated per step of the workflow invocation.

        Warning: We allow anyone to fetch job state information about any object they can guess
        an encoded ID for - it isn't considered protected data. This keeps polling IDs as part
        of state calculation for large histories and collections as efficient as possible.

        Args:
            invocation_id (str)      : The encoded database identifier of the Invocation.
            run-as (Optional[WorkflowsStepJobsSummaryInvocationStepJobsSummaryParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem202]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/invocations/{invocation_id}/step_jobs_summary"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem202], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_step_jobs_summary_invocation_step_jobs_summary_2_2(
        self,
        invocation_id: str,
        run_as: WorkflowsStepJobsSummaryInvocationStepJobsSummaryParamRunAs | None = None,
    ) -> list[AnonymousArrayItem202]:
        """
        Get job state summary info aggregated per step of the workflow invocation.

        Warning: We allow anyone to fetch job state information about any object they can guess
        an encoded ID for - it isn't considered protected data. This keeps polling IDs as part
        of state calculation for large histories and collections as efficient as possible.

        Args:
            invocation_id (str)      : The encoded database identifier of the Invocation.
            run-as (Optional[WorkflowsStepJobsSummaryInvocationStepJobsSummaryParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem202]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/invocations/{invocation_id}/step_jobs_summary"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem202], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_steps_invocation_step_2_2(
        self,
        invocation_id: str,
        step_id: str,
        run_as: WorkflowsStepsInvocationStepParamRunAs | None = None,
    ) -> InvocationStep:
        """
        Show details of workflow invocation step.

        An alias for `GET /api/invocations/steps/{step_id}`. `invocation_id` is ignored.

        Args:
            invocation_id (str)      : The encoded database identifier of the Invocation.
            step_id (str)            : The encoded database identifier of the
                                       WorkflowInvocationStep.
            run-as (Optional[WorkflowsStepsInvocationStepParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            InvocationStep: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/invocations/{invocation_id}/steps/{step_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(InvocationStep, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_steps_invocation_step_2_2(
        self,
        invocation_id: str,
        step_id: str,
        run_as: WorkflowsStepsInvocationStepParamRunAs | None = None,
    ) -> InvocationStep:
        """
        Show details of workflow invocation step.

        An alias for `GET /api/invocations/steps/{step_id}`. `invocation_id` is ignored.

        Args:
            invocation_id (str)      : The encoded database identifier of the Invocation.
            step_id (str)            : The encoded database identifier of the
                                       WorkflowInvocationStep.
            run-as (Optional[WorkflowsStepsInvocationStepParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            InvocationStep: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/invocations/{invocation_id}/steps/{step_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(InvocationStep, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_steps_update_invocation_step_2_2(
        self,
        invocation_id: str,
        step_id: str,
        body: InvocationUpdatePayload,
        run_as: WorkflowsStepsUpdateInvocationStepParamRunAs | None = None,
    ) -> InvocationStep:
        """
        Update state of running workflow step invocation - still very nebulous but this would be
        for stuff like confirming paused steps can proceed etc.

        Args:
            invocation_id (str)      : The encoded database identifier of the Invocation.
            step_id (str)            : The encoded database identifier of the
                                       WorkflowInvocationStep.
            run-as (Optional[WorkflowsStepsUpdateInvocationStepParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (InvocationUpdatePayload)
                                     : Request body. (json)

        Returns:
            InvocationStep: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/invocations/{invocation_id}/steps/{step_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: InvocationUpdatePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(InvocationStep, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_steps_update_invocation_step_2_2(
        self,
        invocation_id: str,
        step_id: str,
        body: InvocationUpdatePayload,
        run_as: WorkflowsStepsUpdateInvocationStepParamRunAs | None = None,
    ) -> InvocationStep:
        """
        Update state of running workflow step invocation - still very nebulous but this would be
        for stuff like confirming paused steps can proceed etc.

        Args:
            invocation_id (str)      : The encoded database identifier of the Invocation.
            step_id (str)            : The encoded database identifier of the
                                       WorkflowInvocationStep.
            run-as (Optional[WorkflowsStepsUpdateInvocationStepParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (InvocationUpdatePayload)
                                     : Request body. (json)

        Returns:
            InvocationStep: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/invocations/{invocation_id}/steps/{step_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: InvocationUpdatePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(InvocationStep, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_write_store_write_store_2_2(
        self,
        invocation_id: str,
        body: WriteInvocationStoreToPayload,
        run_as: WorkflowsWriteStoreWriteStoreParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Prepare a workflow invocation export-style download and write to supplied URI.

        Args:
            invocation_id (str)      : The encoded database identifier of the Invocation.
            run-as (Optional[WorkflowsWriteStoreWriteStoreParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (WriteInvocationStoreToPayload)
                                     : Request body. (json)

        Returns:
            AsyncTaskResultSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/invocations/{invocation_id}/write_store"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: WriteInvocationStoreToPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(AsyncTaskResultSummary, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_write_store_write_store_2_2(
        self,
        invocation_id: str,
        body: WriteInvocationStoreToPayload,
        run_as: WorkflowsWriteStoreWriteStoreParamRunAs | None = None,
    ) -> AsyncTaskResultSummary:
        """
        Prepare a workflow invocation export-style download and write to supplied URI.

        Args:
            invocation_id (str)      : The encoded database identifier of the Invocation.
            run-as (Optional[WorkflowsWriteStoreWriteStoreParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (WriteInvocationStoreToPayload)
                                     : Request body. (json)

        Returns:
            AsyncTaskResultSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/invocations/{invocation_id}/write_store"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: WriteInvocationStoreToPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(AsyncTaskResultSummary, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_create_landing_2_2(
        self,
        body: CreateWorkflowLandingRequestPayload,
        run_as: WorkflowsCreateLandingParamRunAs | None = None,
    ) -> WorkflowLandingRequest:
        """
        Create Landing

        Args:
            run-as (Optional[WorkflowsCreateLandingParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateWorkflowLandingRequestPayload)
                                     : Request body. (json)

        Returns:
            WorkflowLandingRequest: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflow_landings"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateWorkflowLandingRequestPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(WorkflowLandingRequest, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_create_landing_2_2(
        self,
        body: CreateWorkflowLandingRequestPayload,
        run_as: WorkflowsCreateLandingParamRunAs | None = None,
    ) -> WorkflowLandingRequest:
        """
        Create Landing

        Args:
            run-as (Optional[WorkflowsCreateLandingParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateWorkflowLandingRequestPayload)
                                     : Request body. (json)

        Returns:
            WorkflowLandingRequest: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflow_landings"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateWorkflowLandingRequestPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(WorkflowLandingRequest, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_get_landing_2_2(
        self,
        uuid_: UUID,
        run_as: WorkflowsGetLandingParamRunAs | None = None,
    ) -> WorkflowLandingRequest:
        """
        Get Landing

        Args:
            uuid (UUID)              : The UUID used to identify a persisted landing request.
            run-as (Optional[WorkflowsGetLandingParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            WorkflowLandingRequest: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflow_landings/{uuid_}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(WorkflowLandingRequest, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_get_landing_2_2(
        self,
        uuid_: UUID,
        run_as: WorkflowsGetLandingParamRunAs | None = None,
    ) -> WorkflowLandingRequest:
        """
        Get Landing

        Args:
            uuid (UUID)              : The UUID used to identify a persisted landing request.
            run-as (Optional[WorkflowsGetLandingParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            WorkflowLandingRequest: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflow_landings/{uuid_}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(WorkflowLandingRequest, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_claim_claim_landing_2_2(
        self,
        uuid_: UUID,
        body: WorkflowsClaimClaimLandingRequestBody2 | None,
        run_as: WorkflowsClaimClaimLandingParamRunAs | None = None,
    ) -> WorkflowLandingRequest:
        """
        Claim Landing

        Args:
            uuid (UUID)              : The UUID used to identify a persisted landing request.
            run-as (Optional[WorkflowsClaimClaimLandingParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (Optional[WorkflowsClaimClaimLandingRequestBody2])
                                     : Request body. (json)

        Returns:
            WorkflowLandingRequest: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflow_landings/{uuid_}/claim"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: WorkflowsClaimClaimLandingRequestBody2 | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(WorkflowLandingRequest, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_claim_claim_landing_2_2(
        self,
        uuid_: UUID,
        body: WorkflowsClaimClaimLandingRequestBody2 | None,
        run_as: WorkflowsClaimClaimLandingParamRunAs | None = None,
    ) -> WorkflowLandingRequest:
        """
        Claim Landing

        Args:
            uuid (UUID)              : The UUID used to identify a persisted landing request.
            run-as (Optional[WorkflowsClaimClaimLandingParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (Optional[WorkflowsClaimClaimLandingRequestBody2])
                                     : Request body. (json)

        Returns:
            WorkflowLandingRequest: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflow_landings/{uuid_}/claim"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: WorkflowsClaimClaimLandingRequestBody2 | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(WorkflowLandingRequest, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_index_2_2(
        self,
        show_deleted: bool | None = False,
        show_hidden: bool | None = False,
        missing_tools: bool | None = False,
        show_published: WorkflowsIndexParamShowPublished | None = None,
        show_shared: WorkflowsIndexParamShowShared | None = None,
        sort_by: WorkflowsIndexParamSortBy | None = None,
        sort_desc: WorkflowsIndexParamSortDesc | None = None,
        limit: WorkflowsIndexParamLimit | None = None,
        offset: WorkflowsIndexParamOffset | None = 0,
        search: WorkflowsIndexParamSearch | None = None,
        skip_step_counts: bool | None = False,
        run_as: WorkflowsIndexParamRunAs | None = None,
    ) -> list[AnonymousArrayItem224]:
        """
        Lists stored workflows viewable by the user.

        Lists stored workflows viewable by the user.

        Args:
            show_deleted (Optional[bool])
                                     : Whether to restrict result to deleted workflows.
            show_hidden (Optional[bool])
                                     : Whether to restrict result to hidden workflows.
            missing_tools (Optional[bool])
                                     : Whether to include a list of missing tools per workflow
                                       entry
            show_published (Optional[WorkflowsIndexParamShowPublished])
                                     :
            show_shared (Optional[WorkflowsIndexParamShowShared])
                                     :
            sort_by (Optional[WorkflowsIndexParamSortBy])
                                     : In unspecified, default ordering depends on other
                                       parameters but generally the user's own workflows appear
                                       first based on update time
            sort_desc (Optional[WorkflowsIndexParamSortDesc])
                                     : Sort in descending order?
            limit (Optional[WorkflowsIndexParamLimit])
                                     :
            offset (Optional[WorkflowsIndexParamOffset])
                                     :
            search (Optional[WorkflowsIndexParamSearch])
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
                                       Tags Available  `name` : The stored workflow's name. (The
                                       tag `n` can be used a short hand alias for this tag to
                                       filter on this attribute.)  `tag` : The workflow's tag,
                                       if the tag contains a colon an approach will be made to
                                       match the key and value of the tag separately. (The tag
                                       `t` can be used a short hand alias for this tag to filter
                                       on this attribute.)  `user` : The stored workflow's
                                       owner's username. (The tag `u` can be used a short hand
                                       alias for this tag to filter on this attribute.)
                                       `is:published` : Include only published workflows in the
                                       final result. Be sure the query parameter
                                       `show_published` is set to `true` if to include all
                                       published workflows and not just the requesting user's.
                                       `is:importable` : Include only importable workflows in
                                       the final result.  `is:deleted` : Include only deleted
                                       workflows in the final result.  `is:shared_with_me` :
                                       Include only workflows shared with the requesting user.
                                       Be sure the query parameter `show_shared` is set to
                                       `true` if to include shared workflows.  `is:bookmarked` :
                                       Include only workflows bookmarked by the requesting user.
                                       ## Free Text  Free text search terms will be searched
                                       against the following attributes of the Stored Workflows:
                                       `name`, `tag`, `user`.
            skip_step_counts (Optional[bool])
                                     : Set this to true to skip joining workflow step counts and
                                       optimize the resulting index query. Response objects will
                                       not contain step counts.
            run-as (Optional[WorkflowsIndexParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem224]: A list with summary stored workflow information per
                                         viewable entry.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows"

        params: dict[str, Any] = {
            **({"show_deleted": show_deleted} if show_deleted is not None else {}),
            **({"show_hidden": show_hidden} if show_hidden is not None else {}),
            **({"missing_tools": missing_tools} if missing_tools is not None else {}),
            **({"show_published": show_published} if show_published is not None else {}),
            **({"show_shared": show_shared} if show_shared is not None else {}),
            **({"sort_by": sort_by} if sort_by is not None else {}),
            **({"sort_desc": sort_desc} if sort_desc is not None else {}),
            **({"limit": limit} if limit is not None else {}),
            **({"offset": offset} if offset is not None else {}),
            **({"search": search} if search is not None else {}),
            **({"skip_step_counts": skip_step_counts} if skip_step_counts is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem224], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_index_2_2(
        self,
        show_deleted: bool | None = False,
        show_hidden: bool | None = False,
        missing_tools: bool | None = False,
        show_published: WorkflowsIndexParamShowPublished | None = None,
        show_shared: WorkflowsIndexParamShowShared | None = None,
        sort_by: WorkflowsIndexParamSortBy | None = None,
        sort_desc: WorkflowsIndexParamSortDesc | None = None,
        limit: WorkflowsIndexParamLimit | None = None,
        offset: WorkflowsIndexParamOffset | None = 0,
        search: WorkflowsIndexParamSearch | None = None,
        skip_step_counts: bool | None = False,
        run_as: WorkflowsIndexParamRunAs | None = None,
    ) -> list[AnonymousArrayItem224]:
        """
        Lists stored workflows viewable by the user.

        Lists stored workflows viewable by the user.

        Args:
            show_deleted (Optional[bool])
                                     : Whether to restrict result to deleted workflows.
            show_hidden (Optional[bool])
                                     : Whether to restrict result to hidden workflows.
            missing_tools (Optional[bool])
                                     : Whether to include a list of missing tools per workflow
                                       entry
            show_published (Optional[WorkflowsIndexParamShowPublished])
                                     :
            show_shared (Optional[WorkflowsIndexParamShowShared])
                                     :
            sort_by (Optional[WorkflowsIndexParamSortBy])
                                     : In unspecified, default ordering depends on other
                                       parameters but generally the user's own workflows appear
                                       first based on update time
            sort_desc (Optional[WorkflowsIndexParamSortDesc])
                                     : Sort in descending order?
            limit (Optional[WorkflowsIndexParamLimit])
                                     :
            offset (Optional[WorkflowsIndexParamOffset])
                                     :
            search (Optional[WorkflowsIndexParamSearch])
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
                                       Tags Available  `name` : The stored workflow's name. (The
                                       tag `n` can be used a short hand alias for this tag to
                                       filter on this attribute.)  `tag` : The workflow's tag,
                                       if the tag contains a colon an approach will be made to
                                       match the key and value of the tag separately. (The tag
                                       `t` can be used a short hand alias for this tag to filter
                                       on this attribute.)  `user` : The stored workflow's
                                       owner's username. (The tag `u` can be used a short hand
                                       alias for this tag to filter on this attribute.)
                                       `is:published` : Include only published workflows in the
                                       final result. Be sure the query parameter
                                       `show_published` is set to `true` if to include all
                                       published workflows and not just the requesting user's.
                                       `is:importable` : Include only importable workflows in
                                       the final result.  `is:deleted` : Include only deleted
                                       workflows in the final result.  `is:shared_with_me` :
                                       Include only workflows shared with the requesting user.
                                       Be sure the query parameter `show_shared` is set to
                                       `true` if to include shared workflows.  `is:bookmarked` :
                                       Include only workflows bookmarked by the requesting user.
                                       ## Free Text  Free text search terms will be searched
                                       against the following attributes of the Stored Workflows:
                                       `name`, `tag`, `user`.
            skip_step_counts (Optional[bool])
                                     : Set this to true to skip joining workflow step counts and
                                       optimize the resulting index query. Response objects will
                                       not contain step counts.
            run-as (Optional[WorkflowsIndexParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem224]: A list with summary stored workflow information per
                                         viewable entry.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows"

        params: dict[str, Any] = {
            **({"show_deleted": show_deleted} if show_deleted is not None else {}),
            **({"show_hidden": show_hidden} if show_hidden is not None else {}),
            **({"missing_tools": missing_tools} if missing_tools is not None else {}),
            **({"show_published": show_published} if show_published is not None else {}),
            **({"show_shared": show_shared} if show_shared is not None else {}),
            **({"sort_by": sort_by} if sort_by is not None else {}),
            **({"sort_desc": sort_desc} if sort_desc is not None else {}),
            **({"limit": limit} if limit is not None else {}),
            **({"offset": offset} if offset is not None else {}),
            **({"search": search} if search is not None else {}),
            **({"skip_step_counts": skip_step_counts} if skip_step_counts is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem224], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_menu_get_workflow_menu_2_2(
        self,
        show_deleted: WorkflowsMenuGetWorkflowMenuParamShowDeleted | None = False,
        show_hidden: WorkflowsMenuGetWorkflowMenuParamShowHidden | None = False,
        missing_tools: WorkflowsMenuGetWorkflowMenuParamMissingTools | None = False,
        show_published: WorkflowsMenuGetWorkflowMenuParamShowPublished | None = None,
        show_shared: WorkflowsMenuGetWorkflowMenuParamShowShared | None = None,
        run_as: WorkflowsMenuGetWorkflowMenuParamRunAs | None = None,
    ) -> Any:
        """
        Get workflows present in the tools panel.

        Args:
            show_deleted (Optional[WorkflowsMenuGetWorkflowMenuParamShowDeleted])
                                     : Whether to restrict result to deleted workflows.
            show_hidden (Optional[WorkflowsMenuGetWorkflowMenuParamShowHidden])
                                     : Whether to restrict result to hidden workflows.
            missing_tools (Optional[WorkflowsMenuGetWorkflowMenuParamMissingTools])
                                     : Whether to include a list of missing tools per workflow
                                       entry
            show_published (Optional[WorkflowsMenuGetWorkflowMenuParamShowPublished])
                                     :
            show_shared (Optional[WorkflowsMenuGetWorkflowMenuParamShowShared])
                                     :
            run-as (Optional[WorkflowsMenuGetWorkflowMenuParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/menu"

        params: dict[str, Any] = {
            **({"show_deleted": show_deleted} if show_deleted is not None else {}),
            **({"show_hidden": show_hidden} if show_hidden is not None else {}),
            **({"missing_tools": missing_tools} if missing_tools is not None else {}),
            **({"show_published": show_published} if show_published is not None else {}),
            **({"show_shared": show_shared} if show_shared is not None else {}),
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

    async def workflows_menu_get_workflow_menu_2_2(
        self,
        show_deleted: WorkflowsMenuGetWorkflowMenuParamShowDeleted | None = False,
        show_hidden: WorkflowsMenuGetWorkflowMenuParamShowHidden | None = False,
        missing_tools: WorkflowsMenuGetWorkflowMenuParamMissingTools | None = False,
        show_published: WorkflowsMenuGetWorkflowMenuParamShowPublished | None = None,
        show_shared: WorkflowsMenuGetWorkflowMenuParamShowShared | None = None,
        run_as: WorkflowsMenuGetWorkflowMenuParamRunAs | None = None,
    ) -> Any:
        """
        Get workflows present in the tools panel.

        Args:
            show_deleted (Optional[WorkflowsMenuGetWorkflowMenuParamShowDeleted])
                                     : Whether to restrict result to deleted workflows.
            show_hidden (Optional[WorkflowsMenuGetWorkflowMenuParamShowHidden])
                                     : Whether to restrict result to hidden workflows.
            missing_tools (Optional[WorkflowsMenuGetWorkflowMenuParamMissingTools])
                                     : Whether to include a list of missing tools per workflow
                                       entry
            show_published (Optional[WorkflowsMenuGetWorkflowMenuParamShowPublished])
                                     :
            show_shared (Optional[WorkflowsMenuGetWorkflowMenuParamShowShared])
                                     :
            run-as (Optional[WorkflowsMenuGetWorkflowMenuParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/menu"

        params: dict[str, Any] = {
            **({"show_deleted": show_deleted} if show_deleted is not None else {}),
            **({"show_hidden": show_hidden} if show_hidden is not None else {}),
            **({"missing_tools": missing_tools} if missing_tools is not None else {}),
            **({"show_published": show_published} if show_published is not None else {}),
            **({"show_shared": show_shared} if show_shared is not None else {}),
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

    async def workflows_delete_workflow_2_2(
        self,
        workflow_id: str,
        run_as: WorkflowsDeleteWorkflowParamRunAs | None = None,
    ) -> Any:
        """
        Add the deleted flag to a workflow.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            run-as (Optional[WorkflowsDeleteWorkflowParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_delete_workflow_2_2(
        self,
        workflow_id: str,
        run_as: WorkflowsDeleteWorkflowParamRunAs | None = None,
    ) -> Any:
        """
        Add the deleted flag to a workflow.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            run-as (Optional[WorkflowsDeleteWorkflowParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_show_workflow_2_2(
        self,
        workflow_id: str,
        instance: WorkflowsShowWorkflowParamInstance | None = False,
        legacy: WorkflowsShowWorkflowParamLegacy | None = False,
        version: WorkflowsShowWorkflowParamVersion | None = None,
        run_as: WorkflowsShowWorkflowParamRunAs | None = None,
    ) -> StoredWorkflowDetailed:
        """
        Displays information needed to run a workflow.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            instance (Optional[WorkflowsShowWorkflowParamInstance])
                                     :
            legacy (Optional[WorkflowsShowWorkflowParamLegacy])
                                     : Use the legacy workflow format.
            version (Optional[WorkflowsShowWorkflowParamVersion])
                                     : The version of the workflow to fetch.
            run-as (Optional[WorkflowsShowWorkflowParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            StoredWorkflowDetailed: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}"

        params: dict[str, Any] = {
            **({"instance": instance} if instance is not None else {}),
            **({"legacy": legacy} if legacy is not None else {}),
            **({"version": version} if version is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(StoredWorkflowDetailed, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_show_workflow_2_2(
        self,
        workflow_id: str,
        instance: WorkflowsShowWorkflowParamInstance | None = False,
        legacy: WorkflowsShowWorkflowParamLegacy | None = False,
        version: WorkflowsShowWorkflowParamVersion | None = None,
        run_as: WorkflowsShowWorkflowParamRunAs | None = None,
    ) -> StoredWorkflowDetailed:
        """
        Displays information needed to run a workflow.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            instance (Optional[WorkflowsShowWorkflowParamInstance])
                                     :
            legacy (Optional[WorkflowsShowWorkflowParamLegacy])
                                     : Use the legacy workflow format.
            version (Optional[WorkflowsShowWorkflowParamVersion])
                                     : The version of the workflow to fetch.
            run-as (Optional[WorkflowsShowWorkflowParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            StoredWorkflowDetailed: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}"

        params: dict[str, Any] = {
            **({"instance": instance} if instance is not None else {}),
            **({"legacy": legacy} if legacy is not None else {}),
            **({"version": version} if version is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(StoredWorkflowDetailed, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_invocation_counts_2_2(
        self,
        workflow_id: str,
        instance: WorkflowsInvocationCountsParamInstance | None = False,
        run_as: WorkflowsInvocationCountsParamRunAs | None = None,
    ) -> RootModelDictStrInt2:
        """
        Get state counts for accessible workflow.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            instance (Optional[WorkflowsInvocationCountsParamInstance])
                                     : Is provided workflow id for Workflow instead of
                                       StoredWorkflow?
            run-as (Optional[WorkflowsInvocationCountsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            RootModelDictStrInt2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/counts"

        params: dict[str, Any] = {
            **({"instance": instance} if instance is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(RootModelDictStrInt2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_invocation_counts_2_2(
        self,
        workflow_id: str,
        instance: WorkflowsInvocationCountsParamInstance | None = False,
        run_as: WorkflowsInvocationCountsParamRunAs | None = None,
    ) -> RootModelDictStrInt2:
        """
        Get state counts for accessible workflow.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            instance (Optional[WorkflowsInvocationCountsParamInstance])
                                     : Is provided workflow id for Workflow instead of
                                       StoredWorkflow?
            run-as (Optional[WorkflowsInvocationCountsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            RootModelDictStrInt2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/counts"

        params: dict[str, Any] = {
            **({"instance": instance} if instance is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(RootModelDictStrInt2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_disable_link_access_disable_link_access_2_2(
        self,
        workflow_id: str,
        run_as: WorkflowsDisableLinkAccessDisableLinkAccessParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Makes this item inaccessible by a URL link.

        Makes this item inaccessible by a URL link and return the current sharing status.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            run-as (Optional[WorkflowsDisableLinkAccessDisableLinkAccessParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            SharingStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/disable_link_access"

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

    async def workflows_disable_link_access_disable_link_access_2_2(
        self,
        workflow_id: str,
        run_as: WorkflowsDisableLinkAccessDisableLinkAccessParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Makes this item inaccessible by a URL link.

        Makes this item inaccessible by a URL link and return the current sharing status.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            run-as (Optional[WorkflowsDisableLinkAccessDisableLinkAccessParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            SharingStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/disable_link_access"

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

    async def workflows_enable_link_access_enable_link_access_2_2(
        self,
        workflow_id: str,
        run_as: WorkflowsEnableLinkAccessEnableLinkAccessParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Makes this item accessible by a URL link.

        Makes this item accessible by a URL link and return the current sharing status.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            run-as (Optional[WorkflowsEnableLinkAccessEnableLinkAccessParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            SharingStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/enable_link_access"

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

    async def workflows_enable_link_access_enable_link_access_2_2(
        self,
        workflow_id: str,
        run_as: WorkflowsEnableLinkAccessEnableLinkAccessParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Makes this item accessible by a URL link.

        Makes this item accessible by a URL link and return the current sharing status.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            run-as (Optional[WorkflowsEnableLinkAccessEnableLinkAccessParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            SharingStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/enable_link_access"

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

    async def workflows_invocations_index_workflow_invocations_2_2(
        self,
        workflow_id: str,
        history_id: WorkflowsInvocationsIndexWorkflowInvocationsParamHistoryId | None = None,
        job_id: WorkflowsInvocationsIndexWorkflowInvocationsParamJobId | None = None,
        user_id: WorkflowsInvocationsIndexWorkflowInvocationsParamUserId | None = None,
        sort_by: WorkflowsInvocationsIndexWorkflowInvocationsParamSortBy | None = None,
        sort_desc: bool | None = False,
        include_terminal: WorkflowsInvocationsIndexWorkflowInvocationsParamIncludeTerminal | None = True,
        limit: WorkflowsInvocationsIndexWorkflowInvocationsParamLimit | None = 20,
        offset: WorkflowsInvocationsIndexWorkflowInvocationsParamOffset | None = None,
        instance: WorkflowsInvocationsIndexWorkflowInvocationsParamInstance | None = False,
        view: WorkflowsInvocationsIndexWorkflowInvocationsParamView | None = None,
        step_details: bool | None = False,
        run_as: WorkflowsInvocationsIndexWorkflowInvocationsParamRunAs | None = None,
    ) -> list[WorkflowInvocationResponse]:
        """
        Get the list of a user's workflow invocations.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            history_id (Optional[WorkflowsInvocationsIndexWorkflowInvocationsParamHistoryId])
                                     : Return only invocations for this History ID
            job_id (Optional[WorkflowsInvocationsIndexWorkflowInvocationsParamJobId])
                                     : Return only invocations for this Job ID
            user_id (Optional[WorkflowsInvocationsIndexWorkflowInvocationsParamUserId])
                                     : Return invocations for this User ID.
            sort_by (Optional[WorkflowsInvocationsIndexWorkflowInvocationsParamSortBy])
                                     : Sort Workflow Invocations by this attribute
            sort_desc (Optional[bool]): Sort in descending order?
            include_terminal (Optional[WorkflowsInvocationsIndexWorkflowInvocationsParamIncludeTerminal])
                                     : Set to false to only include terminal Invocations.
            limit (Optional[WorkflowsInvocationsIndexWorkflowInvocationsParamLimit])
                                     : Limit the number of invocations to return.
            offset (Optional[WorkflowsInvocationsIndexWorkflowInvocationsParamOffset])
                                     : Number of invocations to skip.
            instance (Optional[WorkflowsInvocationsIndexWorkflowInvocationsParamInstance])
                                     : Is provided workflow id for Workflow instead of
                                       StoredWorkflow?
            view (Optional[WorkflowsInvocationsIndexWorkflowInvocationsParamView])
                                     : View to be passed to the serializer
            step_details (Optional[bool])
                                     : Include details for individual invocation steps and
                                       populate a steps attribute in the resulting dictionary.
            run-as (Optional[WorkflowsInvocationsIndexWorkflowInvocationsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[WorkflowInvocationResponse]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/invocations"

        params: dict[str, Any] = {
            **({"history_id": history_id} if history_id is not None else {}),
            **({"job_id": job_id} if job_id is not None else {}),
            **({"user_id": user_id} if user_id is not None else {}),
            **({"sort_by": sort_by} if sort_by is not None else {}),
            **({"sort_desc": sort_desc} if sort_desc is not None else {}),
            **({"include_terminal": include_terminal} if include_terminal is not None else {}),
            **({"limit": limit} if limit is not None else {}),
            **({"offset": offset} if offset is not None else {}),
            **({"instance": instance} if instance is not None else {}),
            **({"view": view} if view is not None else {}),
            **({"step_details": step_details} if step_details is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[WorkflowInvocationResponse], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_invocations_index_workflow_invocations_2_2(
        self,
        workflow_id: str,
        history_id: WorkflowsInvocationsIndexWorkflowInvocationsParamHistoryId | None = None,
        job_id: WorkflowsInvocationsIndexWorkflowInvocationsParamJobId | None = None,
        user_id: WorkflowsInvocationsIndexWorkflowInvocationsParamUserId | None = None,
        sort_by: WorkflowsInvocationsIndexWorkflowInvocationsParamSortBy | None = None,
        sort_desc: bool | None = False,
        include_terminal: WorkflowsInvocationsIndexWorkflowInvocationsParamIncludeTerminal | None = True,
        limit: WorkflowsInvocationsIndexWorkflowInvocationsParamLimit | None = 20,
        offset: WorkflowsInvocationsIndexWorkflowInvocationsParamOffset | None = None,
        instance: WorkflowsInvocationsIndexWorkflowInvocationsParamInstance | None = False,
        view: WorkflowsInvocationsIndexWorkflowInvocationsParamView | None = None,
        step_details: bool | None = False,
        run_as: WorkflowsInvocationsIndexWorkflowInvocationsParamRunAs | None = None,
    ) -> list[WorkflowInvocationResponse]:
        """
        Get the list of a user's workflow invocations.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            history_id (Optional[WorkflowsInvocationsIndexWorkflowInvocationsParamHistoryId])
                                     : Return only invocations for this History ID
            job_id (Optional[WorkflowsInvocationsIndexWorkflowInvocationsParamJobId])
                                     : Return only invocations for this Job ID
            user_id (Optional[WorkflowsInvocationsIndexWorkflowInvocationsParamUserId])
                                     : Return invocations for this User ID.
            sort_by (Optional[WorkflowsInvocationsIndexWorkflowInvocationsParamSortBy])
                                     : Sort Workflow Invocations by this attribute
            sort_desc (Optional[bool]): Sort in descending order?
            include_terminal (Optional[WorkflowsInvocationsIndexWorkflowInvocationsParamIncludeTerminal])
                                     : Set to false to only include terminal Invocations.
            limit (Optional[WorkflowsInvocationsIndexWorkflowInvocationsParamLimit])
                                     : Limit the number of invocations to return.
            offset (Optional[WorkflowsInvocationsIndexWorkflowInvocationsParamOffset])
                                     : Number of invocations to skip.
            instance (Optional[WorkflowsInvocationsIndexWorkflowInvocationsParamInstance])
                                     : Is provided workflow id for Workflow instead of
                                       StoredWorkflow?
            view (Optional[WorkflowsInvocationsIndexWorkflowInvocationsParamView])
                                     : View to be passed to the serializer
            step_details (Optional[bool])
                                     : Include details for individual invocation steps and
                                       populate a steps attribute in the resulting dictionary.
            run-as (Optional[WorkflowsInvocationsIndexWorkflowInvocationsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[WorkflowInvocationResponse]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/invocations"

        params: dict[str, Any] = {
            **({"history_id": history_id} if history_id is not None else {}),
            **({"job_id": job_id} if job_id is not None else {}),
            **({"user_id": user_id} if user_id is not None else {}),
            **({"sort_by": sort_by} if sort_by is not None else {}),
            **({"sort_desc": sort_desc} if sort_desc is not None else {}),
            **({"include_terminal": include_terminal} if include_terminal is not None else {}),
            **({"limit": limit} if limit is not None else {}),
            **({"offset": offset} if offset is not None else {}),
            **({"instance": instance} if instance is not None else {}),
            **({"view": view} if view is not None else {}),
            **({"step_details": step_details} if step_details is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[WorkflowInvocationResponse], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_invocations_invoke_2_2(
        self,
        workflow_id: WorkflowsInvocationsInvokeParamWorkflowId,
        body: InvokeWorkflowPayload,
        run_as: WorkflowsInvocationsInvokeParamRunAs | None = None,
    ) -> WorkflowsInvocationsInvoke200Response2:
        """
        Schedule the workflow specified by `workflow_id` to run.

        Args:
            workflow_id (WorkflowsInvocationsInvokeParamWorkflowId)
                                     : The database identifier - UUID or encoded - of the
                                       Workflow.
            run-as (Optional[WorkflowsInvocationsInvokeParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (InvokeWorkflowPayload)
                                     : Request body. (json)

        Returns:
            WorkflowsInvocationsInvoke200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/invocations"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: InvokeWorkflowPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(WorkflowsInvocationsInvoke200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_invocations_invoke_2_2(
        self,
        workflow_id: WorkflowsInvocationsInvokeParamWorkflowId,
        body: InvokeWorkflowPayload,
        run_as: WorkflowsInvocationsInvokeParamRunAs | None = None,
    ) -> WorkflowsInvocationsInvoke200Response2:
        """
        Schedule the workflow specified by `workflow_id` to run.

        Args:
            workflow_id (WorkflowsInvocationsInvokeParamWorkflowId)
                                     : The database identifier - UUID or encoded - of the
                                       Workflow.
            run-as (Optional[WorkflowsInvocationsInvokeParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (InvokeWorkflowPayload)
                                     : Request body. (json)

        Returns:
            WorkflowsInvocationsInvoke200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/invocations"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: InvokeWorkflowPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(WorkflowsInvocationsInvoke200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_invocations_cancel_workflow_invocation_2_2(
        self,
        invocation_id: str,
        workflow_id: str,
        step_details: bool | None = False,
        legacy_job_state: bool | None = False,
        run_as: WorkflowsInvocationsCancelWorkflowInvocationParamRunAs | None = None,
    ) -> WorkflowInvocationResponse:
        """
        Cancel the specified workflow invocation.

        An alias for `DELETE /api/invocations/{invocation_id}`. `workflow_id` is ignored.

        Args:
            invocation_id (str)      : The encoded database identifier of the Invocation.
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            step_details (Optional[bool])
                                     : Include details for individual invocation steps and
                                       populate a steps attribute in the resulting dictionary.
            legacy_job_state (Optional[bool])
                                     : Populate the invocation step state with the job state
                                       instead of the invocation step state.         This will
                                       also produce one step per job in mapping jobs to mimic
                                       the older behavior with respect to collections.
                                       Partially scheduled steps may provide incomplete
                                       information and the listed steps outputs         are not
                                       the mapped over step outputs but the individual job
                                       outputs.
            run-as (Optional[WorkflowsInvocationsCancelWorkflowInvocationParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            WorkflowInvocationResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/invocations/{invocation_id}"

        params: dict[str, Any] = {
            **({"step_details": step_details} if step_details is not None else {}),
            **({"legacy_job_state": legacy_job_state} if legacy_job_state is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(WorkflowInvocationResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_invocations_cancel_workflow_invocation_2_2(
        self,
        invocation_id: str,
        workflow_id: str,
        step_details: bool | None = False,
        legacy_job_state: bool | None = False,
        run_as: WorkflowsInvocationsCancelWorkflowInvocationParamRunAs | None = None,
    ) -> WorkflowInvocationResponse:
        """
        Cancel the specified workflow invocation.

        An alias for `DELETE /api/invocations/{invocation_id}`. `workflow_id` is ignored.

        Args:
            invocation_id (str)      : The encoded database identifier of the Invocation.
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            step_details (Optional[bool])
                                     : Include details for individual invocation steps and
                                       populate a steps attribute in the resulting dictionary.
            legacy_job_state (Optional[bool])
                                     : Populate the invocation step state with the job state
                                       instead of the invocation step state.         This will
                                       also produce one step per job in mapping jobs to mimic
                                       the older behavior with respect to collections.
                                       Partially scheduled steps may provide incomplete
                                       information and the listed steps outputs         are not
                                       the mapped over step outputs but the individual job
                                       outputs.
            run-as (Optional[WorkflowsInvocationsCancelWorkflowInvocationParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            WorkflowInvocationResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/invocations/{invocation_id}"

        params: dict[str, Any] = {
            **({"step_details": step_details} if step_details is not None else {}),
            **({"legacy_job_state": legacy_job_state} if legacy_job_state is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(WorkflowInvocationResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_invocations_show_workflow_invocation_2_2(
        self,
        workflow_id: str,
        invocation_id: str,
        step_details: bool | None = False,
        legacy_job_state: bool | None = False,
        run_as: WorkflowsInvocationsShowWorkflowInvocationParamRunAs | None = None,
    ) -> WorkflowInvocationResponse:
        """
        Get detailed description of a workflow invocation.

        An alias for `GET /api/invocations/{invocation_id}`. `workflow_id` is ignored.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            invocation_id (str)      : The encoded database identifier of the Invocation.
            step_details (Optional[bool])
                                     : Include details for individual invocation steps and
                                       populate a steps attribute in the resulting dictionary.
            legacy_job_state (Optional[bool])
                                     : Populate the invocation step state with the job state
                                       instead of the invocation step state.         This will
                                       also produce one step per job in mapping jobs to mimic
                                       the older behavior with respect to collections.
                                       Partially scheduled steps may provide incomplete
                                       information and the listed steps outputs         are not
                                       the mapped over step outputs but the individual job
                                       outputs.
            run-as (Optional[WorkflowsInvocationsShowWorkflowInvocationParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            WorkflowInvocationResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/invocations/{invocation_id}"

        params: dict[str, Any] = {
            **({"step_details": step_details} if step_details is not None else {}),
            **({"legacy_job_state": legacy_job_state} if legacy_job_state is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(WorkflowInvocationResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_invocations_show_workflow_invocation_2_2(
        self,
        workflow_id: str,
        invocation_id: str,
        step_details: bool | None = False,
        legacy_job_state: bool | None = False,
        run_as: WorkflowsInvocationsShowWorkflowInvocationParamRunAs | None = None,
    ) -> WorkflowInvocationResponse:
        """
        Get detailed description of a workflow invocation.

        An alias for `GET /api/invocations/{invocation_id}`. `workflow_id` is ignored.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            invocation_id (str)      : The encoded database identifier of the Invocation.
            step_details (Optional[bool])
                                     : Include details for individual invocation steps and
                                       populate a steps attribute in the resulting dictionary.
            legacy_job_state (Optional[bool])
                                     : Populate the invocation step state with the job state
                                       instead of the invocation step state.         This will
                                       also produce one step per job in mapping jobs to mimic
                                       the older behavior with respect to collections.
                                       Partially scheduled steps may provide incomplete
                                       information and the listed steps outputs         are not
                                       the mapped over step outputs but the individual job
                                       outputs.
            run-as (Optional[WorkflowsInvocationsShowWorkflowInvocationParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            WorkflowInvocationResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/invocations/{invocation_id}"

        params: dict[str, Any] = {
            **({"step_details": step_details} if step_details is not None else {}),
            **({"legacy_job_state": legacy_job_state} if legacy_job_state is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(WorkflowInvocationResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_invocations_jobs_summary_workflow_invocation_jobs_summary_2_2(
        self,
        workflow_id: str,
        invocation_id: str,
        run_as: WorkflowsInvocationsJobsSummaryWorkflowInvocationJobsSummaryParamRunAs | None = None,
    ) -> InvocationJobsResponse:
        """
        Get job state summary info aggregated across all current jobs of the workflow
        invocation.

        An alias for `GET /api/invocations/{invocation_id}/jobs_summary`. `workflow_id` is
        ignored.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            invocation_id (str)      : The encoded database identifier of the Invocation.
            run-as (Optional[WorkflowsInvocationsJobsSummaryWorkflowInvocationJobsSummaryParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            InvocationJobsResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/invocations/{invocation_id}/jobs_summary"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(InvocationJobsResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_invocations_jobs_summary_workflow_invocation_jobs_summary_2_2(
        self,
        workflow_id: str,
        invocation_id: str,
        run_as: WorkflowsInvocationsJobsSummaryWorkflowInvocationJobsSummaryParamRunAs | None = None,
    ) -> InvocationJobsResponse:
        """
        Get job state summary info aggregated across all current jobs of the workflow
        invocation.

        An alias for `GET /api/invocations/{invocation_id}/jobs_summary`. `workflow_id` is
        ignored.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            invocation_id (str)      : The encoded database identifier of the Invocation.
            run-as (Optional[WorkflowsInvocationsJobsSummaryWorkflowInvocationJobsSummaryParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            InvocationJobsResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/invocations/{invocation_id}/jobs_summary"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(InvocationJobsResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_invocations_report_show_workflow_invocation_report_2_2(
        self,
        invocation_id: str,
        workflow_id: str,
        run_as: WorkflowsInvocationsReportShowWorkflowInvocationReportParamRunAs | None = None,
    ) -> InvocationReport:
        """
        Get JSON summarizing invocation for reporting.

        An alias for `GET /api/invocations/{invocation_id}/report`. `workflow_id` is ignored.

        Args:
            invocation_id (str)      : The encoded database identifier of the Invocation.
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            run-as (Optional[WorkflowsInvocationsReportShowWorkflowInvocationReportParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            InvocationReport: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/invocations/{invocation_id}/report"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(InvocationReport, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_invocations_report_show_workflow_invocation_report_2_2(
        self,
        invocation_id: str,
        workflow_id: str,
        run_as: WorkflowsInvocationsReportShowWorkflowInvocationReportParamRunAs | None = None,
    ) -> InvocationReport:
        """
        Get JSON summarizing invocation for reporting.

        An alias for `GET /api/invocations/{invocation_id}/report`. `workflow_id` is ignored.

        Args:
            invocation_id (str)      : The encoded database identifier of the Invocation.
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            run-as (Optional[WorkflowsInvocationsReportShowWorkflowInvocationReportParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            InvocationReport: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/invocations/{invocation_id}/report"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(InvocationReport, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_invocations_report_pdf_show_workflow_invocation_report_pdf_2_2(
        self,
        workflow_id: str,
        invocation_id: str,
        run_as: WorkflowsInvocationsReportPdfShowWorkflowInvocationReportPdfParamRunAs | None = None,
    ) -> None:
        """
        Get PDF summarizing invocation for reporting.

        An alias for `GET /api/invocations/{invocation_id}/report.pdf`. `workflow_id` is
        ignored.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            invocation_id (str)      : The encoded database identifier of the Invocation.
            run-as (Optional[WorkflowsInvocationsReportPdfShowWorkflowInvocationReportPdfParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/invocations/{invocation_id}/report.pdf"

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

    async def workflows_invocations_report_pdf_show_workflow_invocation_report_pdf_2_2(
        self,
        workflow_id: str,
        invocation_id: str,
        run_as: WorkflowsInvocationsReportPdfShowWorkflowInvocationReportPdfParamRunAs | None = None,
    ) -> None:
        """
        Get PDF summarizing invocation for reporting.

        An alias for `GET /api/invocations/{invocation_id}/report.pdf`. `workflow_id` is
        ignored.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            invocation_id (str)      : The encoded database identifier of the Invocation.
            run-as (Optional[WorkflowsInvocationsReportPdfShowWorkflowInvocationReportPdfParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/invocations/{invocation_id}/report.pdf"

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

    async def workflows_invocations_step_jobs_summary_workflow_invocation_step_jobs_summary_2_2(
        self,
        workflow_id: str,
        invocation_id: str,
        run_as: WorkflowsInvocationsStepJobsSummaryWorkflowInvocationStepJobsSummaryParamRunAs | None = None,
    ) -> list[AnonymousArrayItem226]:
        """
        Get job state summary info aggregated per step of the workflow invocation.

        An alias for `GET /api/invocations/{invocation_id}/step_jobs_summary`. `workflow_id` is
        ignored.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            invocation_id (str)      : The encoded database identifier of the Invocation.
            run-as (Optional[WorkflowsInvocationsStepJobsSummaryWorkflowInvocationStepJobsSummaryParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem226]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/invocations/{invocation_id}/step_jobs_summary"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem226], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_invocations_step_jobs_summary_workflow_invocation_step_jobs_summary_2_2(
        self,
        workflow_id: str,
        invocation_id: str,
        run_as: WorkflowsInvocationsStepJobsSummaryWorkflowInvocationStepJobsSummaryParamRunAs | None = None,
    ) -> list[AnonymousArrayItem226]:
        """
        Get job state summary info aggregated per step of the workflow invocation.

        An alias for `GET /api/invocations/{invocation_id}/step_jobs_summary`. `workflow_id` is
        ignored.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            invocation_id (str)      : The encoded database identifier of the Invocation.
            run-as (Optional[WorkflowsInvocationsStepJobsSummaryWorkflowInvocationStepJobsSummaryParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem226]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/invocations/{invocation_id}/step_jobs_summary"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem226], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_invocations_steps_workflow_invocation_step_2_2(
        self,
        workflow_id: str,
        invocation_id: str,
        step_id: str,
        run_as: WorkflowsInvocationsStepsWorkflowInvocationStepParamRunAs | None = None,
    ) -> InvocationStep:
        """
        Show details of workflow invocation step.

        An alias for `GET /api/invocations/{invocation_id}/steps/{step_id}`. `workflow_id` and
        `invocation_id` are ignored.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            invocation_id (str)      : The encoded database identifier of the Invocation.
            step_id (str)            : The encoded database identifier of the
                                       WorkflowInvocationStep.
            run-as (Optional[WorkflowsInvocationsStepsWorkflowInvocationStepParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            InvocationStep: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/invocations/{invocation_id}/steps/{step_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(InvocationStep, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_invocations_steps_workflow_invocation_step_2_2(
        self,
        workflow_id: str,
        invocation_id: str,
        step_id: str,
        run_as: WorkflowsInvocationsStepsWorkflowInvocationStepParamRunAs | None = None,
    ) -> InvocationStep:
        """
        Show details of workflow invocation step.

        An alias for `GET /api/invocations/{invocation_id}/steps/{step_id}`. `workflow_id` and
        `invocation_id` are ignored.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            invocation_id (str)      : The encoded database identifier of the Invocation.
            step_id (str)            : The encoded database identifier of the
                                       WorkflowInvocationStep.
            run-as (Optional[WorkflowsInvocationsStepsWorkflowInvocationStepParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            InvocationStep: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/invocations/{invocation_id}/steps/{step_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(InvocationStep, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_invocations_steps_update_workflow_invocation_step_2_2(
        self,
        workflow_id: str,
        invocation_id: str,
        step_id: str,
        body: InvocationUpdatePayload,
        run_as: WorkflowsInvocationsStepsUpdateWorkflowInvocationStepParamRunAs | None = None,
    ) -> InvocationStep:
        """
        Update state of running workflow step invocation.

        An alias for `PUT /api/invocations/{invocation_id}/steps/{step_id}`. `workflow_id` is
        ignored.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            invocation_id (str)      : The encoded database identifier of the Invocation.
            step_id (str)            : The encoded database identifier of the
                                       WorkflowInvocationStep.
            run-as (Optional[WorkflowsInvocationsStepsUpdateWorkflowInvocationStepParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (InvocationUpdatePayload)
                                     : Request body. (json)

        Returns:
            InvocationStep: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/invocations/{invocation_id}/steps/{step_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: InvocationUpdatePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(InvocationStep, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_invocations_steps_update_workflow_invocation_step_2_2(
        self,
        workflow_id: str,
        invocation_id: str,
        step_id: str,
        body: InvocationUpdatePayload,
        run_as: WorkflowsInvocationsStepsUpdateWorkflowInvocationStepParamRunAs | None = None,
    ) -> InvocationStep:
        """
        Update state of running workflow step invocation.

        An alias for `PUT /api/invocations/{invocation_id}/steps/{step_id}`. `workflow_id` is
        ignored.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            invocation_id (str)      : The encoded database identifier of the Invocation.
            step_id (str)            : The encoded database identifier of the
                                       WorkflowInvocationStep.
            run-as (Optional[WorkflowsInvocationsStepsUpdateWorkflowInvocationStepParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (InvocationUpdatePayload)
                                     : Request body. (json)

        Returns:
            InvocationStep: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/invocations/{invocation_id}/steps/{step_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: InvocationUpdatePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(InvocationStep, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_publish_publish_2_2(
        self,
        workflow_id: str,
        run_as: WorkflowsPublishPublishParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Makes this item public and accessible by a URL link.

        Makes this item publicly available by a URL link and return the current sharing status.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            run-as (Optional[WorkflowsPublishPublishParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            SharingStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/publish"

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

    async def workflows_publish_publish_2_2(
        self,
        workflow_id: str,
        run_as: WorkflowsPublishPublishParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Makes this item public and accessible by a URL link.

        Makes this item publicly available by a URL link and return the current sharing status.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            run-as (Optional[WorkflowsPublishPublishParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            SharingStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/publish"

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

    async def workflows_refactor_refactor_2_2(
        self,
        workflow_id: str,
        body: RefactorRequest,
        instance: WorkflowsRefactorRefactorParamInstance | None = False,
        run_as: WorkflowsRefactorRefactorParamRunAs | None = None,
    ) -> RefactorResponse:
        """
        Updates the workflow stored with the given ID.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            instance (Optional[WorkflowsRefactorRefactorParamInstance])
                                     :
            run-as (Optional[WorkflowsRefactorRefactorParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (RefactorRequest)   : Request body. (json)

        Returns:
            RefactorResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/refactor"

        params: dict[str, Any] = {
            **({"instance": instance} if instance is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: RefactorRequest = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(RefactorResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_refactor_refactor_2_2(
        self,
        workflow_id: str,
        body: RefactorRequest,
        instance: WorkflowsRefactorRefactorParamInstance | None = False,
        run_as: WorkflowsRefactorRefactorParamRunAs | None = None,
    ) -> RefactorResponse:
        """
        Updates the workflow stored with the given ID.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            instance (Optional[WorkflowsRefactorRefactorParamInstance])
                                     :
            run-as (Optional[WorkflowsRefactorRefactorParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (RefactorRequest)   : Request body. (json)

        Returns:
            RefactorResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/refactor"

        params: dict[str, Any] = {
            **({"instance": instance} if instance is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: RefactorRequest = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(RefactorResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_share_with_users_share_with_users_2_2(
        self,
        workflow_id: str,
        body: ShareWithPayload,
        run_as: WorkflowsShareWithUsersShareWithUsersParamRunAs | None = None,
    ) -> ShareWithStatus:
        """
        Share this item with specific users.

        Shares this item with specific users and return the current sharing status.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            run-as (Optional[WorkflowsShareWithUsersShareWithUsersParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (ShareWithPayload)  : Request body. (json)

        Returns:
            ShareWithStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/share_with_users"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: ShareWithPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ShareWithStatus, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_share_with_users_share_with_users_2_2(
        self,
        workflow_id: str,
        body: ShareWithPayload,
        run_as: WorkflowsShareWithUsersShareWithUsersParamRunAs | None = None,
    ) -> ShareWithStatus:
        """
        Share this item with specific users.

        Shares this item with specific users and return the current sharing status.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            run-as (Optional[WorkflowsShareWithUsersShareWithUsersParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (ShareWithPayload)  : Request body. (json)

        Returns:
            ShareWithStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/share_with_users"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: ShareWithPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ShareWithStatus, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_sharing_sharing_2_2(
        self,
        workflow_id: str,
        run_as: WorkflowsSharingSharingParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Get the current sharing status of the given item.

        Return the sharing status of the item.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            run-as (Optional[WorkflowsSharingSharingParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            SharingStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/sharing"

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

    async def workflows_sharing_sharing_2_2(
        self,
        workflow_id: str,
        run_as: WorkflowsSharingSharingParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Get the current sharing status of the given item.

        Return the sharing status of the item.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            run-as (Optional[WorkflowsSharingSharingParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            SharingStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/sharing"

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

    async def workflows_slug_set_slug_2_2(
        self,
        workflow_id: str,
        body: SetSlugPayload,
        run_as: WorkflowsSlugSetSlugParamRunAs | None = None,
    ) -> None:
        """
        Set a new slug for this shared item.

        Sets a new slug to access this item by URL. The new slug must be unique.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            run-as (Optional[WorkflowsSlugSetSlugParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (SetSlugPayload)    : Request body. (json)

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/slug"

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

    async def workflows_slug_set_slug_2_2(
        self,
        workflow_id: str,
        body: SetSlugPayload,
        run_as: WorkflowsSlugSetSlugParamRunAs | None = None,
    ) -> None:
        """
        Set a new slug for this shared item.

        Sets a new slug to access this item by URL. The new slug must be unique.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            run-as (Optional[WorkflowsSlugSetSlugParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (SetSlugPayload)    : Request body. (json)

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/slug"

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

    async def workflows_tags_index(
        self,
        workflow_id: str,
        run_as: WorkflowsTagsIndexParamRunAs | None = None,
    ) -> ItemTagsListResponse:
        """
        Show tags based on workflow_id

        Args:
            workflow_id (str)        :
            run-as (Optional[WorkflowsTagsIndexParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ItemTagsListResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/tags"

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

    async def workflows_tags_delete(
        self,
        workflow_id: str,
        tag_name: str,
        run_as: WorkflowsTagsDeleteParamRunAs | None = None,
    ) -> bool:
        """
        Delete tag based on workflow_id

        Args:
            workflow_id (str)        :
            tag_name (str)           :
            run-as (Optional[WorkflowsTagsDeleteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            bool: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/tags/{tag_name}"

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

    async def workflows_tags_show(
        self,
        workflow_id: str,
        tag_name: str,
        run_as: WorkflowsTagsShowParamRunAs | None = None,
    ) -> ItemTagsResponse:
        """
        Show tag based on workflow_id

        Args:
            workflow_id (str)        :
            tag_name (str)           :
            run-as (Optional[WorkflowsTagsShowParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ItemTagsResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/tags/{tag_name}"

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

    async def workflows_tags_create(
        self,
        workflow_id: str,
        tag_name: str,
        run_as: WorkflowsTagsCreateParamRunAs | None = None,
        body: ItemTagsCreatePayload | None = None,
    ) -> ItemTagsResponse:
        """
        Create tag based on workflow_id

        Args:
            workflow_id (str)        :
            tag_name (str)           :
            run-as (Optional[WorkflowsTagsCreateParamRunAs])
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
        url = f"{self.base_url}/api/workflows/{workflow_id}/tags/{tag_name}"

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

    async def workflows_tags_update(
        self,
        workflow_id: str,
        tag_name: str,
        body: ItemTagsCreatePayload,
        run_as: WorkflowsTagsUpdateParamRunAs | None = None,
    ) -> ItemTagsResponse:
        """
        Update tag based on workflow_id

        Args:
            workflow_id (str)        :
            tag_name (str)           :
            run-as (Optional[WorkflowsTagsUpdateParamRunAs])
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
        url = f"{self.base_url}/api/workflows/{workflow_id}/tags/{tag_name}"

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

    async def workflows_undelete_undelete_workflow_2_2(
        self,
        workflow_id: str,
        run_as: WorkflowsUndeleteUndeleteWorkflowParamRunAs | None = None,
    ) -> Any:
        """
        Remove the deleted flag from a workflow.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            run-as (Optional[WorkflowsUndeleteUndeleteWorkflowParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/undelete"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_undelete_undelete_workflow_2_2(
        self,
        workflow_id: str,
        run_as: WorkflowsUndeleteUndeleteWorkflowParamRunAs | None = None,
    ) -> Any:
        """
        Remove the deleted flag from a workflow.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            run-as (Optional[WorkflowsUndeleteUndeleteWorkflowParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/undelete"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_unpublish_unpublish_2_2(
        self,
        workflow_id: str,
        run_as: WorkflowsUnpublishUnpublishParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Removes this item from the published list.

        Removes this item from the published list and return the current sharing status.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            run-as (Optional[WorkflowsUnpublishUnpublishParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            SharingStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/unpublish"

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

    async def workflows_unpublish_unpublish_2_2(
        self,
        workflow_id: str,
        run_as: WorkflowsUnpublishUnpublishParamRunAs | None = None,
    ) -> SharingStatus:
        """
        Removes this item from the published list.

        Removes this item from the published list and return the current sharing status.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            run-as (Optional[WorkflowsUnpublishUnpublishParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            SharingStatus: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/unpublish"

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

    async def workflows_usage_index_workflow_invocations_2_2(
        self,
        workflow_id: str,
        history_id: WorkflowsUsageIndexWorkflowInvocationsParamHistoryId | None = None,
        job_id: WorkflowsUsageIndexWorkflowInvocationsParamJobId | None = None,
        user_id: WorkflowsUsageIndexWorkflowInvocationsParamUserId | None = None,
        sort_by: WorkflowsUsageIndexWorkflowInvocationsParamSortBy | None = None,
        sort_desc: bool | None = False,
        include_terminal: WorkflowsUsageIndexWorkflowInvocationsParamIncludeTerminal | None = True,
        limit: WorkflowsUsageIndexWorkflowInvocationsParamLimit | None = 20,
        offset: WorkflowsUsageIndexWorkflowInvocationsParamOffset | None = None,
        instance: WorkflowsUsageIndexWorkflowInvocationsParamInstance | None = False,
        view: WorkflowsUsageIndexWorkflowInvocationsParamView | None = None,
        step_details: bool | None = False,
        run_as: WorkflowsUsageIndexWorkflowInvocationsParamRunAs | None = None,
    ) -> list[WorkflowInvocationResponse]:
        """
        Get the list of a user's workflow invocations.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            history_id (Optional[WorkflowsUsageIndexWorkflowInvocationsParamHistoryId])
                                     : Return only invocations for this History ID
            job_id (Optional[WorkflowsUsageIndexWorkflowInvocationsParamJobId])
                                     : Return only invocations for this Job ID
            user_id (Optional[WorkflowsUsageIndexWorkflowInvocationsParamUserId])
                                     : Return invocations for this User ID.
            sort_by (Optional[WorkflowsUsageIndexWorkflowInvocationsParamSortBy])
                                     : Sort Workflow Invocations by this attribute
            sort_desc (Optional[bool]): Sort in descending order?
            include_terminal (Optional[WorkflowsUsageIndexWorkflowInvocationsParamIncludeTerminal])
                                     : Set to false to only include terminal Invocations.
            limit (Optional[WorkflowsUsageIndexWorkflowInvocationsParamLimit])
                                     : Limit the number of invocations to return.
            offset (Optional[WorkflowsUsageIndexWorkflowInvocationsParamOffset])
                                     : Number of invocations to skip.
            instance (Optional[WorkflowsUsageIndexWorkflowInvocationsParamInstance])
                                     : Is provided workflow id for Workflow instead of
                                       StoredWorkflow?
            view (Optional[WorkflowsUsageIndexWorkflowInvocationsParamView])
                                     : View to be passed to the serializer
            step_details (Optional[bool])
                                     : Include details for individual invocation steps and
                                       populate a steps attribute in the resulting dictionary.
            run-as (Optional[WorkflowsUsageIndexWorkflowInvocationsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[WorkflowInvocationResponse]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/usage"

        params: dict[str, Any] = {
            **({"history_id": history_id} if history_id is not None else {}),
            **({"job_id": job_id} if job_id is not None else {}),
            **({"user_id": user_id} if user_id is not None else {}),
            **({"sort_by": sort_by} if sort_by is not None else {}),
            **({"sort_desc": sort_desc} if sort_desc is not None else {}),
            **({"include_terminal": include_terminal} if include_terminal is not None else {}),
            **({"limit": limit} if limit is not None else {}),
            **({"offset": offset} if offset is not None else {}),
            **({"instance": instance} if instance is not None else {}),
            **({"view": view} if view is not None else {}),
            **({"step_details": step_details} if step_details is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[WorkflowInvocationResponse], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_usage_index_workflow_invocations_2_2(
        self,
        workflow_id: str,
        history_id: WorkflowsUsageIndexWorkflowInvocationsParamHistoryId | None = None,
        job_id: WorkflowsUsageIndexWorkflowInvocationsParamJobId | None = None,
        user_id: WorkflowsUsageIndexWorkflowInvocationsParamUserId | None = None,
        sort_by: WorkflowsUsageIndexWorkflowInvocationsParamSortBy | None = None,
        sort_desc: bool | None = False,
        include_terminal: WorkflowsUsageIndexWorkflowInvocationsParamIncludeTerminal | None = True,
        limit: WorkflowsUsageIndexWorkflowInvocationsParamLimit | None = 20,
        offset: WorkflowsUsageIndexWorkflowInvocationsParamOffset | None = None,
        instance: WorkflowsUsageIndexWorkflowInvocationsParamInstance | None = False,
        view: WorkflowsUsageIndexWorkflowInvocationsParamView | None = None,
        step_details: bool | None = False,
        run_as: WorkflowsUsageIndexWorkflowInvocationsParamRunAs | None = None,
    ) -> list[WorkflowInvocationResponse]:
        """
        Get the list of a user's workflow invocations.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            history_id (Optional[WorkflowsUsageIndexWorkflowInvocationsParamHistoryId])
                                     : Return only invocations for this History ID
            job_id (Optional[WorkflowsUsageIndexWorkflowInvocationsParamJobId])
                                     : Return only invocations for this Job ID
            user_id (Optional[WorkflowsUsageIndexWorkflowInvocationsParamUserId])
                                     : Return invocations for this User ID.
            sort_by (Optional[WorkflowsUsageIndexWorkflowInvocationsParamSortBy])
                                     : Sort Workflow Invocations by this attribute
            sort_desc (Optional[bool]): Sort in descending order?
            include_terminal (Optional[WorkflowsUsageIndexWorkflowInvocationsParamIncludeTerminal])
                                     : Set to false to only include terminal Invocations.
            limit (Optional[WorkflowsUsageIndexWorkflowInvocationsParamLimit])
                                     : Limit the number of invocations to return.
            offset (Optional[WorkflowsUsageIndexWorkflowInvocationsParamOffset])
                                     : Number of invocations to skip.
            instance (Optional[WorkflowsUsageIndexWorkflowInvocationsParamInstance])
                                     : Is provided workflow id for Workflow instead of
                                       StoredWorkflow?
            view (Optional[WorkflowsUsageIndexWorkflowInvocationsParamView])
                                     : View to be passed to the serializer
            step_details (Optional[bool])
                                     : Include details for individual invocation steps and
                                       populate a steps attribute in the resulting dictionary.
            run-as (Optional[WorkflowsUsageIndexWorkflowInvocationsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[WorkflowInvocationResponse]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/usage"

        params: dict[str, Any] = {
            **({"history_id": history_id} if history_id is not None else {}),
            **({"job_id": job_id} if job_id is not None else {}),
            **({"user_id": user_id} if user_id is not None else {}),
            **({"sort_by": sort_by} if sort_by is not None else {}),
            **({"sort_desc": sort_desc} if sort_desc is not None else {}),
            **({"include_terminal": include_terminal} if include_terminal is not None else {}),
            **({"limit": limit} if limit is not None else {}),
            **({"offset": offset} if offset is not None else {}),
            **({"instance": instance} if instance is not None else {}),
            **({"view": view} if view is not None else {}),
            **({"step_details": step_details} if step_details is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[WorkflowInvocationResponse], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_usage_invoke_2_2(
        self,
        workflow_id: WorkflowsUsageInvokeParamWorkflowId,
        body: InvokeWorkflowPayload,
        run_as: WorkflowsUsageInvokeParamRunAs | None = None,
    ) -> WorkflowsUsageInvoke200Response2:
        """
        Schedule the workflow specified by `workflow_id` to run.

        Args:
            workflow_id (WorkflowsUsageInvokeParamWorkflowId)
                                     : The database identifier - UUID or encoded - of the
                                       Workflow.
            run-as (Optional[WorkflowsUsageInvokeParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (InvokeWorkflowPayload)
                                     : Request body. (json)

        Returns:
            WorkflowsUsageInvoke200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/usage"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: InvokeWorkflowPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(WorkflowsUsageInvoke200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_usage_invoke_2_2(
        self,
        workflow_id: WorkflowsUsageInvokeParamWorkflowId,
        body: InvokeWorkflowPayload,
        run_as: WorkflowsUsageInvokeParamRunAs | None = None,
    ) -> WorkflowsUsageInvoke200Response2:
        """
        Schedule the workflow specified by `workflow_id` to run.

        Args:
            workflow_id (WorkflowsUsageInvokeParamWorkflowId)
                                     : The database identifier - UUID or encoded - of the
                                       Workflow.
            run-as (Optional[WorkflowsUsageInvokeParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (InvokeWorkflowPayload)
                                     : Request body. (json)

        Returns:
            WorkflowsUsageInvoke200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/usage"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: InvokeWorkflowPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(WorkflowsUsageInvoke200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_usage_cancel_workflow_invocation_2_2(
        self,
        invocation_id: str,
        workflow_id: str,
        step_details: bool | None = False,
        legacy_job_state: bool | None = False,
        run_as: WorkflowsUsageCancelWorkflowInvocationParamRunAs | None = None,
    ) -> WorkflowInvocationResponse:
        """
        Cancel the specified workflow invocation.

        An alias for `DELETE /api/invocations/{invocation_id}`. `workflow_id` is ignored.

        Args:
            invocation_id (str)      : The encoded database identifier of the Invocation.
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            step_details (Optional[bool])
                                     : Include details for individual invocation steps and
                                       populate a steps attribute in the resulting dictionary.
            legacy_job_state (Optional[bool])
                                     : Populate the invocation step state with the job state
                                       instead of the invocation step state.         This will
                                       also produce one step per job in mapping jobs to mimic
                                       the older behavior with respect to collections.
                                       Partially scheduled steps may provide incomplete
                                       information and the listed steps outputs         are not
                                       the mapped over step outputs but the individual job
                                       outputs.
            run-as (Optional[WorkflowsUsageCancelWorkflowInvocationParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            WorkflowInvocationResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/usage/{invocation_id}"

        params: dict[str, Any] = {
            **({"step_details": step_details} if step_details is not None else {}),
            **({"legacy_job_state": legacy_job_state} if legacy_job_state is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(WorkflowInvocationResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_usage_cancel_workflow_invocation_2_2(
        self,
        invocation_id: str,
        workflow_id: str,
        step_details: bool | None = False,
        legacy_job_state: bool | None = False,
        run_as: WorkflowsUsageCancelWorkflowInvocationParamRunAs | None = None,
    ) -> WorkflowInvocationResponse:
        """
        Cancel the specified workflow invocation.

        An alias for `DELETE /api/invocations/{invocation_id}`. `workflow_id` is ignored.

        Args:
            invocation_id (str)      : The encoded database identifier of the Invocation.
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            step_details (Optional[bool])
                                     : Include details for individual invocation steps and
                                       populate a steps attribute in the resulting dictionary.
            legacy_job_state (Optional[bool])
                                     : Populate the invocation step state with the job state
                                       instead of the invocation step state.         This will
                                       also produce one step per job in mapping jobs to mimic
                                       the older behavior with respect to collections.
                                       Partially scheduled steps may provide incomplete
                                       information and the listed steps outputs         are not
                                       the mapped over step outputs but the individual job
                                       outputs.
            run-as (Optional[WorkflowsUsageCancelWorkflowInvocationParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            WorkflowInvocationResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/usage/{invocation_id}"

        params: dict[str, Any] = {
            **({"step_details": step_details} if step_details is not None else {}),
            **({"legacy_job_state": legacy_job_state} if legacy_job_state is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(WorkflowInvocationResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_usage_show_workflow_invocation_2_2(
        self,
        workflow_id: str,
        invocation_id: str,
        step_details: bool | None = False,
        legacy_job_state: bool | None = False,
        run_as: WorkflowsUsageShowWorkflowInvocationParamRunAs | None = None,
    ) -> WorkflowInvocationResponse:
        """
        Get detailed description of a workflow invocation.

        An alias for `GET /api/invocations/{invocation_id}`. `workflow_id` is ignored.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            invocation_id (str)      : The encoded database identifier of the Invocation.
            step_details (Optional[bool])
                                     : Include details for individual invocation steps and
                                       populate a steps attribute in the resulting dictionary.
            legacy_job_state (Optional[bool])
                                     : Populate the invocation step state with the job state
                                       instead of the invocation step state.         This will
                                       also produce one step per job in mapping jobs to mimic
                                       the older behavior with respect to collections.
                                       Partially scheduled steps may provide incomplete
                                       information and the listed steps outputs         are not
                                       the mapped over step outputs but the individual job
                                       outputs.
            run-as (Optional[WorkflowsUsageShowWorkflowInvocationParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            WorkflowInvocationResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/usage/{invocation_id}"

        params: dict[str, Any] = {
            **({"step_details": step_details} if step_details is not None else {}),
            **({"legacy_job_state": legacy_job_state} if legacy_job_state is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(WorkflowInvocationResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_usage_show_workflow_invocation_2_2(
        self,
        workflow_id: str,
        invocation_id: str,
        step_details: bool | None = False,
        legacy_job_state: bool | None = False,
        run_as: WorkflowsUsageShowWorkflowInvocationParamRunAs | None = None,
    ) -> WorkflowInvocationResponse:
        """
        Get detailed description of a workflow invocation.

        An alias for `GET /api/invocations/{invocation_id}`. `workflow_id` is ignored.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            invocation_id (str)      : The encoded database identifier of the Invocation.
            step_details (Optional[bool])
                                     : Include details for individual invocation steps and
                                       populate a steps attribute in the resulting dictionary.
            legacy_job_state (Optional[bool])
                                     : Populate the invocation step state with the job state
                                       instead of the invocation step state.         This will
                                       also produce one step per job in mapping jobs to mimic
                                       the older behavior with respect to collections.
                                       Partially scheduled steps may provide incomplete
                                       information and the listed steps outputs         are not
                                       the mapped over step outputs but the individual job
                                       outputs.
            run-as (Optional[WorkflowsUsageShowWorkflowInvocationParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            WorkflowInvocationResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/usage/{invocation_id}"

        params: dict[str, Any] = {
            **({"step_details": step_details} if step_details is not None else {}),
            **({"legacy_job_state": legacy_job_state} if legacy_job_state is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(WorkflowInvocationResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_usage_jobs_summary_workflow_invocation_jobs_summary_2_2(
        self,
        workflow_id: str,
        invocation_id: str,
        run_as: WorkflowsUsageJobsSummaryWorkflowInvocationJobsSummaryParamRunAs | None = None,
    ) -> InvocationJobsResponse:
        """
        Get job state summary info aggregated across all current jobs of the workflow
        invocation.

        An alias for `GET /api/invocations/{invocation_id}/jobs_summary`. `workflow_id` is
        ignored.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            invocation_id (str)      : The encoded database identifier of the Invocation.
            run-as (Optional[WorkflowsUsageJobsSummaryWorkflowInvocationJobsSummaryParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            InvocationJobsResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/usage/{invocation_id}/jobs_summary"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(InvocationJobsResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_usage_jobs_summary_workflow_invocation_jobs_summary_2_2(
        self,
        workflow_id: str,
        invocation_id: str,
        run_as: WorkflowsUsageJobsSummaryWorkflowInvocationJobsSummaryParamRunAs | None = None,
    ) -> InvocationJobsResponse:
        """
        Get job state summary info aggregated across all current jobs of the workflow
        invocation.

        An alias for `GET /api/invocations/{invocation_id}/jobs_summary`. `workflow_id` is
        ignored.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            invocation_id (str)      : The encoded database identifier of the Invocation.
            run-as (Optional[WorkflowsUsageJobsSummaryWorkflowInvocationJobsSummaryParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            InvocationJobsResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/usage/{invocation_id}/jobs_summary"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(InvocationJobsResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_usage_report_show_workflow_invocation_report_2_2(
        self,
        invocation_id: str,
        workflow_id: str,
        run_as: WorkflowsUsageReportShowWorkflowInvocationReportParamRunAs | None = None,
    ) -> InvocationReport:
        """
        Get JSON summarizing invocation for reporting.

        An alias for `GET /api/invocations/{invocation_id}/report`. `workflow_id` is ignored.

        Args:
            invocation_id (str)      : The encoded database identifier of the Invocation.
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            run-as (Optional[WorkflowsUsageReportShowWorkflowInvocationReportParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            InvocationReport: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/usage/{invocation_id}/report"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(InvocationReport, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_usage_report_show_workflow_invocation_report_2_2(
        self,
        invocation_id: str,
        workflow_id: str,
        run_as: WorkflowsUsageReportShowWorkflowInvocationReportParamRunAs | None = None,
    ) -> InvocationReport:
        """
        Get JSON summarizing invocation for reporting.

        An alias for `GET /api/invocations/{invocation_id}/report`. `workflow_id` is ignored.

        Args:
            invocation_id (str)      : The encoded database identifier of the Invocation.
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            run-as (Optional[WorkflowsUsageReportShowWorkflowInvocationReportParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            InvocationReport: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/usage/{invocation_id}/report"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(InvocationReport, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_usage_report_pdf_show_workflow_invocation_report_pdf_2_2(
        self,
        workflow_id: str,
        invocation_id: str,
        run_as: WorkflowsUsageReportPdfShowWorkflowInvocationReportPdfParamRunAs | None = None,
    ) -> None:
        """
        Get PDF summarizing invocation for reporting.

        An alias for `GET /api/invocations/{invocation_id}/report.pdf`. `workflow_id` is
        ignored.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            invocation_id (str)      : The encoded database identifier of the Invocation.
            run-as (Optional[WorkflowsUsageReportPdfShowWorkflowInvocationReportPdfParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/usage/{invocation_id}/report.pdf"

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

    async def workflows_usage_report_pdf_show_workflow_invocation_report_pdf_2_2(
        self,
        workflow_id: str,
        invocation_id: str,
        run_as: WorkflowsUsageReportPdfShowWorkflowInvocationReportPdfParamRunAs | None = None,
    ) -> None:
        """
        Get PDF summarizing invocation for reporting.

        An alias for `GET /api/invocations/{invocation_id}/report.pdf`. `workflow_id` is
        ignored.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            invocation_id (str)      : The encoded database identifier of the Invocation.
            run-as (Optional[WorkflowsUsageReportPdfShowWorkflowInvocationReportPdfParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/usage/{invocation_id}/report.pdf"

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

    async def workflows_usage_step_jobs_summary_workflow_invocation_step_jobs_summary_2_2(
        self,
        workflow_id: str,
        invocation_id: str,
        run_as: WorkflowsUsageStepJobsSummaryWorkflowInvocationStepJobsSummaryParamRunAs | None = None,
    ) -> list[AnonymousArrayItem228]:
        """
        Get job state summary info aggregated per step of the workflow invocation.

        An alias for `GET /api/invocations/{invocation_id}/step_jobs_summary`. `workflow_id` is
        ignored.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            invocation_id (str)      : The encoded database identifier of the Invocation.
            run-as (Optional[WorkflowsUsageStepJobsSummaryWorkflowInvocationStepJobsSummaryParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem228]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/usage/{invocation_id}/step_jobs_summary"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem228], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_usage_step_jobs_summary_workflow_invocation_step_jobs_summary_2_2(
        self,
        workflow_id: str,
        invocation_id: str,
        run_as: WorkflowsUsageStepJobsSummaryWorkflowInvocationStepJobsSummaryParamRunAs | None = None,
    ) -> list[AnonymousArrayItem228]:
        """
        Get job state summary info aggregated per step of the workflow invocation.

        An alias for `GET /api/invocations/{invocation_id}/step_jobs_summary`. `workflow_id` is
        ignored.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            invocation_id (str)      : The encoded database identifier of the Invocation.
            run-as (Optional[WorkflowsUsageStepJobsSummaryWorkflowInvocationStepJobsSummaryParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem228]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/usage/{invocation_id}/step_jobs_summary"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem228], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_usage_steps_workflow_invocation_step_2_2(
        self,
        workflow_id: str,
        invocation_id: str,
        step_id: str,
        run_as: WorkflowsUsageStepsWorkflowInvocationStepParamRunAs | None = None,
    ) -> InvocationStep:
        """
        Show details of workflow invocation step.

        An alias for `GET /api/invocations/{invocation_id}/steps/{step_id}`. `workflow_id` and
        `invocation_id` are ignored.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            invocation_id (str)      : The encoded database identifier of the Invocation.
            step_id (str)            : The encoded database identifier of the
                                       WorkflowInvocationStep.
            run-as (Optional[WorkflowsUsageStepsWorkflowInvocationStepParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            InvocationStep: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/usage/{invocation_id}/steps/{step_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(InvocationStep, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_usage_steps_workflow_invocation_step_2_2(
        self,
        workflow_id: str,
        invocation_id: str,
        step_id: str,
        run_as: WorkflowsUsageStepsWorkflowInvocationStepParamRunAs | None = None,
    ) -> InvocationStep:
        """
        Show details of workflow invocation step.

        An alias for `GET /api/invocations/{invocation_id}/steps/{step_id}`. `workflow_id` and
        `invocation_id` are ignored.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            invocation_id (str)      : The encoded database identifier of the Invocation.
            step_id (str)            : The encoded database identifier of the
                                       WorkflowInvocationStep.
            run-as (Optional[WorkflowsUsageStepsWorkflowInvocationStepParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            InvocationStep: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/usage/{invocation_id}/steps/{step_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(InvocationStep, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_usage_steps_update_workflow_invocation_step_2_2(
        self,
        workflow_id: str,
        invocation_id: str,
        step_id: str,
        body: InvocationUpdatePayload,
        run_as: WorkflowsUsageStepsUpdateWorkflowInvocationStepParamRunAs | None = None,
    ) -> InvocationStep:
        """
        Update state of running workflow step invocation.

        An alias for `PUT /api/invocations/{invocation_id}/steps/{step_id}`. `workflow_id` is
        ignored.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            invocation_id (str)      : The encoded database identifier of the Invocation.
            step_id (str)            : The encoded database identifier of the
                                       WorkflowInvocationStep.
            run-as (Optional[WorkflowsUsageStepsUpdateWorkflowInvocationStepParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (InvocationUpdatePayload)
                                     : Request body. (json)

        Returns:
            InvocationStep: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/usage/{invocation_id}/steps/{step_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: InvocationUpdatePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(InvocationStep, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_usage_steps_update_workflow_invocation_step_2_2(
        self,
        workflow_id: str,
        invocation_id: str,
        step_id: str,
        body: InvocationUpdatePayload,
        run_as: WorkflowsUsageStepsUpdateWorkflowInvocationStepParamRunAs | None = None,
    ) -> InvocationStep:
        """
        Update state of running workflow step invocation.

        An alias for `PUT /api/invocations/{invocation_id}/steps/{step_id}`. `workflow_id` is
        ignored.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            invocation_id (str)      : The encoded database identifier of the Invocation.
            step_id (str)            : The encoded database identifier of the
                                       WorkflowInvocationStep.
            run-as (Optional[WorkflowsUsageStepsUpdateWorkflowInvocationStepParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (InvocationUpdatePayload)
                                     : Request body. (json)

        Returns:
            InvocationStep: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/usage/{invocation_id}/steps/{step_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: InvocationUpdatePayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(InvocationStep, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def workflows_versions_show_versions_2_2(
        self,
        workflow_id: str,
        instance: WorkflowsVersionsShowVersionsParamInstance | None = False,
        run_as: WorkflowsVersionsShowVersionsParamRunAs | None = None,
    ) -> Any:
        """
        List all versions of a workflow.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            instance (Optional[WorkflowsVersionsShowVersionsParamInstance])
                                     :
            run-as (Optional[WorkflowsVersionsShowVersionsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/versions"

        params: dict[str, Any] = {
            **({"instance": instance} if instance is not None else {}),
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

    async def workflows_versions_show_versions_2_2(
        self,
        workflow_id: str,
        instance: WorkflowsVersionsShowVersionsParamInstance | None = False,
        run_as: WorkflowsVersionsShowVersionsParamRunAs | None = None,
    ) -> Any:
        """
        List all versions of a workflow.

        Args:
            workflow_id (str)        : The encoded database identifier of the Stored Workflow.
            instance (Optional[WorkflowsVersionsShowVersionsParamInstance])
                                     :
            run-as (Optional[WorkflowsVersionsShowVersionsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/workflows/{workflow_id}/versions"

        params: dict[str, Any] = {
            **({"instance": instance} if instance is not None else {}),
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
