from typing import TYPE_CHECKING, Any

from ...models.chat_exchange_feedback_set_exchange_feedback_200_response import (
    ChatExchangeFeedbackSetExchangeFeedback200Response,
)
from ...models.chat_exchange_feedback_set_exchange_feedback_param_run_as import (
    ChatExchangeFeedbackSetExchangeFeedbackParamRunAs,
)
from ...models.chat_exchange_feedback_set_exchange_feedback_request import (
    ChatExchangeFeedbackSetExchangeFeedbackRequest,
)
from ...models.chat_exchange_messages_get_exchange_messages_param_run_as import (
    ChatExchangeMessagesGetExchangeMessagesParamRunAs,
)
from ...models.chat_feedback_feedback_200_response import ChatFeedbackFeedback200Response
from ...models.chat_feedback_feedback_param_run_as import ChatFeedbackFeedbackParamRunAs
from ...models.chat_history_clear_chat_history_200_response import ChatHistoryClearChatHistory200Response
from ...models.chat_history_clear_chat_history_param_run_as import ChatHistoryClearChatHistoryParamRunAs
from ...models.chat_history_get_chat_history_param_run_as import ChatHistoryGetChatHistoryParamRunAs
from ...models.chat_query_param_job_id import ChatQueryParamJobId
from ...models.chat_query_param_query import ChatQueryParamQuery
from ...models.chat_query_param_run_as import ChatQueryParamRunAs
from ...models.chat_query_request_body import ChatQueryRequestBody
from ...models.chat_response import ChatResponse

if TYPE_CHECKING:
    pass


class MockChatClient:
    """
    Mock implementation of ChatClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestChatClient(MockChatClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def chat_query(
        self,
        job_id: ChatQueryParamJobId | None = None,
        query: ChatQueryParamQuery | None = None,
        agent_type: str | None = None,
        run_as: ChatQueryParamRunAs | None = None,
        body: ChatQueryRequestBody | None = None,
    ) -> ChatResponse:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockChatClient.chat_query() not implemented. Override this method in your test subclass."
        )

    async def chat_exchange_feedback_set_exchange_feedback(
        self,
        exchange_id: int,
        body: ChatExchangeFeedbackSetExchangeFeedbackRequest,
        run_as: ChatExchangeFeedbackSetExchangeFeedbackParamRunAs | None = None,
    ) -> ChatExchangeFeedbackSetExchangeFeedback200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockChatClient.chat_exchange_feedback_set_exchange_feedback() not implemented. Override this method in your test subclass."
        )

    async def chat_exchange_messages_get_exchange_messages(
        self,
        exchange_id: int,
        run_as: ChatExchangeMessagesGetExchangeMessagesParamRunAs | None = None,
    ) -> list[Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockChatClient.chat_exchange_messages_get_exchange_messages() not implemented. Override this method in your test subclass."
        )

    async def chat_history_clear_chat_history(
        self,
        run_as: ChatHistoryClearChatHistoryParamRunAs | None = None,
    ) -> ChatHistoryClearChatHistory200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockChatClient.chat_history_clear_chat_history() not implemented. Override this method in your test subclass."
        )

    async def chat_history_get_chat_history(
        self,
        limit: int | None = None,
        run_as: ChatHistoryGetChatHistoryParamRunAs | None = None,
    ) -> list[Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockChatClient.chat_history_get_chat_history() not implemented. Override this method in your test subclass."
        )

    async def chat_feedback_feedback(
        self,
        job_id: str,
        feedback: int,
        run_as: ChatFeedbackFeedbackParamRunAs | None = None,
    ) -> ChatFeedbackFeedback200Response | None:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockChatClient.chat_feedback_feedback() not implemented. Override this method in your test subclass."
        )
