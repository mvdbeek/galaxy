from typing import Any, Protocol, cast, runtime_checkable

from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import structure_from_dict
from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.anonymous_array_item_87 import AnonymousArrayItem87
from ..models.anonymous_array_item_115 import AnonymousArrayItem115
from ..models.anonymous_array_item_117 import AnonymousArrayItem117
from ..models.anonymous_array_item_119 import AnonymousArrayItem119
from ..models.dataset_source_type import DatasetSourceType
from ..models.encoded_job_details import EncodedJobDetails
from ..models.job_console_output import JobConsoleOutput
from ..models.job_create_response import JobCreateResponse
from ..models.job_destination_params import JobDestinationParams
from ..models.job_display_parameters_summary import JobDisplayParametersSummary
from ..models.job_error_summary import JobErrorSummary
from ..models.job_index_sort_by_enum import JobIndexSortByEnum
from ..models.job_index_view_enum import JobIndexViewEnum
from ..models.job_input_association import JobInputAssociation
from ..models.job_input_summary import JobInputSummary
from ..models.job_output_association import JobOutputAssociation
from ..models.job_request import JobRequest
from ..models.jobs_common_problems_common_problems_param_run_as import JobsCommonProblemsCommonProblemsParamRunAs
from ..models.jobs_console_output_console_output_param_run_as import JobsConsoleOutputConsoleOutputParamRunAs
from ..models.jobs_create_param_run_as import JobsCreateParamRunAs
from ..models.jobs_delete_param_run_as import JobsDeleteParamRunAs
from ..models.jobs_delete_request_body import JobsDeleteRequestBody
from ..models.jobs_destination_params_destination_params_param_run_as import (
    JobsDestinationParamsDestinationParamsParamRunAs,
)
from ..models.jobs_error_error_param_run_as import JobsErrorErrorParamRunAs
from ..models.jobs_index_param_date_range_max import JobsIndexParamDateRangeMax
from ..models.jobs_index_param_date_range_min import JobsIndexParamDateRangeMin
from ..models.jobs_index_param_history_id import JobsIndexParamHistoryId
from ..models.jobs_index_param_implicit_collection_jobs_id import JobsIndexParamImplicitCollectionJobsId
from ..models.jobs_index_param_invocation_id import JobsIndexParamInvocationId
from ..models.jobs_index_param_run_as import JobsIndexParamRunAs
from ..models.jobs_index_param_search import JobsIndexParamSearch
from ..models.jobs_index_param_state import JobsIndexParamState
from ..models.jobs_index_param_tool_id import JobsIndexParamToolId
from ..models.jobs_index_param_tool_id_like import JobsIndexParamToolIdLike
from ..models.jobs_index_param_tool_request_id import JobsIndexParamToolRequestId
from ..models.jobs_index_param_user_id import JobsIndexParamUserId
from ..models.jobs_index_param_workflow_id import JobsIndexParamWorkflowId
from ..models.jobs_inputs_inputs_param_run_as import JobsInputsInputsParamRunAs
from ..models.jobs_metrics_metrics_by_dataset_param_run_as import JobsMetricsMetricsByDatasetParamRunAs
from ..models.jobs_metrics_metrics_by_job_param_hda_ldda import JobsMetricsMetricsByJobParamHdaLdda
from ..models.jobs_metrics_metrics_by_job_param_run_as import JobsMetricsMetricsByJobParamRunAs
from ..models.jobs_outputs_outputs_param_run_as import JobsOutputsOutputsParamRunAs
from ..models.jobs_parameters_display_parameters_display_by_dataset_param_run_as import (
    JobsParametersDisplayParametersDisplayByDatasetParamRunAs,
)
from ..models.jobs_parameters_display_parameters_display_by_job_param_hda_ldda import (
    JobsParametersDisplayParametersDisplayByJobParamHdaLdda,
)
from ..models.jobs_parameters_display_parameters_display_by_job_param_run_as import (
    JobsParametersDisplayParametersDisplayByJobParamRunAs,
)
from ..models.jobs_resume_resume_param_run_as import JobsResumeResumeParamRunAs
from ..models.jobs_search_search_param_run_as import JobsSearchSearchParamRunAs
from ..models.jobs_show_200_response import JobsShow200Response
from ..models.jobs_show_param_full import JobsShowParamFull
from ..models.jobs_show_param_run_as import JobsShowParamRunAs
from ..models.report_job_error_payload import ReportJobErrorPayload
from ..models.search_jobs_payload import SearchJobsPayload


@runtime_checkable
class JobsClientProtocol(Protocol):
    """Protocol defining the interface of JobsClient for dependency injection."""

    async def jobs_metrics_metrics_by_dataset(
        self,
        dataset_id: str,
        hda_ldda: DatasetSourceType | None = None,
        run_as: JobsMetricsMetricsByDatasetParamRunAs | None = None,
    ) -> list[AnonymousArrayItem87]: ...

    async def jobs_metrics_metrics_by_dataset(
        self,
        dataset_id: str,
        hda_ldda: DatasetSourceType | None = None,
        run_as: JobsMetricsMetricsByDatasetParamRunAs | None = None,
    ) -> list[AnonymousArrayItem87]: ...

    async def jobs_parameters_display_parameters_display_by_dataset(
        self,
        dataset_id: str,
        hda_ldda: DatasetSourceType | None = None,
        run_as: JobsParametersDisplayParametersDisplayByDatasetParamRunAs | None = None,
    ) -> JobDisplayParametersSummary: ...

    async def jobs_parameters_display_parameters_display_by_dataset(
        self,
        dataset_id: str,
        hda_ldda: DatasetSourceType | None = None,
        run_as: JobsParametersDisplayParametersDisplayByDatasetParamRunAs | None = None,
    ) -> JobDisplayParametersSummary: ...

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
    ) -> list[AnonymousArrayItem115]: ...

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
    ) -> list[AnonymousArrayItem115]: ...

    async def jobs_create(
        self,
        body: JobRequest,
        run_as: JobsCreateParamRunAs | None = None,
    ) -> JobCreateResponse: ...

    async def jobs_create(
        self,
        body: JobRequest,
        run_as: JobsCreateParamRunAs | None = None,
    ) -> JobCreateResponse: ...

    async def jobs_search_search(
        self,
        body: SearchJobsPayload,
        run_as: JobsSearchSearchParamRunAs | None = None,
    ) -> list[EncodedJobDetails]: ...

    async def jobs_search_search(
        self,
        body: SearchJobsPayload,
        run_as: JobsSearchSearchParamRunAs | None = None,
    ) -> list[EncodedJobDetails]: ...

    async def jobs_delete(
        self,
        job_id: str,
        run_as: JobsDeleteParamRunAs | None = None,
        body: JobsDeleteRequestBody | None = None,
    ) -> bool: ...

    async def jobs_delete(
        self,
        job_id: str,
        run_as: JobsDeleteParamRunAs | None = None,
        body: JobsDeleteRequestBody | None = None,
    ) -> bool: ...

    async def jobs_show(
        self,
        job_id: str,
        full: JobsShowParamFull | None = None,
        run_as: JobsShowParamRunAs | None = None,
    ) -> JobsShow200Response: ...

    async def jobs_show(
        self,
        job_id: str,
        full: JobsShowParamFull | None = None,
        run_as: JobsShowParamRunAs | None = None,
    ) -> JobsShow200Response: ...

    async def jobs_common_problems_common_problems(
        self,
        job_id: str,
        run_as: JobsCommonProblemsCommonProblemsParamRunAs | None = None,
    ) -> JobInputSummary: ...

    async def jobs_common_problems_common_problems(
        self,
        job_id: str,
        run_as: JobsCommonProblemsCommonProblemsParamRunAs | None = None,
    ) -> JobInputSummary: ...

    async def jobs_console_output_console_output(
        self,
        job_id: str,
        stdout_position: int,
        stdout_length: int,
        stderr_position: int,
        stderr_length: int,
        run_as: JobsConsoleOutputConsoleOutputParamRunAs | None = None,
    ) -> JobConsoleOutput: ...

    async def jobs_console_output_console_output(
        self,
        job_id: str,
        stdout_position: int,
        stdout_length: int,
        stderr_position: int,
        stderr_length: int,
        run_as: JobsConsoleOutputConsoleOutputParamRunAs | None = None,
    ) -> JobConsoleOutput: ...

    async def jobs_destination_params_destination_params(
        self,
        job_id: str,
        run_as: JobsDestinationParamsDestinationParamsParamRunAs | None = None,
    ) -> JobDestinationParams: ...

    async def jobs_destination_params_destination_params(
        self,
        job_id: str,
        run_as: JobsDestinationParamsDestinationParamsParamRunAs | None = None,
    ) -> JobDestinationParams: ...

    async def jobs_error_error(
        self,
        job_id: str,
        body: ReportJobErrorPayload,
        run_as: JobsErrorErrorParamRunAs | None = None,
    ) -> JobErrorSummary: ...

    async def jobs_error_error(
        self,
        job_id: str,
        body: ReportJobErrorPayload,
        run_as: JobsErrorErrorParamRunAs | None = None,
    ) -> JobErrorSummary: ...

    async def jobs_inputs_inputs(
        self,
        job_id: str,
        run_as: JobsInputsInputsParamRunAs | None = None,
    ) -> list[JobInputAssociation]: ...

    async def jobs_inputs_inputs(
        self,
        job_id: str,
        run_as: JobsInputsInputsParamRunAs | None = None,
    ) -> list[JobInputAssociation]: ...

    async def jobs_metrics_metrics_by_job(
        self,
        job_id: str,
        hda_ldda: JobsMetricsMetricsByJobParamHdaLdda | None = None,
        run_as: JobsMetricsMetricsByJobParamRunAs | None = None,
    ) -> list[AnonymousArrayItem117]: ...

    async def jobs_metrics_metrics_by_job(
        self,
        job_id: str,
        hda_ldda: JobsMetricsMetricsByJobParamHdaLdda | None = None,
        run_as: JobsMetricsMetricsByJobParamRunAs | None = None,
    ) -> list[AnonymousArrayItem117]: ...

    async def jobs_outputs_outputs(
        self,
        job_id: str,
        run_as: JobsOutputsOutputsParamRunAs | None = None,
    ) -> list[AnonymousArrayItem119]: ...

    async def jobs_outputs_outputs(
        self,
        job_id: str,
        run_as: JobsOutputsOutputsParamRunAs | None = None,
    ) -> list[AnonymousArrayItem119]: ...

    async def jobs_parameters_display_parameters_display_by_job(
        self,
        job_id: str,
        hda_ldda: JobsParametersDisplayParametersDisplayByJobParamHdaLdda | None = None,
        run_as: JobsParametersDisplayParametersDisplayByJobParamRunAs | None = None,
    ) -> JobDisplayParametersSummary: ...

    async def jobs_parameters_display_parameters_display_by_job(
        self,
        job_id: str,
        hda_ldda: JobsParametersDisplayParametersDisplayByJobParamHdaLdda | None = None,
        run_as: JobsParametersDisplayParametersDisplayByJobParamRunAs | None = None,
    ) -> JobDisplayParametersSummary: ...

    async def jobs_resume_resume(
        self,
        job_id: str,
        run_as: JobsResumeResumeParamRunAs | None = None,
    ) -> list[JobOutputAssociation]: ...

    async def jobs_resume_resume(
        self,
        job_id: str,
        run_as: JobsResumeResumeParamRunAs | None = None,
    ) -> list[JobOutputAssociation]: ...


class JobsClient(JobsClientProtocol):
    """Client for jobs endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def jobs_metrics_metrics_by_dataset(
        self,
        dataset_id: str,
        hda_ldda: DatasetSourceType | None = None,
        run_as: JobsMetricsMetricsByDatasetParamRunAs | None = None,
    ) -> list[AnonymousArrayItem87]:
        """
        Return job metrics for specified job.

        Args:
            dataset_id (str)         : The ID of the dataset
            hda_ldda (DatasetSourceType | None)
                                     : Whether this dataset belongs to a history (HDA) or a
                                       library (LDDA).
            run-as (JobsMetricsMetricsByDatasetParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem87]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        dataset_id = DataclassSerializer.serialize(dataset_id)

        url = f"{self.base_url}/api/datasets/{dataset_id}/metrics"

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
                return structure_from_dict(response.json(), list[AnonymousArrayItem87])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def jobs_metrics_metrics_by_dataset(
        self,
        dataset_id: str,
        hda_ldda: DatasetSourceType | None = None,
        run_as: JobsMetricsMetricsByDatasetParamRunAs | None = None,
    ) -> list[AnonymousArrayItem87]:
        """
        Return job metrics for specified job.

        Args:
            dataset_id (str)         : The ID of the dataset
            hda_ldda (DatasetSourceType | None)
                                     : Whether this dataset belongs to a history (HDA) or a
                                       library (LDDA).
            run-as (JobsMetricsMetricsByDatasetParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem87]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        dataset_id = DataclassSerializer.serialize(dataset_id)

        url = f"{self.base_url}/api/datasets/{dataset_id}/metrics"

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
                return structure_from_dict(response.json(), list[AnonymousArrayItem87])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def jobs_parameters_display_parameters_display_by_dataset(
        self,
        dataset_id: str,
        hda_ldda: DatasetSourceType | None = None,
        run_as: JobsParametersDisplayParametersDisplayByDatasetParamRunAs | None = None,
    ) -> JobDisplayParametersSummary:
        """
        Resolve parameters as a list for nested display.

        **Warning**: This API is unstable and may change without notice.

        Args:
            dataset_id (str)         : The ID of the dataset
            hda_ldda (DatasetSourceType | None)
                                     : Whether this dataset belongs to a history (HDA) or a
                                       library (LDDA).
            run-as (JobsParametersDisplayParametersDisplayByDatasetParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            JobDisplayParametersSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        dataset_id = DataclassSerializer.serialize(dataset_id)

        url = f"{self.base_url}/api/datasets/{dataset_id}/parameters_display"

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
                return structure_from_dict(response.json(), JobDisplayParametersSummary)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def jobs_parameters_display_parameters_display_by_dataset(
        self,
        dataset_id: str,
        hda_ldda: DatasetSourceType | None = None,
        run_as: JobsParametersDisplayParametersDisplayByDatasetParamRunAs | None = None,
    ) -> JobDisplayParametersSummary:
        """
        Resolve parameters as a list for nested display.

        **Warning**: This API is unstable and may change without notice.

        Args:
            dataset_id (str)         : The ID of the dataset
            hda_ldda (DatasetSourceType | None)
                                     : Whether this dataset belongs to a history (HDA) or a
                                       library (LDDA).
            run-as (JobsParametersDisplayParametersDisplayByDatasetParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            JobDisplayParametersSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        dataset_id = DataclassSerializer.serialize(dataset_id)

        url = f"{self.base_url}/api/datasets/{dataset_id}/parameters_display"

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
                return structure_from_dict(response.json(), JobDisplayParametersSummary)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

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
        Index

        Args:
            user_details (bool | None): If true, and requester is an admin, will return external
                                        job id and user email. This is only available to admins.
            user_id (JobsIndexParamUserId | None)
                                     : an encoded user id to restrict query to, must be own id
                                       if not admin user
            view (JobIndexViewEnum | None)
                                     : Determines columns to return. Defaults to 'collection'.
            date_range_min (JobsIndexParamDateRangeMin | None)
                                     : Limit listing of jobs to those that are updated after
                                       specified date (e.g. '2014-01-01')
            date_range_max (JobsIndexParamDateRangeMax | None)
                                     : Limit listing of jobs to those that are updated before
                                       specified date (e.g. '2014-01-01')
            history_id (JobsIndexParamHistoryId | None)
                                     : Limit listing of jobs to those that match the history_id.
                                       If none, jobs from any history may be returned.
            workflow_id (JobsIndexParamWorkflowId | None)
                                     : Limit listing of jobs to those that match the specified
                                       workflow ID. If none, jobs from any workflow (or from no
                                       workflows) may be returned.
            invocation_id (JobsIndexParamInvocationId | None)
                                     : Limit listing of jobs to those that match the specified
                                       workflow invocation ID. If none, jobs from any workflow
                                       invocation (or from no workflows) may be returned.
            implicit_collection_jobs_id (JobsIndexParamImplicitCollectionJobsId | None)
                                     : Limit listing of jobs to those that match the specified
                                       implicit collection job ID. If none, jobs from any
                                       implicit collection execution (or from no implicit
                                       collection execution) may be returned.
            tool_request_id (JobsIndexParamToolRequestId | None)
                                     : Limit listing of jobs to those that were created from the
                                       supplied tool request ID. If none, jobs from any tool
                                       request (or from no workflows) may be returned.
            order_by (JobIndexSortByEnum | None)
                                     : Sort results by specified field.
            search (JobsIndexParamSearch | None)
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
                                       Tags Available  `user` : The user email of the user that
                                       executed the Job. (The tag `u` can be used a short hand
                                       alias for this tag to filter on this attribute.)
                                       `tool_id` : The tool ID corresponding to the job. (The
                                       tag `t` can be used a short hand alias for this tag to
                                       filter on this attribute.)  `runner` : The job runner
                                       name used to execute the job. (The tag `r` can be used a
                                       short hand alias for this tag to filter on this
                                       attribute.) This tag is only available for requests using
                                       admin keys and/or sessions.  `handler` : The job handler
                                       name used to execute the job. (The tag `h` can be used a
                                       short hand alias for this tag to filter on this
                                       attribute.) This tag is only available for requests using
                                       admin keys and/or sessions.  ## Free Text  Free text
                                       search terms will be searched against the following
                                       attributes of the Jobs: `user`, `tool`, `handler`,
                                       `runner`.
            limit (int | None)       : Maximum number of jobs to return.
            offset (int | None)      : Return jobs starting from this specified position. For
                                       example, if ``limit`` is set to 100 and ``offset`` to
                                       200, jobs 200-299 will be returned.
            state (JobsIndexParamState | None)
                                     : A list or comma-separated list of states to filter job
                                       query on. If unspecified, jobs of any state may be
                                       returned.
            tool_id (JobsIndexParamToolId | None)
                                     : Limit listing of jobs to those that match one of the
                                       included tool_ids. If none, all are returned
            tool_id_like (JobsIndexParamToolIdLike | None)
                                     : Limit listing of jobs to those that match one of the
                                       included tool ID sql-like patterns. If none, all are
                                       returned
            run-as (JobsIndexParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem115]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/jobs"

        params: dict[str, Any] = {
            **({"user_details": DataclassSerializer.serialize(user_details)} if user_details is not None else {}),
            **({"user_id": DataclassSerializer.serialize(user_id)} if user_id is not None else {}),
            **({"view": DataclassSerializer.serialize(view)} if view is not None else {}),
            **({"date_range_min": DataclassSerializer.serialize(date_range_min)} if date_range_min is not None else {}),
            **({"date_range_max": DataclassSerializer.serialize(date_range_max)} if date_range_max is not None else {}),
            **({"history_id": DataclassSerializer.serialize(history_id)} if history_id is not None else {}),
            **({"workflow_id": DataclassSerializer.serialize(workflow_id)} if workflow_id is not None else {}),
            **({"invocation_id": DataclassSerializer.serialize(invocation_id)} if invocation_id is not None else {}),
            **(
                {"implicit_collection_jobs_id": DataclassSerializer.serialize(implicit_collection_jobs_id)}
                if implicit_collection_jobs_id is not None
                else {}
            ),
            **(
                {"tool_request_id": DataclassSerializer.serialize(tool_request_id)}
                if tool_request_id is not None
                else {}
            ),
            **({"order_by": DataclassSerializer.serialize(order_by)} if order_by is not None else {}),
            **({"search": DataclassSerializer.serialize(search)} if search is not None else {}),
            **({"limit": DataclassSerializer.serialize(limit)} if limit is not None else {}),
            **({"offset": DataclassSerializer.serialize(offset)} if offset is not None else {}),
            **({"state": DataclassSerializer.serialize(state)} if state is not None else {}),
            **({"tool_id": DataclassSerializer.serialize(tool_id)} if tool_id is not None else {}),
            **({"tool_id_like": DataclassSerializer.serialize(tool_id_like)} if tool_id_like is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[AnonymousArrayItem115])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

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
        Index

        Args:
            user_details (bool | None): If true, and requester is an admin, will return external
                                        job id and user email. This is only available to admins.
            user_id (JobsIndexParamUserId | None)
                                     : an encoded user id to restrict query to, must be own id
                                       if not admin user
            view (JobIndexViewEnum | None)
                                     : Determines columns to return. Defaults to 'collection'.
            date_range_min (JobsIndexParamDateRangeMin | None)
                                     : Limit listing of jobs to those that are updated after
                                       specified date (e.g. '2014-01-01')
            date_range_max (JobsIndexParamDateRangeMax | None)
                                     : Limit listing of jobs to those that are updated before
                                       specified date (e.g. '2014-01-01')
            history_id (JobsIndexParamHistoryId | None)
                                     : Limit listing of jobs to those that match the history_id.
                                       If none, jobs from any history may be returned.
            workflow_id (JobsIndexParamWorkflowId | None)
                                     : Limit listing of jobs to those that match the specified
                                       workflow ID. If none, jobs from any workflow (or from no
                                       workflows) may be returned.
            invocation_id (JobsIndexParamInvocationId | None)
                                     : Limit listing of jobs to those that match the specified
                                       workflow invocation ID. If none, jobs from any workflow
                                       invocation (or from no workflows) may be returned.
            implicit_collection_jobs_id (JobsIndexParamImplicitCollectionJobsId | None)
                                     : Limit listing of jobs to those that match the specified
                                       implicit collection job ID. If none, jobs from any
                                       implicit collection execution (or from no implicit
                                       collection execution) may be returned.
            tool_request_id (JobsIndexParamToolRequestId | None)
                                     : Limit listing of jobs to those that were created from the
                                       supplied tool request ID. If none, jobs from any tool
                                       request (or from no workflows) may be returned.
            order_by (JobIndexSortByEnum | None)
                                     : Sort results by specified field.
            search (JobsIndexParamSearch | None)
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
                                       Tags Available  `user` : The user email of the user that
                                       executed the Job. (The tag `u` can be used a short hand
                                       alias for this tag to filter on this attribute.)
                                       `tool_id` : The tool ID corresponding to the job. (The
                                       tag `t` can be used a short hand alias for this tag to
                                       filter on this attribute.)  `runner` : The job runner
                                       name used to execute the job. (The tag `r` can be used a
                                       short hand alias for this tag to filter on this
                                       attribute.) This tag is only available for requests using
                                       admin keys and/or sessions.  `handler` : The job handler
                                       name used to execute the job. (The tag `h` can be used a
                                       short hand alias for this tag to filter on this
                                       attribute.) This tag is only available for requests using
                                       admin keys and/or sessions.  ## Free Text  Free text
                                       search terms will be searched against the following
                                       attributes of the Jobs: `user`, `tool`, `handler`,
                                       `runner`.
            limit (int | None)       : Maximum number of jobs to return.
            offset (int | None)      : Return jobs starting from this specified position. For
                                       example, if ``limit`` is set to 100 and ``offset`` to
                                       200, jobs 200-299 will be returned.
            state (JobsIndexParamState | None)
                                     : A list or comma-separated list of states to filter job
                                       query on. If unspecified, jobs of any state may be
                                       returned.
            tool_id (JobsIndexParamToolId | None)
                                     : Limit listing of jobs to those that match one of the
                                       included tool_ids. If none, all are returned
            tool_id_like (JobsIndexParamToolIdLike | None)
                                     : Limit listing of jobs to those that match one of the
                                       included tool ID sql-like patterns. If none, all are
                                       returned
            run-as (JobsIndexParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem115]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/jobs"

        params: dict[str, Any] = {
            **({"user_details": DataclassSerializer.serialize(user_details)} if user_details is not None else {}),
            **({"user_id": DataclassSerializer.serialize(user_id)} if user_id is not None else {}),
            **({"view": DataclassSerializer.serialize(view)} if view is not None else {}),
            **({"date_range_min": DataclassSerializer.serialize(date_range_min)} if date_range_min is not None else {}),
            **({"date_range_max": DataclassSerializer.serialize(date_range_max)} if date_range_max is not None else {}),
            **({"history_id": DataclassSerializer.serialize(history_id)} if history_id is not None else {}),
            **({"workflow_id": DataclassSerializer.serialize(workflow_id)} if workflow_id is not None else {}),
            **({"invocation_id": DataclassSerializer.serialize(invocation_id)} if invocation_id is not None else {}),
            **(
                {"implicit_collection_jobs_id": DataclassSerializer.serialize(implicit_collection_jobs_id)}
                if implicit_collection_jobs_id is not None
                else {}
            ),
            **(
                {"tool_request_id": DataclassSerializer.serialize(tool_request_id)}
                if tool_request_id is not None
                else {}
            ),
            **({"order_by": DataclassSerializer.serialize(order_by)} if order_by is not None else {}),
            **({"search": DataclassSerializer.serialize(search)} if search is not None else {}),
            **({"limit": DataclassSerializer.serialize(limit)} if limit is not None else {}),
            **({"offset": DataclassSerializer.serialize(offset)} if offset is not None else {}),
            **({"state": DataclassSerializer.serialize(state)} if state is not None else {}),
            **({"tool_id": DataclassSerializer.serialize(tool_id)} if tool_id is not None else {}),
            **({"tool_id_like": DataclassSerializer.serialize(tool_id_like)} if tool_id_like is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[AnonymousArrayItem115])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def jobs_create(
        self,
        body: JobRequest,
        run_as: JobsCreateParamRunAs | None = None,
    ) -> JobCreateResponse:
        """
        Create

        Args:
            run-as (JobsCreateParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (JobRequest)        : Request body. (json)

        Returns:
            JobCreateResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/jobs"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: JobRequest = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), JobCreateResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def jobs_create(
        self,
        body: JobRequest,
        run_as: JobsCreateParamRunAs | None = None,
    ) -> JobCreateResponse:
        """
        Create

        Args:
            run-as (JobsCreateParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (JobRequest)        : Request body. (json)

        Returns:
            JobCreateResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/jobs"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: JobRequest = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), JobCreateResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def jobs_search_search(
        self,
        body: SearchJobsPayload,
        run_as: JobsSearchSearchParamRunAs | None = None,
    ) -> list[EncodedJobDetails]:
        """
        Return jobs for current user

        This method is designed to scan the list of previously run jobs and find records of jobs
        that had the exact some input parameters and datasets. This can be used to minimize the
        amount of repeated work, and simply recycle the old results.

        Args:
            run-as (JobsSearchSearchParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (SearchJobsPayload) : Request body. (json)

        Returns:
            List[EncodedJobDetails]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/jobs/search"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: SearchJobsPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[EncodedJobDetails])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def jobs_search_search(
        self,
        body: SearchJobsPayload,
        run_as: JobsSearchSearchParamRunAs | None = None,
    ) -> list[EncodedJobDetails]:
        """
        Return jobs for current user

        This method is designed to scan the list of previously run jobs and find records of jobs
        that had the exact some input parameters and datasets. This can be used to minimize the
        amount of repeated work, and simply recycle the old results.

        Args:
            run-as (JobsSearchSearchParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (SearchJobsPayload) : Request body. (json)

        Returns:
            List[EncodedJobDetails]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/jobs/search"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: SearchJobsPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[EncodedJobDetails])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def jobs_delete(
        self,
        job_id: str,
        run_as: JobsDeleteParamRunAs | None = None,
        body: JobsDeleteRequestBody | None = None,
    ) -> bool:
        """
        Cancels specified job

        Args:
            job_id (str)             : The ID of the job
            run-as (JobsDeleteParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (JobsDeleteRequestBody | None)
                                     : Request body. (json)

        Returns:
            bool: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        job_id = DataclassSerializer.serialize(job_id)

        url = f"{self.base_url}/api/jobs/{job_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: JobsDeleteRequestBody | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("DELETE", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(bool, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def jobs_delete(
        self,
        job_id: str,
        run_as: JobsDeleteParamRunAs | None = None,
        body: JobsDeleteRequestBody | None = None,
    ) -> bool:
        """
        Cancels specified job

        Args:
            job_id (str)             : The ID of the job
            run-as (JobsDeleteParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (JobsDeleteRequestBody | None)
                                     : Request body. (json)

        Returns:
            bool: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        job_id = DataclassSerializer.serialize(job_id)

        url = f"{self.base_url}/api/jobs/{job_id}"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: JobsDeleteRequestBody | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("DELETE", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(bool, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def jobs_show(
        self,
        job_id: str,
        full: JobsShowParamFull | None = None,
        run_as: JobsShowParamRunAs | None = None,
    ) -> JobsShow200Response:
        """
        Return dictionary containing description of job data.

        Args:
            job_id (str)             : The ID of the job
            full (JobsShowParamFull | None)
                                     : Show extra information.
            run-as (JobsShowParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            JobsShow200Response: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        job_id = DataclassSerializer.serialize(job_id)

        url = f"{self.base_url}/api/jobs/{job_id}"

        params: dict[str, Any] = {
            **({"full": DataclassSerializer.serialize(full)} if full is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), JobsShow200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def jobs_show(
        self,
        job_id: str,
        full: JobsShowParamFull | None = None,
        run_as: JobsShowParamRunAs | None = None,
    ) -> JobsShow200Response:
        """
        Return dictionary containing description of job data.

        Args:
            job_id (str)             : The ID of the job
            full (JobsShowParamFull | None)
                                     : Show extra information.
            run-as (JobsShowParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            JobsShow200Response: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        job_id = DataclassSerializer.serialize(job_id)

        url = f"{self.base_url}/api/jobs/{job_id}"

        params: dict[str, Any] = {
            **({"full": DataclassSerializer.serialize(full)} if full is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), JobsShow200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def jobs_common_problems_common_problems(
        self,
        job_id: str,
        run_as: JobsCommonProblemsCommonProblemsParamRunAs | None = None,
    ) -> JobInputSummary:
        """
        Check inputs and job for common potential problems to aid in error reporting

        Args:
            job_id (str)             : The ID of the job
            run-as (JobsCommonProblemsCommonProblemsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            JobInputSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        job_id = DataclassSerializer.serialize(job_id)

        url = f"{self.base_url}/api/jobs/{job_id}/common_problems"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), JobInputSummary)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def jobs_common_problems_common_problems(
        self,
        job_id: str,
        run_as: JobsCommonProblemsCommonProblemsParamRunAs | None = None,
    ) -> JobInputSummary:
        """
        Check inputs and job for common potential problems to aid in error reporting

        Args:
            job_id (str)             : The ID of the job
            run-as (JobsCommonProblemsCommonProblemsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            JobInputSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        job_id = DataclassSerializer.serialize(job_id)

        url = f"{self.base_url}/api/jobs/{job_id}/common_problems"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), JobInputSummary)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

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
        Returns STDOUT and STDERR from the tool running in a specific job.

        Get the stdout and/or stderr from the tool running in a specific job. The position
        parameters are the index of where to start reading stdout/stderr. The length parameters
        control how much stdout/stderr is read.

        Args:
            job_id (str)             : The ID of the job
            stdout_position (int)    :
            stdout_length (int)      :
            stderr_position (int)    :
            stderr_length (int)      :
            run-as (JobsConsoleOutputConsoleOutputParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            JobConsoleOutput: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        job_id = DataclassSerializer.serialize(job_id)

        url = f"{self.base_url}/api/jobs/{job_id}/console_output"

        params: dict[str, Any] = {
            "stdout_position": DataclassSerializer.serialize(stdout_position),
            "stdout_length": DataclassSerializer.serialize(stdout_length),
            "stderr_position": DataclassSerializer.serialize(stderr_position),
            "stderr_length": DataclassSerializer.serialize(stderr_length),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), JobConsoleOutput)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

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
        Returns STDOUT and STDERR from the tool running in a specific job.

        Get the stdout and/or stderr from the tool running in a specific job. The position
        parameters are the index of where to start reading stdout/stderr. The length parameters
        control how much stdout/stderr is read.

        Args:
            job_id (str)             : The ID of the job
            stdout_position (int)    :
            stdout_length (int)      :
            stderr_position (int)    :
            stderr_length (int)      :
            run-as (JobsConsoleOutputConsoleOutputParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            JobConsoleOutput: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        job_id = DataclassSerializer.serialize(job_id)

        url = f"{self.base_url}/api/jobs/{job_id}/console_output"

        params: dict[str, Any] = {
            "stdout_position": DataclassSerializer.serialize(stdout_position),
            "stdout_length": DataclassSerializer.serialize(stdout_length),
            "stderr_position": DataclassSerializer.serialize(stderr_position),
            "stderr_length": DataclassSerializer.serialize(stderr_length),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), JobConsoleOutput)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def jobs_destination_params_destination_params(
        self,
        job_id: str,
        run_as: JobsDestinationParamsDestinationParamsParamRunAs | None = None,
    ) -> JobDestinationParams:
        """
        Return destination parameters for specified job.

        Args:
            job_id (str)             : The ID of the job
            run-as (JobsDestinationParamsDestinationParamsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            JobDestinationParams: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        job_id = DataclassSerializer.serialize(job_id)

        url = f"{self.base_url}/api/jobs/{job_id}/destination_params"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), JobDestinationParams)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def jobs_destination_params_destination_params(
        self,
        job_id: str,
        run_as: JobsDestinationParamsDestinationParamsParamRunAs | None = None,
    ) -> JobDestinationParams:
        """
        Return destination parameters for specified job.

        Args:
            job_id (str)             : The ID of the job
            run-as (JobsDestinationParamsDestinationParamsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            JobDestinationParams: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        job_id = DataclassSerializer.serialize(job_id)

        url = f"{self.base_url}/api/jobs/{job_id}/destination_params"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), JobDestinationParams)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def jobs_error_error(
        self,
        job_id: str,
        body: ReportJobErrorPayload,
        run_as: JobsErrorErrorParamRunAs | None = None,
    ) -> JobErrorSummary:
        """
        Submits a bug report via the API.

        Args:
            job_id (str)             : The ID of the job
            run-as (JobsErrorErrorParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (ReportJobErrorPayload)
                                     : Request body. (json)

        Returns:
            JobErrorSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        job_id = DataclassSerializer.serialize(job_id)

        url = f"{self.base_url}/api/jobs/{job_id}/error"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: ReportJobErrorPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), JobErrorSummary)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def jobs_error_error(
        self,
        job_id: str,
        body: ReportJobErrorPayload,
        run_as: JobsErrorErrorParamRunAs | None = None,
    ) -> JobErrorSummary:
        """
        Submits a bug report via the API.

        Args:
            job_id (str)             : The ID of the job
            run-as (JobsErrorErrorParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (ReportJobErrorPayload)
                                     : Request body. (json)

        Returns:
            JobErrorSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        job_id = DataclassSerializer.serialize(job_id)

        url = f"{self.base_url}/api/jobs/{job_id}/error"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: ReportJobErrorPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), JobErrorSummary)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def jobs_inputs_inputs(
        self,
        job_id: str,
        run_as: JobsInputsInputsParamRunAs | None = None,
    ) -> list[JobInputAssociation]:
        """
        Returns input datasets created by a job.

        Args:
            job_id (str)             : The ID of the job
            run-as (JobsInputsInputsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[JobInputAssociation]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        job_id = DataclassSerializer.serialize(job_id)

        url = f"{self.base_url}/api/jobs/{job_id}/inputs"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[JobInputAssociation])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def jobs_inputs_inputs(
        self,
        job_id: str,
        run_as: JobsInputsInputsParamRunAs | None = None,
    ) -> list[JobInputAssociation]:
        """
        Returns input datasets created by a job.

        Args:
            job_id (str)             : The ID of the job
            run-as (JobsInputsInputsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[JobInputAssociation]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        job_id = DataclassSerializer.serialize(job_id)

        url = f"{self.base_url}/api/jobs/{job_id}/inputs"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[JobInputAssociation])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def jobs_metrics_metrics_by_job(
        self,
        job_id: str,
        hda_ldda: JobsMetricsMetricsByJobParamHdaLdda | None = None,
        run_as: JobsMetricsMetricsByJobParamRunAs | None = None,
    ) -> list[AnonymousArrayItem117]:
        """
        Return job metrics for specified job.

        Args:
            job_id (str)             : The ID of the job
            hda_ldda (JobsMetricsMetricsByJobParamHdaLdda | None)
                                     : Whether this dataset belongs to a history (HDA) or a
                                       library (LDDA).
            run-as (JobsMetricsMetricsByJobParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem117]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        job_id = DataclassSerializer.serialize(job_id)

        url = f"{self.base_url}/api/jobs/{job_id}/metrics"

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
                return structure_from_dict(response.json(), list[AnonymousArrayItem117])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def jobs_metrics_metrics_by_job(
        self,
        job_id: str,
        hda_ldda: JobsMetricsMetricsByJobParamHdaLdda | None = None,
        run_as: JobsMetricsMetricsByJobParamRunAs | None = None,
    ) -> list[AnonymousArrayItem117]:
        """
        Return job metrics for specified job.

        Args:
            job_id (str)             : The ID of the job
            hda_ldda (JobsMetricsMetricsByJobParamHdaLdda | None)
                                     : Whether this dataset belongs to a history (HDA) or a
                                       library (LDDA).
            run-as (JobsMetricsMetricsByJobParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem117]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        job_id = DataclassSerializer.serialize(job_id)

        url = f"{self.base_url}/api/jobs/{job_id}/metrics"

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
                return structure_from_dict(response.json(), list[AnonymousArrayItem117])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def jobs_outputs_outputs(
        self,
        job_id: str,
        run_as: JobsOutputsOutputsParamRunAs | None = None,
    ) -> list[AnonymousArrayItem119]:
        """
        Returns output datasets created by a job.

        Args:
            job_id (str)             : The ID of the job
            run-as (JobsOutputsOutputsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem119]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        job_id = DataclassSerializer.serialize(job_id)

        url = f"{self.base_url}/api/jobs/{job_id}/outputs"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[AnonymousArrayItem119])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def jobs_outputs_outputs(
        self,
        job_id: str,
        run_as: JobsOutputsOutputsParamRunAs | None = None,
    ) -> list[AnonymousArrayItem119]:
        """
        Returns output datasets created by a job.

        Args:
            job_id (str)             : The ID of the job
            run-as (JobsOutputsOutputsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem119]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        job_id = DataclassSerializer.serialize(job_id)

        url = f"{self.base_url}/api/jobs/{job_id}/outputs"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[AnonymousArrayItem119])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def jobs_parameters_display_parameters_display_by_job(
        self,
        job_id: str,
        hda_ldda: JobsParametersDisplayParametersDisplayByJobParamHdaLdda | None = None,
        run_as: JobsParametersDisplayParametersDisplayByJobParamRunAs | None = None,
    ) -> JobDisplayParametersSummary:
        """
        Resolve parameters as a list for nested display.

        **Warning**: This API is unstable and may change without notice.

        Args:
            job_id (str)             : The ID of the job
            hda_ldda (JobsParametersDisplayParametersDisplayByJobParamHdaLdda | None)
                                     : Whether this dataset belongs to a history (HDA) or a
                                       library (LDDA).
            run-as (JobsParametersDisplayParametersDisplayByJobParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            JobDisplayParametersSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        job_id = DataclassSerializer.serialize(job_id)

        url = f"{self.base_url}/api/jobs/{job_id}/parameters_display"

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
                return structure_from_dict(response.json(), JobDisplayParametersSummary)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def jobs_parameters_display_parameters_display_by_job(
        self,
        job_id: str,
        hda_ldda: JobsParametersDisplayParametersDisplayByJobParamHdaLdda | None = None,
        run_as: JobsParametersDisplayParametersDisplayByJobParamRunAs | None = None,
    ) -> JobDisplayParametersSummary:
        """
        Resolve parameters as a list for nested display.

        **Warning**: This API is unstable and may change without notice.

        Args:
            job_id (str)             : The ID of the job
            hda_ldda (JobsParametersDisplayParametersDisplayByJobParamHdaLdda | None)
                                     : Whether this dataset belongs to a history (HDA) or a
                                       library (LDDA).
            run-as (JobsParametersDisplayParametersDisplayByJobParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            JobDisplayParametersSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        job_id = DataclassSerializer.serialize(job_id)

        url = f"{self.base_url}/api/jobs/{job_id}/parameters_display"

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
                return structure_from_dict(response.json(), JobDisplayParametersSummary)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def jobs_resume_resume(
        self,
        job_id: str,
        run_as: JobsResumeResumeParamRunAs | None = None,
    ) -> list[JobOutputAssociation]:
        """
        Resumes a paused job.

        Args:
            job_id (str)             : The ID of the job
            run-as (JobsResumeResumeParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[JobOutputAssociation]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        job_id = DataclassSerializer.serialize(job_id)

        url = f"{self.base_url}/api/jobs/{job_id}/resume"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[JobOutputAssociation])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def jobs_resume_resume(
        self,
        job_id: str,
        run_as: JobsResumeResumeParamRunAs | None = None,
    ) -> list[JobOutputAssociation]:
        """
        Resumes a paused job.

        Args:
            job_id (str)             : The ID of the job
            run-as (JobsResumeResumeParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[JobOutputAssociation]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        job_id = DataclassSerializer.serialize(job_id)

        url = f"{self.base_url}/api/jobs/{job_id}/resume"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[JobOutputAssociation])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover
