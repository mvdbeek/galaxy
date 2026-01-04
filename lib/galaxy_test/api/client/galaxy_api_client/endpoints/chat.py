from typing import Any, cast

from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.anonymous_array_item_113 import AnonymousArrayItem113
from ..models.anonymous_array_item_115 import AnonymousArrayItem115
from ..models.chat_exchange_feedback_set_exchange_feedback_200_response_2 import (
    ChatExchangeFeedbackSetExchangeFeedback200Response2,
)
from ..models.chat_exchange_feedback_set_exchange_feedback_param_run_as import (
    ChatExchangeFeedbackSetExchangeFeedbackParamRunAs,
)
from ..models.chat_exchange_feedback_set_exchange_feedback_request import ChatExchangeFeedbackSetExchangeFeedbackRequest
from ..models.chat_exchange_messages_get_exchange_messages_param_run_as import (
    ChatExchangeMessagesGetExchangeMessagesParamRunAs,
)
from ..models.chat_feedback_feedback_200_response_2 import ChatFeedbackFeedback200Response2
from ..models.chat_feedback_feedback_param_run_as import ChatFeedbackFeedbackParamRunAs
from ..models.chat_history_clear_chat_history_200_response_2 import ChatHistoryClearChatHistory200Response2
from ..models.chat_history_clear_chat_history_param_run_as import ChatHistoryClearChatHistoryParamRunAs
from ..models.chat_history_get_chat_history_param_run_as import ChatHistoryGetChatHistoryParamRunAs
from ..models.chat_query_param_job_id import ChatQueryParamJobId
from ..models.chat_query_param_query import ChatQueryParamQuery
from ..models.chat_query_param_run_as import ChatQueryParamRunAs
from ..models.chat_query_request_body_2 import ChatQueryRequestBody2
from ..models.chat_response import ChatResponse


class ChatClient:
    """Client for chat endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def chat_query_2_2(
        self,
        job_id: ChatQueryParamJobId | None = None,
        query: ChatQueryParamQuery | None = None,
        agent_type: str | None = "auto",
        run_as: ChatQueryParamRunAs | None = None,
        body: ChatQueryRequestBody2 | None = None,
    ) -> ChatResponse:
        """
        Query

        **Warning**: This API is unstable and may change without notice.

        Args:
            job_id (Optional[ChatQueryParamJobId])
                                     :
            query (Optional[ChatQueryParamQuery])
                                     : Query string for general chat
            agent_type (Optional[str]): Agent type to use for the query
            run-as (Optional[ChatQueryParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (Optional[ChatQueryRequestBody2])
                                     : Request body. (json)

        Returns:
            ChatResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/chat"

        params: dict[str, Any] = {
            **({"job_id": job_id} if job_id is not None else {}),
            **({"query": query} if query is not None else {}),
            **({"agent_type": agent_type} if agent_type is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: ChatQueryRequestBody2 | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ChatResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def chat_query_2_2(
        self,
        job_id: ChatQueryParamJobId | None = None,
        query: ChatQueryParamQuery | None = None,
        agent_type: str | None = "auto",
        run_as: ChatQueryParamRunAs | None = None,
        body: ChatQueryRequestBody2 | None = None,
    ) -> ChatResponse:
        """
        Query

        **Warning**: This API is unstable and may change without notice.

        Args:
            job_id (Optional[ChatQueryParamJobId])
                                     :
            query (Optional[ChatQueryParamQuery])
                                     : Query string for general chat
            agent_type (Optional[str]): Agent type to use for the query
            run-as (Optional[ChatQueryParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (Optional[ChatQueryRequestBody2])
                                     : Request body. (json)

        Returns:
            ChatResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/chat"

        params: dict[str, Any] = {
            **({"job_id": job_id} if job_id is not None else {}),
            **({"query": query} if query is not None else {}),
            **({"agent_type": agent_type} if agent_type is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: ChatQueryRequestBody2 | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ChatResponse, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def chat_exchange_feedback_set_exchange_feedback_2_2(
        self,
        exchange_id: int,
        body: ChatExchangeFeedbackSetExchangeFeedbackRequest,
        run_as: ChatExchangeFeedbackSetExchangeFeedbackParamRunAs | None = None,
    ) -> ChatExchangeFeedbackSetExchangeFeedback200Response2:
        """
        Set Exchange Feedback

        **Warning**: This API is unstable and may change without notice.

        Args:
            exchange_id (int)        :
            run-as (Optional[ChatExchangeFeedbackSetExchangeFeedbackParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (ChatExchangeFeedbackSetExchangeFeedbackRequest)
                                     : Request body. (json)

        Returns:
            ChatExchangeFeedbackSetExchangeFeedback200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/chat/exchange/{exchange_id}/feedback"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: ChatExchangeFeedbackSetExchangeFeedbackRequest = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ChatExchangeFeedbackSetExchangeFeedback200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def chat_exchange_feedback_set_exchange_feedback_2_2(
        self,
        exchange_id: int,
        body: ChatExchangeFeedbackSetExchangeFeedbackRequest,
        run_as: ChatExchangeFeedbackSetExchangeFeedbackParamRunAs | None = None,
    ) -> ChatExchangeFeedbackSetExchangeFeedback200Response2:
        """
        Set Exchange Feedback

        **Warning**: This API is unstable and may change without notice.

        Args:
            exchange_id (int)        :
            run-as (Optional[ChatExchangeFeedbackSetExchangeFeedbackParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (ChatExchangeFeedbackSetExchangeFeedbackRequest)
                                     : Request body. (json)

        Returns:
            ChatExchangeFeedbackSetExchangeFeedback200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/chat/exchange/{exchange_id}/feedback"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: ChatExchangeFeedbackSetExchangeFeedbackRequest = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ChatExchangeFeedbackSetExchangeFeedback200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def chat_exchange_messages_get_exchange_messages_2_2(
        self,
        exchange_id: int,
        run_as: ChatExchangeMessagesGetExchangeMessagesParamRunAs | None = None,
    ) -> list[AnonymousArrayItem113]:
        """
        Get Exchange Messages

        **Warning**: This API is unstable and may change without notice.

        Args:
            exchange_id (int)        :
            run-as (Optional[ChatExchangeMessagesGetExchangeMessagesParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem113]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/chat/exchange/{exchange_id}/messages"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem113], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def chat_exchange_messages_get_exchange_messages_2_2(
        self,
        exchange_id: int,
        run_as: ChatExchangeMessagesGetExchangeMessagesParamRunAs | None = None,
    ) -> list[AnonymousArrayItem113]:
        """
        Get Exchange Messages

        **Warning**: This API is unstable and may change without notice.

        Args:
            exchange_id (int)        :
            run-as (Optional[ChatExchangeMessagesGetExchangeMessagesParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem113]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/chat/exchange/{exchange_id}/messages"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem113], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def chat_history_clear_chat_history_2_2(
        self,
        run_as: ChatHistoryClearChatHistoryParamRunAs | None = None,
    ) -> ChatHistoryClearChatHistory200Response2:
        """
        Clear Chat History

        **Warning**: This API is unstable and may change without notice.

        Args:
            run-as (Optional[ChatHistoryClearChatHistoryParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ChatHistoryClearChatHistory200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/chat/history"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ChatHistoryClearChatHistory200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def chat_history_clear_chat_history_2_2(
        self,
        run_as: ChatHistoryClearChatHistoryParamRunAs | None = None,
    ) -> ChatHistoryClearChatHistory200Response2:
        """
        Clear Chat History

        **Warning**: This API is unstable and may change without notice.

        Args:
            run-as (Optional[ChatHistoryClearChatHistoryParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ChatHistoryClearChatHistory200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/chat/history"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ChatHistoryClearChatHistory200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def chat_history_get_chat_history_2_2(
        self,
        limit: int | None = 50,
        run_as: ChatHistoryGetChatHistoryParamRunAs | None = None,
    ) -> list[AnonymousArrayItem115]:
        """
        Get Chat History

        **Warning**: This API is unstable and may change without notice.

        Args:
            limit (Optional[int])    : Maximum number of chats to return
            run-as (Optional[ChatHistoryGetChatHistoryParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem115]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/chat/history"

        params: dict[str, Any] = {
            **({"limit": limit} if limit is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem115], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def chat_history_get_chat_history_2_2(
        self,
        limit: int | None = 50,
        run_as: ChatHistoryGetChatHistoryParamRunAs | None = None,
    ) -> list[AnonymousArrayItem115]:
        """
        Get Chat History

        **Warning**: This API is unstable and may change without notice.

        Args:
            limit (Optional[int])    : Maximum number of chats to return
            run-as (Optional[ChatHistoryGetChatHistoryParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem115]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/chat/history"

        params: dict[str, Any] = {
            **({"limit": limit} if limit is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem115], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def chat_feedback_feedback_2_2(
        self,
        job_id: str,
        feedback: int,
        run_as: ChatFeedbackFeedbackParamRunAs | None = None,
    ) -> ChatFeedbackFeedback200Response2:
        """
        Feedback

        **Warning**: This API is unstable and may change without notice.

        Args:
            job_id (str)             : The Job ID the chat exchange is linked to.
            feedback (int)           :
            run-as (Optional[ChatFeedbackFeedbackParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ChatFeedbackFeedback200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/chat/{job_id}/feedback"

        params: dict[str, Any] = {
            "feedback": feedback,
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ChatFeedbackFeedback200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def chat_feedback_feedback_2_2(
        self,
        job_id: str,
        feedback: int,
        run_as: ChatFeedbackFeedbackParamRunAs | None = None,
    ) -> ChatFeedbackFeedback200Response2:
        """
        Feedback

        **Warning**: This API is unstable and may change without notice.

        Args:
            job_id (str)             : The Job ID the chat exchange is linked to.
            feedback (int)           :
            run-as (Optional[ChatFeedbackFeedbackParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ChatFeedbackFeedback200Response2: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/chat/{job_id}/feedback"

        params: dict[str, Any] = {
            "feedback": feedback,
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ChatFeedbackFeedback200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover
