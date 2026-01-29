from typing import Any, Protocol, runtime_checkable

from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import structure_from_dict
from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.agent_list_response import AgentListResponse
from ..models.agent_query_request import AgentQueryRequest
from ..models.agent_query_response import AgentQueryResponse
from ..models.agent_response import AgentResponse
from ..models.ai_agents_custom_tool_create_custom_tool_param_run_as import AiAgentsCustomToolCreateCustomToolParamRunAs
from ..models.ai_agents_error_analysis_analyze_error_param_run_as import AiAgentsErrorAnalysisAnalyzeErrorParamRunAs
from ..models.ai_agents_list_agents_param_run_as import AiAgentsListAgentsParamRunAs
from ..models.ai_agents_query_query_agent_param_run_as import AiAgentsQueryQueryAgentParamRunAs
from ..models.body_ai_agents_custom_tool_create_custom_tool_2 import BodyAiAgentsCustomToolCreateCustomTool2
from ..models.body_ai_agents_error_analysis_analyze_error_2 import BodyAiAgentsErrorAnalysisAnalyzeError2


@runtime_checkable
class AiClientProtocol(Protocol):
    """Protocol defining the interface of AiClient for dependency injection."""

    async def ai_agents_list_agents(
        self,
        run_as: AiAgentsListAgentsParamRunAs | None = None,
    ) -> AgentListResponse: ...

    async def ai_agents_list_agents(
        self,
        run_as: AiAgentsListAgentsParamRunAs | None = None,
    ) -> AgentListResponse: ...

    async def ai_agents_custom_tool_create_custom_tool(
        self,
        body: BodyAiAgentsCustomToolCreateCustomTool2,
        run_as: AiAgentsCustomToolCreateCustomToolParamRunAs | None = None,
    ) -> AgentResponse: ...

    async def ai_agents_custom_tool_create_custom_tool(
        self,
        body: BodyAiAgentsCustomToolCreateCustomTool2,
        run_as: AiAgentsCustomToolCreateCustomToolParamRunAs | None = None,
    ) -> AgentResponse: ...

    async def ai_agents_error_analysis_analyze_error(
        self,
        body: BodyAiAgentsErrorAnalysisAnalyzeError2,
        run_as: AiAgentsErrorAnalysisAnalyzeErrorParamRunAs | None = None,
    ) -> AgentResponse: ...

    async def ai_agents_error_analysis_analyze_error(
        self,
        body: BodyAiAgentsErrorAnalysisAnalyzeError2,
        run_as: AiAgentsErrorAnalysisAnalyzeErrorParamRunAs | None = None,
    ) -> AgentResponse: ...

    async def ai_agents_query_query_agent(
        self,
        body: AgentQueryRequest,
        run_as: AiAgentsQueryQueryAgentParamRunAs | None = None,
    ) -> AgentQueryResponse: ...

    async def ai_agents_query_query_agent(
        self,
        body: AgentQueryRequest,
        run_as: AiAgentsQueryQueryAgentParamRunAs | None = None,
    ) -> AgentQueryResponse: ...


class AiClient(AiClientProtocol):
    """Client for ai endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def ai_agents_list_agents(
        self,
        run_as: AiAgentsListAgentsParamRunAs | None = None,
    ) -> AgentListResponse:
        """
        List Agents

        **Warning**: This API is unstable and may change without notice.

        Args:
            run-as (AiAgentsListAgentsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            AgentListResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/ai/agents"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), AgentListResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def ai_agents_list_agents(
        self,
        run_as: AiAgentsListAgentsParamRunAs | None = None,
    ) -> AgentListResponse:
        """
        List Agents

        **Warning**: This API is unstable and may change without notice.

        Args:
            run-as (AiAgentsListAgentsParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            AgentListResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/ai/agents"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), AgentListResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def ai_agents_custom_tool_create_custom_tool(
        self,
        body: BodyAiAgentsCustomToolCreateCustomTool2,
        run_as: AiAgentsCustomToolCreateCustomToolParamRunAs | None = None,
    ) -> AgentResponse:
        """
        Create Custom Tool

        **Warning**: This API is unstable and may change without notice.

        Args:
            run-as (AiAgentsCustomToolCreateCustomToolParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (BodyAiAgentsCustomToolCreateCustomTool2)
                                     : Request body. (json)

        Returns:
            AgentResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/ai/agents/custom-tool"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: BodyAiAgentsCustomToolCreateCustomTool2 = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), AgentResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def ai_agents_custom_tool_create_custom_tool(
        self,
        body: BodyAiAgentsCustomToolCreateCustomTool2,
        run_as: AiAgentsCustomToolCreateCustomToolParamRunAs | None = None,
    ) -> AgentResponse:
        """
        Create Custom Tool

        **Warning**: This API is unstable and may change without notice.

        Args:
            run-as (AiAgentsCustomToolCreateCustomToolParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (BodyAiAgentsCustomToolCreateCustomTool2)
                                     : Request body. (json)

        Returns:
            AgentResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/ai/agents/custom-tool"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: BodyAiAgentsCustomToolCreateCustomTool2 = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), AgentResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def ai_agents_error_analysis_analyze_error(
        self,
        body: BodyAiAgentsErrorAnalysisAnalyzeError2,
        run_as: AiAgentsErrorAnalysisAnalyzeErrorParamRunAs | None = None,
    ) -> AgentResponse:
        """
        Analyze Error

        **Warning**: This API is unstable and may change without notice.

        Args:
            run-as (AiAgentsErrorAnalysisAnalyzeErrorParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (BodyAiAgentsErrorAnalysisAnalyzeError2)
                                     : Request body. (json)

        Returns:
            AgentResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/ai/agents/error-analysis"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: BodyAiAgentsErrorAnalysisAnalyzeError2 = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), AgentResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def ai_agents_error_analysis_analyze_error(
        self,
        body: BodyAiAgentsErrorAnalysisAnalyzeError2,
        run_as: AiAgentsErrorAnalysisAnalyzeErrorParamRunAs | None = None,
    ) -> AgentResponse:
        """
        Analyze Error

        **Warning**: This API is unstable and may change without notice.

        Args:
            run-as (AiAgentsErrorAnalysisAnalyzeErrorParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (BodyAiAgentsErrorAnalysisAnalyzeError2)
                                     : Request body. (json)

        Returns:
            AgentResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/ai/agents/error-analysis"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: BodyAiAgentsErrorAnalysisAnalyzeError2 = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), AgentResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def ai_agents_query_query_agent(
        self,
        body: AgentQueryRequest,
        run_as: AiAgentsQueryQueryAgentParamRunAs | None = None,
    ) -> AgentQueryResponse:
        """
        Query Agent

        **Warning**: This API is unstable and may change without notice.

        Args:
            run-as (AiAgentsQueryQueryAgentParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (AgentQueryRequest) : Request body. (json)

        Returns:
            AgentQueryResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/ai/agents/query"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: AgentQueryRequest = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), AgentQueryResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def ai_agents_query_query_agent(
        self,
        body: AgentQueryRequest,
        run_as: AiAgentsQueryQueryAgentParamRunAs | None = None,
    ) -> AgentQueryResponse:
        """
        Query Agent

        **Warning**: This API is unstable and may change without notice.

        Args:
            run-as (AiAgentsQueryQueryAgentParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (AgentQueryRequest) : Request body. (json)

        Returns:
            AgentQueryResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/ai/agents/query"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: AgentQueryRequest = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), AgentQueryResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover
