from typing import TYPE_CHECKING

from ...models.anonymous_array_item_87 import AnonymousArrayItem87
from ...models.anonymous_array_item_115 import AnonymousArrayItem115
from ...models.anonymous_array_item_117 import AnonymousArrayItem117
from ...models.anonymous_array_item_119 import AnonymousArrayItem119
from ...models.dataset_source_type import DatasetSourceType
from ...models.encoded_job_details import EncodedJobDetails
from ...models.job_console_output import JobConsoleOutput
from ...models.job_create_response import JobCreateResponse
from ...models.job_destination_params import JobDestinationParams
from ...models.job_display_parameters_summary import JobDisplayParametersSummary
from ...models.job_error_summary import JobErrorSummary
from ...models.job_index_sort_by_enum import JobIndexSortByEnum
from ...models.job_index_view_enum import JobIndexViewEnum
from ...models.job_input_association import JobInputAssociation
from ...models.job_input_summary import JobInputSummary
from ...models.job_output_association import JobOutputAssociation
from ...models.job_request import JobRequest
from ...models.jobs_common_problems_common_problems_param_run_as import JobsCommonProblemsCommonProblemsParamRunAs
from ...models.jobs_console_output_console_output_param_run_as import JobsConsoleOutputConsoleOutputParamRunAs
from ...models.jobs_create_param_run_as import JobsCreateParamRunAs
from ...models.jobs_delete_param_run_as import JobsDeleteParamRunAs
from ...models.jobs_delete_request_body import JobsDeleteRequestBody
from ...models.jobs_destination_params_destination_params_param_run_as import (
    JobsDestinationParamsDestinationParamsParamRunAs,
)
from ...models.jobs_error_error_param_run_as import JobsErrorErrorParamRunAs
from ...models.jobs_index_param_date_range_max import JobsIndexParamDateRangeMax
from ...models.jobs_index_param_date_range_min import JobsIndexParamDateRangeMin
from ...models.jobs_index_param_history_id import JobsIndexParamHistoryId
from ...models.jobs_index_param_implicit_collection_jobs_id import JobsIndexParamImplicitCollectionJobsId
from ...models.jobs_index_param_invocation_id import JobsIndexParamInvocationId
from ...models.jobs_index_param_run_as import JobsIndexParamRunAs
from ...models.jobs_index_param_search import JobsIndexParamSearch
from ...models.jobs_index_param_state import JobsIndexParamState
from ...models.jobs_index_param_tool_id import JobsIndexParamToolId
from ...models.jobs_index_param_tool_id_like import JobsIndexParamToolIdLike
from ...models.jobs_index_param_tool_request_id import JobsIndexParamToolRequestId
from ...models.jobs_index_param_user_id import JobsIndexParamUserId
from ...models.jobs_index_param_workflow_id import JobsIndexParamWorkflowId
from ...models.jobs_inputs_inputs_param_run_as import JobsInputsInputsParamRunAs
from ...models.jobs_metrics_metrics_by_dataset_param_run_as import JobsMetricsMetricsByDatasetParamRunAs
from ...models.jobs_metrics_metrics_by_job_param_hda_ldda import JobsMetricsMetricsByJobParamHdaLdda
from ...models.jobs_metrics_metrics_by_job_param_run_as import JobsMetricsMetricsByJobParamRunAs
from ...models.jobs_outputs_outputs_param_run_as import JobsOutputsOutputsParamRunAs
from ...models.jobs_parameters_display_parameters_display_by_dataset_param_run_as import (
    JobsParametersDisplayParametersDisplayByDatasetParamRunAs,
)
from ...models.jobs_parameters_display_parameters_display_by_job_param_hda_ldda import (
    JobsParametersDisplayParametersDisplayByJobParamHdaLdda,
)
from ...models.jobs_parameters_display_parameters_display_by_job_param_run_as import (
    JobsParametersDisplayParametersDisplayByJobParamRunAs,
)
from ...models.jobs_resume_resume_param_run_as import JobsResumeResumeParamRunAs
from ...models.jobs_search_search_param_run_as import JobsSearchSearchParamRunAs
from ...models.jobs_show_200_response import JobsShow200Response
from ...models.jobs_show_param_full import JobsShowParamFull
from ...models.jobs_show_param_run_as import JobsShowParamRunAs
from ...models.report_job_error_payload import ReportJobErrorPayload
from ...models.search_jobs_payload import SearchJobsPayload

if TYPE_CHECKING:
    pass


class MockJobsClient:
    """
    Mock implementation of JobsClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestJobsClient(MockJobsClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def jobs_metrics_metrics_by_dataset(
        self,
        dataset_id: str,
        hda_ldda: DatasetSourceType | None = None,
        run_as: JobsMetricsMetricsByDatasetParamRunAs | None = None,
    ) -> list[AnonymousArrayItem87]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockJobsClient.jobs_metrics_metrics_by_dataset() not implemented. Override this method in your test subclass."
        )

    async def jobs_parameters_display_parameters_display_by_dataset(
        self,
        dataset_id: str,
        hda_ldda: DatasetSourceType | None = None,
        run_as: JobsParametersDisplayParametersDisplayByDatasetParamRunAs | None = None,
    ) -> JobDisplayParametersSummary:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockJobsClient.jobs_parameters_display_parameters_display_by_dataset() not implemented. Override this method in your test subclass."
        )

    async def jobs_index(
        self,
        user_details: bool | None = None,
        user_id: JobsIndexParamUserId | None = None,
        view: JobIndexViewEnum | None = None,
        date_range_min: JobsIndexParamDateRangeMin | None = None,
        date_range_max: JobsIndexParamDateRangeMax | None = None,
        history_id: JobsIndexParamHistoryId | None = None,
        workflow_id: JobsIndexParamWorkflowId | None = None,
        invocation_id: JobsIndexParamInvocationId | None = None,
        implicit_collection_jobs_id: JobsIndexParamImplicitCollectionJobsId | None = None,
        tool_request_id: JobsIndexParamToolRequestId | None = None,
        order_by: JobIndexSortByEnum | None = None,
        search: JobsIndexParamSearch | None = None,
        limit: int | None = None,
        offset: int | None = None,
        state: JobsIndexParamState | None = None,
        tool_id: JobsIndexParamToolId | None = None,
        tool_id_like: JobsIndexParamToolIdLike | None = None,
        run_as: JobsIndexParamRunAs | None = None,
    ) -> list[AnonymousArrayItem115]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockJobsClient.jobs_index() not implemented. Override this method in your test subclass."
        )

    async def jobs_create(
        self,
        body: JobRequest,
        run_as: JobsCreateParamRunAs | None = None,
    ) -> JobCreateResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockJobsClient.jobs_create() not implemented. Override this method in your test subclass."
        )

    async def jobs_search_search(
        self,
        body: SearchJobsPayload,
        run_as: JobsSearchSearchParamRunAs | None = None,
    ) -> list[EncodedJobDetails]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockJobsClient.jobs_search_search() not implemented. Override this method in your test subclass."
        )

    async def jobs_delete(
        self,
        job_id: str,
        run_as: JobsDeleteParamRunAs | None = None,
        body: JobsDeleteRequestBody | None = None,
    ) -> bool:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockJobsClient.jobs_delete() not implemented. Override this method in your test subclass."
        )

    async def jobs_show(
        self,
        job_id: str,
        full: JobsShowParamFull | None = None,
        run_as: JobsShowParamRunAs | None = None,
    ) -> JobsShow200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockJobsClient.jobs_show() not implemented. Override this method in your test subclass."
        )

    async def jobs_common_problems_common_problems(
        self,
        job_id: str,
        run_as: JobsCommonProblemsCommonProblemsParamRunAs | None = None,
    ) -> JobInputSummary:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockJobsClient.jobs_common_problems_common_problems() not implemented. Override this method in your test subclass."
        )

    async def jobs_console_output_console_output(
        self,
        job_id: str,
        stdout_position: int,
        stdout_length: int,
        stderr_position: int,
        stderr_length: int,
        run_as: JobsConsoleOutputConsoleOutputParamRunAs | None = None,
    ) -> JobConsoleOutput:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockJobsClient.jobs_console_output_console_output() not implemented. Override this method in your test subclass."
        )

    async def jobs_destination_params_destination_params(
        self,
        job_id: str,
        run_as: JobsDestinationParamsDestinationParamsParamRunAs | None = None,
    ) -> JobDestinationParams:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockJobsClient.jobs_destination_params_destination_params() not implemented. Override this method in your test subclass."
        )

    async def jobs_error_error(
        self,
        job_id: str,
        body: ReportJobErrorPayload,
        run_as: JobsErrorErrorParamRunAs | None = None,
    ) -> JobErrorSummary:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockJobsClient.jobs_error_error() not implemented. Override this method in your test subclass."
        )

    async def jobs_inputs_inputs(
        self,
        job_id: str,
        run_as: JobsInputsInputsParamRunAs | None = None,
    ) -> list[JobInputAssociation]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockJobsClient.jobs_inputs_inputs() not implemented. Override this method in your test subclass."
        )

    async def jobs_metrics_metrics_by_job(
        self,
        job_id: str,
        hda_ldda: JobsMetricsMetricsByJobParamHdaLdda | None = None,
        run_as: JobsMetricsMetricsByJobParamRunAs | None = None,
    ) -> list[AnonymousArrayItem117]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockJobsClient.jobs_metrics_metrics_by_job() not implemented. Override this method in your test subclass."
        )

    async def jobs_outputs_outputs(
        self,
        job_id: str,
        run_as: JobsOutputsOutputsParamRunAs | None = None,
    ) -> list[AnonymousArrayItem119]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockJobsClient.jobs_outputs_outputs() not implemented. Override this method in your test subclass."
        )

    async def jobs_parameters_display_parameters_display_by_job(
        self,
        job_id: str,
        hda_ldda: JobsParametersDisplayParametersDisplayByJobParamHdaLdda | None = None,
        run_as: JobsParametersDisplayParametersDisplayByJobParamRunAs | None = None,
    ) -> JobDisplayParametersSummary:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockJobsClient.jobs_parameters_display_parameters_display_by_job() not implemented. Override this method in your test subclass."
        )

    async def jobs_resume_resume(
        self,
        job_id: str,
        run_as: JobsResumeResumeParamRunAs | None = None,
    ) -> list[JobOutputAssociation]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockJobsClient.jobs_resume_resume() not implemented. Override this method in your test subclass."
        )
