from typing import Any, cast

from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.anonymous_array_item_127 import AnonymousArrayItem127
from ..models.anonymous_array_item_210 import AnonymousArrayItem210
from ..models.anonymous_array_item_212 import AnonymousArrayItem212
from ..models.anonymous_array_item_214 import AnonymousArrayItem214
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
from ..models.jobs_delete_request_body_2 import JobsDeleteRequestBody2
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
from ..models.jobs_show_200_response_2 import JobsShow200Response2
from ..models.jobs_show_param_full import JobsShowParamFull
from ..models.jobs_show_param_run_as import JobsShowParamRunAs
from ..models.report_job_error_payload import ReportJobErrorPayload
from ..models.search_jobs_payload import SearchJobsPayload


class JobsClient:
    """Client for jobs endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def jobs_metrics_metrics_by_dataset_2_2(
        self,
        dataset_id: str,
        hda_ldda: DatasetSourceType | None = None,
        run_as: JobsMetricsMetricsByDatasetParamRunAs | None = None,
    ) -> list[AnonymousArrayItem127]:
        """
        Return job metrics for specified job.

        Args:
            dataset_id (str)         : The ID of the dataset
            hda_ldda (Optional[DatasetSourceType])
                                     : Whether this dataset belongs to a history (HDA) or a
                                       library (LDDA).
            run-as (Optional[JobsMetricsMetricsByDatasetParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem127]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets/{dataset_id}/metrics"

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
                return cast(list[AnonymousArrayItem127], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def jobs_metrics_metrics_by_dataset_2_2(
        self,
        dataset_id: str,
        hda_ldda: DatasetSourceType | None = None,
        run_as: JobsMetricsMetricsByDatasetParamRunAs | None = None,
    ) -> list[AnonymousArrayItem127]:
        """
        Return job metrics for specified job.

        Args:
            dataset_id (str)         : The ID of the dataset
            hda_ldda (Optional[DatasetSourceType])
                                     : Whether this dataset belongs to a history (HDA) or a
                                       library (LDDA).
            run-as (Optional[JobsMetricsMetricsByDatasetParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem127]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets/{dataset_id}/metrics"

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
                return cast(list[AnonymousArrayItem127], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def jobs_parameters_display_parameters_display_by_dataset_2_2(
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
            hda_ldda (Optional[DatasetSourceType])
                                     : Whether this dataset belongs to a history (HDA) or a
                                       library (LDDA).
            run-as (Optional[JobsParametersDisplayParametersDisplayByDatasetParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            JobDisplayParametersSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets/{dataset_id}/parameters_display"

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
                return cast(JobDisplayParametersSummary, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def jobs_parameters_display_parameters_display_by_dataset_2_2(
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
            hda_ldda (Optional[DatasetSourceType])
                                     : Whether this dataset belongs to a history (HDA) or a
                                       library (LDDA).
            run-as (Optional[JobsParametersDisplayParametersDisplayByDatasetParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            JobDisplayParametersSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/datasets/{dataset_id}/parameters_display"

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
                return cast(JobDisplayParametersSummary, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def jobs_index_2_2(
        self,
        user_details: bool | None = False,
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
        limit: int | None = 500,
        offset: int | None = 0,
        state: JobsIndexParamState | None = None,
        tool_id: JobsIndexParamToolId | None = None,
        tool_id_like: JobsIndexParamToolIdLike | None = None,
        run_as: JobsIndexParamRunAs | None = None,
    ) -> list[AnonymousArrayItem210]:
        """
        Index

        Args:
            user_details (Optional[bool])
                                     : If true, and requester is an admin, will return external
                                       job id and user email. This is only available to admins.
            user_id (Optional[JobsIndexParamUserId])
                                     : an encoded user id to restrict query to, must be own id
                                       if not admin user
            view (Optional[JobIndexViewEnum])
                                     : Determines columns to return. Defaults to 'collection'.
            date_range_min (Optional[JobsIndexParamDateRangeMin])
                                     : Limit listing of jobs to those that are updated after
                                       specified date (e.g. '2014-01-01')
            date_range_max (Optional[JobsIndexParamDateRangeMax])
                                     : Limit listing of jobs to those that are updated before
                                       specified date (e.g. '2014-01-01')
            history_id (Optional[JobsIndexParamHistoryId])
                                     : Limit listing of jobs to those that match the history_id.
                                       If none, jobs from any history may be returned.
            workflow_id (Optional[JobsIndexParamWorkflowId])
                                     : Limit listing of jobs to those that match the specified
                                       workflow ID. If none, jobs from any workflow (or from no
                                       workflows) may be returned.
            invocation_id (Optional[JobsIndexParamInvocationId])
                                     : Limit listing of jobs to those that match the specified
                                       workflow invocation ID. If none, jobs from any workflow
                                       invocation (or from no workflows) may be returned.
            implicit_collection_jobs_id (Optional[JobsIndexParamImplicitCollectionJobsId])
                                     : Limit listing of jobs to those that match the specified
                                       implicit collection job ID. If none, jobs from any
                                       implicit collection execution (or from no implicit
                                       collection execution) may be returned.
            tool_request_id (Optional[JobsIndexParamToolRequestId])
                                     : Limit listing of jobs to those that were created from the
                                       supplied tool request ID. If none, jobs from any tool
                                       request (or from no workflows) may be returned.
            order_by (Optional[JobIndexSortByEnum])
                                     : Sort results by specified field.
            search (Optional[JobsIndexParamSearch])
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
            limit (Optional[int])    : Maximum number of jobs to return.
            offset (Optional[int])   : Return jobs starting from this specified position. For
                                       example, if ``limit`` is set to 100 and ``offset`` to
                                       200, jobs 200-299 will be returned.
            state (Optional[JobsIndexParamState])
                                     : A list or comma-separated list of states to filter job
                                       query on. If unspecified, jobs of any state may be
                                       returned.
            tool_id (Optional[JobsIndexParamToolId])
                                     : Limit listing of jobs to those that match one of the
                                       included tool_ids. If none, all are returned
            tool_id_like (Optional[JobsIndexParamToolIdLike])
                                     : Limit listing of jobs to those that match one of the
                                       included tool ID sql-like patterns. If none, all are
                                       returned
            run-as (Optional[JobsIndexParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem210]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/jobs"

        params: dict[str, Any] = {
            **({"user_details": user_details} if user_details is not None else {}),
            **({"user_id": user_id} if user_id is not None else {}),
            **({"view": view} if view is not None else {}),
            **({"date_range_min": date_range_min} if date_range_min is not None else {}),
            **({"date_range_max": date_range_max} if date_range_max is not None else {}),
            **({"history_id": history_id} if history_id is not None else {}),
            **({"workflow_id": workflow_id} if workflow_id is not None else {}),
            **({"invocation_id": invocation_id} if invocation_id is not None else {}),
            **(
                {"implicit_collection_jobs_id": implicit_collection_jobs_id}
                if implicit_collection_jobs_id is not None
                else {}
            ),
            **({"tool_request_id": tool_request_id} if tool_request_id is not None else {}),
            **({"order_by": order_by} if order_by is not None else {}),
            **({"search": search} if search is not None else {}),
            **({"limit": limit} if limit is not None else {}),
            **({"offset": offset} if offset is not None else {}),
            **({"state": state} if state is not None else {}),
            **({"tool_id": tool_id} if tool_id is not None else {}),
            **({"tool_id_like": tool_id_like} if tool_id_like is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem210], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def jobs_index_2_2(
        self,
        user_details: bool | None = False,
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
        limit: int | None = 500,
        offset: int | None = 0,
        state: JobsIndexParamState | None = None,
        tool_id: JobsIndexParamToolId | None = None,
        tool_id_like: JobsIndexParamToolIdLike | None = None,
        run_as: JobsIndexParamRunAs | None = None,
    ) -> list[AnonymousArrayItem210]:
        """
        Index

        Args:
            user_details (Optional[bool])
                                     : If true, and requester is an admin, will return external
                                       job id and user email. This is only available to admins.
            user_id (Optional[JobsIndexParamUserId])
                                     : an encoded user id to restrict query to, must be own id
                                       if not admin user
            view (Optional[JobIndexViewEnum])
                                     : Determines columns to return. Defaults to 'collection'.
            date_range_min (Optional[JobsIndexParamDateRangeMin])
                                     : Limit listing of jobs to those that are updated after
                                       specified date (e.g. '2014-01-01')
            date_range_max (Optional[JobsIndexParamDateRangeMax])
                                     : Limit listing of jobs to those that are updated before
                                       specified date (e.g. '2014-01-01')
            history_id (Optional[JobsIndexParamHistoryId])
                                     : Limit listing of jobs to those that match the history_id.
                                       If none, jobs from any history may be returned.
            workflow_id (Optional[JobsIndexParamWorkflowId])
                                     : Limit listing of jobs to those that match the specified
                                       workflow ID. If none, jobs from any workflow (or from no
                                       workflows) may be returned.
            invocation_id (Optional[JobsIndexParamInvocationId])
                                     : Limit listing of jobs to those that match the specified
                                       workflow invocation ID. If none, jobs from any workflow
                                       invocation (or from no workflows) may be returned.
            implicit_collection_jobs_id (Optional[JobsIndexParamImplicitCollectionJobsId])
                                     : Limit listing of jobs to those that match the specified
                                       implicit collection job ID. If none, jobs from any
                                       implicit collection execution (or from no implicit
                                       collection execution) may be returned.
            tool_request_id (Optional[JobsIndexParamToolRequestId])
                                     : Limit listing of jobs to those that were created from the
                                       supplied tool request ID. If none, jobs from any tool
                                       request (or from no workflows) may be returned.
            order_by (Optional[JobIndexSortByEnum])
                                     : Sort results by specified field.
            search (Optional[JobsIndexParamSearch])
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
            limit (Optional[int])    : Maximum number of jobs to return.
            offset (Optional[int])   : Return jobs starting from this specified position. For
                                       example, if ``limit`` is set to 100 and ``offset`` to
                                       200, jobs 200-299 will be returned.
            state (Optional[JobsIndexParamState])
                                     : A list or comma-separated list of states to filter job
                                       query on. If unspecified, jobs of any state may be
                                       returned.
            tool_id (Optional[JobsIndexParamToolId])
                                     : Limit listing of jobs to those that match one of the
                                       included tool_ids. If none, all are returned
            tool_id_like (Optional[JobsIndexParamToolIdLike])
                                     : Limit listing of jobs to those that match one of the
                                       included tool ID sql-like patterns. If none, all are
                                       returned
            run-as (Optional[JobsIndexParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem210]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/jobs"

        params: dict[str, Any] = {
            **({"user_details": user_details} if user_details is not None else {}),
            **({"user_id": user_id} if user_id is not None else {}),
            **({"view": view} if view is not None else {}),
            **({"date_range_min": date_range_min} if date_range_min is not None else {}),
            **({"date_range_max": date_range_max} if date_range_max is not None else {}),
            **({"history_id": history_id} if history_id is not None else {}),
            **({"workflow_id": workflow_id} if workflow_id is not None else {}),
            **({"invocation_id": invocation_id} if invocation_id is not None else {}),
            **(
                {"implicit_collection_jobs_id": implicit_collection_jobs_id}
                if implicit_collection_jobs_id is not None
                else {}
            ),
            **({"tool_request_id": tool_request_id} if tool_request_id is not None else {}),
            **({"order_by": order_by} if order_by is not None else {}),
            **({"search": search} if search is not None else {}),
            **({"limit": limit} if limit is not None else {}),
            **({"offset": offset} if offset is not None else {}),
            **({"state": state} if state is not None else {}),
            **({"tool_id": tool_id} if tool_id is not None else {}),
            **({"tool_id_like": tool_id_like} if tool_id_like is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem210], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def jobs_create_2_2(
        self,
        body: JobRequest,
        run_as: JobsCreateParamRunAs | None = None,
    ) -> JobCreateResponse:
        """
        Create

        Args:
            run-as (Optional[JobsCreateParamRunAs])
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
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: JobRequest = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(JobCreateResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def jobs_create_2_2(
        self,
        body: JobRequest,
        run_as: JobsCreateParamRunAs | None = None,
    ) -> JobCreateResponse:
        """
        Create

        Args:
            run-as (Optional[JobsCreateParamRunAs])
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
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: JobRequest = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(JobCreateResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def jobs_search_search_2_2(
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
            run-as (Optional[JobsSearchSearchParamRunAs])
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
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: SearchJobsPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[EncodedJobDetails], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def jobs_search_search_2_2(
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
            run-as (Optional[JobsSearchSearchParamRunAs])
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
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: SearchJobsPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[EncodedJobDetails], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def jobs_delete_2_2(
        self,
        job_id: str,
        run_as: JobsDeleteParamRunAs | None = None,
        body: JobsDeleteRequestBody2 | None = None,
    ) -> bool:
        """
        Cancels specified job

        Args:
            job_id (str)             : The ID of the job
            run-as (Optional[JobsDeleteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (Optional[JobsDeleteRequestBody2])
                                     : Request body. (json)

        Returns:
            bool: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/jobs/{job_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: JobsDeleteRequestBody2 | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("DELETE", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(bool, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def jobs_delete_2_2(
        self,
        job_id: str,
        run_as: JobsDeleteParamRunAs | None = None,
        body: JobsDeleteRequestBody2 | None = None,
    ) -> bool:
        """
        Cancels specified job

        Args:
            job_id (str)             : The ID of the job
            run-as (Optional[JobsDeleteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (Optional[JobsDeleteRequestBody2])
                                     : Request body. (json)

        Returns:
            bool: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/jobs/{job_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: JobsDeleteRequestBody2 | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("DELETE", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(bool, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def jobs_show_2_2(
        self,
        job_id: str,
        full: JobsShowParamFull | None = False,
        run_as: JobsShowParamRunAs | None = None,
    ) -> JobsShow200Response2:
        """
        Return dictionary containing description of job data.

        Args:
            job_id (str)             : The ID of the job
            full (Optional[JobsShowParamFull])
                                     : Show extra information.
            run-as (Optional[JobsShowParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            JobsShow200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/jobs/{job_id}"

        params: dict[str, Any] = {
            **({"full": full} if full is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(JobsShow200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def jobs_show_2_2(
        self,
        job_id: str,
        full: JobsShowParamFull | None = False,
        run_as: JobsShowParamRunAs | None = None,
    ) -> JobsShow200Response2:
        """
        Return dictionary containing description of job data.

        Args:
            job_id (str)             : The ID of the job
            full (Optional[JobsShowParamFull])
                                     : Show extra information.
            run-as (Optional[JobsShowParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            JobsShow200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/jobs/{job_id}"

        params: dict[str, Any] = {
            **({"full": full} if full is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(JobsShow200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def jobs_common_problems_common_problems_2_2(
        self,
        job_id: str,
        run_as: JobsCommonProblemsCommonProblemsParamRunAs | None = None,
    ) -> JobInputSummary:
        """
        Check inputs and job for common potential problems to aid in error reporting

        Args:
            job_id (str)             : The ID of the job
            run-as (Optional[JobsCommonProblemsCommonProblemsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            JobInputSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/jobs/{job_id}/common_problems"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(JobInputSummary, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def jobs_common_problems_common_problems_2_2(
        self,
        job_id: str,
        run_as: JobsCommonProblemsCommonProblemsParamRunAs | None = None,
    ) -> JobInputSummary:
        """
        Check inputs and job for common potential problems to aid in error reporting

        Args:
            job_id (str)             : The ID of the job
            run-as (Optional[JobsCommonProblemsCommonProblemsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            JobInputSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/jobs/{job_id}/common_problems"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(JobInputSummary, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def jobs_console_output_console_output_2_2(
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
            run-as (Optional[JobsConsoleOutputConsoleOutputParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            JobConsoleOutput: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/jobs/{job_id}/console_output"

        params: dict[str, Any] = {
            "stdout_position": stdout_position,
            "stdout_length": stdout_length,
            "stderr_position": stderr_position,
            "stderr_length": stderr_length,
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(JobConsoleOutput, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def jobs_console_output_console_output_2_2(
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
            run-as (Optional[JobsConsoleOutputConsoleOutputParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            JobConsoleOutput: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/jobs/{job_id}/console_output"

        params: dict[str, Any] = {
            "stdout_position": stdout_position,
            "stdout_length": stdout_length,
            "stderr_position": stderr_position,
            "stderr_length": stderr_length,
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(JobConsoleOutput, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def jobs_destination_params_destination_params_2_2(
        self,
        job_id: str,
        run_as: JobsDestinationParamsDestinationParamsParamRunAs | None = None,
    ) -> JobDestinationParams:
        """
        Return destination parameters for specified job.

        Args:
            job_id (str)             : The ID of the job
            run-as (Optional[JobsDestinationParamsDestinationParamsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            JobDestinationParams: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/jobs/{job_id}/destination_params"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(JobDestinationParams, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def jobs_destination_params_destination_params_2_2(
        self,
        job_id: str,
        run_as: JobsDestinationParamsDestinationParamsParamRunAs | None = None,
    ) -> JobDestinationParams:
        """
        Return destination parameters for specified job.

        Args:
            job_id (str)             : The ID of the job
            run-as (Optional[JobsDestinationParamsDestinationParamsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            JobDestinationParams: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/jobs/{job_id}/destination_params"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(JobDestinationParams, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def jobs_error_error_2_2(
        self,
        job_id: str,
        body: ReportJobErrorPayload,
        run_as: JobsErrorErrorParamRunAs | None = None,
    ) -> JobErrorSummary:
        """
        Submits a bug report via the API.

        Args:
            job_id (str)             : The ID of the job
            run-as (Optional[JobsErrorErrorParamRunAs])
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
        url = f"{self.base_url}/api/jobs/{job_id}/error"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: ReportJobErrorPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(JobErrorSummary, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def jobs_error_error_2_2(
        self,
        job_id: str,
        body: ReportJobErrorPayload,
        run_as: JobsErrorErrorParamRunAs | None = None,
    ) -> JobErrorSummary:
        """
        Submits a bug report via the API.

        Args:
            job_id (str)             : The ID of the job
            run-as (Optional[JobsErrorErrorParamRunAs])
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
        url = f"{self.base_url}/api/jobs/{job_id}/error"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: ReportJobErrorPayload = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(JobErrorSummary, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def jobs_inputs_inputs_2_2(
        self,
        job_id: str,
        run_as: JobsInputsInputsParamRunAs | None = None,
    ) -> list[JobInputAssociation]:
        """
        Returns input datasets created by a job.

        Args:
            job_id (str)             : The ID of the job
            run-as (Optional[JobsInputsInputsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[JobInputAssociation]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/jobs/{job_id}/inputs"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[JobInputAssociation], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def jobs_inputs_inputs_2_2(
        self,
        job_id: str,
        run_as: JobsInputsInputsParamRunAs | None = None,
    ) -> list[JobInputAssociation]:
        """
        Returns input datasets created by a job.

        Args:
            job_id (str)             : The ID of the job
            run-as (Optional[JobsInputsInputsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[JobInputAssociation]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/jobs/{job_id}/inputs"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[JobInputAssociation], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def jobs_metrics_metrics_by_job_2_2(
        self,
        job_id: str,
        hda_ldda: JobsMetricsMetricsByJobParamHdaLdda | None = "hda",
        run_as: JobsMetricsMetricsByJobParamRunAs | None = None,
    ) -> list[AnonymousArrayItem212]:
        """
        Return job metrics for specified job.

        Args:
            job_id (str)             : The ID of the job
            hda_ldda (Optional[JobsMetricsMetricsByJobParamHdaLdda])
                                     : Whether this dataset belongs to a history (HDA) or a
                                       library (LDDA).
            run-as (Optional[JobsMetricsMetricsByJobParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem212]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/jobs/{job_id}/metrics"

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
                return cast(list[AnonymousArrayItem212], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def jobs_metrics_metrics_by_job_2_2(
        self,
        job_id: str,
        hda_ldda: JobsMetricsMetricsByJobParamHdaLdda | None = "hda",
        run_as: JobsMetricsMetricsByJobParamRunAs | None = None,
    ) -> list[AnonymousArrayItem212]:
        """
        Return job metrics for specified job.

        Args:
            job_id (str)             : The ID of the job
            hda_ldda (Optional[JobsMetricsMetricsByJobParamHdaLdda])
                                     : Whether this dataset belongs to a history (HDA) or a
                                       library (LDDA).
            run-as (Optional[JobsMetricsMetricsByJobParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem212]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/jobs/{job_id}/metrics"

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
                return cast(list[AnonymousArrayItem212], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def jobs_outputs_outputs_2_2(
        self,
        job_id: str,
        run_as: JobsOutputsOutputsParamRunAs | None = None,
    ) -> list[AnonymousArrayItem214]:
        """
        Returns output datasets created by a job.

        Args:
            job_id (str)             : The ID of the job
            run-as (Optional[JobsOutputsOutputsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem214]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/jobs/{job_id}/outputs"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem214], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def jobs_outputs_outputs_2_2(
        self,
        job_id: str,
        run_as: JobsOutputsOutputsParamRunAs | None = None,
    ) -> list[AnonymousArrayItem214]:
        """
        Returns output datasets created by a job.

        Args:
            job_id (str)             : The ID of the job
            run-as (Optional[JobsOutputsOutputsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem214]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/jobs/{job_id}/outputs"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem214], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def jobs_parameters_display_parameters_display_by_job_2_2(
        self,
        job_id: str,
        hda_ldda: JobsParametersDisplayParametersDisplayByJobParamHdaLdda | None = "hda",
        run_as: JobsParametersDisplayParametersDisplayByJobParamRunAs | None = None,
    ) -> JobDisplayParametersSummary:
        """
        Resolve parameters as a list for nested display.

        **Warning**: This API is unstable and may change without notice.

        Args:
            job_id (str)             : The ID of the job
            hda_ldda (Optional[JobsParametersDisplayParametersDisplayByJobParamHdaLdda])
                                     : Whether this dataset belongs to a history (HDA) or a
                                       library (LDDA).
            run-as (Optional[JobsParametersDisplayParametersDisplayByJobParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            JobDisplayParametersSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/jobs/{job_id}/parameters_display"

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
                return cast(JobDisplayParametersSummary, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def jobs_parameters_display_parameters_display_by_job_2_2(
        self,
        job_id: str,
        hda_ldda: JobsParametersDisplayParametersDisplayByJobParamHdaLdda | None = "hda",
        run_as: JobsParametersDisplayParametersDisplayByJobParamRunAs | None = None,
    ) -> JobDisplayParametersSummary:
        """
        Resolve parameters as a list for nested display.

        **Warning**: This API is unstable and may change without notice.

        Args:
            job_id (str)             : The ID of the job
            hda_ldda (Optional[JobsParametersDisplayParametersDisplayByJobParamHdaLdda])
                                     : Whether this dataset belongs to a history (HDA) or a
                                       library (LDDA).
            run-as (Optional[JobsParametersDisplayParametersDisplayByJobParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            JobDisplayParametersSummary: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/jobs/{job_id}/parameters_display"

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
                return cast(JobDisplayParametersSummary, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def jobs_resume_resume_2_2(
        self,
        job_id: str,
        run_as: JobsResumeResumeParamRunAs | None = None,
    ) -> list[JobOutputAssociation]:
        """
        Resumes a paused job.

        Args:
            job_id (str)             : The ID of the job
            run-as (Optional[JobsResumeResumeParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[JobOutputAssociation]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/jobs/{job_id}/resume"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[JobOutputAssociation], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def jobs_resume_resume_2_2(
        self,
        job_id: str,
        run_as: JobsResumeResumeParamRunAs | None = None,
    ) -> list[JobOutputAssociation]:
        """
        Resumes a paused job.

        Args:
            job_id (str)             : The ID of the job
            run-as (Optional[JobsResumeResumeParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[JobOutputAssociation]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/jobs/{job_id}/resume"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[JobOutputAssociation], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover
