from typing import TYPE_CHECKING

from ...models.agent_list_response import AgentListResponse
from ...models.agent_query_request import AgentQueryRequest
from ...models.agent_query_response import AgentQueryResponse
from ...models.agent_response import AgentResponse
from ...models.ai_agents_custom_tool_create_custom_tool_param_run_as import AiAgentsCustomToolCreateCustomToolParamRunAs
from ...models.ai_agents_error_analysis_analyze_error_param_run_as import AiAgentsErrorAnalysisAnalyzeErrorParamRunAs
from ...models.ai_agents_list_agents_param_run_as import AiAgentsListAgentsParamRunAs
from ...models.ai_agents_query_query_agent_param_run_as import AiAgentsQueryQueryAgentParamRunAs
from ...models.body_ai_agents_custom_tool_create_custom_tool_2 import BodyAiAgentsCustomToolCreateCustomTool2
from ...models.body_ai_agents_error_analysis_analyze_error_2 import BodyAiAgentsErrorAnalysisAnalyzeError2

if TYPE_CHECKING:
    pass


class MockAiClient:
    """
    Mock implementation of AiClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestAiClient(MockAiClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def ai_agents_list_agents(
        self,
        run_as: AiAgentsListAgentsParamRunAs | None = None,
    ) -> AgentListResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockAiClient.ai_agents_list_agents() not implemented. Override this method in your test subclass."
        )

    async def ai_agents_custom_tool_create_custom_tool(
        self,
        body: BodyAiAgentsCustomToolCreateCustomTool2,
        run_as: AiAgentsCustomToolCreateCustomToolParamRunAs | None = None,
    ) -> AgentResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockAiClient.ai_agents_custom_tool_create_custom_tool() not implemented. Override this method in your test subclass."
        )

    async def ai_agents_error_analysis_analyze_error(
        self,
        body: BodyAiAgentsErrorAnalysisAnalyzeError2,
        run_as: AiAgentsErrorAnalysisAnalyzeErrorParamRunAs | None = None,
    ) -> AgentResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockAiClient.ai_agents_error_analysis_analyze_error() not implemented. Override this method in your test subclass."
        )

    async def ai_agents_query_query_agent(
        self,
        body: AgentQueryRequest,
        run_as: AiAgentsQueryQueryAgentParamRunAs | None = None,
    ) -> AgentQueryResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockAiClient.ai_agents_query_query_agent() not implemented. Override this method in your test subclass."
        )
