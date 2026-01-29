from typing import Any, Protocol, runtime_checkable

from galaxy_test.api.client.galaxy_api_client.core.cattrs_converter import structure_from_dict
from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.anonymous_array_item_77 import AnonymousArrayItem77
from ..models.anonymous_array_item_79 import AnonymousArrayItem79
from ..models.chat_exchange_feedback_set_exchange_feedback_200_response import (
    ChatExchangeFeedbackSetExchangeFeedback200Response,
)
from ..models.chat_exchange_feedback_set_exchange_feedback_param_run_as import (
    ChatExchangeFeedbackSetExchangeFeedbackParamRunAs,
)
from ..models.chat_exchange_feedback_set_exchange_feedback_request import ChatExchangeFeedbackSetExchangeFeedbackRequest
from ..models.chat_exchange_messages_get_exchange_messages_param_run_as import (
    ChatExchangeMessagesGetExchangeMessagesParamRunAs,
)
from ..models.chat_feedback_feedback_200_response import ChatFeedbackFeedback200Response
from ..models.chat_feedback_feedback_param_run_as import ChatFeedbackFeedbackParamRunAs
from ..models.chat_history_clear_chat_history_200_response import ChatHistoryClearChatHistory200Response
from ..models.chat_history_clear_chat_history_param_run_as import ChatHistoryClearChatHistoryParamRunAs
from ..models.chat_history_get_chat_history_param_run_as import ChatHistoryGetChatHistoryParamRunAs
from ..models.chat_query_param_job_id import ChatQueryParamJobId
from ..models.chat_query_param_query import ChatQueryParamQuery
from ..models.chat_query_param_run_as import ChatQueryParamRunAs
from ..models.chat_query_request_body import ChatQueryRequestBody
from ..models.chat_response import ChatResponse


@runtime_checkable
class ChatClientProtocol(Protocol):
    """Protocol defining the interface of ChatClient for dependency injection."""

    async def chat_query(
        self,
        job_id: ChatQueryParamJobId | None = None,
        query: ChatQueryParamQuery | None = None,
        agent_type: str | None = None,
        run_as: ChatQueryParamRunAs | None = None,
        body: ChatQueryRequestBody | None = None,
    ) -> ChatResponse: ...

    async def chat_query(
        self,
        job_id: ChatQueryParamJobId | None = None,
        query: ChatQueryParamQuery | None = None,
        agent_type: str | None = None,
        run_as: ChatQueryParamRunAs | None = None,
        body: ChatQueryRequestBody | None = None,
    ) -> ChatResponse: ...

    async def chat_exchange_feedback_set_exchange_feedback(
        self,
        exchange_id: int,
        body: ChatExchangeFeedbackSetExchangeFeedbackRequest,
        run_as: ChatExchangeFeedbackSetExchangeFeedbackParamRunAs | None = None,
    ) -> ChatExchangeFeedbackSetExchangeFeedback200Response: ...

    async def chat_exchange_feedback_set_exchange_feedback(
        self,
        exchange_id: int,
        body: ChatExchangeFeedbackSetExchangeFeedbackRequest,
        run_as: ChatExchangeFeedbackSetExchangeFeedbackParamRunAs | None = None,
    ) -> ChatExchangeFeedbackSetExchangeFeedback200Response: ...

    async def chat_exchange_messages_get_exchange_messages(
        self,
        exchange_id: int,
        run_as: ChatExchangeMessagesGetExchangeMessagesParamRunAs | None = None,
    ) -> list[AnonymousArrayItem77]: ...

    async def chat_exchange_messages_get_exchange_messages(
        self,
        exchange_id: int,
        run_as: ChatExchangeMessagesGetExchangeMessagesParamRunAs | None = None,
    ) -> list[AnonymousArrayItem77]: ...

    async def chat_history_clear_chat_history(
        self,
        run_as: ChatHistoryClearChatHistoryParamRunAs | None = None,
    ) -> ChatHistoryClearChatHistory200Response: ...

    async def chat_history_clear_chat_history(
        self,
        run_as: ChatHistoryClearChatHistoryParamRunAs | None = None,
    ) -> ChatHistoryClearChatHistory200Response: ...

    async def chat_history_get_chat_history(
        self,
        limit: int | None = None,
        run_as: ChatHistoryGetChatHistoryParamRunAs | None = None,
    ) -> list[AnonymousArrayItem79]: ...

    async def chat_history_get_chat_history(
        self,
        limit: int | None = None,
        run_as: ChatHistoryGetChatHistoryParamRunAs | None = None,
    ) -> list[AnonymousArrayItem79]: ...

    async def chat_feedback_feedback(
        self,
        job_id: str,
        feedback: int,
        run_as: ChatFeedbackFeedbackParamRunAs | None = None,
    ) -> ChatFeedbackFeedback200Response | None: ...

    async def chat_feedback_feedback(
        self,
        job_id: str,
        feedback: int,
        run_as: ChatFeedbackFeedbackParamRunAs | None = None,
    ) -> ChatFeedbackFeedback200Response | None: ...


class ChatClient(ChatClientProtocol):
    """Client for chat endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def chat_query(
        self,
        job_id: ChatQueryParamJobId | None = None,
        query: ChatQueryParamQuery | None = None,
        agent_type: str | None = None,
        run_as: ChatQueryParamRunAs | None = None,
        body: ChatQueryRequestBody | None = None,
    ) -> ChatResponse:
        """
        Query

        **Warning**: This API is unstable and may change without notice.

        Args:
            job_id (ChatQueryParamJobId | None)
                                     :
            query (ChatQueryParamQuery | None)
                                     : Query string for general chat
            agent_type (str | None)  : Agent type to use for the query
            run-as (ChatQueryParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (ChatQueryRequestBody | None)
                                     : Request body. (json)

        Returns:
            ChatResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/chat"

        params: dict[str, Any] = {
            **({"job_id": DataclassSerializer.serialize(job_id)} if job_id is not None else {}),
            **({"query": DataclassSerializer.serialize(query)} if query is not None else {}),
            **({"agent_type": DataclassSerializer.serialize(agent_type)} if agent_type is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: ChatQueryRequestBody | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), ChatResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def chat_query(
        self,
        job_id: ChatQueryParamJobId | None = None,
        query: ChatQueryParamQuery | None = None,
        agent_type: str | None = None,
        run_as: ChatQueryParamRunAs | None = None,
        body: ChatQueryRequestBody | None = None,
    ) -> ChatResponse:
        """
        Query

        **Warning**: This API is unstable and may change without notice.

        Args:
            job_id (ChatQueryParamJobId | None)
                                     :
            query (ChatQueryParamQuery | None)
                                     : Query string for general chat
            agent_type (str | None)  : Agent type to use for the query
            run-as (ChatQueryParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (ChatQueryRequestBody | None)
                                     : Request body. (json)

        Returns:
            ChatResponse: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/chat"

        params: dict[str, Any] = {
            **({"job_id": DataclassSerializer.serialize(job_id)} if job_id is not None else {}),
            **({"query": DataclassSerializer.serialize(query)} if query is not None else {}),
            **({"agent_type": DataclassSerializer.serialize(agent_type)} if agent_type is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: ChatQueryRequestBody | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=params, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), ChatResponse)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def chat_exchange_feedback_set_exchange_feedback(
        self,
        exchange_id: int,
        body: ChatExchangeFeedbackSetExchangeFeedbackRequest,
        run_as: ChatExchangeFeedbackSetExchangeFeedbackParamRunAs | None = None,
    ) -> ChatExchangeFeedbackSetExchangeFeedback200Response:
        """
        Set Exchange Feedback

        **Warning**: This API is unstable and may change without notice.

        Args:
            exchange_id (int)        :
            run-as (ChatExchangeFeedbackSetExchangeFeedbackParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (ChatExchangeFeedbackSetExchangeFeedbackRequest)
                                     : Request body. (json)

        Returns:
            ChatExchangeFeedbackSetExchangeFeedback200Response: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        exchange_id = DataclassSerializer.serialize(exchange_id)

        url = f"{self.base_url}/api/chat/exchange/{exchange_id}/feedback"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: ChatExchangeFeedbackSetExchangeFeedbackRequest = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), ChatExchangeFeedbackSetExchangeFeedback200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def chat_exchange_feedback_set_exchange_feedback(
        self,
        exchange_id: int,
        body: ChatExchangeFeedbackSetExchangeFeedbackRequest,
        run_as: ChatExchangeFeedbackSetExchangeFeedbackParamRunAs | None = None,
    ) -> ChatExchangeFeedbackSetExchangeFeedback200Response:
        """
        Set Exchange Feedback

        **Warning**: This API is unstable and may change without notice.

        Args:
            exchange_id (int)        :
            run-as (ChatExchangeFeedbackSetExchangeFeedbackParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (ChatExchangeFeedbackSetExchangeFeedbackRequest)
                                     : Request body. (json)

        Returns:
            ChatExchangeFeedbackSetExchangeFeedback200Response: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        exchange_id = DataclassSerializer.serialize(exchange_id)

        url = f"{self.base_url}/api/chat/exchange/{exchange_id}/feedback"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        json_body: ChatExchangeFeedbackSetExchangeFeedbackRequest = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), ChatExchangeFeedbackSetExchangeFeedback200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def chat_exchange_messages_get_exchange_messages(
        self,
        exchange_id: int,
        run_as: ChatExchangeMessagesGetExchangeMessagesParamRunAs | None = None,
    ) -> list[AnonymousArrayItem77]:
        """
        Get Exchange Messages

        **Warning**: This API is unstable and may change without notice.

        Args:
            exchange_id (int)        :
            run-as (ChatExchangeMessagesGetExchangeMessagesParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem77]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        exchange_id = DataclassSerializer.serialize(exchange_id)

        url = f"{self.base_url}/api/chat/exchange/{exchange_id}/messages"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[AnonymousArrayItem77])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def chat_exchange_messages_get_exchange_messages(
        self,
        exchange_id: int,
        run_as: ChatExchangeMessagesGetExchangeMessagesParamRunAs | None = None,
    ) -> list[AnonymousArrayItem77]:
        """
        Get Exchange Messages

        **Warning**: This API is unstable and may change without notice.

        Args:
            exchange_id (int)        :
            run-as (ChatExchangeMessagesGetExchangeMessagesParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem77]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        exchange_id = DataclassSerializer.serialize(exchange_id)

        url = f"{self.base_url}/api/chat/exchange/{exchange_id}/messages"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[AnonymousArrayItem77])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def chat_history_clear_chat_history(
        self,
        run_as: ChatHistoryClearChatHistoryParamRunAs | None = None,
    ) -> ChatHistoryClearChatHistory200Response:
        """
        Clear Chat History

        **Warning**: This API is unstable and may change without notice.

        Args:
            run-as (ChatHistoryClearChatHistoryParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ChatHistoryClearChatHistory200Response: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/chat/history"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), ChatHistoryClearChatHistory200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def chat_history_clear_chat_history(
        self,
        run_as: ChatHistoryClearChatHistoryParamRunAs | None = None,
    ) -> ChatHistoryClearChatHistory200Response:
        """
        Clear Chat History

        **Warning**: This API is unstable and may change without notice.

        Args:
            run-as (ChatHistoryClearChatHistoryParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ChatHistoryClearChatHistory200Response: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/chat/history"

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("DELETE", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), ChatHistoryClearChatHistory200Response)
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def chat_history_get_chat_history(
        self,
        limit: int | None = None,
        run_as: ChatHistoryGetChatHistoryParamRunAs | None = None,
    ) -> list[AnonymousArrayItem79]:
        """
        Get Chat History

        **Warning**: This API is unstable and may change without notice.

        Args:
            limit (int | None)       : Maximum number of chats to return
            run-as (ChatHistoryGetChatHistoryParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem79]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/chat/history"

        params: dict[str, Any] = {
            **({"limit": DataclassSerializer.serialize(limit)} if limit is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[AnonymousArrayItem79])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def chat_history_get_chat_history(
        self,
        limit: int | None = None,
        run_as: ChatHistoryGetChatHistoryParamRunAs | None = None,
    ) -> list[AnonymousArrayItem79]:
        """
        Get Chat History

        **Warning**: This API is unstable and may change without notice.

        Args:
            limit (int | None)       : Maximum number of chats to return
            run-as (ChatHistoryGetChatHistoryParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem79]: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/chat/history"

        params: dict[str, Any] = {
            **({"limit": DataclassSerializer.serialize(limit)} if limit is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return structure_from_dict(response.json(), list[AnonymousArrayItem79])
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def chat_feedback_feedback(
        self,
        job_id: str,
        feedback: int,
        run_as: ChatFeedbackFeedbackParamRunAs | None = None,
    ) -> ChatFeedbackFeedback200Response | None:
        """
        Feedback

        **Warning**: This API is unstable and may change without notice.

        Args:
            job_id (str)             : The Job ID the chat exchange is linked to.
            feedback (int)           :
            run-as (ChatFeedbackFeedbackParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ChatFeedbackFeedback200Response | None: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        job_id = DataclassSerializer.serialize(job_id)

        url = f"{self.base_url}/api/chat/{job_id}/feedback"

        params: dict[str, Any] = {
            "feedback": DataclassSerializer.serialize(feedback),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return (
                    structure_from_dict(response.json(), ChatFeedbackFeedback200Response)
                    if response.json() is not None
                    else None
                )
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover

    async def chat_feedback_feedback(
        self,
        job_id: str,
        feedback: int,
        run_as: ChatFeedbackFeedbackParamRunAs | None = None,
    ) -> ChatFeedbackFeedback200Response | None:
        """
        Feedback

        **Warning**: This API is unstable and may change without notice.

        Args:
            job_id (str)             : The Job ID the chat exchange is linked to.
            feedback (int)           :
            run-as (ChatFeedbackFeedbackParamRunAs | None)
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ChatFeedbackFeedback200Response | None: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        job_id = DataclassSerializer.serialize(job_id)

        url = f"{self.base_url}/api/chat/{job_id}/feedback"

        params: dict[str, Any] = {
            "feedback": DataclassSerializer.serialize(feedback),
        }

        headers: dict[str, Any] = {
            **({"run-as": DataclassSerializer.serialize(run_as)} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return (
                    structure_from_dict(response.json(), ChatFeedbackFeedback200Response)
                    if response.json() is not None
                    else None
                )
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        raise RuntimeError("Unexpected code path")  # pragma: no cover
